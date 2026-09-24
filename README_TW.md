# Seedance 2.5 提示詞：看案例、複製、開始製作

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![橘色電車沿彎軌前進，街區從線稿、紙模型過渡到暖燈照亮的寫實建築。AI 製作封面，非 Seedance 影片輸出。](assets/seaimagine-seedance-hero-v5.jpg)

以原創場景呈現從結構草圖到材質、光照與運動的創作構想。

本頁由本公司 Flaq 原始儲存庫改編為 SeaImagine 版本。120 組配方包含中文 60 組、英文 60 組；另有 14 種語言的補充檔案，各含 6 組練習提示詞，並非將全部 120 組翻譯成每一種語言。

## 先從一個鏡頭開始

在索引選擇用途，複製提示詞，再替換主體、素材與運鏡。如果使用圖片，請準備有權使用的參考圖。在 SeaImagine 介面確認可用的輸入模式與片長，檢查生成結果後再延長。

[繁體中文練習 6 組](prompts/i18n/prompt-library.zh-TW.md) · [120 組配方索引 · 簡體中文](prompts/README.md)

## 從社群影片學習

模型名稱依作者自述，這些是外部作者的作品，我們尚未確認是否透過 SeaImagine 生成。點選縮圖可觀看影片，前往作者原始貼文可查看提示詞。這是編輯選例，不是經過驗證的人氣排行榜。

### 料理與聲音節奏

[![料理與聲音節奏 — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[作者原始貼文與提示詞](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

觀察食材特寫和同步音效，如何鋪陳最後的喜劇收尾。

### 一件衣服，多種搭配

[![一件衣服，多種搭配 — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[作者原始貼文與提示詞](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

保持服裝顏色與結構一致，用相似動作銜接不同搭配。

[完整 12 組社群案例 · 簡體中文](README_ZH.md) · [官方案例與來源 · 英文](docs/official-examples.md)

## 提示詞基本結構

```text
[模式] 文字 / 圖片 / 參考素材 / 編輯
[目標] 觀眾、情緒、片長、畫面比例
[素材用途] 圖片1僅參考主體，影片1僅參考運鏡
[固定要素] 臉孔、服裝、商品形狀、光源、物件數量
[時間軸] 開場 → 動作 → 變化 → 結尾畫面
[運鏡] 起點、路徑、速度、焦點、停止位置
[物理與演出] 視線、手部、重量、接觸、布料、水
[聲音] 對白、環境音、音效、同步點
[避免] 變形、重複、多餘肢體、假文字、標誌
```

## 複製完整商品影片提示詞

![氣泡茶參考圖](assets/product-sparkling-tea-reference.png)

來自 Flaq 原始儲存庫的參考圖片，並非影片生成成果，可直接作為這組練習的輸入圖片。

準備一張無品牌瓶子的參考圖。以下是練習提示詞，並非上方影片使用的原始提示詞，也不宣稱已完成生成測試。請依介面限制縮短時間或拆成多個鏡頭。

```text
以圖片1中的透明玻璃瓶為唯一產品錨點。保持瓶身輪廓、瓶蓋、空白標籤比例、琥珀色液面、凝露與主光方向不變，不生成文字。

00:00–00:05 微距對焦一顆凝露，再轉焦到液體中上升的細小氣泡。00:05–00:11 鏡頭順時針環繞35度並緩慢拉遠，冰台折射自然，瓶子完全穩定。00:11–00:17 暖光從瓶後掃過，瓶蓋只輕微彈起並釋放少量霧氣。00:17–00:24 降到略低機位，停在上方留有後製空間的正面英雄鏡頭。

聲音：瓶蓋、氣泡、冰塊與極簡原創節奏。禁止多餘瓶子、標籤漂移、玻璃變形、液體穿模、偽文字、標誌、商標與浮水印。
```

## 使用 SeaImagine 製作

![金色紙帆船駛向紙海中的暖光燈塔。](assets/seaimagine-paper-sea.jpg)

本庫以 AI 製作的原創插畫，不是 Seedance 影片生成結果。

把前面商品練習的「保持外形、指定材質、安排運鏡」，用在一個小故事裡。打開 SeaImagine，從文字生成影片開始，先試試下面這個 5 秒構想。這是練習提示詞，尚未完成生成實測。

```text
5 秒，一鏡到底。金色紙帆船緩緩穿過藍綠色紙浪。鏡頭從低處跟隨帆船，遠方燈塔投下暖光。保持船身、船帆與紙張纖維，結尾平穩停住。不出現文字、標誌、多餘船隻或變形。
```

[SeaImagine · Seedance 2.5](https://seaimagine.com/tw/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/tw/create/)

[繁體中文練習 6 組](prompts/i18n/prompt-library.zh-TW.md) · [120 組配方索引 · 簡體中文](prompts/README.md) · [製作步驟 · 英文](docs/seaimagine-workflow.md) · [來源與歸屬說明 · 英文](docs/PROVENANCE.md)

[Flaq · GitHub](https://github.com/flaqai/awesome_seedance_2_5) · [SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)
