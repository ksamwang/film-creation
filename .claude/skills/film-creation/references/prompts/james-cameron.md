---
name: james-cameron
title: 詹姆斯·卡梅隆 James Cameron
style_file: ../directors/james-cameron.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic underwater film still, a diver suspended in deep teal water, volumetric light shafts from above, saturated cyan and blue-green with a warm orange practical accent, wet skin and steel, centered stable composition, human figure in the lower third beneath a massive structure, clear deep space, 35mm grain, sincere and physical.

## 图像提示
- 主体 / 场景：a diver in a flooded steel chamber; a woman in an exosuit facing a huge machine; a small submersible descending into a blue trench.
- 景别 / 构图：wide enough to read the machine-to-body ratio, then close on wet hands, eyes or a gauge; centered, stable, human in the lower third, mass above; no tilted chaos.
- 镜头 / 焦段：21–35mm wide for immersion; 50–85mm for faces; no telephoto voyeurism.
- 光线：underwater artificial beams, bioluminescence, hard practicals, visible volumetric shafts; no flat lighting.
- 色彩：deep cyan and blue-green, saturated, with warm orange fire or practical accent; no desaturated grey.
- 材质：water, steel, glass, rubber, wet skin, bioluminescent plants; real water and practical texture.

## 视频提示
- 镜头运动：smooth underwater tracking shot, one direction only; no handheld, no whip pan.
- 主体运动：a diver swims or a machine advances slowly; bubbles and fabric drift; no chaotic flailing.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, natural underwater motion blur; hold on the body.

## 负面提示
no handheld shake, no ironic tone, no desaturated grey grade, no dry studio lighting, no pure CGI plastic surfaces, no fast cutting mid-action, no dutch angle, no flat green-screen background, no ambiguous ending, no cold detachment.

## 一致性锚点
- 色彩：deep cyan / blue-green / warm orange accent, high saturation.
- 镜头：21–35mm wide, 50–85mm close, or .
- 光线：underwater beams, bioluminescence, hard practicals, volumetric shafts.
- 构图：centered and stable, human lower third, mass above.
- 材质：water, steel, glass, rubber, wet skin, 35mm grain.
- 禁止漂移：no neon cyberpunk, no grey desaturation, no clean digital skin, no drone aerial.
