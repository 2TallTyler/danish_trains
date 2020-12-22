#################################
####### SET UP FILES HERE #######
#################################

# Name of NewGRF, as it appears in file names
vehicle_name = "mf_1_rear"

vehicle_manifest = "8_standard"

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

import subprocess
import shutil

input_voxel = "voxel/" + vehicle_name + ".vox"
manifest_path = "voxel/manifest/" + vehicle_manifest + ".json"
output_sprite = "src/gfx/" + vehicle_name


gorender = subprocess.run(["C:/tools/gorender/renderobject.exe", "-input", input_voxel, "-m", manifest_path, "-output", output_sprite, "-8", "-palette", "C:/tools/gorender/files/ttd_palette.json"], stdout = subprocess.PIPE, text=True)
print(gorender.stdout)
