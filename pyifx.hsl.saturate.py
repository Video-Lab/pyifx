from test_vars import *
set_paths("../tests/imgs/hsl/saturate")

pyifx.hsl.saturate(img1, 70)

call_error_test("pyifx.hsl.saturate", ["asdf", 70])
call_error_test("pyifx.hsl.saturate", [img1, "s"])