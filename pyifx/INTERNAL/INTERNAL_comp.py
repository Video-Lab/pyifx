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

					return new_imgs.append(_resize_operation(img, new_size, write=write))
				return new_imgs

			else:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")


def _resize_operation(img, new_size, write=True):
	img_size = [int(d) for d in new_size.split('x')]
	img_size.append(3)
	img_size[0], img_size[1] = img_size[1], img_size[0]

	width_factor = math.floor(img_size[1]/img.image[1])
	height_factor = math.floor(img_size[0]/img.image[0])

	if (img.image[0]*img.image[1] < img_size[0]*img_size[1]):
		return _expand_operation(img, img_size, width_factor, height_factor, write=write)

	else:
		return _compress_operation(img, img_size, width_factor, height_factor, write=write)




def _expand_operation(img, img_size, width_factor, height_factor, write=True):
	
	new_img = np.empty(shape=img_size)

	for r in range(len(img.image)):
		for p in range(len(img.image[r])):

			val = img.image[r][p]
			new_loc = [r*height_factor, p*width_factor]
			new_loc = _out_of_bounds_check(new_loc, img_size)

			for r_new in range(r, new_loc[1]):
				for p_new in range(p, new_loc[0]):
					new_img[r_new][p_new] = val

	new_img = misc.PyifxImage(img.path, img.output_path, new_img)

	if write:
		_write_file(new_img)

	return new_img



def _compress_operation(img, img_size, width_factor, height_factor, write=True):
	pass

def _out_of_bounds_check(new_loc, index_range):
	new_loc = [math.floor(i) for i in new_loc]

	for d in range(len(new_loc)):

		if new_loc[d] > index_range[d]-1:
			new_loc[d] = index_range[d]-1 

	return new_loc
