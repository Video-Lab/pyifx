# INTERNAL.py
import os
import sys
import numpy as np
import matplotlib as mpl
import imageio

# INTERNAL.py

def check_path_type(path):
	if os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None

def convert_dir_to_images(dirc):
	images = []
	possible_extensions = ['.jpg', '.jpeg', '.png']

	def add_to_images(idirc):
		for f in os.listdir(idirc):
		 	if os.path.splitext(f)[1] in possible_extensions:
		 		images.append(os.path.join(idirc,f))
		 	elif os.path.isdir(f):
		 		add_to_images(f)

	add_to_images(dirc)
	return images

def _brighten(img,factor=0.35):
	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):
				value = img.image[row][p][v]
				img.image[row][p][v] = min(255, value*(1+factor))

	out_path, extension = os.path.splitext(img.output_path)
	file_count = 1
	temp_path = out_path

	while os.path.isfile(out_path + extension):
		out_path = temp_path
		out_path += f" ({file_count})"
		file_count += 1

	imageio.imwrite(out_path + extension, img.image)
	return img

# misc.py

class PyifxImage():
	def __init__(self, path, out_path=None, create_image=True):
		self.path = path
		self.output_path = out_path
		self.image = None
		if create_image:
			self.image = np.asarray(imageio.imread(path))


	@classmethod
	def from_image(cls, image):
		i = cls(None)
		i.image = image
		return i

class ImageVolume():
	def __init__(self, i, o, p="_"):
		self.idir = i
		self.odir = o
		self.prefix = p

	def volume_to_list(self):
		old_imgs = convert_dir_to_images(self.idir)
		new_imgs = [PyifxImage(img, os.path.join(self.odir,f"{self.prefix}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs

# hsl.py

def brighten(img_paths,factor=0.35):
	if type(img_paths) == ImageVolume:
		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume_to_list()

		for img in new_imgs:
			_brighten(img, factor)

	elif type(img_paths) == PyifxImage:
		_brighten(img_paths, factor)

	elif type(img_paths) == list:
		for img in img_paths:
			if type(img) != PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			else:
				_brighten(img, factor)
	else:
		raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")