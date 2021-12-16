#!/usr/bin/env python3
# File name: MP4_Converter.py
# Author: Moritz Mohr
# Date created: 2021/12/16
# Date last modified: 2021/12/16

# =============================================================================
# Imports
# =============================================================================
import cv2
from PIL import Image

# =============================================================================
# Method
# =============================================================================

class MP4_Converter():
    """ Takes all .jpg images from a directory, resizes them and generates a MP4 video slideshow """
    def __init__(self):
    # checking the directory
        print("Initializing MP4 Converter...")

    # resizing images
    def resize_images(self):
        print("resizing.. ")

    # converting jpg sequence to MP4
    def generate_video(self):
        print("generating_video...")


# =============================================================================
# Module Test
# =============================================================================
if __name__ == '__main__':
    converter = MP4_Converter()
    converter.resize_images()
    converter.generate_video()

