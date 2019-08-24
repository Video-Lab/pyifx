import os
import sys
import numpy as np
import pyifx

def set_paths(new_path):
	for img in img_list:
		img.set_output_path(os.path.join(new_path, os.path.split(img.get_output_path())[1]))


	img_vol.set_output_path(new_path)

	img1.set_output_path(os.path.join(new_path, os.path.split(img1.get_output_path())[1]))
	img2.set_output_path(os.path.join(new_path, os.path.split(img2.get_output_path())[1]))

def call_error_test(function, arguments):
	try:
		globals()[function](*arguments)
	except Exception:
		print("Error caught successfully.")
		return True

	print(f"ERROR NOT CAUGHT: {function}({args})")
	return False

img1 = pyifx.misc.PyifxImage("../tests/imgs/512x512-jpeg-1.jpg", "../tests/imgs/hsl/brightness/512x512-jpeg-1.jpg")
img2 = pyifx.misc.PyifxImage("../tests/imgs/512x512-png-1.png", "../tests/imgs/hsl/brightness/512x512-png-1.png")

img_vol = pyifx.misc.ImageVolume("../tests/imgs/", "../tests/imgs/hsl/brightness", "VOLUME-")

img_list = [pyifx.misc.PyifxImage("../tests/imgs/512x512-jpeg-1.jpg", "../tests/imgs/hsl/brightness/LIST-512x512-jpeg-1.jpg"), 
pyifx.misc.PyifxImage("../tests/imgs/512x512-png-1.png", "../tests/imgs/hsl/brightness/LIST-512x512-png-1.png"),
pyifx.misc.PyifxImage("../tests/imgs/512x512-jpg-1.jpg", "../tests/imgs/hsl/brightness/LIST-512x512-jpg-1.jpg")]