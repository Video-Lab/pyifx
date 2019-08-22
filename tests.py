""" This is the testing file for the Pyifx library. All function definitions are contained
in the file named "test_function_defs.py" for the purpose of testing. """


# HSL

pyifx.hsl.brighten(img1, percent=50)
pyifx.hsl.darken(img2, percent=50)
pyifx.hsl.brighten(img_vol, percent=70)
pyifx.hsl.darken(img_list, percent=70)

call_error_test("pyifx.hsl.brighten", ["s", 50])
call_error_test("pyifx.hsl.brighten", [img1, 's'])
call_error_test("pyifx.hsl.brighten", [img1, 50, 's'])
call_error_test("pyifx.hsl.darken", [img1, 50, 's'])
call_error_test("pyifx.hsl.darken", ['s', 50])
call_error_test("pyifx.hsl.darken", [img1, 50, 's'])
call_error_test("pyifx.hsl.brighten", [img1, 200])
call_error_test("pyifx.hsl.darken", [img1, -10])

set_paths("tests/imgs/hsl/color_overlay/")

pyifx.hsl.color_overlay(img1, [255,0,0], 100)
pyifx.hsl.color_overlay(img_vol, [0,255,0], 100)
pyifx.hsl.color_overlay(img_list, [0,0,255], 100)

call_error_test("pyifx.hsl.color_overlay", ["asdf", [255,0,0], 60])
call_error_test("pyifx.hsl.color_overlay", [img1, [255,0], 60])
call_error_test("pyifx.hsl.color_overlay", [img1, [255,0, 'e'], 60])
call_error_test("pyifx.hsl.color_overlay", [img1, [255,0,0], "s"])
call_error_test("pyifx.hsl.color_overlay", [img1, [255,0,0], 200])
call_error_test("pyifx.hsl.color_overlay", [img1, [255,0], -10])
call_error_test("pyifx.hsl.color_overlay", [img1, [255,0,0], 60, "s"])

set_paths("tests/imgs/hsl/saturation/")

pyifx.hsl.saturate(img1, 70)
pyifx.hsl.desaturate(img2, 60)
pyifx.hsl.desaturate(img_vol, 30)
pyifx.hsl.to_grayscale(img_list)

call_error_test("pyifx.hsl.saturate", ["asdf", 70])
call_error_test("pyifx.hsl.desaturate", ["asdf", 70])
call_error_test("pyifx.hsl.to_grayscale", [10000])
call_error_test("pyifx.hsl.saturate", [img1, "s"])
call_error_test("pyifx.hsl.desaturate", [img1, "s"])
call_error_test("pyifx.hsl.desaturate", [img1, -10])


# Composition

set_paths("tests/imgs/comp/resize/")

pyifx.comp.resize(img1, "1024x1024")
pyifx.comp.resize(img2, "256x256")
pyifx.comp.resize(img_list, "694x1440")
pyifx.comp.resize(img_vol, "1532x393")

call_error_test("pyifx.comp.resize", [img1, "10241024"])
call_error_test("pyifx.comp.resize", [img1, "1024xs"])
call_error_test("pyifx.comp.resize", ["s", "1024x1024"])
call_error_test("pyifx.comp.resize", [img1, "1024x1024x1024"])
call_error_test("pyifx.comp.resize", [img1, 2])
call_error_test("pyifx.comp.resize", [img1, "1024x1024", "s"])

set_paths("tests/imgs/comp/file_type/")

pyifx.comp.change_file_type(img1, '.png')
pyifx.comp.change_file_type(img2, '.jpg')
pyifx.comp.change_file_type(img_list, 'png')
pyifx.comp.change_file_type(img_vol, 'jpeg')

call_error_test("pyifx.comp.change_file_type", [img1, "ekr"])
call_error_test("pyifx.comp.change_file_type", [2, "png"])
call_error_test("pyifx.comp.change_file_type", [2, "ekr"])
call_error_test("pyifx.comp.change_file_type", [img1, "png", "s"])

# Graphics

set_paths("tests/imgs/graphics/blur")

pyifx.graphics.blur_gaussian(img1,3)
pyifx.graphics.blur_mean(img2, 3)
pyifx.graphics.blur_gaussian(img_list, 1)
pyifx.graphics.blur_mean(img_vol, 1)

call_error_test("pyifx.graphics.blur_gaussian", ["s", 3])
call_error_test("pyifx.graphics.blur_gaussian", [img1, "s"])
call_error_test("pyifx.graphics.blur_gaussian", [img1, 2, (3,3), "s"])
call_error_test("pyifx.graphics.blur_mean", ["s", 3])
call_error_test("pyifx.graphics.blur_mean", [img1, "s"])
call_error_test("pyifx.graphics.blur_mean", [img1, 2, 's'])


set_paths("tests/imgs/graphics/pixelate")

pyifx.graphics.pixelate(img1, 4)
pyifx.graphics.pixelate(img_list, 2)
pyifx.graphics.pixelate(img_vol, 3)

call_error_test("pyifx.graphics.pixelate", [img1, 's'])
call_error_test("pyifx.graphics.pixelate", ['s', 4])
call_error_test("pyifx.graphics.pixelate", [img1, 4, 's'])

set_paths("tests/imgs/graphics/edge")

pyifx.graphics.detect_edges(img1)
pyifx.graphics.detect_edges(img_list)
pyifx.graphics.detect_edges(img_vol)

call_error_test("pyifx.graphics.detect_edges", ['s'])
call_error_test("pyifx.graphics.pixelate", [img1, 's'])

set_paths("tests/imgs/graphics/custom_convolution")

sobel_horizontal_np = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
sobel_vertical = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
box_blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

pyifx.graphics.convolute_custom(img1, sobel_horizontal_np)
pyifx.graphics.convolute_custom(img_list, sobel_vertical)
pyifx.graphics.convolute_custom(img_vol, box_blur)

call_error_test("pyifx.graphics.convolute_custom", ['s', sobel_horizontal_np])
call_error_test("pyifx.graphics.convolute_custom", [img1, 's'])
call_error_test("pyifx.graphics.convolute_custom", [img1, sobel_horizontal_np, 's'])

# Misc

set_paths("tests/imgs/misc/combine/")

pyifx.misc.combine(img1, img2, "tests/imgs/misc/combine/combined.jpg")
pyifx.misc.combine([img_list[0]], [img_list[1]], "tests/imgs/misc/combine/LIST-combined.jpg")
img_vol_new = pyifx.misc.ImageVolume("tests/imgs/", "tests/imgs/misc/combine/", "VOLUME-")
img_vol_new = img_vol.set_volume([img_list[0]])
pyifx.misc.combine(img_vol_new, [img_list[1]], "tests/imgs/misc/combine/VOLUME-combined.jpg")


call_error_test("pyifx.misc.combine", [img1, 's', "tests/imgs/misc/combine"])
call_error_test("pyifx.misc.combine", [img1, [img_list[0]], "tests/imgs/misc/combine"])