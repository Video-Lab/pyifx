"""This file contains tests for new features/changes that haven't been designated to a file yet. Feel free to use this function as a playground to test your changes & additions."""
from test_vars import *
import sys


set_paths("../tests/imgs/misc/PyifxImage/set_input_path")
sys.path.append("../tests/imgs/")

img1.set_input_path("512x512-jpeg-1.jpg")
img1.set_output_path("OUT-512x512-jpeg-1.jpg")

pyifx.hsl.darken(img1, 100)