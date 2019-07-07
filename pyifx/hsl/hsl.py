import INTERNAL

def brighten(i,oi,factor=0.35):
	image = INTERNAL.PyifxImage(i,oi)

	for row in range(len(image.image)):
		for p in range(len(image.image[row])):
			for v in range(len(image.image[row][p])):
				value = image.image[row][p][v]
				image.image[row][p][v] = min(255, value*(1+factor))

	imageio.imwrite(oi, image.image)
	return image

def brighten_multiple(dirc,output_path="pyifx/",prefix="_",factor=0.35):
	if not os.path.exists(output_path):
		os.makedirs(output_path)

	new_imgs = misc.to_image_list(dirc, output_path, prefix)

	for img in new_imgs:
		brighten(img.path, img.output_path, factor)