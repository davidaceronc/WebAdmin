from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.pagina_inicio,name='base-service'),
    path('servicio/',views.nuevo_servicio,name='servicios'),
    path('servicio/<int:pk>/', views.nueva_consulta,name='servicio'),
]