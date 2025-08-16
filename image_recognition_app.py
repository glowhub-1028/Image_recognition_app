import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18, ResNet18_Weights
import os

class ImageRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Recognition App")
        self.root.geometry("600x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize the model
        self.model = None
        self.transform = None
        self.class_names = []
        
        # Load the model and classes
        self.load_model()
        self.load_class_names()
        
        # Create the GUI
        self.create_widgets()
        
    def load_model(self):
        """Load the pre-trained ResNet18 model"""
        try:
            # Load pre-trained ResNet18 model
            self.model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
            self.model.eval()  # Set to evaluation mode
            
            # Define the image transformation
            self.transform = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225]
                )
            ])
            
            print("Model loaded successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {str(e)}")
    
    def load_class_names(self):
        """Load ImageNet class names from file"""
        try:
            if os.path.exists('imagenet_classes.txt'):
                with open('imagenet_classes.txt', 'r', encoding='utf-8') as f:
                    self.class_names = [line.strip() for line in f.readlines()]
                print(f"Loaded {len(self.class_names)} class names")
            else:
                messagebox.showwarning("Warning", "imagenet_classes.txt not found. Using default class names.")
                # Fallback to a few common classes
                self.class_names = [
                    "golden retriever", "labrador retriever", "german shepherd",
                    "cat", "bird", "car", "truck", "bicycle", "person"
                ]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load class names: {str(e)}")
    
    def create_widgets(self):
        """Create the GUI widgets"""
        # Main title
        title_label = tk.Label(
            self.root,
            text="Image Recognition App",
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=10)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Upload an image to recognize objects using AI",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#666666'
        )
        subtitle_label.pack(pady=5)
        
        # Upload button
        self.upload_button = tk.Button(
            self.root,
            text="Upload Image",
            command=self.upload_image,
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.upload_button.pack(pady=10)
        
        # Create a main content frame with scrollbar
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(main_frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Image display area (fixed size)
        self.image_frame = tk.Frame(
            scrollable_frame,
            bg='white',
            relief='solid',
            bd=2,
            width=550,
            height=300
        )
        self.image_frame.pack(pady=10, fill='x')
        self.image_frame.pack_propagate(False)  # Keep fixed size
        
        # Image label
        self.image_label = tk.Label(
            self.image_frame,
            text="No image uploaded",
            font=("Arial", 14),
            bg='white',
            fg='#999999'
        )
        self.image_label.pack(expand=True)
        
        # Prediction result (always visible)
        self.result_label = tk.Label(
            scrollable_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#333333',
            wraplength=350,
            pady=10
        )
        self.result_label.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(
            scrollable_frame,
            text="Ready to upload image",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666666'
        )
        self.status_label.pack(pady=5)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        # scrollbar.pack(side="right", fill="y")
        
        # # Bind mouse wheel to scroll
        # def _on_mousewheel(event):
        #     canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Store canvas reference for later use
        self.canvas = canvas
    
    def upload_image(self):
        """Handle image upload and recognition"""
        # Open file dialog
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.status_label.config(text="Processing image...")
                self.root.update()
                
                # Load and display the image
                self.display_image(file_path)
                
                # Perform prediction
                prediction = self.predict_image(file_path)
                
                # Display result
                self.result_label.config(text=f"Prediction: {prediction}")
                self.status_label.config(text="Prediction completed!")
                
                # Ensure the result is visible by scrolling to it
                self.root.after(100, self.scroll_to_result)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process image: {str(e)}")
                self.status_label.config(text="Error occurred")
    
    def display_image(self, file_path):
        """Display the uploaded image in the GUI"""
        try:
            # Load image with PIL
            image = Image.open(file_path)
            
            # Get original dimensions
            original_width, original_height = image.size
            print(f"Original image size: {original_width}x{original_height}")
            
            # Calculate display size to fit in the frame (400x300)
            frame_width, frame_height = 380, 280  # Leave some margin
            
            # Calculate scaling factor
            scale_x = frame_width / original_width
            scale_y = frame_height / original_height
            scale = min(scale_x, scale_y, 1.0)  # Don't scale up, only down
            
            # Calculate new dimensions
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)
            
            
            print(f"Display size: {new_width}x{new_height}")
            
            # Resize image
            if scale < 1.0:
                image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage for tkinter
            photo = ImageTk.PhotoImage(image)
            
            # Update the image label
            self.image_label.config(image=photo, text="")
            self.image_label.image = photo  # Keep a reference
            
            # Update canvas scroll region to ensure result is visible
            self.canvas.update_idletasks()
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            
        except Exception as e:
            raise Exception(f"Failed to display image: {str(e)}")
    
    def scroll_to_result(self):
        """Scroll the canvas to make the result visible."""
        try:
            # Get the position of the result label
            result_bbox = self.result_label.winfo_bbox()
            if result_bbox:
                # Scroll to show the result
                self.canvas.yview_moveto(1.0)  # Scroll to bottom
        except Exception as e:
            print(f"Could not scroll to result: {e}")
    
    def predict_image(self, file_path):
        """Predict the object in the image using ResNet18"""
        try:
            # Load and preprocess the image
            image = Image.open(file_path).convert('RGB')
            input_tensor = self.transform(image)
            input_batch = input_tensor.unsqueeze(0)  # Add batch dimension
            
            # Perform prediction
            with torch.no_grad():
                output = self.model(input_batch)
            
            # Get the predicted class
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            predicted_class_id = torch.argmax(probabilities).item()
            confidence = probabilities[predicted_class_id].item()
            
            # Debug information
            print(f"Predicted class ID: {predicted_class_id}")
            print(f"Number of class names loaded: {len(self.class_names)}")
            print(f"Confidence: {confidence:.4f}")
            
            # Get class name
            if predicted_class_id < len(self.class_names):
                class_name = self.class_names[predicted_class_id]
                print(f"Class name: {class_name}")
            else:
                class_name = f"Class {predicted_class_id}"
                print(f"Class ID {predicted_class_id} is out of range (max: {len(self.class_names)-1})")
            
            # Format the result
            confidence_percent = confidence * 100
            result = f"{class_name} ({confidence_percent:.1f}%)"
            print(f"Final result: {result}")
            return result
            
        except Exception as e:
            raise Exception(f"Failed to predict image: {str(e)}")

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = ImageRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
