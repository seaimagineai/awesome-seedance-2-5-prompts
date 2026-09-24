# Seedance 2.5 prompts: watch, copy, create

[English](README_EN.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![Original guide illustration; not a model-generated sample](assets/seaimagine-seedance-hero.svg)

A SeaImagine edition of the company’s Flaq source library: 120 recipes, comprising 60 Chinese and 60 English entries. Fourteen language supplements provide six practice prompts each; the 120 recipes have not all been translated into every language.

## Start with one shot

Choose a scene in the index, copy a prompt, then replace the subject, materials and camera movement. For image-based work, prepare an image you have permission to use. In SeaImagine, select the available input mode and supported duration; review the result before extending it.

[120-recipe index](prompts/README.en.md) · [Six English exercises](prompts/i18n/prompt-library.en.md)

## Create with SeaImagine

Open the Seedance page for this model. Use Create to prepare visual references and find image and video tools. Current availability, prices and limits are shown in the interface. A suggested duration is a creative brief, not a service guarantee.

[SeaImagine · Seedance 2.5](https://seaimagine.com/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/create/)

## Learn from community videos

The model name is the community author’s claim. These videos are works by external creators; we have not verified whether they were generated through SeaImagine. Click a thumbnail to watch the video, and read the author’s original post for the source prompt. These are editorial references, not a verified popularity ranking.

### Cooking and sound timing

[![Cooking and sound timing — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[Original post and author’s prompt](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

Notice how close-ups of ingredients and synchronized sounds prepare the final comic beat.

### One garment, several looks

[![One garment, several looks — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[Original post and author’s prompt](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

Keep the garment’s color and construction consistent; use matching movements to connect the outfits.

[All 12 community examples](README.md) · [Official examples and sources](docs/official-examples.md)

## Prompt structure

```text
[Mode] Text / image / reference / edit
[Goal] Audience, emotion, duration, aspect ratio
[References] Image 1: subject; video 1: camera movement only
[Keep fixed] Face, outfit, product shape, light, object count
[Timeline] Opening → action → change → final frame
[Camera] Start, path, speed, focus, stopping point
[Physics] Gaze, hands, weight, contact, fabric, water
[Sound] Dialogue, ambience, effects, synchronization
[Avoid] Warping, duplicates, extra limbs, fake text, logos
```

## Copy a complete product-shot prompt

![Sparkling tea reference image](assets/product-sparkling-tea-reference.png)

Reference image from the Flaq source repository, not a video output. You can use it directly as the input for this exercise.

Use one reference image of an unbranded bottle. This is a practice prompt, not the prompt used in either video above; no output test is claimed. Shorten or split the timeline if your chosen interface requires it.

```text
Use the clear glass bottle in Image 1 as the only product anchor. Preserve its silhouette, cap, blank-label proportions, amber liquid level, condensation, and key-light direction. Generate no text.

00:00–00:05: Macro focus on one condensation drop, then rack focus to fine bubbles rising through the liquid. 00:05–00:11: Orbit clockwise by 35 degrees while slowly pulling back; the ice pedestal refracts naturally and the bottle remains perfectly stable. 00:11–00:17: A warm backlight passes behind the bottle; the cap lifts only slightly with a clean click and releases a restrained mist. 00:17–00:24: Lower to a subtle hero angle and stop on a clean front view with negative space above.

Audio: cap click, fine carbonation, a light ice sound, and minimal original rhythm. No extra bottles, label drift, warped glass, liquid clipping, fake text, logo, trademark, or watermark.
```

[Six English exercises](prompts/i18n/prompt-library.en.md) · [120-recipe index](prompts/README.en.md) · [Workflow guide](docs/seaimagine-workflow.md) · [Source and attribution notes](docs/PROVENANCE.md)

[Flaq · GitHub](https://github.com/flaqai/awesome_seedance_2_5) · [SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)
