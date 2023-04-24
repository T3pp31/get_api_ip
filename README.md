# はじめに

 特定のサイトのAPIのIPを取得する必要があったので，このアプリを作成

# 使い方

```
docker-compose build
docker-compose up -d
```

# 処理の流れ

1.ウェブ上の href=''にあるAPI urlを抜き出す
2.抜き出したurlを使って，そのAPIのIPアドレスを取得
3.特定のIPを探したかった場合は，探したいIPを指定し，合致するものがあればそれだけを表示する
