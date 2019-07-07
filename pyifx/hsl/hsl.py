def brighten(i,oi,factor=0.35):
	image = INTERNAL.PyifxImage(i,oi)

	for row in range(len(image.image)):
		for p in range(len(image.image[row])):
			for v in range(len(image.image[row][p])):
				value = image.image[row][p][v]
				image.image[row][p][v] = min(255, value*(1+factor))

	imageio.imwrite(oi, image.image)
	return image

def brighten_multiple(dirc,opath="pyifx/",prefix="_",factor=0.35):
	if not os.path.exists(opath):
		os.makedirs(opath)

	old_imgs = convert_dir_to_images(dirc)
	new_imgs = {img: os.path.join(opath,f"{prefix}{os.path.split(img)[1]}") for img in old_imgs}


	for i, o in new_imgs.items():
		brighten(i,o,factor)