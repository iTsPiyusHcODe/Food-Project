from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Order, OrderItem
from recipes.models import Recipe
from .serializers import OrderSerializer, OrderItemSerializer, CartItemSerializer, CheckoutSerializer

class OrderListAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class CartAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get cart from session
        cart_items = request.session.get('cart', {})
        items = []
        total = 0
        
        # Get recipe details for each item in cart
        for recipe_id, quantity in cart_items.items():
            try:
                recipe = Recipe.objects.get(id=recipe_id)
                subtotal = recipe.price * quantity
                total += subtotal
                items.append({
                    'recipe_id': recipe.id,
                    'recipe': recipe,
                    'quantity': quantity,
                    'subtotal': subtotal
                })
            except Recipe.DoesNotExist:
                # Remove invalid recipe from cart
                del cart_items[recipe_id]
                request.session['cart'] = cart_items
                request.session.modified = True
        
        serializer = CartItemSerializer(items, many=True)
        
        return Response({
            'items': serializer.data,
            'total': total,
            'item_count': sum(cart_items.values())
        })
    
    def post(self, request):
        recipe_id = request.data.get('recipe_id')
        quantity = int(request.data.get('quantity', 1))
        
        if quantity <= 0:
            return Response(
                {'error': 'Quantity must be greater than 0'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            
            # Check if recipe is available for order
            if not recipe.available_for_order:
                return Response(
                    {'error': 'This recipe is not available for ordering'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get or create cart in session
            cart = request.session.get('cart', {})
            
            # Convert recipe_id to string because session keys must be strings
            recipe_id_str = str(recipe_id)
            
            # Add to cart or update quantity
            if recipe_id_str in cart:
                cart[recipe_id_str] += quantity
            else:
                cart[recipe_id_str] = quantity
            
            # Save cart back to session
            request.session['cart'] = cart
            request.session.modified = True
            
            return Response({
                'status': 'success',
                'message': f'Added {recipe.title} to your cart',
                'cart_count': sum(cart.values())
            })
            
        except Recipe.DoesNotExist:
            return Response(
                {'error': 'Recipe not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request):
        recipe_id = request.data.get('recipe_id')
        
        # Get cart from session
        cart = request.session.get('cart', {})
        
        # Convert recipe_id to string because session keys must be strings
        recipe_id_str = str(recipe_id)
        
        # Remove from cart
        if recipe_id_str in cart:
            del cart[recipe_id_str]
            request.session['cart'] = cart
            request.session.modified = True
            
            return Response({
                'status': 'success',
                'message': 'Item removed from your cart',
                'cart_count': sum(cart.values())
            })
        
        return Response(
            {'error': 'Item not found in cart'},
            status=status.HTTP_404_NOT_FOUND
        )

class CheckoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        # Get cart from session
        cart_items = request.session.get('cart', {})
        
        # Check if cart is empty
        if not cart_items:
            return Response(
                {'error': 'Your cart is empty'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Calculate total
        total = 0
        items = []
        for recipe_id, quantity in cart_items.items():
            try:
                recipe = Recipe.objects.get(id=recipe_id)
                subtotal = recipe.price * quantity
                total += subtotal
                items.append({
                    'recipe': recipe,
                    'quantity': quantity,
                    'subtotal': subtotal
                })
            except Recipe.DoesNotExist:
                # Remove invalid recipe from cart
                del cart_items[recipe_id]
                request.session['cart'] = cart_items
                request.session.modified = True
        
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            # Create order
            order = Order.objects.create(
                user=request.user,
                full_name=serializer.validated_data['full_name'],
                email=serializer.validated_data['email'],
                phone=serializer.validated_data['phone'],
                address=serializer.validated_data['address'],
                city=serializer.validated_data['city'],
                postal_code=serializer.validated_data['postal_code'],
                total_amount=total,
                payment_method=serializer.validated_data['payment_method'],
                delivery_instructions=serializer.validated_data.get('delivery_instructions', '')
            )
            
            # Create order items
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    recipe=item['recipe'],
                    quantity=item['quantity'],
                    price=item['recipe'].price
                )
            
            # Clear cart
            request.session['cart'] = {}
            request.session.modified = True
            
            # Return order details
            order_serializer = OrderSerializer(order)
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 