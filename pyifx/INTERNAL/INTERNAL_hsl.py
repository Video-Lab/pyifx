from INTERNAL import *

def _brightness_operation(img, percent, method, write=True):

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
	if write:
		_write_file(img)

	return img

def _brightness_handler(img_paths, percent, method, write=True):
		if type(img_paths) == misc.ImageVolume:

			if not os.path.exists(img_paths.odir):
				os.makedirs(img_paths.odir)

			new_imgs = img_paths.volume

			for img in new_imgs:
				if method == "b" or method == "d":
					return _brightness_operation(img, percent, method, write=write)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == misc.PyifxImage:
				if method == "b" or method == "d":
					return _brightness_operation(img_paths, percent, method, write=write)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == list:

			for img in img_paths:
				if type(img) != misc.PyifxImage:
					raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
				if method == "b" or method == "d":
					return _brightness_operation(img, percent, method, write=write)
				else:
					raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _color_overlay_handler(img_paths, color, opacity, write=True):

			if type(img_paths) == misc.ImageVolume:
				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_imgs = img_paths.volume

				for img in new_imgs:
					return _color_overlay_operation(img, color, opacity, write=write)

			elif type(img_paths) == misc.PyifxImage:
				return _color_overlay_operation(img_paths, color, opacity, write=write)

			elif type(img_paths) == list:

				for img in img_paths:
					if type(img) != misc.PyifxImage:
						raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

					return _color_overlay_operation(img, color, opacity, write=write)

			else:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _color_overlay_operation(img, color, opacity, write=True):
	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):

				val = img.image[row][p][v]
				diff = color[v] - val
				diff *= opacity
				img.image[row][p][v] += diff

	if write:
		_write_file(img)

	return img


def _saturation_handler(img_paths, percent, method, write=True):
	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			if method == "s" or method == "ds":
				return _saturation_operation(img, percent, method, write=write)
			else:
				raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == misc.PyifxImage:
		if method == "s" or method == "ds":
			return _saturation_operation(img_paths, percent, method, write=write)
		else:
			raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			if method == "s" or method == "ds":
				return _saturation_operation(img, percent, method, write=write)
			else:
				raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _saturation_operation(img, percent, method, write=True):
	type_map = {"s": 1, "ds": -1}

	for row in range(len(img.image)):
		for p in range(len(img.image[row])):

			gray_val = sum(img.image[row][p])/3
			for v in range(len(img.image[row][p])):

				value = img.image[row][p][v]
				diff = gray_val - value
				pixel_change = diff * (type_map[method]*percent)
				img.image[row][p][v] = max(0, min((img.image[row][p][v]-pixel_change), 255))

	if write:
		_write_file(img)
		
	return img