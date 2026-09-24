# Seedance 2.5 プロンプト集：見て、コピーして、作る

[English](README_EN.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![オレンジ色の路面電車が曲線の線路を進み、街並みは線画から紙模型、暖かな光に照らされた写実的な建物へと変化します。AI制作の表紙で、Seedanceの動画出力ではありません。](assets/seaimagine-seedance-hero-v5.jpg)

構造のスケッチから質感、光、動きへと発展する創作のアイデアを、オリジナルの風景で表現しました。

社内の Flaq 元リポジトリを SeaImagine 向けに編集したものです。120本のレシピは中国語60本と英語60本で構成され、14言語の補足資料には各6本の練習用プロンプトがあります。120本すべてを各言語に翻訳したものではありません。

## まずはワンカットから

索引で用途を選び、プロンプトをコピーして、被写体・素材・カメラの動きを置き換えます。画像を使う場合は、使用権限のある画像を用意してください。SeaImagine の画面で対応する入力方式と尺を確認し、生成結果を見てから延長します。

[120本の索引](prompts/README.md) · [日本語の練習6本](prompts/i18n/prompt-library.ja.md)

## SeaImagine で作成

モデルの利用は Seedance ページへ。参照画像の準備や画像・動画ツールの選択には Create を使います。提供状況、料金、制限は利用画面で確認してください。例の秒数は演出案であり、サービスの保証ではありません。

[SeaImagine · Seedance 2.5](https://seaimagine.com/ja/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/ja/create/)

## コミュニティの動画から学ぶ

モデル名は投稿者の説明に基づきます。外部の作者による作品であり、SeaImagine を使って生成されたかどうかは確認していません。サムネイルから動画を開き、作者の原投稿で元のプロンプトを確認できます。編集上の参考例であり、人気順位を検証した一覧ではありません。

### 調理と音のタイミング

[![調理と音のタイミング — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[作者の原投稿とプロンプト](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

食材の接写と同期した音が、最後の笑いにつながる流れに注目します。

### 一着から複数のコーデへ

[![一着から複数のコーデへ — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[作者の原投稿とプロンプト](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

服の色と構造を保ち、似た動きをつないで着こなしを切り替えます。

[コミュニティ全12例](README.md) · [公式の作例と出典](docs/official-examples.md)

## プロンプトの基本構造

```text
[モード] テキスト / 画像 / 参照 / 編集
[目的] 用途、対象、感情、尺、アスペクト比
[素材の役割] 画像1は人物のみ、動画1はカメラ経路のみ参照
[固定要素] 顔、衣装、製品形状、背景、光源、物の数
[時間軸] 導入 -> 主動作 -> 変化 -> 最終画面
[撮影] 画角、カメラ高、移動経路、速度、焦点、停止位置
[演技と物理] 視線、手、重さ、慣性、接触、布、水、煙
[音] セリフ、環境音、効果音、音楽、同期点
[禁止] 変形、重複、手足の追加、偽文字、ロゴ、透かし
```

## 商品動画のプロンプトをコピー

![炭酸ティーの参照画像](assets/product-sparkling-tea-reference.png)

Flaq 元リポジトリの参照画像です。動画の生成結果ではありません。この練習の入力画像としてそのまま使えます。

無地のボトルを写した参照画像を1枚用意してください。以下は練習用で、上の動画の元プロンプトではなく、生成検証済みともしていません。画面の制限に合わせて尺を短くするか、複数カットに分けます。

```text
画像1の透明なガラス瓶を唯一の商品基準にする。瓶の形、キャップ、無地ラベルの比率、琥珀色の液面、結露、主光源を維持し、文字は生成しない。

00:00–00:05 結露の一滴をマクロ撮影し、液体内の細かな気泡へフォーカスを移す。00:05–00:11 時計回りに35度回りながらゆっくり引く。氷台の屈折は自然で、瓶は完全に安定。00:11–00:17 暖色の逆光が通過し、キャップはわずかに上がって少量の霧だけを放つ。00:17–00:24 少し低いヒーローアングルへ下がり、上部に後編集用の余白を残して停止する。

音：キャップ、炭酸、氷、最小限のオリジナルリズム。瓶の追加、ラベルのずれ、ガラス変形、液体の貫通、偽文字、ロゴ、商標、透かしは禁止。
```

[日本語の練習6本](prompts/i18n/prompt-library.ja.md) · [120本の索引](prompts/README.md) · [作成手順](docs/seaimagine-workflow.md) · [出典と帰属](docs/PROVENANCE.md)

[Flaq · GitHub](https://github.com/flaqai/awesome_seedance_2_5) · [SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)
