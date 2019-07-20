from INTERNAL import *

def _resize_handler(img_paths, new_size, write=True):

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = [] 

		for img in img_paths.volume:
			new_vol.volume.append(_resize_operation(img, new_size, write=write))

		return new_vol

	elif type(img_paths) == misc.PyifxImage:
		return _resize_operation(img_paths, new_size, write=write)

	elif type(img_paths) == list:
		new_imgs = []

		for img in img_paths:

			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			new_imgs.append(_resize_operation(img, new_size, write=write))

		return new_imgs

	else:
		raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")


def _resize_operation(img, new_size, write=True):
	img_size = [int(d) for d in new_size.split('x')]
	img_size.append(3)
	img_size[0], img_size[1] = img_size[1], img_size[0]

	width_factor = img_size[1]/img.image.shape[1]
	height_factor = img_size[0]/img.image.shape[0]

	new_img = np.full(shape=img_size, fill_value=None)

	for r in range(len(new_img)):
		for p in range(len(new_img[r])):
			for c in range(len(new_img[r][p])):

				if new_img[r][p][c] != None:
						new_img[r][p][c] += img.image[math.floor(r/height_factor)][math.floor(p/width_factor)][c]
						new_img[r][p][c] = math.floor(new_img[r][p][c]/2)
				else:
					new_img[r][p][c] = img.image[math.floor(r/height_factor)][math.floor(p/width_factor)][c]

	new_img = misc.PyifxImage(img.path, img.output_path, new_img, False)

	if write:
		_write_file(new_img)

	return new_img




def _change_file_type_handler(img_paths, new_type, write=True):
	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = [] 

		for img in img_paths.volume:
			new_vol.volume.append(_change_file_type_operation(img, new_type, write=write))

		return new_vol

	elif type(img_paths) == misc.PyifxImage:
		return _change_file_type_operation(img, new_type, write=write)

	elif type(img_paths) == list:
		new_imgs = []

		for img in img_paths:

			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			new_imgs.append(_change_file_type_operation(img, new_type, write=write))

		return new_imgs

	else:
		raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _change_file_type_operation(img, new_type, write=True):
	pass