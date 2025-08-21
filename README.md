# TOOL-FastBatchImageCrop
A simple UI tool to batch crop images to prepare datasets with precise dimensions.


![Preview](./mat/preview.gif)

## Key Difference Over Original
**Direct Dimension Cropping:** Unlike the original which only applied dimensions after cropping, this fork allows you to specify and visualize the exact pixel dimensions (e.g., 512×512) of your crop in real-time. The crop rectangle maintains the precise dimensions you need, ensuring consistent dataset images without post-processing distortion.

## Features
- Crop images from videos and image folders with custom aspect ratios
- **NEW**: Crop images at exact output dimensions (e.g., 512x512, 1024x768)
- Resize cropped images automatically
- Extract frames from videos
- Crop images from videos while playing the video
- Save cropped images to different class folders
- Tag images to txt files while cropping

## Usage

Install requirements with:

```bash
pip install -r requirements.txt
```

Run the application with:

```bash
python main.py
```

### Basic Usage
1. Select input folder
2. Choose output folder (defaults to input_folder/out)
3. Select cropping mode:
   - **Aspect Ratio Mode**: Adjust crop rectangle size with mousewheel
   - **NEW - Output Dimensions Mode**: Check "Use Output Dimensions for Crop" to crop at exact pixel dimensions
4. Click on the image to crop
5. Repeat

### Output Dimensions Mode
When "Use Output Dimensions for Crop" is checked:
1. Enter desired width and height in pixels
2. The crop rectangle will maintain these exact dimensions
3. Cropped images will have the exact pixel dimensions specified

**Main Logic Difference:** In the original version, dimensions were only applied after cropping as a scaling operation. This fork modifies the core cropping logic to use your specified dimensions directly for the crop rectangle itself, giving you pixel-perfect crops without distortion.

### Class Names and Descriptions
- Enter class names to save crops in separate directories
- Add image descriptions to create accompanying text files
- Use the Tag Editor to add specific tags to images

### Shortcut Keys
When cursor is on canvas:
- **q**: Rotate image counter-clockwise
- **e**: Rotate image clockwise
- **r**: Toggle roll to next image on crop
- **space**: Roll to next image

## Requirements
- Python 3.6+
- OpenCV
- Pillow (PIL)
- PyYAML
- tkinter

## License
See LICENSE.md file for details.
