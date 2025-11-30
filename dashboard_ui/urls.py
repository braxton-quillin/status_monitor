
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.ui, name='dashboard'),
    path('add-appliance/', views.add_appliance, name='add_appliance'),
]