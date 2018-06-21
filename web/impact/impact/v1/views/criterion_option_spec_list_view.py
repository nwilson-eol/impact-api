# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from impact.v1.views.post_mixin import PostMixin
from impact.v1.views.base_list_view import BaseListView
from impact.v1.helpers import CriterionOptionSpecHelper


class CriterionOptionSpecListView(BaseListView,
                                  PostMixin):
    helper_class = CriterionOptionSpecHelper    
    view_name = "criterion_option_spec"
    actions = ['GET', 'POST']  # Should get this from PostMixin
