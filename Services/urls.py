from django.urls import path, include
from . import views

urlpatterns = [
    # Servicio
    path('services/', views.base_service, name='base-service'),
    path('services/list', views.ServiceListView.as_view(), name='service-list'),
    path('services/create', views.ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/edit', views.ServiceUpdateView.as_view(), name='service-edit'),   
    path('services/<int:pk>/delete', views.ServiceDeleteView.as_view(), name='service-delete'),

    # Catalogo de objetos perdidos
    path('services/items/list', views.MissingItemListView.as_view(), name='item-list'),
    path('services/items/<int:service_id>/configure', views.item_configure, name='item-configure'),
    path('services/items/<int:service_id>/create', views.item_create, name='item-create'),
    path('services/items/<int:service_id>/<int:pk>/edit', views.MissingItemUpdateView.as_view(), name='item-edit'),   
    path('services/items/<int:service_id>/<int:pk>/delete', views.MissingItemDeleteView.as_view(), name='item-delete'),

    # Directorio de dependencias
    path('services/offices/list', views.OfficeListView.as_view(), name='office-list'),
    path('services/offices/<int:service_id>/configure', views.office_configure, name='office-configure'),
    path('services/offices/<int:service_id>/create', views.office_create, name='office-create'),
    path('services/offices/<int:service_id>/<int:pk>/edit', views.OfficeUpdateView.as_view(), name='office-edit'),   
    path('services/offices/<int:service_id>/<int:pk>/delete', views.OfficeDeleteView.as_view(), name='office-delete'),

    # Mapa de Bloques
    path('services/locations/list', views.LocationListView.as_view(), name='location-list'),
    path('services/locations/<int:service_id>/configure', views.location_configure, name='location-configure'),
    path('services/locations/<int:service_id>/create', views.location_create, name='location-create'),
    path('services/locations/<int:service_id>/<int:pk>/edit', views.LocationUpdateView.as_view(), name='location-edit'),   
    path('services/locations/<int:service_id>/<int:pk>/delete', views.LocationDeleteView.as_view(), name='location-delete'),

    # Consulta SQL
    path('services/query/list', views.SQLQueryListView.as_view(), name='query-list'),
    path('services/query/<int:service_id>/configure', views.query_configure, name='query-configure'),
]