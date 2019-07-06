import os
import sys
import cv2
import numpy as np
import matplotlib as mpl

class _PyfixImage():
	def __init__(self, path,image=None):
		self.path = path
		self.image = cv2.imread(path)

	@classmethod
	def from_image(cls, image):
		i = cls(None)
		i.image = image
		return i


def _check_path_type(path):
	is os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None

def _convert_dir_to_images(dir):
		images = []
	 	possible_extensions = ['.tif', '.tiff', '.jpg', '.jpeg', '.png', '.raw']

	 	for f in os.listdir(dir):
	 		if os.path.splitext(f)[1] in possible_extensions:
	 			images.append(cls(os.path.join(dir,f)))
	 			
	 	return images

