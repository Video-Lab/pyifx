from test_vars import *
set_paths("../tests/imgs/graphics/blur_gaussian")

pyifx.graphics.blur_gaussian(img1,3)
pyifx.graphics.blur_gaussian(img_list, 1)

call_error_test("pyifx.graphics.blur_gaussian", ["s", 3])
call_error_test("pyifx.graphics.blur_gaussian", [img1, "s"])
call_error_test("pyifx.graphics.blur_gaussian", [img1, 2, (3,3), "s"])