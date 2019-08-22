from test_vars import *
set_paths("../tests/imgs/misc/combine")

pyifx.misc.combine(img1, img2, "tests/imgs/misc/combine/combined.jpg")
pyifx.misc.combine([img_list[0]], [img_list[1]], "tests/imgs/misc/combine/LIST-combined.jpg")
img_vol_new = pyifx.misc.ImageVolume("tests/imgs/", "tests/imgs/misc/combine/", "VOLUME-")
img_vol_new = img_vol.set_volume([img_list[0]])
pyifx.misc.combine(img_vol_new, [img_list[1]], "tests/imgs/misc/combine/VOLUME-combined.jpg")


call_error_test("pyifx.misc.combine", [img1, 's', "tests/imgs/misc/combine"])
call_error_test("pyifx.misc.combine", [img1, [img_list[0]], "tests/imgs/misc/combine"])