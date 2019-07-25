import pyifx.INTERNAL as INTERNAL
import pyifx.misc as misc

def brighten(img_paths,percent=45, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	if percent < 0 or percent > 100:
		raise ValueError("Invalid value used: percentage must be between 0 and 100.")

	return INTERNAL._brightness_handler(img_paths, percent/100, "b", write=write)


def darken(img_paths,percent=45, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	if percent < 0 or percent > 100:
		raise ValueError("Invalid value used: percentage must be between 0 and 100.")

	return INTERNAL._brightness_handler(img_paths, percent/100, "d", write=write)


def color_overlay(img_paths, color, opacity=30, write=True):
	INTERNAL._type_checker(opacity, [float, int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	if len(color) != 3:
		raise ValueError("Invalid value used: Please enter a color using the following format: [R,G,B].")

	for channel in color:
		INTERNAL._type_checker(channel, [int])
		if channel < 0 or channel > 255:
			raise ValueError("Invalid value used: Color channels must be between 0 and 255.")

	if opacity < 0 or opacity > 100:
		raise ValueError("Invalid value used: opacity must be between 0 and 100.")	

	return INTERNAL._color_overlay_handler(img_paths, color, opacity/100, write=write)


def saturate(img_paths, percent=30, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	if percent < 0:
		raise ValueError("Invalid value used: percentage must be greater than 0.")

	return INTERNAL._saturation_handler(img_paths, percent/100, "s", write=write)


def desaturate(img_paths, percent=30, write=True):
	INTERNAL._type_checker(percent, [float, int])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	if percent < 0 or percent > 100:
		raise ValueError("Invalid value used: percentage must be between 0 and 100.")

	return INTERNAL._saturation_handler(img_paths, percent/100, "ds", write=write)


def to_grayscale(img_paths, write=True):
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])
	INTERNAL._type_checker(write, [bool])

	return INTERNAL._saturation_handler(img_paths, 1, "ds", write=write)