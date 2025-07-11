from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(path, size, text, bg_color=(220, 220, 220), text_color=(80, 80, 80)):
    """Create a placeholder image with text"""
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw a border
    draw.rectangle([(0, 0), (size[0]-1, size[1]-1)], outline=(180, 180, 180))
    
    # Add text
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", size=24)
    except IOError:
        # Fall back to default font
        font = ImageFont.load_default()
    
    # Position text in the center (approximate for default font)
    text_width = 100  # Default approximate width
    text_height = 20  # Default approximate height
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    draw.text(position, text, fill=text_color, font=font)
    
    # Save the image
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print(f"Created image: {path}")

# Create hero image
hero_path = 'static/images/hero-food.jpg'
create_placeholder_image(hero_path, (1200, 600), "Hero Food Image", bg_color=(255, 200, 200))

# Create mobile app image
app_path = 'static/images/mobile-app.png'
create_placeholder_image(app_path, (600, 800), "Mobile App Image", bg_color=(200, 200, 255))

print("All placeholder images created successfully!") 