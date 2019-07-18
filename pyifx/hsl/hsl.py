import INTERNAL

def brighten(img_paths,percent=45, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._brightness_handler(img_paths, max(0, min(percent, 100))/100, "b", write=write)


def darken(img_paths,percent=45, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._brightness_handler(img_paths, max(0, min(percent, 100))/100, "d", write=write)


def color_overlay(img_paths, color, opacity=30, write=True):
	INTERNAL._type_checker(opacity, [float, int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._color_overlay_handler(img_paths, color, max(0, min(opacity, 100))/100, write=write)


def saturate(img_paths, percent=30, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._saturation_handler(img_paths, max(0, min(percent, 100))/100, "s", write=write)


def desaturate(img_paths, percent=30, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._saturation_handler(img_paths, max(0, min(percent, 100))/100, "ds", write=write)


def to_grayscale(img_paths, write=True):
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._saturation_handler(img_paths, 1, "ds", write=write)