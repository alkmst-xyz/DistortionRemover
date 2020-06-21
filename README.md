## Prerequisites:

- cv2 >= 4.2
- numpy >= 1.18
- tqdm (Progress bar : pip install tqdm)

## To get camera matrix:

- common.py
- calibrate.py

## To get undistorted images (.bmp):

- main.py : Applies barrel_undist to images(.bmp) in data folder
- remove_distortion.py: Contains the DistortionRemover
- utils.py: Utilities to read and write images, load config, etc.

## Data:

- calibration_images
- data
- output

## Future modifications:

- Calibrate outputs config.json
