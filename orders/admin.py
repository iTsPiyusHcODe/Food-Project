from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'payment_method', 'payment_completed', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'address')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'recipe', 'quantity', 'price')
    list_filter = ('order__status',)
    search_fields = ('order__full_name', 'recipe__title')
