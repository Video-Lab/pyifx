from INTERNAL import *


def _create_kernel(radius, type_kernel, size):

	if size != None:
		if len(size) != 2:
			raise ValueError("Incorrect tuple dimensions used.")

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

	else:
		raise Exception("Something went wrong. Please try again.")

	kernel = np.flip(kernel, axis=1)

	return kernel

def _convolute_over_image(img, kernel):
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

				new_img[r][p][c] = new_pixel_value	

	new_img = new_img.astype(np.uint8)
	img.image = new_img
	return img

def _blur_handler(img_paths, radius, type_kernel, size):

	kernel = _create_kernel(radius, type_kernel, size)	

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			_blur_operation(img, kernel)

	elif type(img_paths) == misc.PyifxImage:
		_blur_operation(img_paths, kernel)

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			_blur_operation(img, kernel)

def _blur_operation(img, kernel):
	new_img = _convolute_over_image(img, kernel)
	_write_file(new_img)
	return new_img

def _pixelate_handler(img_paths, factor):

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			_pixelate_operation(img, factor)

	elif type(img_paths) == misc.PyifxImage:
		_pixelate_operation(img_paths, factor)

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			_pixelate_operation(img, factor)

def _pixelate_operation(img, factor):
	
	for r in range(0, len(img.image)-factor, factor+1):
		for p in range(0, len(img.image[r])-factor, factor+1):
			value = img.image[r][p]

			for row_fill in range(r, r+factor+1):
				for column_fill in range(p, p+factor+1):
					img.image[row_fill][column_fill] = value

	_write_file(img)
	return img

def _detect_edges_handler(img_paths):
	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			_detect_edges_operation(img)

	elif type(img_paths) == misc.PyifxImage:
		_detect_edges_operation(img_paths)

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			_detect_edges_operation(img)

def _detect_edges_operation(img):
	x_dir_kernel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
	y_dir_kernel = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])

	x_dir_img = hsl.to_grayscale(_convolute_over_image(img, x_dir_kernel))
	y_dir_img = hsl.to_grayscale(_convolute_over_image(img, y_dir_kernel))

	edge_img = misc.combine(x_dir_img, y_dir_img, img.output_path)
	_write_file(edge_img)
	return edge_img


