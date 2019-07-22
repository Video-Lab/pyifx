from INTERNAL import *

def _brightness_handler(img_paths, percent, method, write=True):
		if type(img_paths) == misc.ImageVolume:

			if not os.path.exists(img_paths.odir):
				os.makedirs(img_paths.odir)

			new_vol = img_paths
			new_vol.volume = []

			for img in img_paths.volume:
				if method == "b" or method == "d":
					new_vol.volume.append(_brightness_operation(img, percent, method, write=write))
				else:
					raise Exception("An internal error occurred.")

			return new_vol

		elif type(img_paths) == misc.PyifxImage:
				if method == "b" or method == "d":
					return _brightness_operation(img_paths, percent, method, write=write)
				else:
					raise Exception("An internal error occurred.")

		elif type(img_paths) == list:
			new_imgs = []

			for img in img_paths:
				if type(img) != misc.PyifxImage:
					raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")
				if method == "b" or method == "d":
					new_imgs.append(_brightness_operation(img, percent, method, write=write))
				else:
					raise Exception("Something went wrong.")
			return new_imgs

		else:
			raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")


def _brightness_operation(img, percent, method, write=True):
	new_img = np.empty(shape=img.image.shape)

	for row in range(len(new_img)):
		for p in range(len(new_img[row])):
			for v in range(len(new_img[row][p])):
				value = img.image[row][p][v]
				if method == "b":
					new_img[row][p][v] = min(255, value*(1+percent)-(value/6))
				elif method == "d":
					new_img[row][p][v] = max(0, value*(1-percent)-(value/6))
				else:
					raise Exception("An internal error occurred.")

	new_img = misc.PyifxImage(img.path, img.output_path, new_img, False)

	if write:
		_write_file(img)

	return new_img




def _color_overlay_handler(img_paths, color, opacity, write=True):

			if type(img_paths) == misc.ImageVolume:
				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_vol = img_paths
				new_vol.volume = [] 

				for img in img_paths.volume:
					new_vol.volume.append(_color_overlay_operation(img, color, opacity, write=write))

				return new_vol

			elif type(img_paths) == misc.PyifxImage:
				return _color_overlay_operation(img_paths, color, opacity, write=write)

			elif type(img_paths) == list:
				new_imgs = []
				for img in img_paths:
					if type(img) != misc.PyifxImage:
						raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")

					return new_imgs.append(_color_overlay_operation(img, color, opacity, write=write))
				return new_imgs

			else:
				raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")


def _color_overlay_operation(img, color, opacity, write=True):
	new_img = np.empty(shape=img.image.shape)

	for row in range(len(new_img)):
		for p in range(len(new_img[row])):
			for v in range(len(new_img[row][p])):

				val = img.image[row][p][v]
				diff = color[v] - val
				diff *= opacity
				new_img[row][p][v] += diff

	new_img = misc.PyifxImage(img.path, img.output_path, new_img, False)

	if write:
		_write_file(img)

	return img




def _saturation_handler(img_paths, percent, method, write=True):
	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = []

		for img in new_imgs:
			if method == "s" or method == "ds":
				new_vol.volume.append(_saturation_operation(img, percent, method, write=write))
			else:
				raise Exception("An internal error occurred.")

		return new_vol

	elif type(img_paths) == misc.PyifxImage:
		if method == "s" or method == "ds":
			return _saturation_operation(img_paths, percent, method, write=write)
		else:
			raise Exception("An internal error occurred.")

	elif type(img_paths) == list:
		new_imgs = []
		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")
			if method == "s" or method == "ds":
				new_imgs.append(_saturation_operation(img, percent, method, write=write))
			else:
				raise Exception("An internal error occurred.")
		return new_imgs

		else:
			raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")


def _saturation_operation(img, percent, method, write=True):
	type_map = {"s": 1, "ds": -1}
	new_img = np.empty(shape=img.image.shape)

	for row in range(len(new_img)):
		for p in range(len(new_img[row])):

			gray_val = sum(img.image[row][p])/3
			for v in range(len(new_img[row][p])):

				value = img.image[row][p][v]
				diff = gray_val - value
				pixel_change = diff * (type_map[method]*percent)
				new_img[row][p][v] = max(0, min((img.image[row][p][v]-pixel_change), 255))

	new_img = misc.PyifxImage(img.path, img.output_path, new_img, False)
	if write:
		_write_file(img)
		
	return img