import INTERNAL

def blur_gaussian(img_paths, radius=1.5, size=(3,3)):
	INTERNAL._type_checker(radius, [int, float])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])
	INTERNAL._blur(img_paths, radius, "gaussian", size)

def blur_mean(img_paths, radius=3):
	INTERNAL._type_checker(radius, [int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])
	radius = (radius, radius)
	_blur(img_paths, type_kernel="mean", size=radius)