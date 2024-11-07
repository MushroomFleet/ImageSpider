# ImageSpider

A tool for image similarity search using deep learning. ImageSpider uses the VGG19 model to identify and match similar images within a specified directory.

## Features

- Deep learning-based image similarity search using VGG19
- Virtual environment isolation for dependency management
- Real-time progress tracking with color-coded feedback
- Support for multiple image formats (PNG, JPG, JPEG, GIF, BMP)
- Timestamped output generation
- GPU acceleration support (optional)
- Automated dependency management

## Requirements

- Python 3.7 or higher
- Windows OS
- 4GB RAM minimum (8GB recommended)
- GPU optional but recommended for better performance
- Approximately 600MB storage for model download

## Directory Structure

```
ImageSpider/
│
├── scripts/           # Batch scripts
│   ├── install.bat    # Sets up virtual environment and installs dependencies
│   ├── run.bat        # Runs the image processing script
│   ├── test.bat       # Tests Python execution
│   └── update.bat     # Updates project dependencies
│
├── src/              # Source code
│   ├── __init__.py
│   ├── ImageSpiderV1.py
│   ├── download_models.py
│   ├── test_output.py
│   └── requirements.txt
│
├── output/           # Generated results (created during runtime)
│   └── YYYYMMDD_HHMMSS/
│       ├── summary.txt           # Processing details and statistics
│       └── similar_images.txt    # Similar image matches and scores
│
├── models/           # Downloaded model cache (created during first run)
│
├── venv/            # Virtual environment (created by install.bat)
│
├── .gitignore
└── README.md
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ImageSpider.git
   cd ImageSpider
   ```

2. Navigate to the scripts directory:
   ```
   cd scripts
   ```

3. Run the installation script:
   ```
   install.bat
   ```
   This will:
   - Create a new virtual environment
   - Install all required dependencies
   - Set up the necessary directory structure

## Usage

1. Navigate to the scripts directory:
   ```
   cd scripts
   ```

2. Run the processing script:
   ```
   run.bat
   ```

3. When prompted, enter the path to your images folder:
   - Can be relative path (e.g., ..\images)
   - Can be absolute path (e.g., C:\Users\YourName\Pictures)

4. The script will:
   - Validate the input path
   - Initialize the processing environment
   - Find all valid images in the specified folder
   - Process and analyze image similarities
   - Generate timestamped output files

5. Monitor Progress:
   The script provides color-coded, real-time feedback:
   - Green: Success messages
   - Yellow: Progress updates
   - Cyan: Stage headers
   - Red: Error messages

## Output

The program generates timestamped output in the `output` directory:
```
output/
└── YYYYMMDD_HHMMSS/
    ├── summary.txt           # Processing details and statistics
    └── similar_images.txt    # Similarity analysis results
```

### Output Files

- `summary.txt`: Contains:
  - Processing timestamp
  - Input folder path
  - Total images processed
  - List of all processed files

- `similar_images.txt`: Contains:
  - Reference image details (first image found in folder)
  - List of similar images in order of similarity
  - Full paths to all matched images
  - Match levels for each similar image

## Processing Stages

1. **Environment Check**:
   - Verifies virtual environment
   - Validates required packages
   - Checks GPU availability

2. **Input Configuration**:
   - Validates input path
   - Converts to absolute path
   - Sets up environment variables

3. **Image Scanning**:
   - Searches for supported image formats
   - Validates file accessibility
   - Reports total valid images found

4. **Processing**:
   - Loads VGG19 model
   - Indexes all images
   - Generates similarity matches

5. **Output Generation**:
   - Creates timestamped output directory
   - Generates summary report
   - Creates similarity analysis report

## Dependencies

Core dependencies:
- numpy==1.24.2
- torch==2.0.0
- torchvision==0.15.1
- faiss_cpu==1.7.3
- matplotlib==3.5.2
- pandas==1.4.3
- Pillow==9.5.0
- timm==0.6.13
- tqdm==4.65.0
- DeepImageSearch==2.5
- colorama==0.4.6

## Updating Dependencies

To update existing dependencies:

1. Navigate to the scripts directory:
   ```
   cd scripts
   ```

2. Run the update script:
   ```
   update.bat
   ```

## Troubleshooting

1. Installation Issues:
   - Ensure Python 3.7+ is installed and in PATH
   - Run install.bat for a clean installation
   - Check console output for specific error messages

2. Processing Issues:
   - Verify image folder path exists
   - Ensure images are in supported formats
   - Check virtual environment is activated (run.bat handles this)

3. Common Error Messages:
   - "Virtual environment not found": Run install.bat first
   - "No valid images found": Check path and image formats
   - "Cannot access the specified path": Check folder permissions
   - "GPU not found": System will use CPU processing

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Uses VGG19 model for image processing
- Built with PyTorch and FAISS
- Progress tracking powered by tqdm
- Terminal enhancements by colorama