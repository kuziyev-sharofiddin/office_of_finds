from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet, basename='user')


urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
    path('category/create', CategoryCreateAPIView.as_view(), name='category'),


    path('region/', RegionListAPIView.as_view(), name='region'),
    path('region/<int:pk>/', RegionRetrieveUpdateDestroyAPIView.as_view(), name='region'),
    path('region/create', RegionCreateAPIView.as_view(), name='region'),


    path('finding/', FindsListAPIView.as_view(), name='finding'),
    path('finding/<int:pk>/', FindsRetrieveUpdateDestroyAPIView.as_view(), name='finding'),
    path('finding/create', FindsCreateAPIView.as_view(), name='finding'),

]