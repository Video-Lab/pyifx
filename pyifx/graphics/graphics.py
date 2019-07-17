import INTERNAL

def blur_gaussian(img_paths, radius=1.5, size=None, write=True):
	INTERNAL._type_checker(radius, [int, float])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._blur_handler(img_paths, radius=radius, type_kernel="gaussian", size, write=write)

def blur_mean(img_paths, radius=3, write=True):
	INTERNAL._type_checker(radius, [int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._blur_handler(img_paths, radius=radius, type_kernel="mean", size=size, write=write)

def pixelate(img_paths, factor=4, write=True):
	INTERNAL._type_checker(factor, [int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._pixelate_handler(img_paths, factor, write=write)

def detect_edges(img_paths, write=True):
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._detect_edges_handler(img_paths, write=write)