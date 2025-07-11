from django.shortcuts import render
from django.db.models import Q

# Create your views here.

def home(request):
    """View for the home page"""
    # Import models here to avoid circular imports
    from recipes.models import Recipe, Category
    
    try:
        # Get popular recipes (can be modified based on your logic)
        popular_recipes = Recipe.objects.all().order_by('-created_at')[:4]
    except Exception as e:
        # Handle case where Recipe model doesn't have created_at field
        popular_recipes = Recipe.objects.all()[:4] if Recipe.objects.exists() else []
    
    # Get categories for display
    categories = Category.objects.all()
    
    context = {
        'popular_recipes': popular_recipes,
        'categories': categories,
    }
    return render(request, 'base/home.html', context)

def about(request):
    """View for the about page"""
    return render(request, 'base/about.html')

def contact(request):
    """View for the contact page"""
    # Handle contact form submission here if needed
    return render(request, 'base/contact.html')
