""" This is the testing file for the Pyifx library. All function definitions are contained
in the file named "test_function_defs.py" for the purpose of testing. """

from test_function_defs import *

img_list = [PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/bright/list/__512x512-jpg-1.jpg"),
PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/bright/list/__512x512-jpeg-1.jpg"),
PyifxImage("tests/imgs/512x512-png-1.png", "tests/imgs/bright/list/__512x512-png-1.png"),
PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/dark/list/__512x512-jpg-1.jpg"),
PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/dark/list/__512x512-jpeg-1.jpg"),
PyifxImage("tests/imgs/512x512-png-1.png", "tests/imgs/dark/list/__512x512-png-1.png")]

img_vol = ImageVolume("tests/imgs/", "tests/imgs/bright/vol/", "__")
img_vol_dark = ImageVolume("tests/imgs", "tests/imgs/dark/vol", "__")

img_1 = PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/bright/single/__512x512-jpg-1.jpg")
img_2 = PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/dark/mult/512x512-jpeg-1.jpg")

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
# darken(img_2, 0.6) - New Combination Tests

# TESTS TODO

brighten(img_list[:3], 0.5)
darken(img_list[3:], 0.5) 

# FAILED TESTS