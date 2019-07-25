""" This is the testing file for the Pyifx library. All function definitions are contained
in the file named "test_function_defs.py" for the purpose of testing. """
import pyifx

def set_paths(new_path):
	for img in img_list:
		img.set_output_path(os.path.join(new_path, os.path.split(img.get_output_path())[1]))

	img_vol.set_output_path(os.path.join(new_path, os.path.split(vol.get_output_path())[1]))

	img1.set_output_path(os.path.join(new_path, os.path.split(img1.get_output_path())[1]))
	img2.set_output_path(os.path.join(new_path, os.path.split(img2.get_output_path())[1]))

def call_error_test(function, args):
	try:
		globals()[function](*args)
	except Exception:
		print("Error caught successfully.")
		return True

	print(f"ERROR NOT CAUGHT: {function}({args})")
	return False

img1 = pyifx.misc.PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "imgs/hsl/brightness/512x512-jpeg-1.jpg")
img2 = pyifx.misc.PyifxImage("tests/imgs/512x512-png-1.png", "imgs/hsl/brightness/512x512-png-1.png")

img_vol = pyifx.misc.ImageVolume("tests/imgs/", "tests/imgs/hsl/brightness", "VOLUME-")

img_list = [pyifx.misc.PyifxImage("imgs/512x512-jpeg-1.jpg", "tests/imgs/hsl/brightness/LIST-512x512-jpeg-1.jpg"), 
pyifx.misc.PyifxImage("tests/imgs/512x512-png-1.png", "tests/imgs/hsl/brightness/LIST-512x512-png-1.png"),
pyifx.misc.PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/hsl/brightness/LIST-512x512-jpg-1.jpg")]

# # TESTS TODO

# # HSL

# pyifx.hsl.brighten(img1, percent=50)
# pyifx.hsl.darken(img2, percent=50)
# pyifx.hsl.brighten(img_vol, percent=70)
# pyifx.hsl.darken(img_list, percent=70)

# call_error_test("pyifx.hsl.brighten", ["s", 50])
# call_error_test("pyifx.hsl.brighten", [img1, 's'])
# call_error_test("pyifx.hsl.brighten", [img1, 50, 's'])
# call_error_test("pyifx.hsl.darken", [img1, 50, 's'])
# call_error_test("pyifx.hsl.darken", ['s', 50])
# call_error_test("pyifx.hsl.darken", [img1, 50, 's'])
# call_error_test("pyifx.hsl.brighten", [img1, 200])
# call_error_test("pyifx.hsl.darken", [img1, -10])

# set_paths("tests/imgs/hsl/color_overlay/")

# pyifx.hsl.color_overlay(img1, [255,0,0], 60)
# pyifx.hsl.color_overlay(img_vol, [0,255,0], 60)
# pyifx.hsl.color_overlay(img_list, [0,0,255], 60)

# call_error_test("pyifx.hsl.color_overlay", ["asdf", [255,0,0], 60])
# call_error_test("pyifx.hsl.color_overlay", [img1, [255,0], 60])
# call_error_test("pyifx.hsl.color_overlay", [img1, [255,0, 'e'], 60])
# call_error_test("pyifx.hsl.color_overlay", [img1, [255,0,0], "s"])
# call_error_test("pyifx.hsl.color_overlay", [img1, [255,0,0], 200])
# call_error_test("pyifx.hsl.color_overlay", [img1, [255,0], -10])
# call_error_test("pyifx.hsl.color_overlay", [img1, [255,0,0], 60, "s"])

# set_paths("tests/imgs/hsl/saturation/")

# pyifx.hsl.saturate(img1, 70)
# pyifx.hsl.desaturate(img2, 60)
# pyifx.hsl.desaturate(img_vol, 30)
# pyifx.hsl.to_grayscale(img_list)

# call_error_test("pyifx.hsl.saturate", ["asdf", 70])
# call_error_test("pyifx.hsl.desaturate", ["asdf", 70])
# call_error_test("pyifx.hsl.to_grayscale", [10000])
# call_error_test("pyifx.hsl.saturate", [img1, "s"])
# call_error_test("pyifx.hsl.desaturate", [img1, "s"])
# call_error_test("pyifx.hsl.desaturate", [img1, -10])


# # Composition

# set_paths("tests/imgs/comp/resize/")

# pyifx.comp.resize(img1, "1024x1024")
# pyifx.comp.resize(img2, "256x256")
# pyifx.comp.resize(img_list, "694x1440")
# pyifx.comp.resize(img_vol, "1532x393")

# call_error_test("pyifx.comp.resize", [img1, "10241024"])
# call_error_test("pyifx.comp.resize", [img1, "1024xs"])
# call_error_test("pyifx.comp.resize", ["s", "1024x1024"])
# call_error_test("pyifx.comp.resize", [img1, "1024x1024x1024"])
# call_error_test("pyifx.comp.resize", [img1, 2])
# call_error_test("pyifx.comp.resize", [img1, "1024x1024", "s"])

# set_paths("tests/imgs/comp/file_type/")

# pyifx.comp.change_file_type(img1, '.png')
# pyifx.comp.change_file_type(img2, '.jpg')
# pyifx.comp.change_file_type(img_list, 'png')
# pyifx.comp.change_file_type(img_vol, 'jpeg')

# call_error_test("pyifx.comp.change_file_type", [img1, "ekr"])
# call_error_test("pyifx.comp.change_file_type", [2, "png"])
# call_error_test("pyifx.comp.change_file_type", [2, "ekr"])
# call_error_test("pyifx.comp.change_file_type", [img1, "png", "s"])

# # Graphics

# set_paths("tests/imgs/graphics/blur")

# pyifx.graphics.blur_gaussian(img1,3)
# pyifx.graphics.blur_mean(img2, 3)
# pyifx.graphics.blur_gaussian(img_list, 1)
# pyifx.graphics.blur_mean(img_vol, 1)

# call_error_test("pyifx.graphics.blur_gaussian", ["s", 3])
# call_error_test("pyifx.graphics.blur_gaussian", [img1, "s"])
# call_error_test("pyifx.graphics.blur_gaussian", [img1, 2, (3,3), "s"])
# call_error_test("pyifx.graphics.blur_mean", ["s", 3])
# call_error_test("pyifx.graphics.blur_mean", [img1, "s"])
# call_error_test("pyifx.graphics.blur_mean", [img1, 2, 's'])


# set_paths("tests/imgs/graphics/pixelate")

# pyifx.graphics.pixelate(img1, 4)
# pyifx.graphics.pixelate(img_list, 2)
# pyifx.graphics.pixelate(img_vol, 3)

# call_error_test("pyifx.graphics.pixelate", [img1, 's'])
# call_error_test("pyifx.graphics.pixelate", ['s', 4])
# call_error_test("pyifx.graphics.pixelate", [img1, 4, 's'])

# set_paths("tests/imgs/graphics/edge")

# pyifx.graphics.detect_edges(img1)
# pyifx.graphics.detect_edges(img_list)
# pyifx.graphics.detect_edges(img_vol)

# call_error_test("pyifx.graphics.detect_edges", ['s'])
# call_error_test("pyifx.graphics.pixelate", [img1, 's'])

# set_paths("tests/imgs/graphics/custom_convolution")

# sobel_horizontal_np = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
# sobel_vertical = [[-1,-2,-1], [0,0,0], [1,2,1]]
# box_blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

# pyifx.graphics.convolute_custom(img1, sobel_horizontal_np)
# pyifx.graphics.convolute_custom(img_list, sobel_vertical)
# pyifx.graphics.convolute_custom(img_vol, box_blur)

# call_error_text("pyifx.graphics.convolute_custom", ['s', sobel_horizontal_np])
# call_error_text("pyifx.graphics.convolute_custom", [img1, 's'])
# call_error_text("pyifx.graphics.convolute_custom", [img1, sobel_horizontal_np, 's'])

# # Misc

# set_paths("tests/imgs/misc/combine/")

# pyifx.misc.combine(img1, img2, "tests/imgs/misc/combine") #TBC

# call_error_test("pyifx.misc.combine", [img1, 's', "tests/imgs/misc/combine"])

# set_paths("tests/imgs/misc/class_functions/")

# TBA


# COMPLETED TESTS

# brighten(ImageVolume("tests/imgs/", "tests/imgs/brightenedImages", "_"), 0.6) - Image volume class test

# brighten(PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/test_ouput.jpg"), 0.6) - Single image test

# imgs = [PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/test_ouput.jpg"),
# PyifxImage("tests/imgs/512x512-jpg-1.jpg", "tests/imgs/test_output_2.jpg")]
# brighten(imgs, 0.6) - List image test 
# brighten(9999, 0.6) - Wrong type test

# brighten(PyifxImage("tests/imgs/512x512-jpeg-1.jpg", "tests/imgs/test_existing_file.jpg"), 0.6) - Existing file test

# brighten(img_list[:3], 0.6) 
# darken(img_list[3:], 0.6)

# brighten(img_vol, 0.6)
# darken(img_vol_dark, 0.6)

# brighten(img_1, 0.6)
# darken(img_2, 0.6) 

# brighten(img_list[:3], 0.5)
# darken(img_list[3:], 0.5) - New Combination Tests

# color_overlay(img_1, [128,242,242])
# color_overlay(img_2, [74,24,25], 80) - Color Overlay Tests

# saturate(img_1, 80)
# desaturate(img_2, 80)
# to_grayscale(img_1) - Grayscale Tests

# blur_gaussian(img_1, 6)
# blur_mean(img_2, 6) - Blur Tests

# pixelate(img_1, 3)
# pixelate(img_2, 6) - Pixelation tests

# detect_edges(img_1)
# detect_edges(img_2) - Edge detection tests

# resize(img_1, "1024x1024")
# resize(img_1, "512x1024")
# resize(img_1, "256x256")
# resize(img_2, "768x2549") - Resize tests

# v1.0 TESTS

