import os
import sys
import numpy as np
import matplotlib as mpl
import imageio
import math

import ..hsl
import ..graphics
import ..misc
import ..comp

from .INTERNAL_hsl import *
from .INTERNAL_misc import *
from .INTERNAL_graphics import *
from .INTERNAL_comp import *



def _check_path_type(path):
	if os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None




def _convert_dir_to_images(dirc):
	INTERNAL._type_checker(dirc, [str])
	
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