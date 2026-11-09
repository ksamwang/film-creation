---
name: allen-daviau
title: 艾伦·达维奥 Allen Daviau
style_file: ../cinematographers/allen-daviau.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, soft natural window light diffused through sheer curtains, warm amber and honey tones, gentle backlight rimming hair and shoulders, low contrast with glowing highlights, suburban American interior, framed by a doorway or window, dust motes floating in a light beam, practical tungsten lamps, 35–85mm lens, stable camera, 35mm grain and halation, nostalgic, tender, lived-in.

## 图像提示
- 主体 / 场景：a family or a lone child in an ordinary American room; a figure standing at a bright doorway; the room feels lived-in and slightly worn.
- 景别 / 构图：medium and medium close-up, subject framed by a window or doorway, foreground curtain edge or table corner, gentle near-symmetry; comfortable distance.
- 镜头 / 焦段：35–85mm, 50mm as the default; slight compression, soft focus falloff, no wide-angle distortion.
- 光线：window as key through sheer curtains, warm backlight and rim, low contrast, soft highlight bloom, practical lamps in frame.
- 色彩：amber, cream, old wood, night blue; medium saturation, warm but not sepia.
- 材质：sheer fabric, wood grain, wallpaper, dust, haze, suburban practicals.

## 视频提示
- 镜头运动（只选一种）：very slow dolly in, almost imperceptible.
- 主体运动：a person turns from a window or walks slowly through a doorway; curtain and dust move in the light.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no hard direct light on the face, no high-contrast film-noir lighting, no handheld shake, no cold white LED, no teal-orange LUT, no rigid symmetrical centering, no digital-added fog, no oppressive close-up, no modern glass interior, no HDR clarity.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：amber and cream palette with night blue; 50mm; soft window backlight; doorway framing; sheer curtains and dust.
- 禁止漂移：no hard studio key, no cold daylight, no handheld, no clean digital skin, no contemporary minimalist interior.
