---
name: wong-kar-wai
title: 王家卫 Wong Kar-wai
style_file: ../directors/wong-kar-wai.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1990s Hong Kong, saturated emerald green and deep crimson neon, tungsten practical lights, smoky narrow interior, foreground doorframe or window frame cutting the subject, half the face lost in shadow, shallow depth of field, 35mm film grain, melancholic, intimate, off-center, slight motion blur on a passing figure.

## 图像提示
- 主体 / 场景：a lonely woman in a cheongsam in a cramped noodle shop at midnight; a man smoking in a narrow corridor.
- 景别 / 构图：medium close-up, off-center, frame-within-frame, foreground obstruction; no clean single.
- 镜头 / 焦段：50–85mm, shallow focus; 35mm only for tight interiors.
- 光线：practical sources only — neon sign, desk lamp, fridge, television; one side of the face falls into shadow; retain detail in the darks.
- 色彩：saturated green, red, amber; mixed color temperatures; no unified grade.
- 材质：smoke, rain, wet glass, cheap wallpaper, silk, film grain.

## 视频提示
- 镜头运动：slow handheld drift, follow from behind, then hold; no whip pan.
- 主体运动：walking away, smoking, waiting; small gestures, no big emotional display.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, step-printed motion blur on movement.

## 负面提示
no clean symmetrical composition, no even studio lighting, no modern glass architecture, no digital sharpness, no warm nostalgia filter, no slow-motion cliché, no voice-over, no centered hero shot, no bright daylight.

## 一致性锚点
- 色彩：emerald green / deep red / amber, high saturation, mixed tungsten-neon.
- 镜头：50–85mm, shallow depth.
- 光线：practical sources, half-face shadow, detailed darks.
- 构图：doorframe or window frame, foreground obstruction, off-center.
- 材质：smoke, rain, wet glass, film grain.
- 禁止漂移：no modern LED white, no clean glass towers, no digital skin.
