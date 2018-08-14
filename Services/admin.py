from django.contrib import admin
from .models import Service, MissingItem, Location, Office, SQLQuery
# Register your models here.

admin.site.register(Service)
admin.site.register(MissingItem)
admin.site.register(Location)
admin.site.register(SQLQuery)
admin.site.register(Office)