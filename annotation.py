import os
import argparse

import cv2
import torch


# 引数を解析
parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
args = parser.parse_args()

# 入力画像のリストを取得
input_dir = args.input_dir
image_files = os.listdir(input_dir)

# モデルを読み込む
dir = os.getcwd() + "/yolov5"
model = torch.hub.load(dir, "custom", path="best.pt", source="local")

# 入力画像に対して認識を実行し、結果を保存
for image_file in image_files:
    # 入力画像を読み込み
    image_path = os.path.join(input_dir, image_file)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 認識を実行
    results = model(image)

    # 結果を保存
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, image_file)
    cv2.imwrite(output_path, image)

print("終了")
