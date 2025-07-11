from rest_framework import serializers
from orders.models import Order, OrderItem
from recipes.models import Recipe
from recipes.api.serializers import RecipeSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'recipe', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'full_name', 'email', 'phone', 'address', 'city',
            'postal_code', 'created_at', 'updated_at', 'status', 'total_amount',
            'payment_method', 'payment_completed', 'delivery_instructions', 'items'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at', 'total_amount']

class CartItemSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()
    recipe = RecipeSerializer()
    quantity = serializers.IntegerField()
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2)

class CheckoutSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    address = serializers.CharField()
    city = serializers.CharField(max_length=100)
    postal_code = serializers.CharField(max_length=20)
    payment_method = serializers.CharField(max_length=50)
    delivery_instructions = serializers.CharField(required=False, allow_blank=True) 