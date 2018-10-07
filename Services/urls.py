from django.urls import path, include
from . import views

urlpatterns = [
    path('services/', views.base_service, name='base-service'),
    path('services/create', views.ServicesCreateView.as_view(), name='create-service'),
    path('services/<int:pk>/edit', views.ServicesUpdateView.as_view(), name='edit-service'),   
    path('services/list', views.ServicesListView.as_view(), name='list-services'),
    path('services/<int:pk>/delete', views.ServicesDeleteView.as_view(), name='delete-service'),
]