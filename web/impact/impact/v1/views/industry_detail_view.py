# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from impact.v1.helpers import IndustryHelper
from impact.v1.views.base_detail_view import BaseDetailView


class IndustryDetailView(BaseDetailView):
    view_name = "industry_detail"
    helper_class = IndustryHelper
