from test_vars import *
set_paths("../tests/imgs/graphics/blur_mean")

pyifx.graphics.blur_mean(img2, 3)
pyifx.graphics.blur_mean(img_vol, 1)

call_error_test("pyifx.graphics.blur_mean", ["s", 3])
call_error_test("pyifx.graphics.blur_mean", [img1, "s"])
call_error_test("pyifx.graphics.blur_mean", [img1, 2, 's'])