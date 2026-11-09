---
name: hou-hsiao-hsien
title: 侯孝贤 Hou Hsiao-hsien
style_file: ../directors/hou-hsiao-hsien.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, southern Taiwanese wooden house or mountain village, fixed very long shot from outside a doorway, a small figure inside a door or window frame, layered deep space, low-saturation grey-green and earth brown, soft natural daylight, dark interior, wood, lime plaster, tatami, rain, patient, distant, historical weight in the empty edges.

## 图像提示
- 主体 / 场景：a family eating inside a wooden house seen from the yard; a young man standing at a doorway; a figure walking a mountain path; the event happens in depth or beyond the frame.
- 景别 / 构图：medium-long and far shot, subject small, heavy negative space of sky, wall and trees; door or window as a frame within the frame.
- 镜头 / 焦段：medium-long to long lens, camera placed outside the room, deep space.
- 光线：natural daylight, underexposed interiors, readable direction; no fill.
- 色彩：low saturation, grey-green, earth brown, no warm nostalgia.
- 材质：wood, lime plaster, tatami, rain, bamboo.

## 视频提示
- 镜头运动（只选一种）：completely static lock-off; at most one very slow lateral pan, never a push-in.
- 主体运动：entering and leaving frame, eating, walking, waiting; the key action stays offscreen or in the depth of the shot.
- 时长 / 帧率 / 运动模糊：20–40 seconds, 24fps, no motion-blur stylization.

## 负面提示
no dolly-in toward emotion, no tearful close-up, no voice-over explaining history, no score filling the ellipsis, no fast montage of the era, no actor performing grief, no warm nostalgia filter, no cut to the violent event, no symmetrical postcard composition, no clean digital sharpness.

## 一致性锚点
- 色彩：low-saturation grey-green and earth brown.
- 镜头：medium-long to long, deep focus.
- 光线：natural daylight, dark interiors, no fill.
- 构图：camera outside the room, door or window framing, subject small, large empty areas.
- 材质：wood, lime plaster, tatami, rain.
- 禁止漂移：no push-in, no warm filter, no modern glass, no drone landscape, no digital-clean image.
