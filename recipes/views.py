from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Recipe, Category, Review
from .forms import RecipeForm, ReviewForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        recipes = recipes.filter(category=category)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        recipes = recipes.filter(title__icontains=search_query) | recipes.filter(description__icontains=search_query)
    
    # Pagination
    paginator = Paginator(recipes, 9)  # Show 9 recipes per page
    page = request.GET.get('page')
    recipes = paginator.get_page(page)
    
    context = {
        'recipes': recipes,
        'categories': categories,
        'search_query': search_query,
    }
    
    return render(request, 'recipes/recipe_list.html', context)

@login_required
def my_recipes(request):
    """View for displaying the current user's recipes"""
    recipes = Recipe.objects.filter(author=request.user)
    
    # Pagination
    paginator = Paginator(recipes, 9)  # Show 9 recipes per page
    page = request.GET.get('page')
    recipes = paginator.get_page(page)
    
    context = {
        'recipes': recipes,
        'title': 'My Recipes',
    }
    
    return render(request, 'recipes/my_recipes.html', context)

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    reviews = recipe.reviews.all()
    
    # Related recipes
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(id=recipe.id)[:3]
    
    context = {
        'recipe': recipe,
        'reviews': reviews,
        'related_recipes': related_recipes,
    }
    
    return render(request, 'recipes/recipe_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    recipes = Recipe.objects.filter(category=category)
    
    # Pagination
    paginator = Paginator(recipes, 9)  # Show 9 recipes per page
    page = request.GET.get('page')
    recipes = paginator.get_page(page)
    
    context = {
        'category': category,
        'recipes': recipes,
    }
    
    return render(request, 'recipes/category_detail.html', context)

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Your recipe has been created!')
            return redirect('recipe-detail', slug=recipe.slug)
    else:
        form = RecipeForm()
    
    context = {
        'form': form,
        'title': 'Create Recipe',
    }
    
    return render(request, 'recipes/recipe_form.html', context)

@login_required
def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Check if user is the author
    if request.user != recipe.author:
        messages.error(request, 'You are not authorized to update this recipe.')
        return redirect('recipe-detail', slug=slug)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your recipe has been updated!')
            return redirect('recipe-detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
    
    context = {
        'form': form,
        'title': 'Update Recipe',
        'recipe': recipe,
    }
    
    return render(request, 'recipes/recipe_form.html', context)

@login_required
def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Check if user is the author
    if request.user != recipe.author:
        messages.error(request, 'You are not authorized to delete this recipe.')
        return redirect('recipe-detail', slug=slug)
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Your recipe has been deleted!')
        return redirect('recipe-list')
    
    context = {
        'recipe': recipe,
    }
    
    return render(request, 'recipes/recipe_confirm_delete.html', context)

@login_required
def add_review(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    # Check if user already reviewed this recipe
    if Review.objects.filter(recipe=recipe, user=request.user).exists():
        messages.error(request, 'You have already reviewed this recipe.')
        return redirect('recipe-detail', slug=slug)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('recipe-detail', slug=slug)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'recipe': recipe,
    }
    
    return render(request, 'recipes/add_review.html', context)
