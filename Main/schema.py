import graphene
from graphene_django.types import DjangoObjectType
from .models import Configuration

class ConfigurationType(DjangoObjectType):
    class Meta:
        model = Configuration


class Query(graphene.AbstractType):
    all_configurations = graphene.List(ConfigurationType)
    configuration = graphene.Field(ConfigurationType,id=graphene.Int())

    def resolve_all_configurations(self, args):
        return Configuration.objects.all()

    def resolve_configuration(self, args):
        id = args.get('id')

        if id is not None:
            return Configuration.objects.get(pk=id)

        return None