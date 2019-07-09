import INTERNAL

def brighten(img_paths,factor=0.35):
	INTERNAL._brightness(img_paths, factor, "b")

def darken(img_paths,factor=0.35):
	INTERNAL._brightness(img_paths, factor, "d")