Contribution
============

Contribution is an essential step to improving and growing this project. If you want to contribute, please read this short guide detailing the steps you need to take to begin collaborating on this project.

Suggested Prerequisites
-----------------------

You can contribute in may ways besides helping write the underlying code; testers and technical writers are also very important to this project. Please read the list of suggested prerequisites before starting.

Library Contribution
********************

This library is written in Python, so some fundamental understanding of Python can help you navigate the library. Additional libraries (both internal and external) used in the library include:

	* NumPy
	* Imageio
	* OS
	* Math

Understanding these libraries as a whole is not needed. However, understanding their purpose and what some of their main modules do can help when faced with code that uses them.

Documentation Contribution
**************************

Our doucmentation is written in Sphinx, a Python-based documentation tool. You can learn more about Sphinx by visiting their `user guide <https://www.sphinx-doc.org/en/master/index.html>`_.

For those looking to work on the structure of the documentation, some understanding of Sphinx and RST (reStructuredText) can be helpful. However, if you are more focused on the content of the documentation, then these tools will not be of much use. No matter what you are focusing on, some understanding of these tools is still highly recommended.



How to Contribute
-----------------

Any contributions to this project must be done through GitHub pull requests. If you aren't familiar with pull requests, please read `this guide <https://help.github.com/en/articles/about-pull-requests>`_ talking more about them.

All pull request descriptions must include:

	* A short summary of what the change is doing
	* Why the change is being made
	* Any future expansions or plans to expand on the change (if any at all)

Any pull requests with insufficient data will be ignored. 

Once a pull request is made, it will be reviewed. If the change is seen as beneficial or needed, it will be merged into the project.


Library Structure
-----------------

Project Root
************

The root of the project contains files other than the library itself. Below is a table detailing the function of each of these files or directories.

+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|File/Directory name| Purpose                                                                                                                        |
+===================+================================================================================================================================+
|docs               |Contains all the documentation files for the project, including both build and source files                                     |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|pyifx              |The main library. Contains all of the source code and required package files. Any contributions to the library can be made here.|
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|tests              |Includes test materials & altered images.                                                                                       |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|tests_src          |Contains the source files for tests.                                                                                            |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|.gitignore         |Required for ignoring build files regarding version control.                                                                    |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|LICENSE            |The license for the project.                                                                                                    |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+
|README.md          |The README for the project.                                                                                                     |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------+


Library Contents
****************
The main library directory contains files that represent each module. 
:: 
	
	pyifx|
		 hsl.py
		 graphics.py
		 comp.py
		 misc.py
		 INTERNAL.py

To reference a module in a python file (after importing the module), add the name of the module after ``pyifx.``. For example, referencing the ``hsl.py`` file can be done by writing ``pyifx.hsl``.

The library is split into 2 main parts; external and internal functions. External functions are found in the main 4 modules of the library (hsl, graphics, comp, misc) and are made to be used outside the library.

On the other hand, internal functions are made to be used by the library itself. It contains handlers and main algorithms for all of the library's features. These functions are located solely in the file ``INTERNAL.py``, and can be referenced the same way as other modules.

.. note :: Currently, no documentation is provided for the INTERNAL module. It will be added in the coming weeks.

Function System
***************
All external functions follow a specific system to handle inputs properly. The system follows a set of steps similar to the flow chart below:

::

	External function -----------------> Function handler (INTERNAL) -----------------> Function operation (INTERNAL)
	 - Type checking                      - Value checking                               - Modifies image
	                                      - Handles different image types                - Core image

* **External Function** - The function that is called by the user. This is where the user specifies the parameters of the function, and where the function arguments are checked for the correct type.
* **Function Handler** - This function checks the arguments themselves (ex. percent is between 0 and 100) instead of their type. It also handles the various types of image classes that can be entered and calls the appropriate functions in return.
* **Function Operation** - This is where the actual modification of the image happens. Unlike their handlers, most of these functions only accept PyifxImage instances, instead of the variety of types that the external functions accept.

Handler functions end with _handler, and operation functions end with _operation. Both handler and operation functions also begin with _, meaning they are internal and private. Any new features added to the library must follow this system.


Documentation Structure
-----------------------

Because the documentation is written in Sphinx & RST, it can mostly be edited using the same rules & syntax as any other project using the same tools. However, there are a few important exceptions to note.

Titles are underlined using ``=``, subtitles use ``-``, and sub-subtitles use ``*``. No overlining is required.

New functions are automatically documented as long as they have a docstring. Below is an example of the proper way to format a docstring.

.. code-block :: python

	""" detect_edges(img_paths, write=True)
		Takes image(s) and creates new images focusing on edges.

		:type img_paths: pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list 
		:param img_paths: The image(s) to be manipulated.

		:type write: bool
		:param write: Whether to write the manipulated image(s).

		:return: PyifxImage instance, ImageVolume instance, or list with elements of type PyifxImage
		:rtype: pyifx.misc.PyifxImage, pyifx.misc.ImageVolume, list

	"""

Classes need to have docstrings for each individual method. However, the class itself can have a docstring to document information about the class as well as its members. Below is an example of a class docstring.

.. code-block :: python

	""" A class used to create packages of images & their properties created for use with the Pyifx library.
		
		:vartype input_path: str, NoneType
		:ivar input_path: The path to where the image is located. If the image does not have an input path, it means that the instance is a result of combining two or more images.

		:vartype output_path: str, NoneType 
		:ivar output_path: The path to where edited images should be created. If the image does not have an output path, it means the instance is used for read-only purposes.

		:vartype image: numpy.ndarray, NoneType
		:ivar image: The image located at the input path in the form of a numpy n-dimensional array. If the instance does not have an image property, it means that the image had not been read.

	"""

Here is a table of some of the common formatting tags used to reference certain parts of docstrings for both functions and classes.

+-----------------------+---------------------------------------------------+
|Tag                    | Description                                       |
+=======================+===================================================+
|``:vartype MEMBER:``   |The member type (for classes).                     |
+-----------------------+---------------------------------------------------+
|``:ivar MEMBER:``      |The member description (for classes).              |
+-----------------------+---------------------------------------------------+
|``:type PARAMETER:``   |The parameter type (for functions).                |
+-----------------------+---------------------------------------------------+
|``:param PARAMETER:``  |The parameter description (for functions).         |
+-----------------------+---------------------------------------------------+
|``:return:``           |The return value description (for functions).      |
+-----------------------+---------------------------------------------------+
|``:rtype:``            |The return value type (for functions).             |
+-----------------------+---------------------------------------------------+

Although functions can be added to the API reference automatically, they still needed to be added to the 'Library Contents' page manually. If a new function has been approved, it needs to be added to the 'Library Contents' page manually. This page uses the Sphinx autosummary directive to add functions to the page. Below shows an example of what adding a new function would look like.

::

	**pyifx.graphics**

	.. autosummary ::

		pyifx.graphics.function_here
		pyifx.graphics.Class
		pyifx.graphics.new_function <---- New function here

If the module is new and must be added, write the module name (in the format of the module name above) and bold it. Under that, add an autosummary directive and add the function to the list, making sure to follow the same format as the example above. Classes can be added in the same way.

Writing Tests
-------------

Writing tests is one of the most important parts of this project. Whether it is due to changing an existing feature or adding a new one, tests must be written in order to verify the validity of a change to the library. In order to keep tests organized, a few rules must be followed for writing them.

Location & Naming
*****************

As seen in the `project root table <#project-root>`_, the **tests** directory contains test input & output files, while the **tests_src** directory is used to store test sources files. Any new tests **must** be written & saved in the tests_src directory.

Each test file is dedicated to an individual function. Functions must have individual test files and cannot be combined together. Files are named after the function as if they were being referenced from the root package. 

:: 

	tests_src |
		pyifx.hsl.brighten.py
		pyifx.hsl.darken.py
		...
		pyifx.misc.combine.py
		...

As seen above, the test file for the "brighten" function is named "pyifx.hsl.brighten.py", after its location in the package.


Test File Structure
*******************

Tests follow a specific structure in order to thoroughly cover every situation. Below is an example of what a test file would look like.

.. code-block :: python 
	
	# pyifx.graphics.convolute_custom.py

	# Import test materials
	from test_vars import *

	# Set output path(s)
	set_paths("../tests/imgs/graphics/convolute_custom")

	# Custom variables (optional)
	sobel_horizontal_np = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
	sobel_vertical = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
	box_blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

	# Main tests
	pyifx.graphics.convolute_custom(img1, sobel_horizontal_np)
	pyifx.graphics.convolute_custom(img_list, sobel_vertical)
	pyifx.graphics.convolute_custom(img_vol, box_blur)

	# Error tests
	call_error_test("pyifx.graphics.convolute_custom", ['s', sobel_horizontal_np])
	call_error_test("pyifx.graphics.convolute_custom", [img1, 's'])
	call_error_test("pyifx.graphics.convolute_custom", [img1, sobel_horizontal_np, 's'])

* **Test materials**: Test materials, including variables & functions are located in the ``test_vars.py`` file, and can be imported using this statement.
* **Output path**: The directory to which any ouput files should be written. This path should be written in the format ``../tests/imgs/*module*/*function_name*``.
* **Custom variables**: Any extra variables needed for the tests. These should only be included if required by the function.
* **Main tests**: Where the tests should be ran. The tests must be ran for all of the variables included in the `test materials <#test-materials>`_, & any other parameters should include a variety of values.
* **Error tests**: Where the error handling of the function is tested through the `call_error_test function <#test_materials>`_. Try to include all types of potential errors.


Test Materials
**************

All materials needed for the test are provided in the ``test_vars.py`` file, which is located in the same directory as the rest of the tests. This file includes:

* Path-changing function (to help changing paths for individual variables)
* Error handler & catcher
* Variables (2x PyifxImage Instance, 1x ImageVolume, 1x Image List)

.. py:function :: set_paths(new_path)

	Changes the output path of test variables.

	:param str new_path: The new output path.

.. py:function :: call_error_test(function, arguments)

	Calls a function with a provided list of arguments & catches any errors that arise. Prints message if caught successfully.

	:param str function: The function to be called. Should be referenced from package (eg. pyifx.hsl.brighten). Does not include parentheses.
	:param list arguments: The arguments to be passed to the function. Should be contained in a list (in order of passing to the function).

	:return: Boolean indicating if the error was caught.
	:rtype: bool