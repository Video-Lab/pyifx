from test_vars import *

img_vol.set_input_path("../tests/misc/ImageVolume/creation/")
print(img_vol.get_volume())

img_vol.volume_to_list(2)
print(img_vol.get_volume())

img_vol.volume_to_list(3)
print(img_vol.get_volume())