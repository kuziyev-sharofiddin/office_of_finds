from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView, DestroyAPIView, UpdateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer



class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = RegionSerializer


class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegionSerializer

class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegionSerializer



class FindsListAPIView(ListAPIView):
    queryset = Finds.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields =['title','types','description', 'region__name','category__name','tag','lost_time','created_at']
    serializer_class = FindsSerializer


class FindsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Finds.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FindsSerializer

class FindsCreateAPIView(CreateAPIView):
    queryset = Finds.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FindsSerializer
