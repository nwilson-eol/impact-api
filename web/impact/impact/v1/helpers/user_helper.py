from django.conf import settings

from impact.utils import get_profile
from impact.v1.helpers.model_helper import ModelHelper
from impact.v1.helpers.profile_helper import ProfileHelper
from impact.v1.metadata import (
    OPTIONAL_STRING_TYPE,
    OPTIONAL_BOOLEAN_TYPE,
    OPTIONAL_DATE_TYPE,
    OPTIONAL_LIST_TYPE,
    OPTIONAL_ID_TYPE,
)


USER_POST_OPTIONS = {
    "first_name": OPTIONAL_STRING_TYPE,
    "last_name": OPTIONAL_STRING_TYPE,
    "email": OPTIONAL_STRING_TYPE,
    "is_active": OPTIONAL_BOOLEAN_TYPE,
    "gender": OPTIONAL_STRING_TYPE,
    "phone": OPTIONAL_STRING_TYPE,
    "additional_industry_ids": OPTIONAL_LIST_TYPE,
    "expert_category": OPTIONAL_STRING_TYPE,
    "mentoring_specialties": OPTIONAL_LIST_TYPE,
    "primary_industry_id": OPTIONAL_ID_TYPE,
    "updated_at": OPTIONAL_DATE_TYPE,
}
USER_POST_OPTIONS.update(dict([
            (key, OPTIONAL_BOOLEAN_TYPE)
            for key in ProfileHelper.OPTIONAL_BOOLEAN_KEYS]))
USER_POST_OPTIONS.update(dict([
            (key, OPTIONAL_STRING_TYPE)
            for key in ProfileHelper.OPTIONAL_STRING_KEYS]))

USER_GET_OPTIONS = USER_POST_OPTIONS.copy()
USER_GET_OPTIONS.update(
    {
        "id": {
            "type": "integer",
            "required": False,
            "read_only": True,
            "label": "ID"
        },
        "updated_at": {
            "type": "string",
            "read_only": True
        },
        "last_login": {
            "type": "string",
            "read_only": True
        },
        "date_joined": {
            "type": "string",
            "read_only": True
        },
    })


class UserHelper(ModelHelper):
    MODEL = settings.AUTH_USER_MODEL

    DETAIL_GET_METADATA = USER_GET_OPTIONS
    DETAIL_PATCH_METADATA = USER_POST_OPTIONS
    LIST_POST_METADATA = USER_POST_OPTIONS

    REQUIRED_KEYS = [
        "email",
        "first_name",
        "last_name",
        ]
    OPTIONAL_KEYS = [
        "is_active",
        ]
    USER_INPUT_KEYS = REQUIRED_KEYS + OPTIONAL_KEYS
    READ_ONLY_KEYS = [
        "date_joined",
        "id",
        "last_login",
        ]
    OUTPUT_KEYS = READ_ONLY_KEYS + USER_INPUT_KEYS + ProfileHelper.OUTPUT_KEYS
    INPUT_KEYS = USER_INPUT_KEYS + ProfileHelper.INPUT_KEYS
    KEY_TRANSLATIONS = {
        "first_name": "full_name",
        "last_name": "short_name",
        }

    def __init__(self, *args, **kwargs):
        super(UserHelper, self).__init__(*args, **kwargs)
        self.profile = get_profile(self.subject)

    @classmethod
    def translate_key(cls, key):
        return cls.KEY_TRANSLATIONS.get(key, key)

    def field_value(self, field):
        result = super(UserHelper, self).field_value(field)
        if result is not None:
            return result
        return ProfileHelper(self.profile).field_value(field)

    @property
    def first_name(self):
        return self.subject.full_name

    @property
    def last_name(self):
        return self.subject.short_name
