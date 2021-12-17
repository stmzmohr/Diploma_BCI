#!/usr/bin/env python3
# File name: main.py
# Author: Moritz Mohr
# Date created: 2021/12/17
# Date last modified: 2021/12/17

# =============================================================================
# Imports
# =============================================================================

from bing_image_downloader import downloader

from MP4_Converter import MP4_Converter

# =============================================================================
# Method
# =============================================================================

# user inputs, search word and number of images
search = input("search for:")
number_images = int(input("How many images do you want to download?:"))


# using bing_image_downloader to download a predefined number of images into a new directory "/search"
downloader.download(search, number_images, output_dir='',adult_filter_off=True, force_replace=False, timeout=10)
# defining directory with images

path_to_images = input("path to images: ")

#launching the MP4_Converter

converter = MP4_Converter(path_to_images)
# print("Converter Path: ", converter.path_to_images)

converter.resize_images()
converter.generate_video('video')









