Usage
=====

Importing an Image
------------------
As stated in the previous section, most of pyifx's functionality is based around the use of `image classes <image_classes.html>`_. There are three options to create data that is compatible with the Pyifx library.

PyifxImage
**********

The `PyifxImage class <image_classes.html#pyifx-image>`_ allows you to package data about an image into a class instance. This instance can then be passed to functions provided by the library to manipulate image data.

The snippet below shows an example of what creating an instance of this class would look like. You can view the full code example of this article `here <usage.html#full-code-example>`_.

.. code-block :: python

	#demo_file.py
	import pyifx

	# Creating the image
	image = pyifx.misc.PyifxImage(input_path="path/to/img.png", output_path="path/to/new_img.png")



.. note :: More information about the PyifxImage class is available `here <image_classes.html#pyifx-image>`_.

ImageVolume
***********

The `ImageVolume class <image_classes.html#image-volume>`_ allows for the generation of a list of PyifxImage instances based on specified parameters. As with the PyifxImage class, instances of this class can be passed to library-provided functions as well.

Creating an ImageVolume instance is very similar to creating a PyifxImage instance. You can view the full code example of this article `here <usage.html#full-code-example>`_.

.. code-block :: python

	# Creating the volume
	volume = pyifx.misc.ImageVolume(input_path="lots/of/images/", output_path="lots/of/images/modified/", prefix="_")

.. note :: More information about the ImageVolume class is available `here <image_classes.html#image-volume>`_.

PyifxImage list
***************

Lists of PyifxImage instances can also be passed directly into pyifx functions. This can be used to import images from multiple directories, or if PyifxImage instances need to have properties that do not share any patterns or sequences.

Below is an example of what creating a PyifxImage instance list would look like. You can view the full code example of this article `here <usage.html#full-code-example>`_.

.. code-block :: python

	#Creating the list 
	image_2 = pyifx.misc.PyifxImage(input_path="different/path/to/img.png", output_path="different/path/to/new_img.png")

	image_list = [image, image_2]

Using Imported Images
---------------------

Function Categories
*******************

Once an image is imported into an accepted class instance, it can be used by any of the main functions in the library. Functions are split into 4 categories based on their main purpose. These categories can be accessed based on the module names listed below:

.. code-block :: python

	pyifx.hsl
	pyifx.graphics
	pyifx.comp
	pyifx.misc

+------------------------------------+------------------------------+--------------------------------------------------------------------+
| Module name                        | Literal translation          | Description                                                        |
+====================================+==============================+====================================================================+
| `pyifx.hsl <hsl.html>`_            | HSL (Hue, Saturation, Light) | Functions in this section are focused around color & its           |
|                                    |                              | manipulation. In simple terms, hue refers to the color itself,     |
|                                    |                              | saturation to its intensity, and light to how bright or dark the   |
|                                    |                              | color is.                                                          |
+------------------------------------+------------------------------+--------------------------------------------------------------------+
| `pyifx.comp <comp.html>`_          | Compositon                   | This section contains functions related to the manipulation of the |
|                                    |                              | properties of images. This includes its dimensions and file type   |
|                                    |                              | among other properties.                                            |
+------------------------------------+------------------------------+--------------------------------------------------------------------+
| `pyifx.graphics <graphics.html>`_  | Graphics                     | This section focuses on the look and composition of images as a    |
|                                    |                              | whole. Functions in this section mostly apply effects to images to |
|                                    |                              | change their look, such as blurs and pixelations.                  |
+------------------------------------+------------------------------+--------------------------------------------------------------------+ 
| `pyifx.misc <misc.html>`_          | Miscellaneous                | Unlike the composition module, this section focuses on managing    |
|                                    |                              | images instead of editing them. Functions and classes in this      |
|                                    |                              | module include image classes and image import functions.           | 
+------------------------------------+------------------------------+--------------------------------------------------------------------+

.. note :: A full list of functions is available `here <modules.html>`_. To view functions contained in specific categories, visit the category's specific page mentioned in the `table of contents <index.html>`_.

Function Structure
******************

pyifx functions accept any of the image classes mentioned in the `import section <#importing-an-image>`_. They return a new, modified instance of the same class or type as provided in the function. What is modified can vary based on what the function does. This is usually the image data; however, functions can also return modified input and output paths, prefixes (for ImageVolume instances), and other properties.

Below is an example of what using a pyifx function would look like.

.. code-block :: python

	brightened_image = pyifx.hsl.brighten(image, 50)
	print(type(brightened_image))

If this file is run, we can see what the return value of this function would look like.

.. code-block :: bash

	$ python demo_file.py
	<class 'pyifx.misc.PyifxImage'>

The return value type always matches the image input type, regardless of the function.

.. code-block :: python

	brightened_list = pyifx.hsl.brighten(image_list, 50)
	print(type(brightened_list))

.. code-block :: bash
	
	$ python demo_file.py
	<class 'list'>


Full Code Example
-----------------

.. code-block :: python

	#demo_file.py
	import pyifx

	# Creating the image
	image = pyifx.misc.PyifxImage(input_path="path/to/img.png", output_path="path/to/new_img.png")

	# Creating the volume
	volume = pyifx.misc.ImageVolume(input_path="lots/of/images/", output_path="lots/of/images/modified/", prefix="_")

	#Creating the list 
	image_2 = pyifx.misc.PyifxImage(input_path="different/path/to/img.png", output_path="different/path/to/new_img.png")

	image_list = [image, image_2]

	brightened_image = pyifx.hsl.brighten(image, 50)
	print(type(brightened_image))

	brightened_list = pyifx.hsl.brighten(image_list, 50)
	print(type(brightened_list))	
