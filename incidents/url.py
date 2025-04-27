from django.urls import path
from . import views

urlpatterns = [
    path('incidents', views.get_all_incidents, name='get_all_incidents'),
    path('incidents/', views.get_all_incidents, name='get_all_incidents'),  # with trailing slash
    path('incidents/<int:id>', views.get_incident_by_id, name='get_incident_by_id'),
    path('incidents/<int:id>/', views.get_incident_by_id, name='get_incident_by_id'),  # with trailing slash
    path('incidents', views.create_incident, name='create_incident'),
    path('incidents/', views.create_incident, name='create_incident'),
    path('incidents/<int:id>', views.delete_incident, name='delete_incident'),
    path('incidents/<int:id>/', views.delete_incident, name='delete_incident'),
]
