import graphene
from graphene_django.types import DjangoObjectType
from .models import Service, Location, MissingItem, Office, SQLQuery

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class MissingItemType(DjangoObjectType):
    class Meta:
        model = MissingItem

class OfficeType(DjangoObjectType):
    class Meta:
        model = Office

class SQLQueryType(DjangoObjectType):
    class Meta:
        model = SQLQuery


class Query(graphene.AbstractType):
    all_services = graphene.List(ServiceType)
    all_locations = graphene.List(LocationType)
    all_items = graphene.List(MissingItemType)
    all_offices = graphene.List(OfficeType)
    all_querys = graphene.List(SQLQueryType)
    service = graphene.Field(ServiceType,id=graphene.Int())
    location = graphene.Field(LocationType,id=graphene.Int())
    item = graphene.Field(MissingItemType,id=graphene.Int())
    office = graphene.Field(OfficeType,id=graphene.Int())
    query = graphene.Field(SQLQueryType,id=graphene.Int())

    def resolve_all_services(self, args):
        return Service.objects.all()

    def resolve_all_locations(self, args):
        return Service.objects.all()

    def resolve_all_items(self, args):
        return Service.objects.all()

    def resolve_all_offices(self, args):
        return Office.objects.all()

    def resolve_all_querys(self, args):
        return Service.objects.all()

    def resolve_service(self, args):
        id = args.get('id')

        if id is not None:
            return Service.objects.get(pk=id)

        return None

    def resolve_location(self, args, context, info):
        id = args.get('id')
        source = Service.objects.get(pk=id)

        if source is not None:
            return Location.objects.get(Service=source)

        return None

    def resolve_item(self, args, context, info):
        id = args.get('id')
        source = Service.objects.get(pk=id)

        if source is not None:
            return MissingItem.objects.get(Service=source)

        return None

    def resolve_office(self, args, context, info):
        id = args.get('id')
        source = Service.objects.get(pk=id)

        if source is not None:
            return Office.objects.get(Service=source)

        return None

    def resolve_query(self, args, context, info):
        id = args.get('id')
        source = Service.objects.get(pk=id)

        if source is not None:
            return SQLQuery.objects.get(Service=source)

        return None