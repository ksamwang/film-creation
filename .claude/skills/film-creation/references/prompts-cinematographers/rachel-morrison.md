---
name: rachel-morrison
title: 蕾切尔·莫里森 Rachel Morrison
style_file: ../cinematographers/rachel-morrison.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, intimate eye-level medium close-up, soft window light falling across natural skin, low contrast with open shadows, warm brown and quiet grey-green palette, handheld but steady, shallow focus keeping the room present, real interiors with cotton and wood, practical lamps at night, 35–50mm lens, fine film grain, present-tense, tender, unretouched.

## 图像提示
- 主体 / 场景：a person sitting by a window, in a car, or at a kitchen table; a face in honest light, with the room still readable around them.
- 景别 / 构图：medium close-up and close-up, subject to one side, negative space of window or wall, foreground shoulder or doorframe; eye level, never looking down.
- 镜头 / 焦段：35–50mm, 85–100mm for close-ups; shallow focus but the environment remains present.
- 光线：window and doorway daylight as key, soft side light or backlight, low ratio, open shadows, practical lamps at night.
- 色彩：warm brown, grey-green, window blue, tungsten orange; low-to-medium saturation, natural skin tones.
- 材质：skin, hair, cotton, wood, rain, real domestic interiors.

## 视频提示
- 镜头运动（只选一种）：gentle handheld follow, breathing with the subject.
- 主体运动：the subject speaks, listens, turns toward the window, or walks through a doorway.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no dramatic hard light explaining emotion, no high-angle shot of suffering, no skin smoothing, no teal-orange grade, no heavy fill killing window light, no cheap handheld shake, no framing that diminishes the subject, no wide shot replacing the face, no glossy beauty lighting.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：warm brown and grey-green with natural skin; 35–50mm; soft window side light; eye-level off-center framing; cotton and wood.
- 禁止漂移：no studio beauty light, no cold LED, no orange-teal LUT, no aerial or wide establishing default, no plastic skin.
