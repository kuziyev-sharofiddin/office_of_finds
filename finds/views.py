from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter


    
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = CategorySerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = CategorySerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = CategorySerializer(user)
        return Response(serializer.data)

class RegionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Region.objects.all()
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Region.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = RegionSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Region.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = RegionSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Region.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = RegionSerializer(user)
        return Response(serializer.data)


class FindsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Finds.objects.all()
        filter_backends = [filters.SearchFilter]
        search_fields =['title','types','description', 'region__name','category__name','tag','lost_time','created_at']
        serializer = FindsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Finds.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = FindsSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Finds.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = FindsSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Finds.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        permission_classes = [permissions.IsAuthenticated]
        serializer = FindsSerializer(user)
        return Response(serializer.data)


