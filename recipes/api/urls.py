from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipeListAPIView.as_view(), name='api-recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetailAPIView.as_view(), name='api-recipe-detail'),
    path('categories/', views.CategoryListAPIView.as_view(), name='api-category-list'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='api-category-detail'),
    path('recipes/<int:pk>/reviews/', views.ReviewListAPIView.as_view(), name='api-review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='api-review-detail'),
] 