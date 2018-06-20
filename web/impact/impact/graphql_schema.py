import graphene

import impact.graphql.query


class Query(impact.graphql.query.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
