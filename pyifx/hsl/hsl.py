import INTERNAL

def brighten(img_paths,percent=45):
	INTERNAL_misc._type_checker(percent, [float, int])
	INTERNAL._brightness(img_paths, max(0, min(percent, 100))/100, "b")

def darken(img_paths,percent=45):
	INTERNAL_misc._type_checker(percent, [float, int])
	INTERNAL._brightness(img_paths, max(0, min(percent, 100))/100, "d")

def color_overlay(img_paths, color, opacity=30):
	INTERNAL_misc._type_checker(opacity, [float, int])
	INTERNAL._color_overlay(img_paths, color, max(0, min(opacity, 100))/100)

def saturate(img_paths, percent=30):
	INTERNAL_misc._type_checker(percent, [float, int])
	INTERNAL._saturation(img_paths, max(0, min(percent, 100))/100, "s")

def desaturate(img_paths, percent=30):
	INTERNAL_misc._type_checker(percent, [float, int])
	INTERNAL._saturation(img_paths, max(0, min(percent, 100))/100, "ds")

def to_grayscale(img_paths):
	INTERNAL._saturation(img_paths, 1, "ds")