from INTERNAL import *

def _resize_handler(img_paths, new_size, write=True):

	if type(img_paths) == misc.ImageVolume:

				if not os.path.exists(img_paths.odir):
					os.makedirs(img_paths.odir)

				new_vol = img_paths
				new_vol.volume = [] 

				for img in img_paths.volume:
					new_vol.volume.append(_resize_operation(img, new_size, write=write))

				return new_vol

			elif type(img_paths) == misc.PyifxImage:
				return _resize_operation(img_paths, new_size, write=write)

			elif type(img_paths) == list:
				new_imgs = []

				for img in img_paths:
					
					if type(img) != misc.PyifxImage:
						raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

					return new_imgs.append(_resize_operation(img, new_size, write=write))
				return new_imgs

			else:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

def _resize_operation(img, new_size):
	pass

def _expand_operation(img, new_size):
	pass

def _compress_operation(img, new_size):
	pass