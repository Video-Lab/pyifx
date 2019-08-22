from test_vars import *
set_paths("../tests/imgs/hsl/brighten")

pyifx.hsl.brighten(img1, percent=50)
pyifx.hsl.brighten(img_vol, percent=70)

call_error_test("pyifx.hsl.brighten", ["s", 50])
call_error_test("pyifx.hsl.brighten", [img1, 's'])
call_error_test("pyifx.hsl.brighten", [img1, 50, 's'])
call_error_test("pyifx.hsl.brighten", [img1, 200])