from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add/<int:recipe_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place-order/', views.place_order, name='place-order'),
    path('my-orders/', views.my_orders, name='my-orders'),
    path('order/<int:order_id>/', views.order_detail, name='order-detail'),
] 