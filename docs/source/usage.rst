Usage
=====

Importing an Image
-----------------
As stated in the previous section, most of pyifx's functionality is based around the use of `image classes <image_classes.html>`_. There are three options to create data that is compatible with the Pyifx library.

**PyifxImage**

The `PyifxImage class <image_classes.html#pyifx-image>`_ allows you to package data about an image into a class instance. This instance can then be passed to functions provided by the library to manipulate image data.

The snippet below shows an example of what creating an instance of this class would look like.

.. code-block ::

	#demo_file.py
	import pyifx

	# Creating the image
	image = pyifx.misc.PyifxImage(input_path="path/to/img.png", output_path="path/to/new_img.png")



.. note :: More information about the PyifxImage class is available `here <image_classes.html#pyifx-image>`_.

**ImageVolume**

The `ImageVolume class <image_classes.html#image-volume>`_ allows for the generation of a list of PyifxImage instances based on specified parameters. As with the PyifxImage class, instances of this class can be passed to library-provided functions as well.

Creating an ImageVolume instance is very similar to creating a PyifxImage instance.

.. code-block ::

	# Creating the volume
	volume = pyifx.misc.ImageVolume(input_path="lots/of/images/", output_path="lots/of/images/modified/", prefix="_")

.. note :: More information about the ImageVolume class is available `here <image_classes.html#image-volume>`_.