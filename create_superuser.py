import os
import django
import shutil
from PIL import Image, ImageDraw

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodie_app.settings')
django.setup()

from django.contrib.auth.models import User

# Create default images
def create_default_image(path, size=(300, 300), color=(200, 200, 200)):
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    # Draw a simple shape
    draw.ellipse((100, 100, 200, 200), fill=(150, 150, 150))
    img.save(path)
    print(f"Created default image at {path}")

# Create default profile image
profile_img_path = 'media/default.jpg'
if not os.path.exists(profile_img_path) or os.path.getsize(profile_img_path) == 0:
    create_default_image(profile_img_path)

# Create default recipe image
recipe_img_path = 'media/default_recipe.jpg'
if not os.path.exists(recipe_img_path) or os.path.getsize(recipe_img_path) == 0:
    create_default_image(recipe_img_path, size=(600, 400), color=(220, 220, 220))

# Check if superuser already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created successfully!")
else:
    print("Superuser already exists.") 