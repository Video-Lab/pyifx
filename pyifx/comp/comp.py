import INTERNAL

def resize(img_paths, new_size):
	INTERNAL._type_checker(new_size, [str])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	INTERNAL._resize_handler(img_paths, new_size)	