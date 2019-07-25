import pyifx.INTERNAL as INTERNAL
import pyifx.misc as misc

def resize(img_paths, new_size, write=True):
	INTERNAL._type_checker(write, [bool])
	INTERNAL._type_checker(new_size, [str])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])

	return INTERNAL._resize_handler(img_paths, new_size, write)

def change_file_type(img_paths, new_type, write=True):
	INTERNAL._type_checker(write, [bool])
	INTERNAL._type_checker(new_type, [str])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])

	return INTERNAL._change_file_type_handler(img_paths, new_type, write=write)

def rewrite_file(img_paths):
	NTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])

	return INTERNAL._rewrite_file_handler(img_paths)
