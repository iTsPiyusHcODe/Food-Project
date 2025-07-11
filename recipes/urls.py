from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('category/<slug:slug>/', views.category_detail, name='category-detail'),
    path('my-recipes/', views.my_recipes, name='my-recipes'),
    path('<slug:slug>/', views.recipe_detail, name='recipe-detail'),
    path('create/', views.recipe_create, name='recipe-create'),
    path('<slug:slug>/update/', views.recipe_update, name='recipe-update'),
    path('<slug:slug>/delete/', views.recipe_delete, name='recipe-delete'),
    path('<slug:slug>/review/', views.add_review, name='add-review'),
] 