from INTERNAL import *

def _blur_handler(img_paths, radius, type_kernel, size, custom=None, write=True):

	kernel = _create_kernel(radius, type_kernel, size, custom=custom)	

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = []

		for img in new_imgs:
			new_vol.volume.append(_blur_operation(img, kernel, write=write))

		return new_vol

	elif type(img_paths) == misc.PyifxImage:
		return _blur_operation(img_paths, kernel, write=write)

	elif type(img_paths) == list:

		new_imgs = []

		for img in img_paths:

			if type(img) != misc.PyifxImage:
				raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")

			new_imgs.append(_blur_operation(img, kernel, write=write))

		return new_imgs

	else:
		raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")	


def _blur_operation(img, kernel, write=True):

	new_img = _convolute_over_image(img, kernel, write=False)
	new_img.image = new_img.image.astype(np.uint8)

	if write:
		_write_file(new_img)

	return new_img


def _convolute_over_image(img, kernel, write=True):

	new_img = np.empty(shape=img.image.shape)
	k_height = math.floor(kernel.shape[0]/2)
	k_width = math.floor(kernel.shape[1]/2)

	for r in range(len(img.image)):
		for p in range(len(img.image[r])):
			for c in range(len(img.image[r][p])):

				new_pixel_value = 0

				for row in range(-k_height, k_height+1):
					for column in range(-k_width, k_width+1):

						try:
							new_pixel_value += img.image[r+column][p+row][c]*kernel[row+k_height][column+k_width]

						except IndexError:
							pass

				new_img[r][p][c] = min(255, max(0, new_pixel_value))	

	new_img = misc.PyifxImage(img.path, img.output_path, new_img, False)

	if write:
		_write_file(new_img)

	return new_img




def _pixelate_handler(img_paths, factor, write=True):

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = []

		for img in new_imgs:
			new_vol.volume.append(_pixelate_operation(img, factor, write=write))

		return new_vol

	elif type(img_paths) == misc.PyifxImage:

		return _pixelate_operation(img_paths, factor, write=write)

	elif type(img_paths) == list:

		new_imgs = []

		for img in img_paths:

			if type(img) != misc.PyifxImage:
				raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")

			new_imgs.append(_pixelate_operation(img, factor, write=write))

		return new_imgs

	else:
		raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")


def _pixelate_operation(img, factor, write=True):

	new_img = np.empty(shape=img.image.shape)

	for r in range(0, len(new_img)-factor, factor+1):
		for p in range(0, len(new_img[r])-factor, factor+1):

			value = img.image[r][p]

			for row_fill in range(r, r+factor+1):
				for column_fill in range(p, p+factor+1):

					new_img[row_fill][column_fill] = value

	new_img = misc.PyifxImage(img.path, img.output_path, new_img, False)

	if write:
		_write_file(new_img)

	return new_img




def _detect_edges_handler(img_paths, write=True):

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = []

		for img in new_imgs:
			new_vol.volume.append(_detect_edges_operation(img, write=write))

		return new_vol

	elif type(img_paths) == misc.PyifxImage:

		return _detect_edges_operation(img_paths, write=write)

	elif type(img_paths) == list:

		new_imgs = []

		for img in img_paths:

			if type(img) != misc.PyifxImage:
				raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")

			new_imgs.append(_detect_edges_operation(img, write=write))

		return new_imgs

	else:
		raise TypeError("Invalid type used: Input contains non-Pyifx images and/or classes.")


def _detect_edges_operation(img, write=True):

	x_dir_kernel = _create_kernel(None, "x-sobel", None)
	y_dir_kernel = _create_kernel(None, "y-sobel", None)

	x_dir_img = hsl.to_grayscale(_convolute_over_image(img, x_dir_kernel), write=False)
	y_dir_img = hsl.to_grayscale(_convolute_over_image(img, y_dir_kernel), write=False)

	edge_img = misc.combine(x_dir_img, y_dir_img, img.output_path)
	edge_img.image = edge_img.image.astype(np.uint8)

	if write:
		_write_file(edge_img)
		
	return edge_img




def _create_kernel(radius, type_kernel, size, custom=None):

	if custom:
		custom = np.array(custom)

		if len(custom.shape) != 2:
			raise ValueError("Invalid value used: Size of kernel must be 2-dimensional. Use the format (h,w) to achieve this.")

		for d in custom.shape:
			if d % 2 == 0:
				raise ValueError("Invalid value used: Kernel must have odd dimension sizes.")

		def _check_if_int(arr):
			for v in arr:
				if type(v) == list:
					_check_if_int(v)
				INTERNAL._type_checker(v, [int, float])

		_check_if_int(custom)		
		return custom

	if size != None:

		if len(size) != 2:
			raise ValueError("Invalid value used: Size of kernel must be 2-dimensional. Use the format (h,w) to achieve this.")

	kernel = None

	if type_kernel == "gaussian":

		if size == None:
			size = int(2*radius)
			if size % 2 == 0:
				size += 1

			size = (size, size)

		m,n = [(ss-1.)/2. for ss in size]
		y,x = np.ogrid[-m:m+1,-n:n+1]
		kernel = np.exp( -(x*x + y*y) / (2.*radius*radius) )
		kernel[ kernel < np.finfo(kernel.dtype).eps*kernel.max() ] = 0
		sumh = kernel.sum()
		if sumh != 0:
			kernel /= sumh

	elif type_kernel == "mean":
		if radius % 2 == 0:
			radius += 1
			
		divider = radius**2
		kernel = np.array([[1/divider for r in range(radius)] for h in range(radius)])

	elif type_kernel == "y-sobel":
		return np.array([[-1,-2,-1], [0,0,0], [1,2,1]])		

	elif type_kernel == "x-sobel":
		return np.array([[-1,0,1], [-2,0,2], [-1,0,1]])

	else:
		raise Exception("An internal error occurred.")

	kernel = np.flip(kernel, axis=1)

	return kernel	