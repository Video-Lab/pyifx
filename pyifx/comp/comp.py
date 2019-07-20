import INTERNAL

def resize(img_paths, new_size, write=True):
	INTERNAL._type_checker(new_size, [str])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._resize_handler(img_paths, new_size, write)

def change_file_type(img_paths, new_type, write=True):
	INTERNAL._type_checker(new_type, [str])
	INTERNAL._type_checker(img_paths, [INTERNAL.misc.PyifxImage, INTERNAL.misc.ImageVolume, list])

	return INTERNAL._change_file_type_handler(img_paths, new_type, write=write)
