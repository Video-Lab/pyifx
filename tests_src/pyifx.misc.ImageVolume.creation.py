from test_vars import *

print(img_vol.get_volume())

img_vol.refresh_volume(2)
print(img_vol.get_volume())

img_vol.refresh_volume(3)
print(img_vol.get_volume())