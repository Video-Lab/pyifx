from INTERNAL_misc import *
from INTERNAL_graphics import *
from INTERNAL import *

def _brightness_operation(img, percent, method):

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

	INTERNAL_misc._write_file(img)
	return img

def _brightness_handler(img_paths, percent, method):
		if type(img_paths) == misc.ImageVolume:

			if not os.path.exists(img_paths.odir):
				os.makedirs(img_paths.odir)

			new_imgs = img_paths.volume

			for img in new_imgs:
				if method == "b" or method == "d":
					_brightness_operation(img, percent, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == misc.PyifxImage:
				if method == "b" or method == "d":
					_brightness_operation(img_paths, percent, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == list:

			for img in img_paths:
				if type(img) != misc.PyifxImage:
					raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
				if method == "b" or method == "d":
					_brightness_operation(img, percent, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _color_overlay_handler(img_paths, color, opacity):

			if type(img_paths) == misc.ImageVolume:
				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_imgs = img_paths.volume

				for img in new_imgs:
					_color_overlay_operation(img, color, opacity)

			elif type(img_paths) == misc.PyifxImage:
				_color_overlay_operation(img_paths, color, opacity)

			elif type(img_paths) == list:

				for img in img_paths:
					if type(img) != misc.PyifxImage:
						raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

					_color_overlay_operation(img, color, opacity)

			else:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _color_overlay_operation(img, color, opacity):
	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):

				val = img.image[row][p][v]
				diff = color[v] - val
				diff *= opacity
				img.image[row][p][v] += diff


	INTERNAL_misc._write_file(img)
	return img


def _saturation_handler(img_paths, percent, method):
	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			if method == "s" or method == "ds":
				_saturation_operation(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == misc.PyifxImage:
		if method == "s" or method == "ds":
			_saturation_operation(img_paths, percent, method)
		else:
			raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			if method == "s" or method == "ds":
				_saturation_operation(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _saturation_operation(img, percent, method):
	type_map = {"s": 1, "ds": -1}

	for row in range(len(img.image)):
		for p in range(len(img.image[row])):

			gray_val = sum(img.image[row][p])/3
			for v in range(len(img.image[row][p])):

				value = img.image[row][p][v]
				diff = gray_val - value
				pixel_change = diff * (type_map[method]*percent)
				img.image[row][p][v] = max(0, min((img.image[row][p][v]-pixel_change), 255))

	INTERNAL_misc._write_file(img)
	return img