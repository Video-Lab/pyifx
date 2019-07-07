import os
import sys
import cv2
import numpy as np
import matplotlib as mpl

class PyifxImage():
	def __init__(self, path, out_path=None, image=None):
		self.path = path
		self.image = np.asarray(cv2.imread(path))
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
	possible_extensions = ['.tif', '.tiff', '.jpg', '.jpeg', '.png', '.raw']

	def add_to_images(idir):
		for f in os.listdir(idir):
		 	if os.path.splitext(f)[1] in possible_extensions:
		 		images.append(cls(os.path.join(idir,f)))
		 	elif os.path.isdir(f):
		 		add_to_images(f)

	add_to_images(dir)
	return images

def brighten(i,oi,factor=0.35):
	image = PyifxImage(i,oi)

	for row in range(len(image.image)):
		for p in range(len(image.image[row])):
			for v in range(len(image.image[row][p])):
				value = image.image[row][p][v]
				image.image[row][p][v] = min(255, value*(1+factor))

	cv2.imwrite(oi, image.image)
	return image

def brighten_multiple(dir,prefix="_",oprefix="pyifx/",factor=0.35):
	old_imgs = convert_dir_to_images(dir)
	new_imgs = {img: os.path.join(oprefix,f"{prefix}{os.path.split[img][1]}")
	for img in old_imgs}

	for i, o in new_imgs.items():
		brighten(i,o,factor)