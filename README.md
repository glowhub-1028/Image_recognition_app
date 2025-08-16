# Image Recognition Desktop App

A simple Python desktop application for offline image recognition using deep learning. This app uses a pre-trained ResNet18 model to identify objects in uploaded images.

## Features

- **Simple GUI**: Built with tkinter for easy use
- **Offline Operation**: No internet connection required after initial setup
- **Image Upload**: Drag and drop or browse to upload images
- **Real-time Recognition**: Instantly displays predictions with confidence scores
- **Beginner-Friendly**: Perfect for learning and explaining ML concepts

## Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install torch torchvision pillow
   ```

3. **Run the application**:
   ```bash
   python image_recognition_app.py
   ```

## How to Use

1. **Launch the app** by running `python image_recognition_app.py`

2. **Upload an image** by clicking the "Upload Image" button

3. **View the prediction** - the app will display:
   - The uploaded image
   - The predicted object name
   - Confidence percentage

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)

## How It Works

1. **Model Loading**: The app loads a pre-trained ResNet18 model trained on ImageNet
2. **Image Preprocessing**: Uploaded images are resized and normalized for the model
3. **Prediction**: The model analyzes the image and outputs class probabilities
4. **Result Display**: The most likely class is displayed with confidence score

## Technical Details

- **Model**: ResNet18 pre-trained on ImageNet-1K
- **Input Size**: 224x224 pixels
- **Classes**: 1000 ImageNet classes
- **Framework**: PyTorch with torchvision
- **GUI**: tkinter
- **Image Processing**: PIL (Pillow)

## File Structure

```
├── image_recognition_app.py    # Main application
├── imagenet_classes.txt        # ImageNet class names
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## Troubleshooting

### Common Issues

1. **"Model loading failed"**
   - Ensure you have a stable internet connection for the first run
   - The model will be downloaded automatically (~45MB)

2. **"No module named 'torch'"**
   - Install dependencies: `pip install -r requirements.txt`

3. **Slow performance**
   - First run may be slower as the model loads
   - Subsequent predictions will be faster

4. **Memory issues**
   - Close other applications to free up RAM
   - The model requires approximately 500MB of memory

### Performance Tips

- Use images with clear, centered objects for better accuracy
- Avoid very small or blurry images
- The app works best with common objects (animals, vehicles, household items)

## Educational Value

This app is perfect for:
- **Learning AI/ML concepts**: See how neural networks classify images
- **Understanding computer vision**: Observe how models interpret visual data
- **Teaching demonstrations**: Simple interface for explaining AI to others
- **Prototyping**: Base for more complex image recognition applications

## Customization

You can easily modify the app to:
- Use different pre-trained models
- Add support for custom datasets
- Implement batch processing
- Add more detailed analysis features

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.
