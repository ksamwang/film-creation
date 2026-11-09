---
name: denis-villeneuve
title: 丹尼斯·维伦纽瓦 Denis Villeneuve
style_file: ../directors/denis-villeneuve.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic anamorphic film still, a tiny human silhouette at the lower edge of a vast ochre desert or grey monolith, thick atmospheric haze, desaturated sand and steel-blue palette with one saturated accent, diffuse overcast backlight, centered monumental composition, negative space, extreme scale, fine grain, silent and austere.

## 图像提示
- 主体 / 场景：a lone figure before a colossal weathered monolith; a woman in a fog-filled corridor; a small craft crossing an endless dune sea.
- 景别 / 构图：extreme wide with the human reduced to a point, then a medium close-up through haze; centered, low horizon, figure at the lower edge, massive negative space; no busy group medium shot.
- 镜头 / 焦段：25–40mm anamorphic for scale; 85–135mm for faces through dust and fog; no wide-angle face distortion.
- 光线：diffuse overcast, backlit silhouette, one hard shaft through haze; no neon, no colored practicals.
- 色彩：monochrome sand-ochre, grey or steel-blue; one saturated accent only — fire, eye, blood; no multicolor palette.
- 材质：concrete, sand, stone, fog, wet cloth, worn metal; fine grain, matte surfaces.

## 视频提示
- 镜头运动：very slow dolly in, one direction only; no handheld, no quick pan.
- 主体运动：almost still — a head turns, fabric moves in wind, dust drifts; no running.
- 时长 / 帧率 / 运动模糊：6–8 seconds, 24fps, minimal motion blur; let the frame breathe.

## 负面提示
no handheld camera, no fast cutting, no neon, no multicolor palette, no clear transparent background, no busy crowd, no wide-angle face distortion, no glossy digital surfaces, no warm nostalgia filter, no explanatory close-up.

## 一致性锚点
- 色彩：sand-ochre / grey / steel-blue, desaturated, one saturated accent.
- 镜头：25–40mm anamorphic, deep atmospheric layers.
- 光线：diffuse overcast with one hard shaft, backlit silhouettes.
- 构图：centered, low horizon, tiny figure at the lower edge.
- 材质：concrete, sand, stone, fog, wet cloth, fine grain.
- 禁止漂移：no neon cyberpunk, no saturated multi-color grade, no clean glass architecture, no drone tourism shot.
