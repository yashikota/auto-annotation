import argparse
import os
import glob

# 引数を解析
parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
parser.add_argument("output_dir")
args = parser.parse_args()

# input_dirのファイル一覧を取得
input_files = [os.path.basename(file) for file in glob.glob(os.path.join(args.input_dir, "*"))]

# output_dirの.txtファイルでないファイル一覧を取得
output_files = [os.path.basename(file) for file in glob.glob(os.path.join(args.output_dir, "*")) if os.path.splitext(file)[1] != ".txt"]

diff_files = list(set(input_files) - set(output_files))

if len(diff_files) != 0:
    for file in diff_files:
        print(f"削除: {file}")
        os.remove(os.path.join(args.input_dir, file))

print("終了")
