import argparse
import os
import glob

# 引数を解析
parser = argparse.ArgumentParser()
parser.add_argument("target_dir")
args = parser.parse_args()

# 処理対象のディレクトリを取得
os.chdir(args.target_dir)

# ファイルのリストを取得
files = list(os.path.splitext(os.path.basename(file))[0] for file in glob.glob("*"))

# 名前が重複していないファイルを削除
for file in files:
    if files.count(file) < 2:
        try:
            os.remove(file + ".jpg")
            print(f"削除: {file}.jpg")
        except:
            pass
        try:
            os.remove(file + ".png")
            print(f"削除: {file}.png")
        except:
            pass
        try:
            os.remove(file + ".txt")
            print(f"削除: {file}.txt")
        except:
            pass

print("終了")
