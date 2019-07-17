import INTERNAL

def blur_gaussian(img_paths, radius=1.5, size=None):
	INTERNAL._type_checker(radius, [int, float])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	INTERNAL._blur_handler(img_paths, radius=radius, type_kernel="gaussian", size)

def blur_mean(img_paths, radius=3):
	INTERNAL._type_checker(radius, [int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	INTERNAL._blur_handler(img_paths, radius=radius, type_kernel="mean", size=size)

def pixelate(img_paths, factor=4):
	INTERNAL._type_checker(factor, [int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	INTERNAL._pixelate_handler(img_paths, factor)