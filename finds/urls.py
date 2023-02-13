from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('category_list/', CategoryListAPIView.as_view(), name='category_list'),
    path('category_list_update_delete/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_list_update_delete'),
    path('category_create/', CategoryCreateAPIView.as_view(), name='category_create'),


    path('region_list/', RegionListAPIView.as_view(), name='region_list/'),
    path('region_list_update_delete/<int:pk>/', RegionRetrieveUpdateDestroyAPIView.as_view(), name='region_list_update_delete'),
    path('region_create/', RegionCreateAPIView.as_view(), name='region_list/'),


    path('finding_list/', FindsListAPIView.as_view(), name='finding_list/'),
    path('finding_list_update_delete/<int:pk>/', FindsRetrieveUpdateDestroyAPIView.as_view(), name='finding_list_update_delete'),
    path('finding_create/', FindsCreateAPIView.as_view(), name='finding_list'),

]
