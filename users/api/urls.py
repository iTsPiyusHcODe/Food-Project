from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileAPIView.as_view(), name='api-profile'),
    path('register/', views.RegisterAPIView.as_view(), name='api-register'),
    path('users/', views.UserListAPIView.as_view(), name='api-user-list'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='api-user-detail'),
] 