import graphene
from graphene_django import DjangoObjectType
from accelerator.models.expert_profile import ExpertProfile
from impact.graphql.user import UserType
from impact.graphql.industry import IndustryType
from impact.graphql.program_family import ProgramFamilyType
from impact.graphql.startup import StartupType


class ExpertProfileType(DjangoObjectType):
    mentees = graphene.List(StartupType)

    class Meta:
        model = ExpertProfile
        only_fields = (
            'title',
            'company',
            'phone',
            'twitter_handle',
            'linked_in_url',
            'personal_website_url',
            'bio',
            'expert_category',
            'image',
            'primary_industry',
            'additional_industries',
            'home_program_family',
            'user'
        )
