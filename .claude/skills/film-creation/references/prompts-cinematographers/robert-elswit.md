---
name: robert-elswit
title: 罗伯特·艾尔斯维特 Robert Elswit
style_file: ../cinematographers/robert-elswit.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, true anamorphic, 35mm, eye-level camera across the room from the subject, 40–100mm lens, motivated practical light — a desk lamp, a window, a sodium streetlamp, fluorescent tubes, low key at to , half the face in shadow, sodium amber and fluorescent green against neutral daylight, desaturated with one saturated accent, real walls and doorways, sweat and dust, observational, unglamorous, held.

## 图像提示
- 主体 / 场景：a tired man or woman in a real room — an oil field, a law office, a motel, a night street; the place is established before the person.
- 景别 / 构图：wide establishing shot, then medium; off-center, deep staging, a doorway or table in the foreground, no symmetry, shoulders may be cropped.
- 镜头 / 焦段：40mm anamorphic to 100mm; wide for landscape, long to isolate a face.
- 光线：motivated practicals only — window, desk lamp, fluorescent, sodium streetlight; –, one side of the face dark.
- 色彩：sodium amber, fluorescent green, neutral daylight; low saturation plus one saturated red or blue accent.
- 材质：sweat, oil, dust, glass, worn carpet, cheap wood panel, cigarette ash.

## 视频提示
- 镜头运动（只选一种）：slow dolly push-in, almost imperceptible, motivated by a realization.
- 主体运动：a person sits, smokes, walks across a room or stands still while the camera waits.
- 时长 / 帧率 / 运动模糊：8–20 seconds, 24fps, natural motion blur, no speed ramp, no handheld.

## 负面提示
no rim light on faces, no unified teal-orange LUT, no symmetrical composition, no softbox key, no post-production haze, no fast cutting, no postcard skyline, no clean digital skin, no shallow-focus beauty close-up, no graphic centered poster frame.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：sodium amber, fluorescent green, neutral daylight; 40–100mm anamorphic; motivated practicals at –; off-center deep staging; sweat, dust and worn surfaces.
- 禁止漂移：no teal night, no rim light, no studio fill, no drone skyline, no HDR cleanliness.
