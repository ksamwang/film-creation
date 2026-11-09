---
name: bela-tarr
title: 贝拉·塔尔 Béla Tarr
style_file: ../directors/bela-tarr.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, black and white, low horizon with heavy overcast sky filling the upper frame, a small figure seen from behind at half to two metres, 35mm lens, wide but restrained, wet mud, rotting plaster, corrugated iron, sustained grain, no close-up, waiting without event.

## 图像提示
- 主体 / 场景：a farmer or night watchman seen from behind, walking a muddy village road; a tavern yard in rain; a bare plain with a low hut. Weather occupies two thirds of the frame.
- 景别 / 构图：wide shot only; low horizon, sky in the upper third, figure small and off to one side; no close-up, no reaction shot, no clean backdrop behind the character.
- 镜头 / 焦段：35–50mm, restrained wide; camera at half to two metres behind the subject, height level or slightly below the character's eye.
- 光线：overcast daylight, window light, practical lamp; high lights never clip, texture kept in the shadows, no dramatic contrast ratio.
- 色彩：black and white grayscale; natural-colour passages desaturated to a narrow range.
- 材质：wet plaster, mud, unpainted wood, corrugated iron, animal hide, rain on stone; no smooth metal or glass.

## 视频提示
- 镜头运动（只选一种）：slow follow from behind, at walking pace; when the figure stops the camera only drifts a few centimetres, like breathing.
- 主体运动：walking through mud, carrying water, waiting at a window; small, repeated, task-bound movement; no dramatic gesture.
- 时长 / 帧率 / 运动模糊：30–60 seconds, 24fps, natural shutter only; no speed ramp, no step-printing.

## 负面提示
no close-up, no cutaway reaction shot, no psychological flashback, no explanatory dialogue insert, no pre-emptive camera pan before a turn, no unmotivated lateral move, no sepia filter, no digital grain overlay, no high-key exposure, no clipped highlights, no redemption ending, no fast montage compressing waiting, no poverty-as-aesthetic misery postcard, no empty landscape montage, no saturated natural colour.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：black-and-white grayscale, 35–50mm at 0.5–2m behind the figure, overcast flat light with textured darks, low horizon and small human figure, wet plaster and mud.
- 禁止漂移：no colour grade, no drone landscape, no handheld intimacy, no close-up face, no clean modern surfaces, no beautiful-emptiness framing.
