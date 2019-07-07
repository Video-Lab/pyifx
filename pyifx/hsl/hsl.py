def brighten(i,oi,factor=0.4):
	image = INTERNAL.PyifxImage(i,oi)

	for row in range(len(image.image)):
		for p in range(len(image.image[row])):
			for v in range(len(image.image[row][p])):
				value = image.image[row][p][v]
				image.image[row][p][v] = min(255, value*(1+factor))

	cv2.imwrite(oi, image.image)
	return image

def brighten_multiple(dir,prefix="_",oprefix="pyifx/",factor=0.35):
	old_imgs = convert_dir_to_images(dir)
	new_imgs = {img: os.path.join(oprefix,f"{prefix}{os.path.split[img][1]}")
	for img in old_imgs}

	for i, o in new_imgs.items():
		brighten(i,o,factor)