"""
ImageSpider - Image similarity search using deep learning.
"""
import sys
import os
from typing import Tuple, Optional

def verify_environment() -> bool:
    """
    Verify that we're running in the correct virtual environment
    and all required packages are available.
    
    Returns:
        bool: True if environment is properly set up, False otherwise
    """
    # Check virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Warning: Not running in a virtual environment!")
        print("Please run the script using run.bat")
        return False
    
    # Verify critical packages
    try:
        import torch
        import DeepImageSearch
        import tqdm
        import numpy
        import faiss
    except ImportError as e:
        print(f"Error: Missing required package - {str(e)}")
        print("Please run install.bat to set up the environment correctly")
        return False
        
    return True

def check_gpu() -> Tuple[bool, Optional[str]]:
    """
    Check if GPU is available and return status and device info.
    
    Returns:
        Tuple[bool, Optional[str]]: (is_gpu_available, device_info)
    """
    try:
        import torch
        if torch.cuda.is_available():
            device = torch.cuda.get_device_name(0)
            return True, device
        return False, None
    except Exception as e:
        print(f"Warning: Error checking GPU availability - {e}")
        return False, None

def get_version() -> str:
    """Return the current version of ImageSpider"""
    return __version__

# Package metadata
__version__ = '1.0.0'
__author__ = 'ImageSpider Team'
__description__ = 'Image similarity search using deep learning'
__package_name__ = 'ImageSpider'

# Optional: Initialize colorama for Windows color support
try:
    import colorama
    colorama.init()
except ImportError:
    pass  # Colorama is optional, won't affect core functionality