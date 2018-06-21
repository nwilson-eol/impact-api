import graphene

from impact.graphql.expert_profile_type import ExpertProfileType
from accelerator.models.expert_profile import ExpertProfile


class Query(graphene.ObjectType):
    expert_profile = graphene.Field(ExpertProfileType, id=graphene.Int())

    def resolve_expert_profile(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return ExpertProfile.objects.get(pk=id)

        return None
