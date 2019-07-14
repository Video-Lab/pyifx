""" This is the testing file for the Pyifx library. All function definitions are contained
in the file named "test_function_defs.py" for the purpose of testing. """

from test_function_defs import *

out_path_1 = "tests/imgs/blur/__512x512-jpg-1.jpg"
out_path_2 = "tests/imgs/blur/__512x512-jpeg-1.jpg"

img_list = [PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/bright/list/__512x512-jpg-1.jpg"),
PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/bright/list/__512x512-jpeg-1.jpg"),
PyifxImage("tests/imgs/512x512-png-1.png", "tests/imgs/bright/list/__512x512-png-1.png"),
PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/dark/list/__512x512-jpg-1.jpg"),
PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/dark/list/__512x512-jpeg-1.jpg"),
PyifxImage("tests/imgs/512x512-png-1.png", "tests/imgs/dark/list/__512x512-png-1.png")]

img_vol = ImageVolume("tests/imgs/", "tests/imgs/bright/vol/", "__")
img_vol_dark = ImageVolume("tests/imgs", "tests/imgs/dark/vol", "__")

img_1 = PyifxImage("tests/imgs/512x512-jpg-1.jpg", out_path_1)
img_2 = PyifxImage("tests/imgs/512x512-jpeg-1.jpg", out_path_2)

# TESTS TODO

blur_gaussian(img_1, 3)

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

# FAILED TESTS