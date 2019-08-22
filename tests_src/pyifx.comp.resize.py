from test_vars import *
set_paths("../tests/imgs/comp/resize")

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