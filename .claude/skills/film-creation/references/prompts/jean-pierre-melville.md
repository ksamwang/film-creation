---
name: jean-pierre-melville
title: 让-皮埃尔·梅尔维尔 Jean-Pierre Melville
style_file: ../directors/jean-pierre-melville.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s Paris at night, cold blue-grey and black, rain-slick asphalt, a lone man in a trench coat and fedora, white gloves, an almost empty apartment, hard practical light pooling on the floor, deep shadows, symmetrical wide composition, 50mm lens, 35mm grain, silent, ritualistic, fatalistic, no warmth.

## 图像提示
- 主体 / 场景：a hitman adjusting his hat in a bare room with a birdcage; two men across a table in a nightclub back room; a stolen car parked under a single streetlamp.
- 景别 / 构图：medium wide, symmetrical, figure isolated in negative space, doorframe or window as a hard border; no close-up.
- 镜头 / 焦段：35–50mm prime, deep focus; 85mm only for a figure at the end of a corridor.
- 光线：hard practical sources — desk lamp, neon sign, car headlight; one pool of light, the rest falls to black; no fill.
- 色彩：blue-grey, black, off-white; a single red accent only.
- 材质：trench coat, felt fedora, white gloves, wet asphalt, chrome, cigarette smoke, bare plaster.

## 视频提示
- 镜头运动：one slow lateral tracking shot following the lone figure across the street, then hold; no push-in.
- 主体运动：deliberate, economical — putting on gloves, lighting a cigarette, walking to a door, sitting down.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, clean motion blur, no speed ramp.

## 负面提示
no handheld camera, no zoom, no warm color grade, no romantic soft focus, no backstory flashback, no crying close-up, no fast-cut action, no explanatory voice-over, no sympathetic villain, no crowded frame, no modern city glass.

## 一致性锚点
- 色彩：blue-grey / black / off-white, one red accent, no warm highlights.
- 镜头：35–50mm prime, deep focus.
- 光线：hard practical pool, deep shadow, no fill.
- 构图：symmetrical, eye-level, isolated figure, door or window as border.
- 材质：trench coat, fedora, gloves, wet asphalt, chrome, smoke, film grain.
- 禁止漂移：no daylight postcard Paris, no neon rainbow, no digital sharpness, no modern cars, no handheld drift.
