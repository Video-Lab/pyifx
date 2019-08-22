from test_vars import *
set_paths("../tests/imgs/hsl/darken")

pyifx.hsl.darken(img2, percent=50)
pyifx.hsl.darken(img_list, percent=70)

call_error_test("pyifx.hsl.darken", [img1, 50, 's'])
call_error_test("pyifx.hsl.darken", ['s', 50])
call_error_test("pyifx.hsl.darken", [img1, 50, 's'])
call_error_test("pyifx.hsl.darken", [img1, -10])