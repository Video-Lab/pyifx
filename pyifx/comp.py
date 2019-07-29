import pyifx.INTERNAL as INTERNAL
import pyifx.misc as misc

def resize(img_paths, new_size, write=True):
	"""resize(img_paths, new_size, write=True):
			Takes image(s) and converts them to a given size.

			Parameters:
			img_paths (pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list): The images to be converted.

			new_size (str): The new size to convert the image(s) to. It must be entered in the form "WidthxHeight".

			write (bool): Whether to write the resized image(s). 

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)
			ImageVolume instance (pyifx.misc.ImageVolume)
			List with elements of type PyifxImage (list)
			
	"""
	INTERNAL._type_checker(write, [bool])
	INTERNAL._type_checker(new_size, [str])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])

	return INTERNAL._resize_handler(img_paths, new_size, write)

def change_file_type(img_paths, new_type, write=True):
	"""change_file_type(img_paths, new_type, write=True)
			Takes image(s) and converts them to a given file type.

			Parameters:
			img_paths (pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list): The images to be converted.

			new_type (str): The file type that the image(s) should be converted to. Available types: PNG, JPG, JPEG. Can be 
			entered with/without the dot.

			write (bool): Whether to write the resized image(s). 

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)
			ImageVolume instance (pyifx.misc.ImageVolume)
			List with elements of type PyifxImage (list)

	"""
	INTERNAL._type_checker(write, [bool])
	INTERNAL._type_checker(new_type, [str])
	INTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])

	return INTERNAL._change_file_type_handler(img_paths, new_type, write=write)

def rewrite_file(img_paths):
	NTERNAL._type_checker(img_paths, [misc.PyifxImage, misc.ImageVolume, list])

	return INTERNAL._rewrite_file_handler(img_paths)
