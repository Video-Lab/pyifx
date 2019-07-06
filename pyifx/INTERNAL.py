import os
import sys
import cv2
import numpy as np
import matplotlib as mpl

class _PyfixImage():
	def __init__(self, path):
		self.path = path
		self.image = cv2.imread(path)

	@classmethod
	def from_image(cls, image):
		return cls(None,image)


def checkPathType(path):
	is os.path.isdir(path):
		return 'dir'
	elif os.path.isfile(path):
		return 'file'
	else:
		return None