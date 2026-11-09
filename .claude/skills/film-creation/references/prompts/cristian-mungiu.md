---
name: cristian-mungiu
title: 克里斯蒂安·蒙久 Cristian Mungiu
style_file: ../directors/cristian-mungiu.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, contemporary Romania, overcast winter light, desaturated grey-green and beige, a cramped hotel room or institutional corridor, two people at a small table, a doorframe and a corridor visible at the edge of frame, eye-level static wide shot, 35mm lens, deep focus, visible film grain, naturalistic, unsentimental, quiet tension, no stylization.

## 图像提示
- 主体 / 场景：a woman counting banknotes under a table; a father waiting in a parked car outside a school; two people talking in a hotel room with one bed and a bare bulb.
- 景别 / 构图：medium wide two-shot, off-center, a doorway or corridor left in frame, foreground furniture partially blocking the body; no clean single.
- 镜头 / 焦段：35–50mm prime, deep focus; 75mm only for a long corridor or a queue.
- 光线：window light, fluorescent tube, sodium street lamp; no fill, one side of the face may fall dark.
- 色彩：grey-green, beige, brown, low saturation; winter without a warm grade.
- 材质：worn furniture, ceramic tiles, plastic bags, slush and mud, official forms, cigarette smoke.

## 视频提示
- 镜头运动：static tripod shot for the entire duration; no camera movement.
- 主体运动：ordinary tasks — counting money, waiting, smoking, walking to a door; no theatrical gesture.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, natural motion blur, no speed ramp.

## 负面提示
no musical score, no reaction-shot cutting, no handheld shake, no warm color grade, no villain lighting, no close-up tears, no symmetrical hero framing, no montage urgency, no voice-over explanation, no glamorous poverty.

## 一致性锚点
- 色彩：grey-green / beige / brown, low saturation, no warm highlights.
- 镜头：35–50mm prime, deep focus.
- 光线：window or fluorescent practicals, no fill, half-face shadow allowed.
- 构图：eye-level, off-center, doorframe or corridor at the edge, two or three bodies per frame.
- 材质：worn furniture, tiles, plastic, slush, paper forms, film grain.
- 禁止漂移：no modern glass architecture, no LED white, no drone shots, no digital skin, no teal-orange grade.
