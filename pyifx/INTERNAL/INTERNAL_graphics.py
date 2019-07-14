from INTERNAL import *
from INTERNAL_misc import *
from INTERNAL_hsl import *


def _create_kernel(radius, type_kernel, size=(3,3)):

	if len(size) != 2:
		raise ValueError("Incorrect tuple dimensions used.")

	kernel = None

	if type_kernel == "gaussian":

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
		divider = size[0]*size[1]
		kernel = np.array([[1/divider for r in range(size[1])] for h in range(size[0])])

	else:
		raise Exception("Something went wrong. Please try again.")

	kernel = np.flip(kernel, axis=1)

	kernel = _Kernel(kernel, _is_kernel_seperable(kernel))
	return kernel


def _is_kernel_seperable(kernel):
	if int(_rank(kernel)) == 1:
		return True
	else:
		return False


def _convolute_over_image(img, kernel):
	new_img = np.empty(shape=img.image.shape)
	k_height = math.floor(kernel.shape[0]/2)
	k_width = math.floor(kernel.shape[1]/2)

	if k_height == 0:
		k_height = 1

	if k_width == 0:
		k_width = 1

	for r in range(len(img.image)):
		for p in range(len(img.image[r])):
			for c in range(len(img.image[r][p])):
				new_pixel_value = 0

				if k_height == 1:
					for row in range(-k_width, k_width+1):
						try:
							new_pixel_value += img.image[r+row][p+column][c]*kernel[0][column+k_height]
						except IndexError:
							pass

				elif k_width == 1:
					for row in range(-k_width, k_width+1):
						try:
							new_pixel_value += img.image[r+row][p+column][c]*kernel[row+k_width][0]
						except IndexError:
							pass
							
				else:
					for column in range(-k_height, k_height+1):
						for row in range(-k_width, k_width+1):
							try:
								new_pixel_value += img.image[r+row][p+column][c]*kernel[row+k_width][column+k_height]
							except IndexError:
								pass

				new_img[r][p][c] = new_pixel_value	

	new_img = new_img.astype(np.uint8)
	img.image = new_img
	return img

def _convolute(img, kernel):
	if kernel.seperable == False
		return _convolute_over_image(img, kernel.kernel)
	else:
		imgs = []
		for matrix in kernel.seperated_kernel:
			imgs.append(_convolute_over_image(img, matrix))
		return INTERNAL.misc.combine(imgs[0], imgs[1], img.output_path)

def _blur(img_paths, radius, type_kernel, size):

	kernel = _create_kernel(radius, type_kernel, size)	

	if type(img_paths) == misc.ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			_blur_operation(img_paths, kernel)

	elif type(img_paths) == misc.PyifxImage:
		_blur_operation(img, kernel)

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			_blur_operation(img, kernel)

def _blur_operation(img, kernel):
	new_img = _convolute(img, kernel)
	INTERNAL_misc._write_file(new_img)
	return new_img

def _rank(A, atol=1e-13, rtol=0):
    A = np.atleast_2d(A)
    s = np.linalg.svd(A, compute_uv=False)
    tol = max(atol, rtol * s[0])
    rank = int((s >= tol).sum())
    return rank

class _Kernel:
	def __init__(self, kernel, seperable):
		self.seperable = seperable
		if seperable == True:
			self.seperated_kernel = np.array([kernel[0], [c[0] for c in kernel]])
			self.kernel = None

		else:
			self.seperated_kernel = None
			self.kernel = kernel