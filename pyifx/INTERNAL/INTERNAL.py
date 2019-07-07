import os
import sys
import numpy as np
import matplotlib as mpl
import imageio

class PyifxImage():
	def __init__(self, path, out_path=None, image=None):
		self.path = path
		self.image = np.asarray(imageio.imread(path))
		self.out_path = out_path

	@classmethod
	def from_image(cls, image):
		i = cls(None)
		i.image = image
		return i


def check_path_type(path):
	if os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None

def convert_dir_to_images(dirc):
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