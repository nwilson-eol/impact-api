# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from impact.permissions import (
    V1APIPermissions,
)
from impact.v1.helpers import ProgramFamilyHelper
from impact.v1.metadata import ImpactMetadata
from impact.v1.views import ImpactView


class ProgramFamilyDetailView(ImpactView):
    helper_class = ProgramFamilyHelper
    metadata_class = ImpactMetadata

    permission_classes = (
        V1APIPermissions,
    )
