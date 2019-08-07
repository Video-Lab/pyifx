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
|tests              |Includes test files and materials.                                                                                              |
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