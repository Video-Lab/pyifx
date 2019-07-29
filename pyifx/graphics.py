import pyifx.INTERNAL as INTERNAL
import pyifx.misc as misc

def blur_gaussian(img_paths, radius=3, size=None, write=True):
	"""blur_gaussian(img_paths, radius=3, size=None, write=True) 
		Takes images(s) and blurs them using a gaussian kernel.

		Parameters:
		img_paths (pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list): The images to be converted.

		radius (int): The radius of the gaussian kernel. If nothing is entered, this parameter will default to 3.

		size (list, NoneType): The dimensions of the gaussian kernel. Must be entered in

		write (bool): Whether to write the resized image(s). 

		Returns:
		PyifxImage instance (pyifx.misc.PyifxImage)
		ImageVolume instance (pyifx.misc.ImageVolume)
		List with elements of type PyifxImage (list)
	"""
	INTERNAL._type_checker(radius, [int, float])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])
	INTERNAL._type_checker(size, [int, list])

	return INTERNAL._blur_handler(img_paths, radius=radius, type_kernel="gaussian", size=size, write=write)

def blur_mean(img_paths, radius=3, write=True):
	"""blur_mean(img_paths, radius=3, write=True) 
		Takes images(s) and blurs them using a mean kernel.

		Parameters:
		img_paths (pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list): The images to be converted.

		radius (int): The radius of the mean kernel. If nothing is entered, this parameter will default to 3.

		write (bool): Whether to write the resized image(s). 

		Returns:
		PyifxImage instance (pyifx.misc.PyifxImage)
		ImageVolume instance (pyifx.misc.ImageVolume)
		List with elements of type PyifxImage (list)
	"""
	INTERNAL._type_checker(radius, [int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	return INTERNAL._blur_handler(img_paths, radius=radius, type_kernel="mean", size=None, write=write)

def pixelate(img_paths, factor=4, write=True):
	INTERNAL._type_checker(factor, [int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	return INTERNAL._pixelate_handler(img_paths, factor, write=write)

def detect_edges(img_paths, write=True):
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	return INTERNAL._detect_edges_handler(img_paths, write=write)

def convolute_custom(img_paths, kernel, write=True):
	INTERNAL._type_checker(kernel, [np.ndarray, list])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	return INTERNAL._blur_handler(img_paths, radius=None, type_kernel=None, size=None, custom=kernel, write=write)