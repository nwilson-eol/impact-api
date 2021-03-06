# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from accelerator.models import (
    IN_PERSON_JUDGING_ROUND_TYPE,
    ONLINE_JUDGING_ROUND_TYPE,
)

from impact.v1.views.base_list_view import BaseListView
from impact.v1.helpers import JudgingRoundHelper

INVALID_ROUND_TYPE_ERROR = ("Invalid value '{}' for round_type. "
                            "Use 'Online' or 'In-Person'.")


class JudgingRoundListView(BaseListView):
    view_name = "judging_round"
    helper_class = JudgingRoundHelper

    def get(self, request):
        self._validate_round_type(request)
        return super().get(request)

    def _validate_round_type(self, request):
        round_type = request.GET.get("round_type")
        if round_type is not None:
            if round_type.lower() not in [
                    IN_PERSON_JUDGING_ROUND_TYPE.lower(),
                    ONLINE_JUDGING_ROUND_TYPE.lower()]:
                self.errors.append(INVALID_ROUND_TYPE_ERROR.format(round_type))

    def filter(self, qs):
        return self._filter_by_round_type(super().filter(qs))

    def _filter_by_round_type(self, qs):
        round_type = self.request.query_params.get("round_type", None)
        if round_type is not None:
            return qs.filter(round_type=round_type)
        return qs
