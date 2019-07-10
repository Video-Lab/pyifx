import INTERNAL

def brighten(img_paths,percent=45):
	INTERNAL._brightness(img_paths, max(0, min(percent, 100))/100, "b")

def darken(img_paths,percent=45):
	INTERNAL._brightness(img_paths, max(0, min(percent, 100))/100, "d")

def color_overlay(img_paths, color, opacity=30):
	INTERNAL._color_overlay(img_paths, color, max(0, min(opacity, 100))/100)