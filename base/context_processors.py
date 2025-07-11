def categories_processor(request):
    """Add categories to all templates"""
    try:
        # Import here to avoid circular imports
        from recipes.models import Category
        categories = Category.objects.all()
        footer_categories = categories[:5]  # Limit to 5 categories for footer
    except Exception:
        # Handle case where Category model doesn't exist yet
        categories = []
        footer_categories = []
    
    return {
        'categories': categories,
        'footer_categories': footer_categories,
    } 