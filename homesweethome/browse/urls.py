from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.testing_df, name='testing_df'),
    path('list', views.property_list.as_view(), name='property_list'),
]