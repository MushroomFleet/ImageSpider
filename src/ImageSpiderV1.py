"""
ImageSpider V1 - Main processing script for image similarity search
"""
import os
import sys
import time
import shutil
from datetime import datetime
from pathlib import Path
import colorama
from colorama import Fore, Style
from tqdm import tqdm

# Initialize colorama for Windows color support
colorama.init()

def print_stage(stage: str):
    """Print a stage header"""
    print(f"\n{Fore.CYAN}[STAGE] {stage}{Style.RESET_ALL}")
    sys.stdout.flush()

def print_status(message: str, error: bool = False):
    """Print a status message"""
    if error:
        print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}", flush=True)
    else:
        print(f"{Fore.GREEN}[INFO] {message}{Style.RESET_ALL}", flush=True)

def print_progress(message: str):
    """Print a progress message"""
    print(f"{Fore.YELLOW}[PROGRESS] {message}{Style.RESET_ALL}", flush=True)

def cleanup_metadata():
    """Clean up metadata files from previous runs"""
    metadata_dir = Path("metadata-files")
    if metadata_dir.exists():
        try:
            shutil.rmtree(metadata_dir)
            print_status("Cleaned up metadata from previous runs")
        except Exception as e:
            print_status(f"Warning: Failed to clean metadata: {e}", error=True)
            print_status("Continuing with processing anyway...")

def create_output_directory() -> Path:
    """Create output directory in project root"""
    # Get the project root directory (two levels up from current script)
    project_root = Path(__file__).parent.parent
    
    # Create timestamped output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = project_root / "output" / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return output_dir

def main():
    """Main processing function"""
    try:
        # Initialize
        print_stage("Initialization")
        image_folder = os.getenv('IMAGE_FOLDER')
        if not image_folder:
            print_status("IMAGE_FOLDER environment variable not set", error=True)
            return 1

        print_status(f"Processing folder: {image_folder}")

        # Clean up metadata from previous runs
        print_stage("Cleanup")
        cleanup_metadata()

        # Verify imports
        print_stage("Loading Dependencies")
        try:
            import torch
            from PIL import Image
            from DeepImageSearch import Search_Setup
            print_status("All dependencies loaded successfully")
        except ImportError as e:
            print_status(f"Failed to load required dependency: {e}", error=True)
            return 1

        # Check GPU
        if torch.cuda.is_available():
            print_status(f"GPU detected: {torch.cuda.get_device_name(0)}")
        else:
            print_status("No GPU detected, using CPU (processing will be slower)")

        # Scan for images
        print_stage("Scanning for Images")
        valid_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
        image_paths = []
        
        for root, _, files in os.walk(image_folder):
            for file in files:
                if os.path.splitext(file)[1].lower() in valid_extensions:
                    full_path = os.path.join(root, file)
                    if os.path.getsize(full_path) > 0:
                        image_paths.append(full_path)
                        print_progress(f"Found: {file}")

        if not image_paths:
            print_status("No valid images found in specified folder", error=True)
            return 1

        print_status(f"Found {len(image_paths)} valid images")

        # Process images
        print_stage("Processing Images")
        print_progress("Initializing image search engine...")
        st = Search_Setup(image_list=image_paths, model_name='vgg19', pretrained=True)
        
        print_progress("Running image indexing (this may take a while)...")
        with tqdm(total=len(image_paths), desc="Indexing", unit="img") as pbar:
            st.run_index()
            pbar.update(len(image_paths))

        # Generate results
        print_stage("Generating Results")
        output_dir = create_output_directory()
        print_progress(f"Saving results to: {output_dir}")

        # Save summary
        with open(output_dir / "summary.txt", "w") as f:
            f.write(f"Processing Summary\n")
            f.write(f"=================\n\n")
            f.write(f"Processed at: {datetime.now()}\n")
            f.write(f"Input folder: {image_folder}\n")
            f.write(f"Images processed: {len(image_paths)}\n\n")
            f.write("Processed files:\n")
            for img in image_paths:
                f.write(f"- {img}\n")

        # Generate similarity analysis
        if image_paths:
            print_progress("Analyzing image similarities...")
            with open(output_dir / "similar_images.txt", "w") as f:
                f.write("Similarity Analysis Report\n")
                f.write("=======================\n\n")
                
                reference_image = image_paths[0]  # Using first image as reference
                f.write(f"Reference Image:\n")
                f.write(f"- Path: {reference_image}\n")
                f.write(f"- Filename: {os.path.basename(reference_image)}\n")
                f.write("* This is the first image found in the folder\n\n")
                
                similar_images = st.get_similar_images(
                    image_path=reference_image,
                    number_of_images=min(5, len(image_paths))
                )
                
                f.write("Similar Images (in order of similarity):\n")
                f.write("-" * 40 + "\n\n")
                
                for idx, path in similar_images.items():
                    filename = os.path.basename(path)
                    
                    if path == reference_image:
                        f.write(f"{idx+1}. {filename}\n")
                        f.write(f"   Match Level: Reference Image (100% match)\n")
                    else:
                        f.write(f"{idx+1}. {filename}\n")
                        f.write(f"   Match Level: Similar Image #{idx}\n")
                            
                    f.write(f"   Full path: {path}\n\n")
                    print_progress(f"Found match: {filename}")

        print_stage("Processing Complete")
        print_status(f"Results saved to: {output_dir}")
        return 0

    except Exception as e:
        print_status(f"Error during processing: {str(e)}", error=True)
        import traceback
        print(f"{Fore.RED}{traceback.format_exc()}{Style.RESET_ALL}", flush=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())