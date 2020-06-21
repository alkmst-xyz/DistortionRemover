# Summary

## Prerequisites:

- python >= 3.7
- cv2 >= 4.2
- numpy >= 1.18
- tqdm (Progress bar : pip install tqdm)

## Files:

- calibrate.py: cv2 script
- common.py: cv2 script

- main.py : Applies image_undist() to images(.bmp) in data folder
- remove_distortion.py: Contains DistortionRemover class
- utils.py: Utilities to read and write images, load config, etc.

## Data:

- calibration_images: Images to get distortion values
- output : Output folder of calibrate.py
- data : Images to remove distortions from
- undist_output : Output folder of image_undist()

# Usage:

## To get image params:

- Run calibrate.py along with file name
- Example:
  - python calibrate.py "calibration_images/chess_board_jpg.jpg"

## To get undistorted images:

- Run main.py
- Outputs undistorted images to output folder

# Future modifications:

- Use calibrate.py to output config.json
- Support different image types

# References

- https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41862-correcting-for-lens-distortions

- https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html
