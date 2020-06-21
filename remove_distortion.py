"""
This module contains is used to remove distortions from imgaes using cv2.
"""

import cv2
import numpy as np


class DistortionRemover:
    """
    Class used to represent a image and its distortion values.
    Generate Distortion coefficients (D) using calibrate.py

    Attributes:
        image (numpy.array): Image array
        config (dict): Image config containing distortion coefficients (D)

    Methods:
        set_constants(): Set camera matrix (K), distortion coefficients (D)
        image_undist(): Removes distortions from image based on K, D
    """

    def __init__(self, image, config):
        self.image = image
        self.config = config['camera_params']

    def set_constants(self):
        img = self.image
        config = self.config

        height, width = img.shape[:2]

        # Camera matrix (K)
        c_x = width/2.0     # define center x
        c_y = height/2.0    # define center x
        f_x = config['f_x']  # define focal length x
        f_y = config['f_y']  # define focal length x

        cam_mat = np.array([[f_x,     0.,     c_x],
                            [0.,      f_y,    c_y],
                            [0.,      0.,     1.]])

        # Distortion coefficients (D) from calibrate.py
        # k_1 => negative to remove barrel distortion
        k_1 = config['k_1']
        k_2 = config['k_2']
        p_1 = config['p_1']
        p_2 = config['p_2']
        k_3 = config['k_3']

        dist_coeff = np.array([k_1, k_2, p_1, p_2, k_3])

        return cam_mat, dist_coeff

    def image_undist(self):
        img = self.image
        height, width = img.shape[:2]
        cam_mat, dist_coeff = self.set_constants()

        # Generate new camera matrix from parameters
        new_cam_mat, roi = cv2.getOptimalNewCameraMatrix(
            cam_mat, dist_coeff, (width, height), 0)

        # Generate look-up tables for remapping the camera image
        mapx, mapy = cv2.initUndistortRectifyMap(
            cam_mat, dist_coeff, None, new_cam_mat, (width, height), 5)

        # Remap the original image to a new image
        newimg = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

        return newimg
