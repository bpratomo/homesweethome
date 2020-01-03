from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics', views.analytics, name='analytics'),
    path('list', views.property_list.as_view(), name='property_list'),
    path('ajax_list', views.property_list_from_event_ajax, name='property_list_from_event_ajax'),

]