from django.db import models
from DBConnections.models import Connection
#from django.dispatch import receiver
#from django.db.models.signals import post_delete
from django.urls import reverse

# Modelo principal de servicios.
class Service(models.Model):
    kinds = (
        ('sqlquery', 'Consulta SQL'),
        ('item', 'Objetos Perdidos'),
        ('directory', 'Directorio de Dependencias'),
        ('localization', 'Geolocalizacion de Bloques'),
    )

    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=20, choices=kinds)
    permits = models.IntegerField(default=0)
    state = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-list')


# Modelo de configuracion de servicios de consulta SQL
class SQLQuery(models.Model):
    Service = models.OneToOneField(Service, primary_key=True, on_delete="CASCADE",
                                    limit_choices_to={'kind': 'sqlquery'},
                                    related_name="query", related_query_name="query")
    query = models.TextField(max_length=200)
    #Connection = models.ForeignKey(Connection, on_delete='PROTECTED')
    
    def __str__(self):
        return self.Service.name

    def get_absolute_url(self):
        return reverse('query-list')

# Modelos de items individuales, asociados a un servicio general de Objetos Perdidos, Directorio y Geolocalizacion
class MissingItem(models.Model):
    Service = models.ForeignKey(Service, on_delete="CASCADE",
                                limit_choices_to={'kind': 'item'},
                                related_name="items", related_query_name="item")
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=200) 
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(blank=True, upload_to='photos')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-list')

class Office(models.Model):
    Service = models.ForeignKey(Service, on_delete="CASCADE",
                                limit_choices_to={'kind': 'directory'},
                                related_name="offices", related_query_name="office")
    name = models.CharField(max_length=100)
    extension = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('office-list')

class Location(models.Model):
    Service = models.ForeignKey(Service, on_delete="CASCADE",
                                limit_choices_to={'kind': 'localization'},
                                related_name="locations", related_query_name="location")
    name = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location-list')

