from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-api-data/', views.get_api_data, name='get_api_data'),
    path('get-travel-data/', views.get_travel_data, name='get_travel_data'),
]