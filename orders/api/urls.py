from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartAPIView.as_view(), name='api-cart'),
    path('orders/', views.OrderListAPIView.as_view(), name='api-order-list'),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='api-order-detail'),
    path('checkout/', views.CheckoutAPIView.as_view(), name='api-checkout'),
] 