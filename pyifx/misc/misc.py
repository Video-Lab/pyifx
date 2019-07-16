import INTERNAL

class PyifxImage():
	def __init__(self, path, out_path=None, create_image=True):
		self.path = path
		self.output_path = out_path
		self.image = None
		if create_image:
			self.image = np.asarray(imageio.imread(path))


	@classmethod
	def from_image(cls, image):
		i = cls(None)
		i.image = image
		return i

class ImageVolume():
	def __init__(self, i, o, p="_"):
		self.idir = i
		self.odir = o
		self.prefix = p
		self.volume = self.volume_to_list()

	def volume_to_list(self):
		old_imgs = INTERNAL._convert_dir_to_images(self.idir)
		new_imgs = [PyifxImage(img, os.path.join(self.odir,f"{self.prefix}{os.path.split(img)[1]}")) for img in old_imgs]

		return new_imgs

def _combine(img1, img2, out_path):
	if img1.image.shape[0]*img1.image.shape[0] <= img2.image.shape[0]*img2.image.shape[1]:
		shape = img1.image.shape
	else:
		shape = img2.image.shape

	new_img = np.empty(shape)

	for r in range(len(img1.image)):
		for p in range(len(img1.image[r])):
			for c in range(len(img1.image[r][p])):
				try:
					new_img[r][p][c] = (img1.image[r][p][c]+img2.image[r][p][c])/2
				except IndexError:
					pass

	img = PyifxImage(None, out_path, False)
	img.image = new_img.astype(np.uint8)
	return img

