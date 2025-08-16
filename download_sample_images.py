#!/usr/bin/env python3
"""
Script to download sample images for testing the image recognition app.
Downloads various images of common objects that ResNet18 should recognize well.
"""

import os
import requests
from PIL import Image
from io import BytesIO

def download_image(url, filename):
    """Download an image from URL and save it locally."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Open and save the image
        image = Image.open(BytesIO(response.content))
        image.save(filename)
        print(f"✓ Downloaded: {filename}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def create_sample_images():
    """Create sample images directory and download test images."""
    
    # Create samples directory
    if not os.path.exists('sample_images'):
        os.makedirs('sample_images')
        print("Created sample_images directory")
    
    # Sample images from Unsplash (free stock photos)
    sample_images = [
        {
            'url': 'https://images.unsplash.com/photo-1552053831-71594a27632d?w=400',
            'filename': 'sample_images/dog.jpg',
            'description': 'Golden Retriever dog'
        },
        {
            'url': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=400',
            'filename': 'sample_images/cat.jpg',
            'description': 'Cat'
        },
        {
            'url': 'https://images.unsplash.com/photo-1541963463532-d68292c34b19?w=400',
            'filename': 'sample_images/apple.jpg',
            'description': 'Apple'
        },
        {
            'url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400',
            'filename': 'sample_images/mountain.jpg',
            'description': 'Mountain landscape'
        },
        {
            'url': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=400',
            'filename': 'sample_images/car.jpg',
            'description': 'Car'
        },
        {
            'url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400',
            'filename': 'sample_images/pizza.jpg',
            'description': 'Pizza'
        },
        {
            'url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400',
            'filename': 'sample_images/bird.jpg',
            'description': 'Bird'
        },
        {
            'url': 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=400',
            'filename': 'sample_images/computer.jpg',
            'description': 'Desktop computer'
        }
    ]
    
    print("Downloading sample images...")
    print("=" * 50)
    
    successful_downloads = 0
    
    for img in sample_images:
        if download_image(img['url'], img['filename']):
            successful_downloads += 1
            print(f"  Expected: {img['description']}")
        print()
    
    print("=" * 50)
    print(f"Downloaded {successful_downloads}/{len(sample_images)} sample images")
    
    if successful_downloads > 0:
        print("\nSample images are ready in the 'sample_images' folder!")
        print("You can now test your image recognition app with these images.")
        print("\nTo test:")
        print("1. Run: python image_recognition_app.py")
        print("2. Click 'Upload Image'")
        print("3. Navigate to the 'sample_images' folder")
        print("4. Select any image to test")
    else:
        print("No images were downloaded. Check your internet connection.")

def create_simple_test_image():
    """Create a simple colored square as a fallback test image."""
    try:
        if not os.path.exists('sample_images'):
            os.makedirs('sample_images')
        
        # Create a simple test image
        img = Image.new('RGB', (300, 300), color='red')
        img.save('sample_images/test_square.jpg')
        print("✓ Created simple test image: sample_images/test_square.jpg")
        return True
        
    except Exception as e:
        print(f"✗ Failed to create test image: {e}")
        return False

def main():
    """Main function to download sample images."""
    print("Image Recognition App - Sample Images Downloader")
    print("=" * 60)
    
    try:
        # Try to download from internet
        create_sample_images()
        
    except ImportError:
        print("requests library not found. Creating simple test image instead...")
        create_simple_test_image()
        
    except Exception as e:
        print(f"Error downloading images: {e}")
        print("Creating simple test image instead...")
        create_simple_test_image()

if __name__ == "__main__":
    main()
