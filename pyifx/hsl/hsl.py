import INTERNAL

def brighten(img_paths,factor=0.45):
	INTERNAL._brightness(img_paths, factor, "b")

def darken(img_paths,factor=0.45):
	INTERNAL._brightness(img_paths, factor, "d")

def color_overlay(img_paths, color, opacity=30):
	INTERNAL._color_overlay(img_paths, color, opacity/100)