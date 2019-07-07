def brighten(i,oi,factor=0.4):
	image = INTERNAL.PyifxImage(i,oi)

	for row in range(len(image.image)):
		for p in range(len(image.image[row])):
			for v in range(len(image.image[row][p])):
				value = image.image[row][p][v]
				image.image[row][p][v] = min(255, value*(1+factor))

	cv2.imwrite(oi, image.image)
	return image