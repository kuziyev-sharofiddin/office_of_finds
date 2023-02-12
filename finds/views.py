from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter



    
class CategoryViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class RegionViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class FindsViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields =['title','types','description', 'region__name','category__name','tag','lost_time','created_at']
    serializer_class = FindsSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Finds.objects.all()
    
