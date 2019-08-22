from test_vars import *
set_paths("../tests/imgs/hsl/color-overlay")

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