from test_vars import *
set_paths("../tests/imgs/hsl/to-grayscale")

pyifx.hsl.to_grayscale(img_list)

call_error_test("pyifx.hsl.to_grayscale", [10000])