# Seedance 2.5 プロンプト集：見て、コピーして、作る

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![オレンジ色の路面電車が曲線の線路を進み、街並みは線画から紙模型、暖かな光に照らされた写実的な建物へと変化します。](assets/seaimagine-seedance-hero-v5.jpg)

構造のスケッチから質感、光、動きへと発展する創作のアイデアを、オリジナルの風景で表現しました。

120本のレシピを中国語60本・英語60本で収録。日本語の練習6本から、身近な題材で始められます。

## まずはワンカットから

まずは下の日本語の練習から題材を選び、被写体・素材・カメラの動きを置き換えましょう。SeaImagine で入力方式と尺を選び、短い映像を確認しながら仕上げます。

[日本語の練習6本](prompts/i18n/prompt-library.ja.md) · [120本の索引 · 簡体字中国語](prompts/README.md)

## コミュニティの動画から学ぶ

サムネイルから映像を開き、動きや音の組み立てを見てみましょう。作者の原投稿にもリンクしています。

### 調理と音のタイミング

[![調理と音のタイミング — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[作者の原投稿とプロンプト](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

食材の接写と同期した音が、最後の笑いにつながる流れに注目します。

### 一着から複数のコーデへ

[![一着から複数のコーデへ — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[作者の原投稿とプロンプト](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

服の色と構造を保ち、似た動きをつないで着こなしを切り替えます。

[コミュニティ全12例 · 英語](README.md) · [公式の作例と出典 · 英語](docs/official-examples.md)

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

上の画像を参考に、無地のボトルを写した画像を1枚用意します。まずは水滴と気泡の5秒から始め、全体を作る場合は画面で選べる尺に合わせて調整しましょう。

```text
画像1の透明なガラス瓶を唯一の商品基準にする。瓶の形、キャップ、無地ラベルの比率、琥珀色の液面、結露、主光源を維持し、文字は生成しない。

00:00–00:05 結露の一滴をマクロ撮影し、液体内の細かな気泡へフォーカスを移す。00:05–00:11 時計回りに35度回りながらゆっくり引く。氷台の屈折は自然で、瓶は完全に安定。00:11–00:17 暖色の逆光が通過し、キャップはわずかに上がって少量の霧だけを放つ。00:17–00:24 少し低いヒーローアングルへ下がり、上部に後編集用の余白を残して停止する。

音：キャップ、炭酸、氷、最小限のオリジナルリズム。瓶の追加、ラベルのずれ、ガラス変形、液体の貫通、偽文字、ロゴ、商標、透かしは禁止。
```

## SeaImagine で作成

![紙の海を進む金色の帆船と、暖かな灯台。](assets/seaimagine-paper-sea.jpg)

商品例で練習した「形を保つ」「質感を指定する」「カメラを動かす」を、小さな物語に使ってみましょう。SeaImagine で文字から動画を作成し、まずは次の 5 秒の演出案を試せます。

```text
5秒、ワンカット。金色の紙の帆船が青緑色の紙の波をゆっくり進む。低い位置からカメラが船を追い、遠くの灯台が暖かく照らす。船体、帆、紙の繊維を保ち、最後は穏やかに停止。文字、ロゴ、船の追加、変形は不要。
```

[SeaImagine · Seedance 2.5](https://seaimagine.com/ja/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/ja/create/)

[日本語の練習6本](prompts/i18n/prompt-library.ja.md) · [120本の索引 · 簡体字中国語](prompts/README.md) · [作成手順 · 英語](docs/seaimagine-workflow.md)

[SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)

## 出典と利用について

表紙・紙の海・商品参照画像は AI 制作の静止画で、動画の生成結果ではありません。本庫の練習は編集した教材であり、掲載動画の元指示とは異なり、生成実測もしていません。外部作品のモデル名は作者の説明に基づきます。素材の権利・利用条件は[出典一覧（英語）](docs/PROVENANCE.md)と[ライセンス（英語）](LICENSE)をご確認ください。
