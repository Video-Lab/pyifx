import os
import sys
import numpy as np
import matplotlib as mpl
import imageio

# import hsl
# import format
# import graphics
# import misc

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

def _change_light(img, percent, method):

	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):
				value = img.image[row][p][v]
				if method == "b":
					img.image[row][p][v] = min(255, value*(1+percent)-(value/6))
				elif method == "d":
					img.image[row][p][v] = max(0, value*(1-percent)-(value/6))
				else:
					raise Exception("Something went wrong. Please try again.")

	_write_file(img)
	return img

def _brightness(img_paths, percent, method):
		if type(img_paths) == misc.ImageVolume:

			if not os.path.exists(img_paths.odir):
				os.makedirs(img_paths.odir)

			new_imgs = img_paths.volume

			for img in new_imgs:
				if method == "b" or method == "d":
					_change_light(img, percent, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == misc.PyifxImage:
				if method == "b" or method == "d":
					_change_light(img_paths, percent, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == list:

			for img in img_paths:
				if type(img) != misc.PyifxImage:
					raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
				if method == "b" or method == "d":
					_change_light(img, percent, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _color_overlay(img_paths, color, opacity):

			if type(img_paths) == misc.ImageVolume:
				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_imgs = img_paths.volume

				for img in new_imgs:
					_add_color_overlay(img, color, opacity)

			elif type(img_paths) == misc.PyifxImage:
				_add_color_overlay(img_paths, color, opacity)

			elif type(img_paths) == list:

				for img in img_paths:
					if type(img) != misc.PyifxImage:
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
	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			if method == "d" or method == "ds":
				_saturate(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == misc.PyifxImage:
		if method == "d" or method == "ds":
			_saturate(img_paths, percent, method)
		else:
			raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			if method == "d" or method == "ds":
				_saturate(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _saturate(img, percent, method):
	type_map = {"d": 1, "ds": -1}

	for row in range(len(img.image)):
		for p in range(len(img.image[row])):

			gray_val = sum(img.image[row][p])/3
			for v in range(len(img.image[row][p])):

			value = img.image[row][p][v]
			diff = gray_val - value
			pixel_change = diff * (type_map[method]*percent)
			img.image[row][p][v] -= pixel_change
	
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