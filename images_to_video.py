import glob
import sys
from PIL import Image

dataset_name="vegetables"
log_name="original_epock_10"

frames = []
images = sorted(glob.glob(f"logs/colmap/{dataset_name}/{log_name}/rendered/*.png"))

for image in images:
    new_frame = Image.open(image)
    frames.append(new_frame)


frames[0].save(f'logs/colmap/{dataset_name}/{log_name}/{log_name}.gif',
               format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=50,
               loop=0)