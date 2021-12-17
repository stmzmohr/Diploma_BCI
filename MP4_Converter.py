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
import os
from pathlib import Path

# =============================================================================
# Method
# =============================================================================

class MP4_Converter():
    """ Takes all .jpg images from a directory, resizes them and generates a MP4 video slideshow """
    def __init__(self, path_to_images):
        """
        path to images - str
        """

        # Initializing Message
        print("Initializing MP4 Converter...")

        # Checking user input, use Enter to skip
        user_input = input("Enter path to image folder or press Enter to skip:")
        if user_input == "":
            self.path_to_images = path_to_images
        else:
            self.path_to_images = input("Enter path to image directory: ")

        print(self.path_to_images)



    # resizing images
    def resize_images(self):
        print("Resizing_images...")

        os.chdir(self.path_to_images)


        # Setting height and width variables
        mean_height = 0
        mean_width = 0

        # checking number of images in directory
        num_of_images = len(os.listdir(self.path_to_images))
        print(num_of_images)

        # iterating through images and summing up width and height
        for file in os.listdir(self.path_to_images):
            im = Image.open(os.path.join(self.path_to_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            # im.show()

        # averaging height and width of all images.
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        print("mean height: ", mean_height)
        print("mean width: ", mean_width)

        # Resizing of the images to give them same width and height
        for file in os.listdir(self.path_to_images):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png") or file.endswith("gif"):
                # opening image using PIL Image
                im = Image.open(os.path.join(self.path_to_images, file))

                # im.size includes the height and width of image
                # width, height = im.size
                # print(width, height)

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(file, 'JPEG', quality=95)  # setting quality
                # printing each resized image name
                print(im.filename.split('\\')[-1], " is resized")

            else:
                print("found unknown file format.", file)
                pass





    # converting jpg sequence to MP4
    def generate_video(self, video_name):
        print("generating_video...")

        video_path = self.path_to_images + video_name + '.mp4'
        os.chdir(self.path_to_images)


        images = [img for img in os.listdir(self.path_to_images)
                  if img.endswith(".jpg") or
                  img.endswith(".jpeg") or
                  img.endswith("png")]

        # Array images should only consider
        # the image files ignoring others if any
        print(images)

        frame = cv2.imread(os.path.join(self.path_to_images, images[0]))

        # setting the frame width, height width
        # the width, height of first image
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name + '.mp4', 0, 1, (width, height))

        # Appending the images to the video one by one
        for image in images:
            video.write(cv2.imread(os.path.join(self.path_to_images, image)))

        # Deallocating memories taken for window creation
        cv2.destroyAllWindows()
        video.release()  # releasing the video generated




# =============================================================================
# Module Test
# =============================================================================
if __name__ == '__main__':

    path_to_images = os.getcwd() + "\\" + "images"

    converter = MP4_Converter(path_to_images)
    # print("Converter Path: ", converter.path_to_images)

    converter.resize_images()
    converter.generate_video('video')


