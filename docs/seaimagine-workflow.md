# Make your first video with SeaImagine / 从一条短片开始

[Home](../README.md) · [中文首页](../README_ZH.md) · [Official examples](official-examples.md)

Use [Seedance 2.5](https://seaimagine.com/model/seedance-2-5/) when you already have a scene idea or starting image. [Create](https://seaimagine.com/create/) is the general creative entry point; [AI Image Generator](https://seaimagine.com/ai-image-generator/) can help prepare a reference before animating it. These are first-party product links, not affiliate links.

| What you have | What to do | Check the result |
|---|---|---|
| A short idea | Specify one subject, one action, a camera path and ending | Is the action readable? |
| A product photo | Upload it; lock shape, material and part count | Does the product change shape? |
| An illustration | Upload it; preserve silhouette and style | Do new characters or objects appear? |
| A first and last composition | Use the optional end frame if the current interface offers it | Is the transition physically plausible? |
| A complex multi-reference/editing recipe | First confirm the required controls exist in the selected interface | Do not substitute an ordinary image upload for a video-editing control |

## Public page descriptions versus verified operation

Checked on 2026-09-24: the [public SeaImagine model page](https://seaimagine.com/model/seedance-2-5/) describes text/image inputs, an optional ending image, 5–30 seconds in five-second steps, 480p/720p, and six text-mode aspect ratios. The page also mentions synchronized audio and multi-image guidance. These descriptions were read publicly; no paid generation, model-control test, or long-term availability measurement was performed.

The [model developer’s page](https://seed.bytedance.com/en/seedance2_5) describes reference-based generation, extension and editing. Those model capabilities do not establish that every control is available through SeaImagine. Check the live UI, [pricing](https://seaimagine.com/pricing/) and terms before generation. This guide does not provide or assume a SeaImagine API schema.

## A useful first test

1. Open the [sparkling-tea example and its input image](../README.md#premium-unbranded-sparkling-tea-ad).
2. Start with a five-second close-up: lock the bottle, ask for condensation and a slow push-in.
3. Choose an available duration and aspect ratio in the interface; prompt wording alone does not set export parameters.
4. Review product shape, hands, contact, audio and the final frame. Change one instruction at a time.
5. Save the prompt, actual settings, input files and output. Longer timelines in the library are creative briefs; shorten or split them when needed.

## 中文操作要点

有想法就从文字开始，有产品图或插画就先上传参考图。先做 5 秒动作测试，一次只改一个变量：主体、运镜或动作。提示词中的时长、画幅和分辨率只是创作要求，实际生成设置要在界面选择。

本库部分配方使用视频编辑、多参考或延长。模型官方支持某项能力，不代表品牌入口已开放相同控制。上述规格来自公开页面，尚未实际生成验证；也不能据此承诺服务长期稳定。生成前查看当前界面与费用即可。
