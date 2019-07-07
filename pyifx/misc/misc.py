import INTERNAL

def to_image_list(dirc, output_path):
	image_list = []
	old_imgs = INTERNAL.convert_dir_to_images(dirc)
	new_imgs = {img: os.path.join(ouput_path,f"{prefix}{os.path.split(img)[1]}") for img in old_imgs}

	for i,o in new_imgs.items():
		image_list.append(INTERNAL.PyifxImage(i,o,create_image=False))

	return image_list