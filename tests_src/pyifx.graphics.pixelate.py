from test_vars import *
set_paths("../tests/imgs/graphics/pixelate")

pyifx.graphics.pixelate(img1, 4)
pyifx.graphics.pixelate(img_list, 2)
pyifx.graphics.pixelate(img_vol, 3)

call_error_test("pyifx.graphics.pixelate", [img1, 's'])
call_error_test("pyifx.graphics.pixelate", ['s', 4])
call_error_test("pyifx.graphics.pixelate", [img1, 4, 's'])
call_error_test("pyifx.graphics.pixelate", [img1, 's'])