from PIL import Image
import os

images_dir_path="/home/suzuki/NeRF/distilled-feature-fields/dataset/vegetables/images"
images_list=os.listdir(images_dir_path)
for image_file in images_list:
    image = Image.open(os.path.join(images_dir_path,image_file))
    # 画像をリサイズ
    resized_image = image.resize((480,360))
    # リサイズ後の画像を保存
    # import pdb; pdb.set_trace()
    resized_image.save(os.path.join('/home/suzuki/NeRF/distilled-feature-fields/dataset/vegetables/images_480_360',image_file))