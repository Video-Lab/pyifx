from test_vars import *

img_vol.set_input_path("../tests/misc/ImageVolume/creation/")
print(img_vol.get_input_path())
print(len(img_vol.get_volume()))

img_vol.volume_to_list(2)
print(len(img_vol.get_volume()))

img_vol.volume_to_list(0)
print(len(img_vol.get_volume()))