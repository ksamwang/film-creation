---
name: vittorio-storaro
title: 维托里奥·斯托拉罗 Vittorio Storaro
style_file: ../cinematographers/vittorio-storaro.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Operatic anamorphic film still, one dominant hue per scene, amber key against blue fill, coloured light rather than white light, deep shadow that keeps its colour, smoke giving volume to every beam, symmetrical architecture framing the figure, slow lateral drift, Technicolor density, 35mm grain, painted, deliberate, symbolic.

## 图像提示
- 主体 / 场景：a solitary figure inside a painted architectural interior or a smoke-filled exterior; the space is built from arches, columns and doorways.
- 景别 / 构图：medium to wide, symmetrical, centred on axis, framed by architecture; the figure occupies the middle third.
- 镜头 / 焦段：35mm anamorphic, occasional 50mm and 85mm; no wide-angle distortion.
- 光线：tungsten key with amber gel against HMI fill with blue gel; two colour temperatures, no neutral white.
- 色彩：one dominant hue per image, amber / red / green / blue progression, saturated, blacks that still carry colour.
- 材质：smoke, silk, velvet, marble, gel-coloured practical lamps, painted flats.

## 视频提示
- 镜头运动（只选一种）：slow crane rise.
- 主体运动：the figure turns slowly on the axis or walks a straight line through the coloured layers.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no neutral white key light, no evenly lit scene, no handheld camera, no more than one dominant hue, no teal-orange grade, no flat grey shadows, no zoom lens, no off-centre snapshot framing, no clean digital sharpness, no modern LED practicals, no naturalistic daylight.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：one hue per shot; 35mm anamorphic; two colour temperatures; symmetrical axis; smoke and silk.
- 禁止漂移：no white balance to neutral, no daylight-flat look, no modern glass architecture, no desaturated palette, no handheld coverage.
