#!/usr/bin/env python3
"""
Simple test script to verify the image recognition app components.
Run this before using the main app to ensure everything is set up correctly.
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import tkinter as tk
        print("✓ tkinter imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import tkinter: {e}")
        return False
    
    try:
        from PIL import Image, ImageTk
        print("✓ PIL (Pillow) imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import PIL: {e}")
        return False
    
    try:
        import torch
        print(f"✓ PyTorch imported successfully (version: {torch.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import PyTorch: {e}")
        return False
    
    try:
        import torchvision
        print(f"✓ torchvision imported successfully (version: {torchvision.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import torchvision: {e}")
        return False
    
    return True

def test_model_loading():
    """Test if the ResNet18 model can be loaded."""
    print("\nTesting model loading...")
    
    try:
        from torchvision.models import resnet18, ResNet18_Weights
        model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
        model.eval()
        print("✓ ResNet18 model loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to load model: {e}")
        return False

def test_class_names():
    """Test if the ImageNet classes file exists and can be read."""
    print("\nTesting class names file...")
    
    if not os.path.exists('imagenet_classes.txt'):
        print("✗ imagenet_classes.txt not found")
        return False
    
    try:
        with open('imagenet_classes.txt', 'r', encoding='utf-8') as f:
            classes = [line.strip() for line in f.readlines()]
        
        if len(classes) > 0:
            print(f"✓ Loaded {len(classes)} class names")
            print(f"  First few classes: {classes[:5]}")
            return True
        else:
            print("✗ Class names file is empty")
            return False
    except Exception as e:
        print(f"✗ Failed to read class names: {e}")
        return False

def test_gui_creation():
    """Test if the GUI can be created (without showing it)."""
    print("\nTesting GUI creation...")
    
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Test basic GUI elements
        label = tk.Label(root, text="Test")
        button = tk.Button(root, text="Test")
        
        root.destroy()
        print("✓ GUI elements can be created successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to create GUI: {e}")
        return False

def main():
    """Run all tests."""
    print("Image Recognition App - Component Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_model_loading,
        test_class_names,
        test_gui_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! The app should work correctly.")
        print("\nTo run the app, use: python image_recognition_app.py")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        print("\nMake sure to install all dependencies:")
        print("pip install -r requirements.txt")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
