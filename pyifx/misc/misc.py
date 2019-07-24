from pyifx import *

class PyifxImage():
	def __init__(self, path, output_path=None, img=None, create_image=True):
		INTERNAL._type_checker(path, [str, NoneType])
		INTERNAL._type_checker(out_path, [str, NoneType])
		INTERNAL._type_checker(img, [np.ndarray, NoneType])
		INTERNAL._type_checker(create_image, [bool])

		self.path = path
		self.output_path = output_path
		self.image = img
		if create_image:
			self.image = np.asarray(imageio.imread(path))
	
class ImageVolume():
	def __init__(self, i, o, p="_"):
		INTERNAL._type_checker(i, [str])
		INTERNAL._type_checker(o, [str])
		INTERNAL._type_checker(p, [str])

		self.idir = i
		self.odir = o
		self.prefix = p
		self.volume = self.volume_to_list()

	def volume_to_list(self):
		INTERNAL._type_checker(i, [str])
		INTERNAL._type_checker(o, [str])
		INTERNAL._type_checker(p, [str])
				
		old_imgs = INTERNAL._convert_dir_to_images(self.idir)
		new_imgs = [PyifxImage(img, os.path.join(self.odir,f"{self.prefix}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs




def combine(img1, img2, out_path):
	INTERNAL._type_checker(img1, [INTERNAL.misc.PyifxImage])
	INTERNAL._type_checker(img2, [INTERNAL.misc.PyifxImage])
	INTERNAL._type_checker(out_path, [str])

	if img1.image.shape[0]*img1.image.shape[0] <= img2.image.shape[0]*img2.image.shape[1]:
		shape = img1.image.shape
	else:
		shape = img2.image.shape

	new_img = np.empty(shape)

	for r in range(len(img1.image)):
		for p in range(len(img1.image[r])):
			for c in range(len(img1.image[r][p])):
				try:
					new_img[r][p][c] = min(255, max(0, (img1.image[r][p][c]+img2.image[r][p][c])/2))
				except IndexError:
					pass

	img = misc.PyifxImage(None, out_path, new_img, False)
	return img

