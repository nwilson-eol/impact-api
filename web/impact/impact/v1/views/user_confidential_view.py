# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.contrib.auth import get_user_model

from impact.permissions import (
    V1ConfidentialAPIPermissions,
)
from impact.v1.helpers import (
    INTEGER_FIELD,
    PK_FIELD,
    UserHelper,
    STRING_FIELD,
)
from impact.v1.views.base_detail_view import BaseDetailView

User = get_user_model()


class UserConfidentialView(BaseDetailView):
    helper_class = UserHelper

    permission_classes = (
        V1ConfidentialAPIPermissions,
    )

    @classmethod
    def fields(cls):
        return {
            "id": PK_FIELD,
            "expert_group": INTEGER_FIELD,
            "internal_notes": STRING_FIELD,
        }
