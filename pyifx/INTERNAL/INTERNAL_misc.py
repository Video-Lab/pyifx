from INTERNAL import *

def _type_checker(var, types)
	if type(var) in types:
		return True

	raise TypeError("Please use correct variable types.")
	return False

def _write_file(img):
	out_path, extension = os.path.splitext(img.output_path)

	if not os.path.exists(os.path.split(img.output_path)[0]):
		os.makedirs(os.path.split(img.output_path)[0])

	file_count = 1
	temp_path = out_path

	while os.path.isfile(out_path + extension):
		out_path = temp_path
		out_path += f" ({file_count})"
		file_count += 1

	imageio.imwrite(out_path + extension, img.image)
	return img	