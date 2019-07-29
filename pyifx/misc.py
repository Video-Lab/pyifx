import os
import sys
import numpy as np
import imageio
import math
import pyifx.INTERNAL as INTERNAL

class PyifxImage():
	""" A class used to create packages of images & their properties created for use with the Pyifx library.

	Attributes:
		input_path (str, NoneType): The path to where the image is located. If the image does not have an input path,
		it means that the instance is a result of combining two or more images.

		output_path (str, NoneType): The path to where edited images should be created. If the image does not have an
		output path, it means the instance is used for read-only purposes.

		image (numpy.ndarray, NoneType): The image located at the input path in the form of a numpy n-dimensional array.
		If the instance does not have an image property, it means that the image had not been read.

	Methods:
		__init__(self, path, output_path=None, img=None, create_image=True)
			The PyifxImage constructor method.

			Parameters:
			path (str, NoneType): The path to where the image is located. Only use None as a value if the image property of the 
			instace is being specified.

			output_path(str, NoneType): The path to where the edited image should be saved. Only use None as a value if the instance 
			is not going to be saved to a file.

			img (numpy.ndarray, NoneType): The data used for image editing & processing. The image property of the class will be
			set based on the input path unless this parameter is set to a value other than None.

			create_image (bool): Specify whether the image property should be read from the input path. If this is set to true,
			the image at the input path will override the specified image parameter.

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)


		refresh_image(self):
			Re-reads image based on input path & overrides the current image property, then returns the instance.

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)


		get_input_path(self):
			Gets the instances input path and returns it.

			Returns:
			Input path (str)


		set_input_path(self, new_input_path):
			Sets the instances input path and returns the instance.

			Parameters:
			new_input_path (str): What the input path will be set to.

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)


		get_output_path(self):
			Gets the instances output path and returns it.

			Returns:
			Output path (str)


		set_output_path(self, new_output_path):
			Sets the instances output path and returns the instance.

			Parameters:
			new_output_path (str): What the output path will be set to.

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)


		get_image(self):
			Gets the instances image data and returns it.

			Returns:
			Image data (numpy.ndarray)


		set_image(self, new_image):
			Sets the instances image data and returns it.

			Parameters:
			new_image (numpy.ndarray): What the image property will be set to.

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)
	"""
	def __init__(self, path, output_path=None, img=None, create_image=True):
		INTERNAL._type_checker(path, [str, None])
		INTERNAL._type_checker(output_path, [str, None])
		INTERNAL._type_checker(img, [np.ndarray, None])
		INTERNAL._type_checker(create_image, [bool])

		self.input_path = path
		self.output_path = output_path
		self.image = img
		if create_image:
			self.image = np.asarray(imageio.imread(path))

	def refresh_image(self):
		self.image = np.asarray(imageio.imread(self.path))
		return self

	def get_input_path(self):
		return self.input_path

	def set_input_path(self, new_input_path):
		self.input_path = new_input_path
		self.refresh_image()
		return self

	def get_output_path(self):
		return self.output_path

	def set_output_path(self, new_output_path):
		self.output_path = new_output_path
		return self

	def get_image(self):
		return self.image

	def set_image(self, new_image):
		self.image = new_image
		return self

	
class ImageVolume():
	"""A class used to import images from a directory into Python, creating a list of PyifxImage instances.

	Attributes:
		input_path (str): The path to the directory where the images are located.

		output_path (str): The path where images in the volume should be saved.

		prefix (str): The prefix for edited image file names.

		volume (list): The list of images imported from the input path.

	Methods:
		__init__(self, input_path, output_path, prefix="_", convert=False)
			The ImageVolume constructor method.

			Parameters:
			input_path (str): The path to the directory where the images are located.

			output_path (str): The path where images in the volume should be saved.

			prefix (str): The prefix for edited image file names. If nothing is entered for this parameter,
			it will default to "_".

			convert (bool): Whether the instance should also read in images from subdirectories. If nothing is entered for
			this parameter, it will default to false.

			Returns:
			ImageVolume instance (pyifx.misc.ImageVolume)


		volume_to_list(self, convert=False)
			The method used to create a list of PyifxImage instances based on the arguments entered in the constructor method.
			The volume property will be set based on the return value of this function.

			Parameters:
			convert (bool): Whether to import images from subdirectories. If nothing is entered for this parameter,
			it will default to False.

			Returns:
			PyifxImage list (list)


		get_input_path(self):
			Gets the instances input path and returns it.

			Returns:
			Input path (str)


		set_input_path(self, new_input_path, convert=False):
			Sets the instances input path and returns it.

			Parameters:
			new_input_path (str): What the input path will be set to.

			convert (bool): Whether the instance should also read in images from subdirectories. If nothing is entered for this
			parameter, it will default to false.

			Returns:
			ImageVolume instance (pyifx.misc.ImageVolume)


		get_output_path(self):
			Gets the instances output path and returns it.

			Returns:
			Output path (str)


		set_output_path(self, new_output_path):
			Sets the instances output path and returns the instance.

			Parameters:
			new_output_path (str): What the output path will be set to.

			Returns:
			ImageVolume instance (pyifx.misc.ImageVolume)


		get_prefix(self):
			Gets the instances prefix property and returns it.

			Returns:
			Prefix (str)


		set_prefix(self, new_prefix):
			Sets the instances prefix property and returns the instance.

			Parameters:

			new_prefix (str): What the instances prefix property will be set to.

			Returns:
			ImageVolume instance (pyifx.misc.ImageVolume)


		get_volume(self):
			Gets the instances volume and returns it.

			Returns:
			List of images of type PyifxImage OR An empty array (list)


		set_volume(self, new_volume):
			Sets the instances volume property and returns the volume.

			Parameters:
			new_volume (list): What the instances volume will be set to.

			Returns:
			ImageVolume instance (pyifx.misc.ImageVolume)

		convert_dir_to_images(input_dir, convert=False):
			Converts files from a given directory into PyifxImage instances.
			
			Parameters:
			input_dir (str): The directory to read files from.

			convert (bool): Whether to import images from subdirectories as well.

			Returns:
			List with elements of type PyifxImage (list)
	"""
	def __init__(self, input_path, output_path, prefix="_", convert=False):
		INTERNAL._type_checker(input_path, [str])
		INTERNAL._type_checker(output_path, [str])
		INTERNAL._type_checker(prefix, [str])
		INTERNAL._type_checker(convert, [bool])

		self.input_path = input_path
		self.output_path = output_path
		self.prefix = prefix
		self.volume = self.volume_to_list(convert)

	def volume_to_list(self, convert=False): # Add if conversion needed, if create image needed

		INTERNAL._type_checker(self.get_input_path(), [str])
		INTERNAL._type_checker(self.get_output_path(), [str])
		INTERNAL._type_checker(self.get_prefix(), [str])
		
		return self.convert_dir_to_images(self.get_input_path(), convert)

	def get_input_path(self):
		return self.input_path

	def set_input_path(self, new_input_path, convert=False):
		self.input_path = new_input_path
		self.volume = self.volume_to_list(convert)
		return self

	def get_output_path(self):
		return self.output_path

	def set_output_path(self, new_output_path):
		self.output_path = new_output_path
		return self

	def get_prefix(self):
		return self.prefix

	def set_prefix(self, new_prefix):
		self.prefix = new_prefix
		return self

	def get_volume(self):
		return self.volume

	def set_volume(self, new_volume):
		if new_volume != []:
			for img in new_volume:
				INTERNAL._type_checker(img, [PyifxImage])
		self.volume = new_volume
		return self

	def convert_dir_to_images(input_dir, convert=False):
		INTERNAL._type_checker(input_dir, [str])
	
		images = []
		possible_extensions = ['.jpg', '.jpeg', '.png']

		def add_to_images(internal_input_dir):
			for f in os.listdir(internal_input_dir):
			 	if os.path.splitext(f)[1] in possible_extensions:
			 		images.append(PyifxImage(f, os.path.join(self.get_output_path(),f"{self.get_prefix()}{os.path.split(f)[1]}")))

			 	if convert:
				 	if os.path.isdir(f):
				 		add_to_images(f)

		add_to_images(dirc)
		return images


def combine(img1, img2, out_path, write=True):
	"""combine(img1, img2, out_path, write=True)
			Combines the data of two PyifxImages, ImageVolumes, or ImageLists to form new PyifxImages.

			Parameters: 
			img1 (pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list): The first image to be added to the combination.

			img2 (pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list): The second image to be added to the combination.
			Arguments of type ImageVolume and list can be used in conjunction, but images of type PyifxImage must be used together.

			out_path (str): The path that the combine image(s) will be written to.

			write (bool): Whether to write the image or not.

			Returns:
			PyifxImage instance (pyifx.misc.PyifxImage)
			List with elements of type PyifxImage (list)
	"""

	INTERNAL._type_checker(img1, [PyifxImage, ImageVolume, list])
	INTERNAL._type_checker(img2, [PyifxImage, ImageVolume, list])
	INTERNAL._type_checler(out_path, [str])
	INTERNAL._type_checker(write, [bool])

	return INTERNAL._combine_handler(img1, img2, out_path, write=write)



