from test_vars import *
set_paths("../tests/imgs/hsl/desaturate")

pyifx.hsl.desaturate(img2, 60)
pyifx.hsl.desaturate(img_vol, 30)

call_error_test("pyifx.hsl.desaturate", ["asdf", 70])
call_error_test("pyifx.hsl.desaturate", [img1, -10])