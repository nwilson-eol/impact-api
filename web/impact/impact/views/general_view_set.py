# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.apps import apps
from django.db import models
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_tracking.mixins import LoggingMixin


from impact.permissions import DynamicModelPermissions
from impact.serializers import GeneralSerializer


class GeneralViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
        DynamicModelPermissions,
    )

    @property
    def model(self):
        return apps.get_model(
            app_label=self.kwargs['app'],
            model_name=str(self.kwargs['model']))

    def get_queryset(self):
        return self.model.objects.all()

    def get_related_model_fields(self):
        return [getattr(
            self.model, f.name).field.get_attname()
            for f in self.model._meta.fields
            if type(f) == models.fields.related.ForeignKey]

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.model
        return GeneralSerializer
