# Composition

Graphics

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

Misc

set_paths("tests/imgs/misc/combine/")

pyifx.misc.combine(img1, img2, "tests/imgs/misc/combine/combined.jpg")
pyifx.misc.combine([img_list[0]], [img_list[1]], "tests/imgs/misc/combine/LIST-combined.jpg")
img_vol_new = pyifx.misc.ImageVolume("tests/imgs/", "tests/imgs/misc/combine/", "VOLUME-")
img_vol_new = img_vol.set_volume([img_list[0]])
pyifx.misc.combine(img_vol_new, [img_list[1]], "tests/imgs/misc/combine/VOLUME-combined.jpg")


call_error_test("pyifx.misc.combine", [img1, 's', "tests/imgs/misc/combine"])
call_error_test("pyifx.misc.combine", [img1, [img_list[0]], "tests/imgs/misc/combine"])