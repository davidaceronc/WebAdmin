from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.base_connection, name='base-connection'),
    path('connection/listdb', views.list_db, name='list-db'),
    path('connection/<int:id_connection>/check', views.check_connection, name='check-connection'),
    path('connection/create', views.ConnectionCreateView.as_view(), name='create-connection'),
    path('connection/<int:pk>/edit', views.ConnectionUpdateView.as_view(), name='edit-connection'),   
    path('connection/list', views.ConnectionListView.as_view(), name='list-connections'),
    path('connection/<int:pk>/delete', views.ConnectionDeleteView.as_view(), name='delete-connection'),
    path('connection/test', views.ConnectionTestView.as_view(), name='test-connection'),
    path('connection/run', views.test_connection, name='run-test'),
]