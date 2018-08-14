import graphene
import Services.schema, DBConnections.schema, DBConnections.schema2, Main.schema


class Query(Main.schema.Query,
            Services.schema.Query, 
            DBConnections.schema.Query, 
            DBConnections.schema2.Query,
            graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass

schema = graphene.Schema(query=Query)