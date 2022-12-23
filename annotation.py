import os
import argparse

import cv2
import torch


# 引数を解析
parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
parser.add_argument("output_dir")
args = parser.parse_args()

# 入力画像のリストを取得
input_dir = args.input_dir
image_files = os.listdir(input_dir)

# モデルを読み込む
model = torch.jit.load("best.torchscript")

# 入力画像を処理する

print("終了")
