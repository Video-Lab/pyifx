# INTERNAL.py
import os
import sys
import numpy as np
import matplotlib as mpl
import imageio
import math

# INTERNAL.py

def _check_path_type(path):
	if os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None

def _convert_dir_to_images(dirc):
	images = []
	possible_extensions = ['.jpg', '.jpeg', '.png']

	def add_to_images(idirc):
		for f in os.listdir(idirc):
		 	if os.path.splitext(f)[1] in possible_extensions:
		 		images.append(os.path.join(idirc,f))
		 	elif os.path.isdir(f):
		 		add_to_images(f)

	add_to_images(dirc)
	return images

def _write_file(img):
	out_path, extension = os.path.splitext(img.output_path)

	if not os.path.exists(os.path.split(img.output_path)[0]):
		os.makedirs(os.path.split(img.output_path)[0])	

	file_count = 1
	temp_path = out_path

	while os.path.isfile(out_path + extension):
		out_path = temp_path
		out_path += f" ({file_count})"
		file_count += 1

	img.image = img.image.astype(np.uint8)
	imageio.imwrite(out_path + extension, img.image)
	return img

def _type_checker(var, types):
	if type(var) in types:
		return True

	raise TypeError("Please use correct variable types.")
	return False

# misc.py

class PyifxImage():
	def __init__(self, path, out_path=None, img=None, create_image=True):
		self.path = path
		self.output_path = out_path
		self.image = img
		if create_image == True:
			self.image = np.asarray(imageio.imread(path))
		


	@classmethod
	def from_image(cls, image):
		i = cls(None)
		i.image = image
		return i

class ImageVolume():
	def __init__(self, i, o, p="_"):
		self.idir = i
		self.odir = o
		self.prefix = p
		self.volume = self.volume_to_list()

	def volume_to_list(self):
		old_imgs = _convert_dir_to_images(self.idir)
		new_imgs = [PyifxImage(img, os.path.join(self.odir,f"{self.prefix}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs

def combine(img1, img2, out_path):
	if img1.image.shape[0]*img1.image.shape[0] <= img2.image.shape[0]*img2.image.shape[1]:
		shape = img1.image.shape
	else:
		shape = img2.image.shape

	new_img = np.empty(shape)

	for r in range(len(img1.image)):
		for p in range(len(img1.image[r])):
			for c in range(len(img1.image[r][p])):
				try:
					new_img[r][p][c] = min(255, max(0, (img1.image[r][p][c]+img2.image[r][p][c])/2))
				except IndexError:
					pass

	img = PyifxImage(None, out_path, new_img, False)
	return img

def _resize_handler(img_paths, new_size, write=True):

	if type(img_paths) == ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = [] 

		for img in img_paths.volume:
			new_vol.volume.append(_resize_operation(img, new_size, write=write))

		return new_vol

	elif type(img_paths) == PyifxImage:
		return _resize_operation(img_paths, new_size, write=write)

	elif type(img_paths) == list:
		new_imgs = []

		for img in img_paths:

			if type(img) != PyifxImage:
					raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			new_imgs.append(_resize_operation(img, new_size, write=write))

			return new_imgs

	else:
		raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")


def _resize_operation(img, new_size, write=True):
	img_size = [int(d) for d in new_size.split('x')]
	img_size.append(3)
	img_size[0], img_size[1] = img_size[1], img_size[0]

	width_factor = img_size[1]/img.image.shape[1]
	height_factor = img_size[0]/img.image.shape[0]

	new_img = np.full(shape=img_size, fill_value=None)

	for r in range(len(new_img)):
		for p in range(len(new_img[r])):
			for c in range(len(new_img[r][p])):

				if new_img[r][p][c] != None:
						new_img[r][p][c] += img.image[math.floor(r/height_factor)][math.floor(p/width_factor)][c]
						new_img[r][p][c] = math.floor(new_img[r][p][c]/2)
				else:
					new_img[r][p][c] = img.image[math.floor(r/height_factor)][math.floor(p/width_factor)][c]

	new_img = PyifxImage(img.path, img.output_path, new_img, False)

	if write:
		_write_file(new_img)

	return new_img


def _change_file_type_handler(img_paths, new_type, write=True):
	if type(img_paths) == ImageVolume:

		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_vol = img_paths
		new_vol.volume = [] 

		for img in img_paths.volume:
			new_vol.volume.append(_change_file_type_operation(img, new_type, write=write))

		return new_vol

	elif type(img_paths) == PyifxImage:
		return _change_file_type_operation(img_paths, new_type, write=write)

	elif type(img_paths) == list:
		new_imgs = []

		for img in img_paths:

			if type(img) != PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")

			new_imgs.append(_change_file_type_operation(img, new_type, write=write))

		return new_imgs

	else:
		raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
		

def _change_file_type_operation(img, new_type, write=True):

	new_img = img
	accepted_types = ['.jpg', '.png', '.jpeg', 'jpg', 'jpeg', 'png']	
	if new_type not in accepted_types:
		raise ValueError("New file type not in accepted file types.")

	if new_type[0] != '.':
		new_type = f".{new_type}"

	new_img.output_path = os.path.splitext(new_img.output_path)[0] + new_type

	if write:
		_write_file(new_img)
	return new_img
	
# comp.py

def resize(img_paths, new_size, write=True):
	_type_checker(new_size, [str])
	_type_checker(img_paths, [PyifxImage, ImageVolume, list])

	return _resize_handler(img_paths, new_size, write)

def change_file_type(img_paths, new_type, write=True):
	_type_checker(new_type, [str])
	_type_checker(img_paths, [PyifxImage, ImageVolume, list])

	return _change_file_type_handler(img_paths, new_type, write=write)
