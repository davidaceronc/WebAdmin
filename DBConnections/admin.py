from django.contrib import admin
from .models import Connection

# Register your models here.

# Registrar el modelo de la base de datos para el administrador.
# Modelo en la base de datos para la conexión.
admin.site.register(Connection)