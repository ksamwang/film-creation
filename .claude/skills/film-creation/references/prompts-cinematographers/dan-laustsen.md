---
name: dan-laustsen
title: 丹·劳斯特森 Dan Laustsen
style_file: ../cinematographers/dan-laustsen.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Gothic theatrical film still, visible light beams through smoke and rain, deep teal and cyan against amber and blood red, symmetrical centered composition framed by a doorway, hard backlight rim, wet surfaces, practical neon and tungsten, deep focus, anamorphic, 35mm grain, cold and warm in the same room, operatic.

## 图像提示
- 主体 / 场景：a figure standing in a corridor, doorway, flooded room, or rain-soaked street; architecture frames the body.
- 景别 / 构图：medium to wide; symmetrical, centered, frame-within-frame, foreground smoke or rain.
- 镜头 / 焦段：25–50mm anamorphic; wide enough to include the doorway and the room beyond.
- 光线：hard side-backlight through smoke, window light, neon and tungsten practicals; ratio –; visible beams.
- 色彩：teal, cyan, amber, blood red; medium-high saturation, shadow retains color, two dominant hues per scene.
- 材质：rain, snow, blood, wet glass, velvet, polished metal, smoke.

## 视频提示
- 镜头运动（只选一种）：slow dolly forward through the doorway.
- 主体运动：the figure walks toward camera through smoke, coat and hair moving; no sudden turns.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural motion blur, no slow-motion flourish.

## 负面提示
no flat teal-orange LUT, no even fill light, no smoke obscuring the subject, no handheld cutting, no green night-vision filter, no modern glass architecture, no flat frontal symmetry, no clean digital skin, no grey palette, no daylight flatness.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：teal and cyan against amber and blood red; 25–50mm anamorphic; smoke-visible backlight at –; symmetrical doorway framing; rain, velvet, polished metal.
- 禁止漂移：no orange-teal LUT, no LED white, no handheld shakiness, no clean modern interiors, no desaturated grey.
