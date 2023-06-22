import pandas as pd
import matplotlib.pyplot as plt
import os


csv_directory="/home/suzuki/NeRF/distilled-feature-fields/logs/colmap/vegetables/evaluate_epoch_10/datas"
file_names = []  # ファイル名を格納するリスト

for file_name in os.listdir(csv_directory):
    if os.path.isfile(os.path.join(csv_directory, file_name)):
        file_names.append(os.path.splitext(file_name)[0])

print(file_names)
# file_name=["psnr"]
# import pdb; pdb.set_trace()
for file_name in file_names:
    plt.clf()
    file_path = os.path.join(csv_directory, f"{file_name}.csv")
    print(file_path)
    data = pd.read_csv(file_path)
    # 列の選択とデータの整形
    x = data['Step']
    y = data['Value']
    plt.plot(x, y,label=file_name)
    # plt.ylim(20, 25)
    plt.xlabel('iteration')
    plt.ylabel(file_name)
    plt.savefig(f"{csv_directory}/{file_name}.png")  # 例：PNG形式で保存




