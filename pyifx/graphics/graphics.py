import INTERNAL

def blur_gaussian(img_paths, radius=1.5):
	INTERNAL._type_checker(radius, [int, float])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])
	INTERNAL._blur(img_paths, radius, "gaussian", (int(radius), int(radius)))

def blur_mean(img_paths, radius=3):
	INTERNAL._type_checker(radius, [int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])
	radius = (int(radius), int(radius))
	_blur(img_paths, radius=radius[0], type_kernel="mean", size=radius)