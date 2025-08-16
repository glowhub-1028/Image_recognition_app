#!/usr/bin/env python3
"""
Script to download and save the complete ImageNet class names.
This ensures we have all 1000 classes that ResNet18 was trained on.
"""

import torchvision
from torchvision.models import ResNet18_Weights

def get_imagenet_classes():
    """Get the complete list of ImageNet class names."""
    try:
        # Get the ImageNet class names from torchvision
        weights = ResNet18_Weights.IMAGENET1K_V1
        class_names = weights.meta["categories"]
        
        print(f"Downloaded {len(class_names)} ImageNet class names")
        return class_names
        
    except Exception as e:
        print(f"Error getting class names: {e}")
        return None

def save_class_names(class_names, filename="imagenet_classes.txt"):
    """Save class names to a text file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for class_name in class_names:
                f.write(f"{class_name}\n")
        
        print(f"Saved {len(class_names)} class names to {filename}")
        return True
        
    except Exception as e:
        print(f"Error saving class names: {e}")
        return False

def main():
    """Main function to download and save ImageNet classes."""
    print("Downloading ImageNet class names...")
    
    class_names = get_imagenet_classes()
    
    if class_names:
        success = save_class_names(class_names)
        if success:
            print("✓ Successfully created imagenet_classes.txt with all 1000 ImageNet classes")
            print("You can now run the image recognition app!")
        else:
            print("✗ Failed to save class names")
    else:
        print("✗ Failed to download class names")

if __name__ == "__main__":
    main()
