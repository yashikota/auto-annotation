# auto annotation

auto annotation tool for YOLOv5

## annotation.py

用意した独自モデルを用いて画像認識を行い、その結果をYOLOv5のアノテーション形式のテキストファイルと共に書き出す  
その際、YOLOv5のリポジトリが必要になるので以下のコマンドを実行する  

```sh
git submodule update --init
```

以下のコマンドを入力することでアノテーションが行える

```sh
python3 annotation.py {入力ディレクトリ} {出力ディレクトリ}
```

## regulate.py

annotation.pyで生成されたファイルは画像とアノテーションファイルが対になり生成される  
例えばhoge.pngとhoge.txtのように  
しかしhoge.pngは認識の精度が低かったため手動で削除された  
ただhoge.txtが残ったままなのでこのまま学習に用いると画像とアノテーションファイルの枚数が合わなくなりエラーになる  
regulate.pyは対になっていない画像またはアノテーションファイルを削除する    
