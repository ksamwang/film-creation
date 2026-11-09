---
name: elia-suleiman
title: 埃利亚·苏莱曼 Elia Suleiman
style_file: ../directors/elia-suleiman.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, fixed frontal wide shot, symmetrical deep-focus 35mm, a small deadpan man standing at the edge of the frame while the center stays empty, concrete bollards and a doorway framing him, flat even daylight, no dramatic side light, muted concrete grey, olive green and white wall, dust and a plastic chair, static, dry, absurd, no music.

## 图像提示
- 主体 / 场景：a silent man in a suit at a checkpoint; a family on a rooftop; a man waiting at a red light that never changes; a figure at the edge of a wide street.
- 景别 / 构图：wide or medium-wide, frontal and symmetrical, subject at the frame edge or corner, center left empty; frame-within-frame through doorways, walls and concrete blocks.
- 镜头 / 焦段：35mm wide, deep focus, adult eye height, no compression.
- 光线：even daylight or practical fluorescent; no dramatic side light; when violence is offscreen the image stays bright and flat.
- 色彩：concrete grey, olive green, white wall; natural low saturation; no political-poster contrast colors.
- 材质：concrete, dust, plastic chair, wire mesh, old sedan.

## 视频提示
- 镜头运动（只选一种）：completely static — no push, pan, zoom or handheld.
- 主体运动：figures enter and leave the frame, sit, wait, walk away; the camera never follows; one action is held past comfort.
- 时长 / 帧率 / 运动模糊：10–20 seconds, 24fps, no motion blur, no speed change.

## 负面提示
no handheld, no zoom, no dolly, no reaction shot after the gag, no direct on-screen violence, no cartoonish or hateful Israeli characters, no emotive dialogue, no music cueing the joke, no political speech, no hero framing that fills the center, no slapstick exaggeration, no dramatic side light.

## 一致性锚点
- 色彩：concrete grey / olive green / white, low saturation.
- 镜头：35mm wide, deep focus.
- 光线：flat even daylight or fluorescent, no side light.
- 构图：frontal symmetrical wide, subject at the edge, center empty, frame-within-frame.
- 材质：concrete, dust, plastic chair, wire mesh.
- 禁止漂移：no drone, no stylized color grade, no handheld documentary shake, no anamorphic flare, no emotional close-up.
