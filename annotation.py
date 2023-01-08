import os
import argparse

import cv2
import torch


# 引数を解析
parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
parser.add_argument("output_dir")
args = parser.parse_args()

# 出力ディレクトリを作成
os.makedirs(args.output_dir, exist_ok=True)

# 入力画像のリストを取得
input_dir = args.input_dir
image_files = os.listdir(args.input_dir)

# モデルを読み込む
dir = os.getcwd() + "/yolov5"
model = torch.hub.load(dir, "custom", path="best.pt", source="local")
print("The list of classes the model can detect are: ", model.names)

# 入力画像に対して認識を実行し、結果を保存
for image_file in image_files:
    # 入力画像を読み込み
    image_path = os.path.join(input_dir, image_file)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 認識を実行
    results = model(image)

    # 結果を保存
    results.save(save_dir=args.output_dir, exist_ok=True)
    os.rename(os.path.join(args.output_dir, "image0.jpg"), os.path.join(args.output_dir, image_file))

    objects = results.pandas().xyxy[0]
    file_name = os.path.splitext(os.path.basename(image_file))[0]
    with open(os.path.join(args.output_dir, file_name + ".txt"), "w") as f:
        for object in objects.itertuples():
            class_id = object[6]
            center_x = (object.xmin + object.xmax) / 2 / image.shape[1]
            center_y = (object.ymin + object.ymax) / 2 / image.shape[0]
            width = (object.xmax - object.xmin) / image.shape[1]
            height = (object.ymax - object.ymin) / image.shape[0]
            f.write(f"{class_id} {center_x} {center_y} {width} {height}")

print("終了")
