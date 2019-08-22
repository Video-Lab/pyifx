from test_vars import *
set_paths("../tests/imgs/graphics/detect_edges")

pyifx.graphics.detect_edges(img1)
pyifx.graphics.detect_edges(img_list)
pyifx.graphics.detect_edges(img_vol)

call_error_test("pyifx.graphics.detect_edges", ['s'])