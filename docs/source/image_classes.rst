Image Classes
=============

What are They?
--------------
All of the functions in this library are based around the use of Pyifx Image classes. They allow you to store important information about an image in Python while also providing useful functions relating to their properties.

Pyifx Image
-----------
The PyifxImage class allows for images to be read, modified, and written in combination with functions provided by the library. This class can either be instantiated through the use of an input and outputh path, or by providing given image data as long as it is in the form of a NumPy ndarray.

Below is an example of what creating instances of the PyifxImage class would look like.

.. code-block::

	import pyifx

	

	image = pyifx.misc.PyifxImage(input_path="path/to/img.png", output_path="path/to/new_img.png")

	image_from_data = pyifx.misc.PyifxImage(input_path=None, output_path="path/to/new_img.png", img=image_data)

The methods of this class include:
::
	pyifx.misc.PyifxImage.refresh_image()
	pyifx.misc.PyifxImage.get_input_path()
	pyifx.misc.PyifxImage.set_input_path()
	pyifx.misc.PyifxImage.get_output_path()
	pyifx.misc.PyifxImage.set_output_path()
	pyifx.misc.PyifxImage.get_image()
	pyifx.misc.PyifxImage.set_image()

.. note:: A full list & description of parameters & methods in the PyifxImage class can be found `here <misc.html>`_ or by visiting the `general index <modules.html>`_.