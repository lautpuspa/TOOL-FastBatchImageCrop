# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-08-21

### Added
- New feature: Crop images at exact output dimensions
- Added option to use output width/height as the target crop resolution
- Updated UI controls to reflect the new cropping behavior

### Changed
- Modified rectangle drawing logic to maintain output dimensions ratio
- Updated mousewheel behavior to only affect crop size when not using output dimensions
- Improved the README with detailed usage instructions for the new features

### Fixed
- Fixed missing comma in PNG extension pattern in fileops.py
- Fixed incorrect label for output height entry in ui_imageset.py and ui_video.py
- Updated deprecated Image.ANTIALIAS to Image.Resampling.LANCZOS
- Updated yaml.load to yaml.safe_load to fix security warning
- Initialized current_mouse_x and current_mouse_y in VideoTab to prevent NoneType errors
- Updated requirements.txt with specific versions for all dependencies
- Fixed typo in error message 'At lease one' to 'At least one'

## [1.0.0] - 2022

### Added
- Initial release
- Crop images from videos and image folders with custom aspect ratios
- Resize cropped images automatically
- Extract frames from videos
- Crop images from videos while playing the video
- Save cropped images to different class folders
- Tag images to txt files while cropping
