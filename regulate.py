import os
import glob

# テキストファイルと画像ファイルを探すためのパターンを設定
# 画像はjpgとpngの両方を探す
txt_pattern = "*.txt"
jpg_pattern = "*.jpg"
png_pattern = "*.png"

# テキストファイルと画像ファイルのリストを取得
txt_files = glob.glob(txt_pattern)
jpg_files = glob.glob(jpg_pattern)
png_files = glob.glob(png_pattern)

# テキストファイルと画像ファイルを名前で比較し、片方しかない場合は削除する
for txt in txt_files:
    # テキストファイルの名前を取得
    text_name = os.path.splitext(txt)[0]
    # 同じ名前の画像ファイルがあるか確認
    if not any(image_name == text_name for image_name in jpg_files or png_files):
        # 同じ名前の画像ファイルがない場合は、削除するかどうか確認する
        response = input(f"{txt} のみがあります。削除しますか？ [y/n]: ")
        if response == "y":
            os.remove(txt)

for jpg in jpg_files:
    # 画像ファイルの名前を取得
    image_name = os.path.splitext(jpg)[0]
    # 同じ名前のテキストファイルがあるか確認
    if not any(text_name == image_name for text_name in txt_files):
        # 同じ名前のテキストファイルがない場合は、削除するかどうか確認する
        response = input(f"{jpg} のみがあります。削除しますか？ [y/n]: ")
        if response == "y":
            os.remove(jpg)

for png in png_files:
    # 画像ファイルの名前を取得
    image_name = os.path.splitext(png)[0]
    # 同じ名前のテキストファイルがあるか確認
    if not any(text_name == image_name for text_name in txt_files):
        # 同じ名前のテキストファイルがない場合は、削除するかどうか確認する
        response = input(f"{png} のみがあります。削除しますか？ [y/n]: ")
        if response == "y":
            os.remove(png)

print("終了")
