---
name: jean-luc-godard
title: 让-吕克·戈达尔 Jean-Luc Godard
style_file: ../directors/jean-luc-godard.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s Paris street, high-contrast black and white, handheld 50mm, natural light with blown highlights, jump-axis framing that cuts half a head, actors looking into the lens, printed posters and book covers in frame, restless, argumentative, no smooth continuity, sound and image at odds.

## 图像提示
- 主体 / 场景：a young man and woman arguing on a crowded sidewalk; a woman reading at a café table; a wall of book covers and posters; a television screen inside the frame.
- 景别 / 构图：jump between close-up and wide with no transition; off-center, jump-axis, half a head cut off, subject pushed out of frame, on-screen text or posters interrupting.
- 镜头 / 焦段：50mm and wide-angle; later a zoom used to interrupt, not to clarify.
- 光线：natural and artificial mixed, no unified source; overexposure allowed; never fill for prettiness.
- 色彩：period-dependent — 1960–62 black-and-white street; 1963–67 widescreen primary red, blue and yellow; later red-blue title-card collage.
- 材质：wall text, books, posters, TV screen, printed matter.

## 视频提示
- 镜头运动（只选一种）：handheld follow that stops dead — the camera never makes a smooth motivated move.
- 主体运动：actors walk, talk over each other, look into the lens, gesture out of sync with the soundtrack.
- 时长 / 帧率 / 运动模糊：4–8 seconds, 24fps, blur and overexposure allowed, hard cut at the end, no fade.

## 负面提示
no continuity editing, no wall-to-wall score, no music illustrating a political point, no naturalistic performance, no fill light for beauty, no title cards explaining plot, no complete sympathetic psychology, no empty-landscape or slow-motion ending, no grime filter, no tasteful symmetry, no smooth dolly.

## 一致性锚点
- 色彩：black-and-white street; or widescreen primaries; or red-blue title-card collage.
- 镜头：50mm / wide-angle, or .
- 光线：mixed natural and artificial, overexposure allowed, no fill.
- 构图：jump-axis, off-center, half a head cropped, printed text in frame.
- 材质：printed matter, posters, books, TV screen.
- 禁止漂移：no clean digital look, no drone, no gimbal smoothness, no warm nostalgia grade, no Instagram grain.
