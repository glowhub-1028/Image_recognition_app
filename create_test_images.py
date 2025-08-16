#!/usr/bin/env python3
"""
Script to create simple test images for the image recognition app.
Creates basic geometric shapes and colored images for testing.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_sample_images():
    """Create various test images for the image recognition app."""
    
    # Create samples directory
    if not os.path.exists('sample_images'):
        os.makedirs('sample_images')
        print("Created sample_images directory")
    
    # Create different test images
    test_images = [
        {
            'name': 'red_square.jpg',
            'function': create_red_square,
            'description': 'Red square (should be recognized as a simple object)'
        },
        {
            'name': 'blue_circle.jpg',
            'function': create_blue_circle,
            'description': 'Blue circle'
        },
        {
            'name': 'green_triangle.jpg',
            'function': create_green_triangle,
            'description': 'Green triangle'
        },
        {
            'name': 'yellow_rectangle.jpg',
            'function': create_yellow_rectangle,
            'description': 'Yellow rectangle'
        },
        {
            'name': 'colorful_pattern.jpg',
            'function': create_colorful_pattern,
            'description': 'Colorful geometric pattern'
        },
        {
            'name': 'gradient.jpg',
            'function': create_gradient,
            'description': 'Color gradient'
        },
        {
            'name': 'text_image.jpg',
            'function': create_text_image,
            'description': 'Image with text'
        },
        {
            'name': 'checkerboard.jpg',
            'function': create_checkerboard,
            'description': 'Black and white checkerboard'
        }
    ]
    
    print("Creating test images...")
    print("=" * 50)
    
    created_count = 0
    
    for img in test_images:
        try:
            img['function'](f"sample_images/{img['name']}")
            print(f"✓ Created: {img['name']}")
            print(f"  Description: {img['description']}")
            created_count += 1
        except Exception as e:
            print(f"✗ Failed to create {img['name']}: {e}")
        print()
    
    print("=" * 50)
    print(f"Created {created_count}/{len(test_images)} test images")
    
    if created_count > 0:
        print("\nTest images are ready in the 'sample_images' folder!")
        print("You can now test your image recognition app with these images.")
        print("\nTo test:")
        print("1. Run: python image_recognition_app.py")
        print("2. Click 'Upload Image'")
        print("3. Navigate to the 'sample_images' folder")
        print("4. Select any image to test")
        print("\nNote: These are simple geometric shapes, so the AI might not")
        print("recognize them as specific objects, but it will still make predictions!")

def create_red_square(filename):
    """Create a red square image."""
    img = Image.new('RGB', (300, 300), color='red')
    img.save(filename)

def create_blue_circle(filename):
    """Create a blue circle image."""
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)
    draw.ellipse([50, 50, 250, 250], fill='blue')
    img.save(filename)

def create_green_triangle(filename):
    """Create a green triangle image."""
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)
    draw.polygon([(150, 50), (50, 250), (250, 250)], fill='green')
    img.save(filename)

def create_yellow_rectangle(filename):
    """Create a yellow rectangle image."""
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([75, 75, 225, 225], fill='yellow')
    img.save(filename)

def create_colorful_pattern(filename):
    """Create a colorful geometric pattern."""
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for i, color in enumerate(colors):
        x = (i % 3) * 100
        y = (i // 3) * 100
        draw.rectangle([x, y, x + 100, y + 100], fill=color)
    
    img.save(filename)

def create_gradient(filename):
    """Create a color gradient image."""
    img = Image.new('RGB', (300, 300))
    pixels = img.load()
    
    for x in range(300):
        for y in range(300):
            r = int(255 * x / 300)
            g = int(255 * y / 300)
            b = int(255 * (x + y) / 600)
            pixels[x, y] = (r, g, b)
    
    img.save(filename)

def create_text_image(filename):
    """Create an image with text."""
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to use a default font
        font = ImageFont.load_default()
    except:
        font = None
    
    text = "TEST IMAGE"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (300 - text_width) // 2
    y = (300 - text_height) // 2
    
    draw.text((x, y), text, fill='black', font=font)
    img.save(filename)

def create_checkerboard(filename):
    """Create a black and white checkerboard pattern."""
    img = Image.new('RGB', (300, 300))
    pixels = img.load()
    
    square_size = 30
    for x in range(300):
        for y in range(300):
            square_x = x // square_size
            square_y = y // square_size
            if (square_x + square_y) % 2 == 0:
                pixels[x, y] = (255, 255, 255)  # White
            else:
                pixels[x, y] = (0, 0, 0)  # Black
    
    img.save(filename)

def main():
    """Main function to create test images."""
    print("Image Recognition App - Test Image Generator")
    print("=" * 60)
    
    create_sample_images()

if __name__ == "__main__":
    main()
