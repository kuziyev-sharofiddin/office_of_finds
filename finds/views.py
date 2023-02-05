from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters


    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class FindsViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    serializer_class = FindsSerializer
    queryset = Finds.objects.all()
    
