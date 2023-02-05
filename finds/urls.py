from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('finds/', FindsAPIView.as_view(), name='finds/')
# ]

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'regions', RegionViewSet, basename='regions')
router.register(r'finds', FindsViewSet, basename='finds')
urlpatterns = router.urls