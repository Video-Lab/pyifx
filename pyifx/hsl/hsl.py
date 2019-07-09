import INTERNAL

def brighten(img_paths,factor=0.35):
	if type(img_paths) == misc.ImageVolume:
		if not os.path.exists(img_paths.odir):
			os.makedirs(img_paths.odir)

		new_imgs = img_paths.volume

		for img in new_imgs:
			INTERNAL._brighten(img, factor)

	elif type(img_paths) == misc.PyifxImage:
		INTERNAL._brighten(img_paths, factor)

	elif type(img_paths) == list:
		for img in img_paths:
			if type(img) != misc.PyifxImage:
				raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
			else:
				INTERNAL._brighten(img, factor)
	else:
		raise TypeError("Input contains non-Pyifx images and/or classes. Please try again.")
