""" This is the testing file for the Pyifx library. All function definitions are contained
in the file named "test_function_defs.py" for the purpose of testing. """

import .pyifx
import os
import numpy as np

def set_paths(new_path):
	for img in img_list:
		img.set_output_path(os.path.join(new_path, os.path.split(img.get_output_path())[1]))

	img_vol.set_output_path(os.path.join(new_path, os.path.split(vol.get_output_path())[1]))

	img1.set_output_path(os.path.join(new_path, os.path.split(img1.get_output_path())[1])
	img2.set_output_path(os.path.join(new_path, os.path.split(img2.get_output_path())[1])

img1 = pyifx.misc.PyifxImage("imgs/512x512-jpeg-1.jpg", "imgs/hsl/brightness/512x512-jpeg-1.jpg")
img2 = pyifx.misc.PyifxImage("imgs/512x512-png-1.png", "imgs/hsl/brightness/512x512-png-1.png")

img_vol = pyifx.misc.ImageVolume("imgs/", "imgs/hsl/brightness", "VOLUME-")

img_list = [pyifx.misc.PyifxImage("imgs/512x512-jpeg-1.jpg", "imgs/hsl/brightness/LIST-512x512-jpeg-1.jpg"), 
pyifx.misc.PyifxImage("imgs/512x512-png-1.png", "LIST-imgs/hsl/brightness/512x512-png-1.png"),
pyifx.misc.PyifxImage("imgs/512x512-jpg-1.jpg", "LIST-imgs/hsl/brightness/512x512-jpg-1.jpg")]

# TESTS TODO

# HSL

pyifx.hsl.brighten(img1, percent=50)
pyifx.hsl.darken(img2, percent=50)
pyifx.hsl.brighten(img_vol, percent=70)
pyifx.hsl.darken(img_list, percent=70)

set_paths("imgs/hsl/color_overlay/")

pyifx.hsl.color_overlay(img1, [255,0,0], 60)
pyifx.hsl.color_overlay(img_vol, [0,255,0], 60)
pyifx.hsl.color_overlay(img_list, [0,0,255], 60)

set_paths("imgs/hsl/saturation/")

pyifx.hsl.saturate(img1, 70)
pyifx.hsl.desaturate(img2, 60)
pyifx.hsl.desaturate(img_vol, 30)
pyifx.hsl.to_grayscale(img_list)

# Composition

set_paths("imgs/comp/resize/")

pyifx.comp.resize(img1, "1024x1024")
pyifx.comp.resize(img2, "256x256")
pyifx.comp.resize(img_list, "694x1440")
pyifx.comp.resize(img_vol, "1532x393")

set_paths("imgs/comp/file_type/")

pyifx.comp.change_file_type(img1, '.png')
pyifx.comp.change_file_type(img2, '.jpg')
pyifx.comp.change_file_type(img_list, 'png')
pyifx.comp.change_file_type(img_vol, 'jpeg')

# Graphics

set_paths("imgs/graphics/blur")

pyifx.graphics.blur_gaussian(img1,3)
pyifx.graphics.blur_mean(img2, 3)
pyifx.graphics.blur_gaussian(img_list, 1)
pyifx.graphics.blur_mean(img_vol, 1)

set_paths("imgs/graphics/pixelate")

pyifx.graphics.pixelate(img1, 4)
pyifx.graphics.pixelate(img_list, 2)
pyifx.graphics.pixelate(img_vol, 3)

set_paths("imgs/graphics/edge")

pyifx.graphics.detect_edges(img1)
pyifx.graphics.detect_edges(img_list)
pyifx.graphics.detect_edges(img_vol)

set_paths("imgs/graphics/custom_convolution")

sobel_horizontal_np = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
sobel_vertical = [[-1,-2,-1], [0,0,0], [1,2,1]]
box_blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

pyifx.graphics.convolute_custom(img1, sobel_horizontal_np)
pyifx.graphics.convolute_custom(img_list, sobel_vertical)
pyifx.graphics.convolute_custom(img_vol, box_blur)

# Misc

set_paths("imgs/misc/combine/")

pyifx.misc.combine(img1, img2, "imgs/misc/combine") #TBC

set_paths("imgs/misc/class_functions/")

# TBA


# COMPLETED TESTS

# brighten(ImageVolume("tests/imgs/", "tests/imgs/brightenedImages", "_"), 0.6) - Image volume class test

# brighten(PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/test_ouput.jpg"), 0.6) - Single image test

# imgs = [PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/test_ouput.jpg"),
# PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/test_output_2.jpg")]
# brighten(imgs, 0.6) - List image test 
# brighten(9999, 0.6) - Wrong type test

# brighten(PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/test_existing_file.jpg"), 0.6) - Existing file test

# brighten(img_list[:3], 0.6) 
# darken(img_list[3:], 0.6)

# brighten(img_vol, 0.6)
# darken(img_vol_dark, 0.6)

# brighten(img_1, 0.6)
# darken(img_2, 0.6) 

# brighten(img_list[:3], 0.5)
# darken(img_list[3:], 0.5) - New Combination Tests

# color_overlay(img_1, [128,242,242])
# color_overlay(img_2, [74,24,25], 80) - Color Overlay Tests

# saturate(img_1, 80)
# desaturate(img_2, 80)
# to_grayscale(img_1) - Grayscale Tests

# blur_gaussian(img_1, 6)
# blur_mean(img_2, 6) - Blur Tests

# pixelate(img_1, 3)
# pixelate(img_2, 6) - Pixelation tests

# detect_edges(img_1)
# detect_edges(img_2) - Edge detection tests

# resize(img_1, "1024x1024")
# resize(img_1, "512x1024")
# resize(img_1, "256x256")
# resize(img_2, "768x2549") - Resize tests

# v1.0 TESTS

