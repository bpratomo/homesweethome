from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.property_list.as_view(), name='property_list'),
]