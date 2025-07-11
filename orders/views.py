from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Order, OrderItem
from recipes.models import Recipe
from .forms import OrderForm

@login_required
def cart(request):
    # Get or create cart in session
    cart_items = request.session.get('cart', {})
    items = []
    total = 0
    
    # Get recipe details for each item in cart
    for recipe_id, quantity in cart_items.items():
        recipe = get_object_or_404(Recipe, id=recipe_id)
        subtotal = recipe.price * quantity
        total += subtotal
        items.append({
            'recipe': recipe,
            'quantity': quantity,
            'subtotal': subtotal
        })
    
    context = {
        'items': items,
        'total': total
    }
    
    return render(request, 'orders/cart.html', context)

@login_required
def add_to_cart(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Check if recipe is available for order
    if not recipe.available_for_order:
        messages.error(request, 'This recipe is not available for ordering.')
        return redirect('recipe-detail', slug=recipe.slug)
    
    # Get or create cart in session
    cart = request.session.get('cart', {})
    
    # Convert recipe_id to string because session keys must be strings
    recipe_id_str = str(recipe_id)
    
    # Add to cart or increase quantity
    if recipe_id_str in cart:
        cart[recipe_id_str] += 1
    else:
        cart[recipe_id_str] = 1
    
    # Save cart back to session
    request.session['cart'] = cart
    request.session.modified = True
    
    messages.success(request, f'Added {recipe.title} to your cart.')
    
    # Check if AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'cart_count': sum(cart.values())
        })
    
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    # Get cart from session
    cart = request.session.get('cart', {})
    
    # Convert item_id to string because session keys must be strings
    item_id_str = str(item_id)
    
    # Remove from cart
    if item_id_str in cart:
        del cart[item_id_str]
        request.session['cart'] = cart
        request.session.modified = True
        messages.success(request, 'Item removed from your cart.')
    
    # Check if AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'cart_count': sum(cart.values())
        })
    
    return redirect('cart')

@login_required
def checkout(request):
    # Get cart from session
    cart_items = request.session.get('cart', {})
    
    # Check if cart is empty
    if not cart_items:
        messages.error(request, 'Your cart is empty.')
        return redirect('recipe-list')
    
    # Calculate total
    total = 0
    items = []
    for recipe_id, quantity in cart_items.items():
        recipe = get_object_or_404(Recipe, id=recipe_id)
        subtotal = recipe.price * quantity
        total += subtotal
        items.append({
            'recipe': recipe,
            'quantity': quantity,
            'subtotal': subtotal
        })
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = total
            order.save()
            
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
            
            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order-detail', order_id=order.id)
    else:
        # Pre-fill form with user data
        initial_data = {
            'full_name': f"{request.user.first_name} {request.user.last_name}",
            'email': request.user.email,
        }
        # If user has profile with address and phone, add those too
        if hasattr(request.user, 'profile'):
            if request.user.profile.phone_number:
                initial_data['phone'] = request.user.profile.phone_number
            if request.user.profile.address:
                initial_data['address'] = request.user.profile.address
        
        form = OrderForm(initial=initial_data)
    
    context = {
        'form': form,
        'items': items,
        'total': total
    }
    
    return render(request, 'orders/checkout.html', context)

@login_required
def place_order(request):
    # This is a redirect view for POST-REDIRECT-GET pattern
    return redirect('my-orders')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders
    }
    
    return render(request, 'orders/my_orders.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order
    }
    
    return render(request, 'orders/order_detail.html', context)
