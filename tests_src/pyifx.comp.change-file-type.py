from test_vars import *
set_paths("../tests/imgs/comp/change-file-type")

pyifx.comp.change_file_type(img1, '.png')
pyifx.comp.change_file_type(img2, '.jpg')
pyifx.comp.change_file_type(img_list, 'png')
pyifx.comp.change_file_type(img_vol, 'jpeg')

call_error_test("pyifx.comp.change_file_type", [img1, "ekr"])
call_error_test("pyifx.comp.change_file_type", [2, "png"])
call_error_test("pyifx.comp.change_file_type", [2, "ekr"])
call_error_test("pyifx.comp.change_file_type", [img1, "png", "s"])