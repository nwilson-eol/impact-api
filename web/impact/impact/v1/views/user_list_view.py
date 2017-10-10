from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response

from impact.models import BaseProfile
from impact.utils import parse_date
from impact.v1.helpers import (
    ProfileHelper,
    USER_TYPE_TO_PROFILE_MODEL,
    UserHelper,
    VALID_USER_TYPES,
    valid_keys_note,
    validate_boolean,
    validate_choices,
    validate_expert_categories,
    validate_gender,
)
from impact.v1.views.base_list_view import BaseListView


EMAIL_EXISTS_ERROR = "User with email {} already exists"
INVALID_KEY_ERROR = "'{}' is not a valid key."
REQUIRED_KEY_ERROR = "'{}' is required"
UNSUPPORTED_KEY_ERROR = "'{key}' is not supported for {type}"


User = get_user_model()


class UserListView(BaseListView):
    METADATA_ACTIONS = {
        "GET": UserHelper.DETAIL_GET_METADATA,
        "POST": UserHelper.LIST_POST_METADATA,
        }

    def post(self, request):
        user_args = self._user_args(request.POST)
        profile_args = self._profile_args(request.POST)
        self._invalid_keys(request.POST)
        if self.errors:
            note = valid_keys_note(profile_args.get("user_type"), post=True)
            self.errors.append(note)
            return Response(status=403, data=self.errors)
        user = _construct_user(user_args, profile_args)
        return Response({"id": user.id})

    def _user_args(self, dict):
        self._check_required_keys(dict, UserHelper.REQUIRED_KEYS)
        results = self._copy_translated_keys(dict, UserHelper.USER_INPUT_KEYS)
        email = results.get("email")
        if email and User.objects.filter(email=email).exists():
            self.errors.append(EMAIL_EXISTS_ERROR.format(email))
        if "is_active" not in results:
            results["is_active"] = False
        return results

    def _check_required_keys(self, user_keys, required_keys):
        for key in set(required_keys) - set(user_keys):
            self.errors.append(REQUIRED_KEY_ERROR.format(key))

    def _check_unsupported_keys(self, user_type, user_keys, unsupported_keys):
        for key in set(unsupported_keys).intersection(set(user_keys)):
            self.errors.append(UNSUPPORTED_KEY_ERROR.format(key=key,
                                                            type=user_type))

    def _copy_translated_keys(self, user_data, keys):
        result = {}
        for key in keys:
            if key in user_data:
                target_key = UserHelper.translate_key(key)
                value = user_data[key]
                if target_key in ProfileHelper.OPTIONAL_BOOLEAN_KEYS:
                    value = validate_boolean(self, key, value)
                result[target_key] = value
        return result

    def _profile_args(self, user_data):
        self._check_required_keys(user_data, ProfileHelper.CORE_REQUIRED_KEYS)
        results = self._copy_translated_keys(user_data,
                                             ProfileHelper.INPUT_KEYS)
        user_type = validate_choices(
            self, "user_type", results.get("user_type"), VALID_USER_TYPES)
        if user_type == "expert":
            self._check_required_keys(
                user_data, ProfileHelper.EXPERT_REQUIRED_KEYS)
            results["expert_category"] = validate_expert_categories(
                self, "expert_category", results.get("expert_category"))
        else:
            self._check_unsupported_keys(
                user_type, user_data, ProfileHelper.EXPERT_ONLY_KEYS)
            if user_type == "member":
                self._check_unsupported_keys(
                    user_type,
                    user_data,
                    ProfileHelper.ENTREPRENEUR_OPTIONAL_KEYS)
        results["gender"] = validate_gender(
            self, "gender", results.get("gender"))
        results["privacy_policy_accepted"] = False
        results["newsletter_sender"] = False
        return results

    def _invalid_keys(self, user_keys):
        for key in set(user_keys) - set(UserHelper.INPUT_KEYS):
            self.errors.append(INVALID_KEY_ERROR.format(key))

    def _results(self, limit, offset):
        queryset = User.objects.all()
        updated_at_after = self.request.query_params.get(
            'updated_at.after', None)
        updated_at_before = self.request.query_params.get(
            'updated_at.before', None)
        if updated_at_after or updated_at_before:
            queryset = _filter_profiles_by_date(
                queryset,
                updated_at_after,
                updated_at_before)
        count = queryset.count()
        return (count,
                [UserHelper(user).serialize()
                 for user in queryset[offset:offset + limit]])


def _filter_profiles_by_date(queryset, updated_at_after, updated_at_before):
    updated_at_after = parse_date(updated_at_after)
    updated_at_before = parse_date(updated_at_before)
    if updated_at_after:
        queryset = queryset.filter(
            Q(expertprofile__updated_at__gte=updated_at_after) |
            Q(entrepreneurprofile__updated_at__gte=updated_at_after) |
            Q(memberprofile__updated_at__gte=updated_at_after))
    if updated_at_before:
        queryset = queryset.exclude(
            Q(expertprofile__updated_at__gt=updated_at_before) |
            Q(entrepreneurprofile__updated_at__gt=updated_at_before) |
            Q(memberprofile__updated_at__gt=updated_at_before)
        )
    return queryset


def _construct_user(user_args, profile_args):
    user = User.objects.create_user(**user_args)
    user_type = profile_args.pop("user_type")
    BaseProfile.objects.create(user=user, user_type=user_type.upper())
    profile_args["user"] = user
    klass = USER_TYPE_TO_PROFILE_MODEL[user_type]
    klass.objects.create(**profile_args)
    return user
