# INTERNAL.py
import os
import sys
import numpy as np
import matplotlib as mpl
import imageio
import math

# INTERNAL.py

def _check_path_type(path):
	if os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None

def _convert_dir_to_images(dirc):
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

def _type_checker(var, types):
	if type(var) in types:
		return True

	raise TypeError("Please use correct variable types.")
	return False

# misc.py

class PyifxImage():
	def __init__(self, path, out_path=None, create_image=True):
		self.path = path
		self.output_path = out_path
		self.image = None
		if create_image == True:
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
		old_imgs = _convert_dir_to_images(self.idir)
		new_imgs = [PyifxImage(img, os.path.join(self.odir,f"{self.prefix}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs

def _combine(img1, img2, out_path):
	if img1.image.shape[0]*img1.image.shape[0] <= img2.image.shape[0]*img2.image.shape[1]:
		shape = img1.image.shape
	else:
		shape = img2.image.shape

	new_img = np.empty(shape)

	for r in range(len(img1.image)):
		for p in range(len(img1.image[r])):
			for c in range(len(img1.image[r][p])):
				try:
					new_img[r][p][c] = min(255, max(0, (img1.image[r][p][c]+img2.image[r][p][c])/2))
				except IndexError:
					pass

	img = PyifxImage(None, out_path, False)
	img.image = new_img.astype(np.uint8)
	return img

#INTERNAL_graphics.py

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

def _blur(img_paths, radius, type_kernel, size):

	kernel = _create_kernel(radius, type_kernel, size)	

	if type(img_paths) == ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			_blur_operation(img, kernel)

	elif type(img_paths) == PyifxImage:
		_blur_operation(img_paths, kernel)

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			_blur_operation(img, kernel)

def _blur_operation(img, kernel):
	new_img = _convolute_over_image(img, kernel)
	_write_file(new_img)
	return new_img

def _pixelate_handler(img_paths, factor):

	if type(img_paths) == ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			_pixelate_operation(img, factor)

	elif type(img_paths) == PyifxImage:
		_pixelate_operation(img_paths, factor)

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			_pixelate_operation(img, factor)

def _pixelate_operation(img, factor):
	
	for r in range(0, len(img.image)-factor, factor+1):
		for p in range(0, len(img.image[r]-factor, factor+1)):
			value = img.image[r][p]

			for row_fill in range(r, r+factor+1):
				for column_fill in range(p, p+factor+1):
					img.image[row_fill][column_fill] = value

	_write_file(img)
	return img

# graphics.py

def blur_gaussian(img_paths, radius=1.5, size=None):
	_type_checker(radius, [int, float])
	_type_checker(img_paths, [PyifxImage, ImageVolume, list])

	_blur(img_paths, radius=radius, type_kernel="gaussian", size=size)

def blur_mean(img_paths, radius=3):
	_type_checker(radius, [int])
	_type_checker(img_paths, [PyifxImage, ImageVolume, list])

	size = (radius, radius)
	_blur(img_paths, radius=radius, type_kernel="mean", size=size)

def pixelate(img_paths, factor=4):
	_type_checker(factor, [int])
	_type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	_pixelate(img_paths, factor)