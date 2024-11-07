"""
Download required models for ImageSpider
"""
import os
import sys
import time
from pathlib import Path
import torch
from torchvision.models import vgg19, VGG19_Weights

def print_status(message: str):
    """Print status message with progress indicator"""
    print(f"[MODEL SETUP] {message}")
    sys.stdout.flush()

def download_models():
    """Download and cache required models"""
    try:
        print_status("Starting model download...")
        print_status("This will download approximately 600MB of data.")
        print_status("Please wait, this may take several minutes depending on your internet speed.")
        
        # Create models directory if it doesn't exist
        models_dir = Path("models")
        models_dir.mkdir(exist_ok=True)
        
        # Download VGG19
        print_status("Downloading VGG19 model...")
        model = vgg19(weights=VGG19_Weights.IMAGENET1K_V1)
        print_status("VGG19 model downloaded successfully!")
        
        # Save model to ensure it's cached
        torch.save(model.state_dict(), models_dir / "vgg19_cached.pth")
        print_status("Model cached successfully!")
        
        return True

    except Exception as e:
        print_status(f"Error downloading models: {e}")
        return False

if __name__ == "__main__":
    if download_models():
        print_status("Model setup completed successfully!")
        sys.exit(0)
    else:
        print_status("Model setup failed!")
        sys.exit(1)
