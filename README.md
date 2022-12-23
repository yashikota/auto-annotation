# auto annotation

auto annotation tool for YOLOv5

## annotation.py

用意したモデルを用いて画像認識を行い、その結果をYOLOv5のアノテーション形式のテキストファイルと共に書き出す  
その際、YOLOv5のリポジトリが必要になるので以下のコマンドを実行する  

```sh
git submodule update --init
```

以下のコマンドを入力することでアノテーションが行われる  

```sh
python3 annotation.py {入力ディレクトリ} {出力ディレクトリ}
```

## regulate.py

対になっていない画像またはアノテーションファイルを探し削除を行う  
以下のコマンドで実行する  

```sh
python3 regulate.py
```
