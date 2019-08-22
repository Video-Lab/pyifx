from test_vars import *
set_paths("../tests/imgs/graphics/convolute_custom")

sobel_horizontal_np = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
sobel_vertical = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
box_blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

pyifx.graphics.convolute_custom(img1, sobel_horizontal_np)
pyifx.graphics.convolute_custom(img_list, sobel_vertical)
pyifx.graphics.convolute_custom(img_vol, box_blur)

call_error_test("pyifx.graphics.convolute_custom", ['s', sobel_horizontal_np])
call_error_test("pyifx.graphics.convolute_custom", [img1, 's'])
call_error_test("pyifx.graphics.convolute_custom", [img1, sobel_horizontal_np, 's'])
