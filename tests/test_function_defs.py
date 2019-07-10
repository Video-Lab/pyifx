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

def _change_light(img, factor, method):
	
	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):
				value = img.image[row][p][v]
				if method == "b":
					img.image[row][p][v] = min(255, value*(1+factor)-(value/6))
				elif method == "d":
					img.image[row][p][v] = max(0, value*(1-factor)+(value/6))
				else:
					raise Exception("Something went wrong. Please try again.")

	out_path, extension = os.path.splitext(img.output_path)
	file_count = 1
	temp_path = out_path

	while os.path.isfile(out_path + extension):
		out_path = temp_path
		out_path += f" ({file_count})"
		file_count += 1

	imageio.imwrite(out_path + extension, img.image)
	return img

def _brightness(img_paths, factor, method):
		if type(img_paths) == ImageVolume:

			if not os.path.exists(img_paths.odir):
				os.makedirs(img_paths.odir)

			new_imgs = img_paths.volume

			for img in new_imgs:
				if method == "b" or method == "d":
					_change_light(img, factor, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == PyifxImage:
				if method == "b" or method == "d":
					_change_light(img_paths, factor, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == list:

			for img in img_paths:
				if type(img) != PyifxImage:
					raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
				if method == "b" or method == "d":
					_change_light(img, factor, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")


def _color_overlay(img_paths, color, opacity):
			if type(img_paths) == ImageVolume:

				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_imgs = img_paths.volume

				for img in new_imgs:
					_add_color_overlay(img, color, opacity)

			elif type(img_paths) == PyifxImage:
				_add_color_overlay(img_paths, color, opacity )

			elif type(img_paths) == list:

				for img in img_paths:
					if type(img) != PyifxImage:
						raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

					_add_color_overlay(img, color, opacity)

			else:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _add_color_overlay(img, color, opacity):
	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):

				val = img.image[row][p][v]
				diff = color[v] - val
				diff *= opacity
				img.image[row][p][v] += diff


	_write_file(img)
	return img

def _saturation(img_paths, percent, method):
	if type(img_paths) == ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			if method == "s" or method == "ds":
				_saturate(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == PyifxImage:

		if method == "s" or method == "ds":
			_saturate(img_paths, percent, method)

		else:
			raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			if method == "s" or method == "ds":
				_saturate(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _saturate(img, percent, method):
	type_map = {"s": 1, "ds": -1}

	for row in range(len(img.image)):
		for p in range(len(img.image[row])):

			gray_val = sum(img.image[row][p])/3
			for v in range(len(img.image[row][p])):

				value = img.image[row][p][v]
				diff = gray_val - value
				pixel_change = diff * (type_map[method]*percent)
				img.image[row][p][v] = max(0, min((img.image[row][p][v]-pixel_change), 255))
	
	_write_file(img)
	return img

def _write_file(img):
	out_path, extension = os.path.splitext(img.output_path)

	if not os.path.exists(os.path.split(img.output_path)[0]):
		os.makedirs(os.path.split(img.output_path)[0])	

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
		self.volume = self.volume_to_list()

	def volume_to_list(self):
		old_imgs = convert_dir_to_images(self.idir)
		new_imgs = [PyifxImage(img, os.path.join(self.odir,f"{self.prefix}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs

# hsl.py

def brighten(img_paths,factor=0.45):
	_brightness(img_paths, factor, "b")

def darken(img_paths,factor=0.45):
	_brightness(img_paths, factor, "d")

def color_overlay(img_paths, color, opacity=0.3):
	_color_overlay(img_paths, color, opacity)

def saturate(img_paths, percent=30):
	_saturation(img_paths, max(0, min(percent, 100))/100, "s")

def desaturate(img_paths, percent=30):
	_saturation(img_paths, max(0, min(percent, 100))/100, "ds")

def to_grayscale(img_paths):
	_saturation(img_paths, 1, "ds")