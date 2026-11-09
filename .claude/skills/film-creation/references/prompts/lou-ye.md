---
name: lou-ye
title: 娄烨 Lou Ye
style_file: ../directors/lou-ye.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, contemporary Chinese city at night, 24–35mm wide lens held close and handheld, shallow focus drifting off the face and finding it again, cold green and cold blue with a single red wound accent, overexposed window and crushed shadow in the same frame, tilted and obstructed framing, rain, sweat, glass reflection, peeling wall, old bedsheet, bodily, unstable, intimate.

## 图像提示
- 主体 / 场景：two people talking too close in a rented room; a man in a car in the rain; a blind masseur's hands; a couple in a hotel corridor.
- 景别 / 构图：close-up and medium close-up, the subject fills the frame, environment reduced to a slit; tilted, obstructed, only part of the body visible.
- 镜头 / 焦段：24–35mm wide, shallow depth of field, close enough to distort the face.
- 光线：natural and practical only; exposure not “correct” — the window may blow out, the darks may smear.
- 色彩：cold green, cold blue; red only as a wound-like accent, never a broad wash.
- 材质：rain, sweat, glass reflection, peeling wall, old bedsheet, damp air.

## 视频提示
- 镜头运动（只选一种）：handheld follow with a breathing sway — sudden approach and retreat, focus lost and re-found; the camera keeps a slight sway even when the subject stops.
- 主体运动：turning away mid-sentence, reaching, shoving, sitting on a bed, smoking by a window; bodies carry the scene, not dialogue.
- 时长 / 帧率 / 运动模糊：5–10 seconds, 24fps, natural handheld blur, no gimbal smoothing.

## 负面提示
no gimbal-stabilised floating, no piano over the shake, no out-of-focus used as a filter, no characters explaining morality, no moral judgement, no rain-night postcard, no sex in every scene, no voice-over explaining the era, no symmetrical classical framing, no clean digital skin, no warm colour filter.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：cold green and cold blue with one red accent; 24–35mm handheld shallow; practical light, blown window, crushed darks; tilted and obstructed close framing; rain, sweat, glass, peeling wall.
- 禁止漂移：no gimbal, no HDR, no clean digital, no warm filter, no drone.
