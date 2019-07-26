import os
import sys
import numpy as np
import imageio
import math
import pyifx.INTERNAL as INTERNAL

class PyifxImage():
	def __init__(self, path, output_path=None, img=None, create_image=True):
		INTERNAL._type_checker(path, [str, None])
		INTERNAL._type_checker(output_path, [str, None])
		INTERNAL._type_checker(img, [np.ndarray, None])
		INTERNAL._type_checker(create_image, [bool])

		self.input_path = path
		self.output_path = output_path
		self.image = img
		if create_image:
			self.image = np.asarray(imageio.imread(path))

	def refresh_image(self):
		self.image = np.asarray(imageio.imread(self.path))

	def get_input_path(self):
		return self.input_path

	def set_input_path(self, new_input_path):
		self.input_path = new_input_path
		self.refresh_image()
		return self

	def get_output_path(self):
		return self.output_path

	def set_output_path(self, new_output_path):
		self.output_path = new_output_path
		return self

	def get_image(self):
		return self.image

	def set_image(self, new_image):
		self.image = new_image
		return self

	
class ImageVolume():
	def __init__(self, input_path, output_path, prefix="_"):
		INTERNAL._type_checker(i, [str])
		INTERNAL._type_checker(o, [str])
		INTERNAL._type_checker(p, [str])

		self.input_path = input_path
		self.onput_path = output_path
		self.prefix = prefix
		self.volume = self.volume_to_list()

	def volume_to_list(self, convert=False): # Add if conversion needed, if create image needed
		INTERNAL._type_checker(self.get_input_path(), [str])
		INTERNAL._type_checker(self.get_output_path(), [str])
		INTERNAL._type_checker(self.get_prefix(), [str])
		
		old_imgs = INTERNAL._convert_dir_to_images(self.get_input_path(), convert)
		new_imgs = [PyifxImage(img, os.path.join(self.get_output_path(),f"{self.get_prefix()}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs

	def get_input_path(self):
		return self.input_path

	def set_input_path(self, new_input_path):
		self.input_path = new_input_path
		self.volume = self.volume_to_list()
		return self

	def get_output_path(self):
		return self.output_path

	def set_output_path(self, new_output_path):
		self.output_path = new_output_path
		self.volume = self.volume_to_list()
		return self

	def get_prefix(self):
		return self.prefix

	def set_prefix(self, new_prefix):
		self.prefix = new_prefix
		return self

	def get_volume(self):
		return self.volume

	def set_volume(self, new_volume):
		for img in new_volume:
			INTERNAL._type_checker(img, [PyifxImage])
		self.volume = new_volume
		return self


def combine(img1, img2, out_path):
	INTERNAL._type_checker(img1, [PyifxImage])
	INTERNAL._type_checker(img2, [PyifxImage])
	INTERNAL._type_checker(out_path, [str])

	if img1.get_image().shape[0]*img1.get_image().shape[0] <= img2.get_image().shape[0]*img2.get_image().shape[1]:
		shape = img1.get_image().shape
	else:
		shape = img2.get_image().shape

	new_img = np.empty(shape)

	for r in range(len(img1.image)):
		for p in range(len(img1.image[r])):
			for c in range(len(img1.image[r][p])):
				try:
					new_img[r][p][c] = min(255, max(0, (img1.get_image()[r][p][c]+img2.get_image()[r][p][c])/2))
				except IndexError:
					pass

	img = PyifxImage(None, out_path, new_img, False)
	return img

