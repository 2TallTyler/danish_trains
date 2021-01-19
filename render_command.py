#################################
####### SET UP FILES HERE #######
#################################

# Name of NewGRF, as it appears in file names
vehicle_name = "mz_iv"

vehicle_manifest = "8_standard"

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

import subprocess
import shutil
import os

input_voxel = "voxel/" + vehicle_name + ".vox"
manifest_path = "voxel/manifest/" + vehicle_manifest + ".json"
output_sprite = "src/gfx/" + vehicle_name

output_sprite_path = output_sprite + "_8bpp.png"

if os.path.exists(output_sprite_path):
    os.remove(output_sprite_path)

gorender = subprocess.run(["C:/tools/gorender/renderobject.exe", "-input", input_voxel, "-m", manifest_path, "-output", output_sprite, "-8", "-palette", "C:/tools/gorender/files/ttd_palette.json"], stdout = subprocess.PIPE, text=True)
print(gorender.stdout)
