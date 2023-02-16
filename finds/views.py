from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView, DestroyAPIView, UpdateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
 
class ListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 4


# class CategoryViewSet(viewsets.ViewSet):
#     filter_backends = [SearchFilter]
#     pagination_class = ListPagination
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    pagination_class = ListPagination
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
    filter_backends = [SearchFilter]
    search_fields = ['name']
    pagination_class = ListPagination
    serializer_class = RegionSerializer


class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegionSerializer

class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegionSerializer

class FindingFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=TYPE)
    class Meta:
        model = Finds
        fields = ['type']

class FindsListAPIView(ListAPIView):
    pagination_class = ListPagination
    queryset = Finds.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = FindingFilter
    search_fields = ['title','type','description', 'region__name','category__name','tag','lost_time','created_at']
    serializer_class = FindsDetailSerializer


class FindsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Finds.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FindsSerializer

class FindsCreateAPIView(CreateAPIView):
    queryset = Finds.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FindsSerializer