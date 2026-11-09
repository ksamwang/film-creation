---
name: matthew-libatique
title: 马修·利巴蒂克 Matthew Libatique
style_file: ../cinematographers/matthew-libatique.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Raw handheld film still, 18–35mm wide-angle pressed close to the face, hard side light, crushed blacks and blown highlights, heavy 16mm grain, halation and lens flare, off-balance framing, skin with sweat, desaturated grey or saturated red-black palette, nervous, subjective, physical, unpolished.

## 图像提示
- 主体 / 场景：a performer, dancer, or addict in a narrow room, corridor, or backstage space; the body fills the frame.
- 景别 / 构图：medium close-up to close-up; off-balance, cropped at the edge, foreground obstruction, no safe center.
- 镜头 / 焦段：18–35mm wide-angle close to the face; 50–85mm for a held portrait.
- 光线：hard side or top light, window or practical; ratio or more; highlights may blow, shadows may crush.
- 色彩：saturated red and black, or fully desaturated grey; one film, one palette, no neutral middle.
- 材质：16mm grain, sweat, blood, feathers, glass, skin texture, halation.

## 视频提示
- 镜头运动（只选一种）：handheld follow.
- 主体运动：the body moves abruptly, turns, stumbles, or repeats a gesture; the camera keeps close and breathes with it.
- 时长 / 帧率 / 运动模糊：5–10 seconds, 24fps, strong natural motion blur, no gimbal smoothing.

## 负面提示
no gimbal smoothness, no soft beauty light, no unified LUT, no clean digital skin, no fake grain overlay, no symmetrical composition, no telephoto distance, no even fill, no stable tripod, no polished commercial look.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：saturated red-black or desaturated grey; 18–35mm wide; hard side light at +; off-balance close framing; 16mm grain, sweat, halation.
- 禁止漂移：no smooth gimbal, no soft key, no clean skin, no HDR, no neutral grey LUT, no wide establishing distance.
