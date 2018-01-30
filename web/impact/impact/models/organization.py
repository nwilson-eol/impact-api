# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.db import models
from django.core.validators import RegexValidator

from impact.models.mc_model import MCModel
from impact.models.utils import is_managed


class Organization(MCModel):
    name = models.CharField(max_length=100, unique=True)
    website_url = models.URLField(max_length=100, blank=True)
    twitter_handle = models.CharField(
        max_length=40,
        blank=True,
        help_text='Omit the "@". We\'ll add it.')
    public_inquiry_email = models.EmailField(verbose_name="Email address",
                                             max_length=100,
                                             blank=True)
    url_slug = models.CharField(
        max_length=64,
        blank=True,
        default="",  # This actually gets replaced by a real slug.
        unique=True,
        validators=[
            RegexValidator(regex="^[\w-]+$",
                           message="Letters, numbers, and dashes only.")
        ]
    )

    class Meta(MCModel.Meta):
        db_table = 'mc_organization'
        managed = is_managed(db_table)
        verbose_name_plural = 'Organizations'
        ordering = ['name', ]

    def __str__(self):
        return self.name