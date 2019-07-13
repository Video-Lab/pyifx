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

def _change_light(img, factor, method):
	
	for row in range(len(img.image)):
		for p in range(len(img.image[row])):
			for v in range(len(img.image[row][p])):
				value = img.image[row][p][v]
				if method == "b":
					img.image[row][p][v] = min(255, value*(1+factor)-(value/6))
				elif method == "d":
					img.image[row][p][v] = max(0, value*(1-factor)+(value/6))
				else:
					raise Exception("Something went wrong. Please try again.")

	out_path, extension = os.path.splitext(img.output_path)
	file_count = 1
	temp_path = out_path

	while os.path.isfile(out_path + extension):
		out_path = temp_path
		out_path += f" ({file_count})"
		file_count += 1

	imageio.imwrite(out_path + extension, img.image)
	return img

def _brightness(img_paths, factor, method):
		if type(img_paths) == ImageVolume:

			if not os.path.exists(img_paths.odir):
				os.makedirs(img_paths.odir)

			new_imgs = img_paths.volume

			for img in new_imgs:
				if method == "b" or method == "d":
					_change_light(img, factor, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == PyifxImage:
				if method == "b" or method == "d":
					_change_light(img_paths, factor, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		elif type(img_paths) == list:

			for img in img_paths:
				if type(img) != PyifxImage:
					raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
				if method == "b" or method == "d":
					_change_light(img, factor, method)
				else:
					raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")


def _color_overlay(img_paths, color, opacity):
			if type(img_paths) == ImageVolume:

				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_imgs = img_paths.volume

				for img in new_imgs:
					_add_color_overlay(img, color, opacity)

			elif type(img_paths) == PyifxImage:
				_add_color_overlay(img_paths, color, opacity )

			elif type(img_paths) == list:

				for img in img_paths:
					if type(img) != PyifxImage:
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
	if type(img_paths) == ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			if method == "s" or method == "ds":
				_saturate(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == PyifxImage:

		if method == "s" or method == "ds":
			_saturate(img_paths, percent, method)

		else:
			raise Exception("Something went wrong. Please try again.")

	elif type(img_paths) == list:

		for img in img_paths:
			if type(img) != PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			if method == "s" or method == "ds":
				_saturate(img, percent, method)
			else:
				raise Exception("Something went wrong. Please try again.")

		else:
			raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _saturate(img, percent, method):
	type_map = {"s": 1, "ds": -1}

	for row in range(len(img.image)):
		for p in range(len(img.image[row])):

			gray_val = sum(img.image[row][p])/3
			for v in range(len(img.image[row][p])):

				value = img.image[row][p][v]
				diff = gray_val - value
				pixel_change = diff * (type_map[method]*percent)
				img.image[row][p][v] = max(0, min((img.image[row][p][v]-pixel_change), 255))
	
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



# hsl.py

def brighten(img_paths,factor=0.45):
	_brightness(img_paths, factor, "b")

def darken(img_paths,factor=0.45):
	_brightness(img_paths, factor, "d")

def color_overlay(img_paths, color, opacity=0.3):
	_color_overlay(img_paths, color, opacity)

def saturate(img_paths, percent=30):
	_saturation(img_paths, max(0, min(percent, 100))/100, "s")

def desaturate(img_paths, percent=30):
	_saturation(img_paths, max(0, min(percent, 100))/100, "ds")

def to_grayscale(img_paths):
	_saturation(img_paths, 1, "ds")


# graphics.py

def blur_gaussian(img_paths, radius=1.5, size=(3,3)):
	_type_checker(radius, [int, float])
	_type_checker(img_paths, [PyifxImage, ImageVolume, list])
	_blur(img_paths, radius, "gaussian", (int(radius), int(radius)))

def blur_mean(img_paths, radius=3):
	_type_checker(radius, [int])
	_type_checker(img_paths, [PyifxImage, ImageVolume, list])
	radius = (int(radius), int(radius))
	_blur(img_paths, radius[0], type_kernel="mean", size=radius)

#INTERNAL_graphics.py

def _create_kernel(type_kernel, size=(3,3), radius=None):

	if len(size) != 2:
		raise ValueError("Incorrect size tuple used.")

	kernel = None

	if type_kernel == "gaussian":
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

def _convolute(img, kernel):
	if kernel.seperable == False or kernel.seperable == True:

		k_height = math.floor(kernel.kernel.shape[0]/2)
		k_width = math.floor(kernel.kernel.shape[1]/2)		
		new_img = np.zeros(shape=img.image.shape)

		for r in range(len(img.image)):
			for p in range(len(img.image[r])):
				for c in range(len(img.image[r][p])):
					new_pixel_value = 0
					for column in range(-k_height, k_height+1):
						for row in range(-k_width, k_width+1):
							try:
								new_pixel_value += img.image[r+row][p+column][c]*kernel.kernel[row+k_width][column+k_height]
							except IndexError:
								pass


					new_img[r][p][c] = new_pixel_value

		new_img = new_img.astype(np.uint8)
		img.image = new_img
		return img

def _blur(img_paths, radius, type_kernel, size=(3,3)):

	kernel = _create_kernel(type_kernel, size, radius)	

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
	new_img = _convolute(img, kernel)
	_write_file(new_img)
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
			self.kernel = kernel

		else:
			self.seperated_kernel = np.array([kernel[0], [c[0] for c in kernel]])
			self.kernel = kernel