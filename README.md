## Prerequisites:

- cv2 >= 4.2
- numpy >= 1.18
- tqdm (Progress bar : pip install tqdm)

## To get camera matrix:

- common.py
- calibrate.py

## To get undistorted images (.bmp):

- main.py : Applies image_undist() to images(.bmp) in data folder
- remove_distortion.py: Contains the DistortionRemover
- utils.py: Utilities to read and write images, load config, etc.

## Data:

- calibration_images
- data
- output

## Future modifications:

- Calibrate outputs config.json

## References

-https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41862-correcting-for-lens-distortions

- https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html
