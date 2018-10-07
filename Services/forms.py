from django import forms
from .models import *

#Formulario para gestionar conexión.
class ServiceForm(forms.ModelForm):
    
    class Meta:

        model = Service

        fields = [
            'name',
            'kind',
            'permits',
            'state',
        ]

        labels = {
            'name':'Nombre del Servicio',
            'kind':'Tipo de Servicio',
            'permits':'Permisos de acceso al Servicio',
            'state':'Estado del Servicio',
        }

        error_messages = {
            'name': {
                'unique':"El nombre del servicio ya existe.",
            },
        }