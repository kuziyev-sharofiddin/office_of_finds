from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('category_list/', CategoryListAPIView.as_view(), name='category'),
    path('category_list_update_delete/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
    path('category_create/', CategoryCreateAPIView.as_view(), name='category'),


    path('region_list/', RegionListAPIView.as_view(), name='region'),
    path('region_list_update_delete/<int:pk>/', RegionRetrieveUpdateDestroyAPIView.as_view(), name='region'),
    path('region_create/', RegionCreateAPIView.as_view(), name='region'),


    path('finding_list/', FindsListAPIView.as_view(), name='finding'),
    path('finding_list_update_delete/<int:pk>/', FindsRetrieveUpdateDestroyAPIView.as_view(), name='finding'),
    path('finding_create/', FindsCreateAPIView.as_view(), name='finding'),

]
