from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import RegisterAPIView, LogOutAPIView,UserMeAPIView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('register/', RegisterAPIView.as_view()),
    path('logout/', LogOutAPIView.as_view(), name='logout_view'),
    path('me/', UserMeAPIView.as_view(), name='userme'),
    ]
