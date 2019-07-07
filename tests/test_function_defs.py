import os
import sys
import cv2
import numpy as np
import matplotlib as mpl

class PyifxImage():
	def __init__(self, path, out_path=None, image=None):
		self.path = path
		self.image = cv2.imread(path)
		self.out_path = out_path

	@classmethod
	def from_image(cls, image):
		i = cls(None)
		i.image = image
		return i


def check_path_type(path):
	if os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None

def convert_dir_to_images(dir):
	images = []
	possible_extensions = ['.tif', '.tiff', '.jpg', '.jpeg', '.png', '.raw']

	def add_to_images(idir):
		for f in os.listdir(idir):
		 	if os.path.splitext(f)[1] in possible_extensions:
		 		images.append(cls(os.path.join(idir,f)))
		 	elif os.path.isdir(f):
		 		add_to_images(f)

	add_to_images(dir)
	return images

