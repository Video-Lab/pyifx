""" This is the testing file for the Pyifx library. All function definitions are contained
in the file named "test_function_defs.py" for the purpose of testing. """

from test_function_defs import *

img = PyifxImage("tests/512x512-png-1.png")
print(img.path)
print(img.image)
