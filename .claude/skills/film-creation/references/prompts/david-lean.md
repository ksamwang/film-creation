---
name: david-lean
title: 大卫·里恩 David Lean
style_file: ../directors/david-lean.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s 70mm epic, extreme wide desert or snow plain, a tiny figure walking along a measurable horizon, vast empty sky, sun-bleached ochre khaki and slate blue, hard noon sunlight and long shadows, deep focus, 28–40mm wide lens, no medium-shot bridge, one face held at the end of the journey, fine 65mm grain, patient, austere, monumental.

## 图像提示
- 主体 / 场景：a lone officer or engineer crossing a desert, a snow plain, a railway bridge, a station platform; the figure tiny against the land, carrying a task rather than a mood.
- 景别 / 构图：extreme wide first, the body a dot on the horizon; then cut straight to a close-up, no medium-shot bridge. Lateral composition, horizon low or high in the frame, the figure placed on the line, not centered like a hero portrait.
- 镜头 / 焦段：28–40mm to hold the landscape and the walker; 100–150mm for the face, compressing the background; middle focal lengths only for necessary dialogue.
- 光线：hard noon sun, long shadows, mirage shimmer; interiors lit by a single shaft of window light, no fill.
- 色彩：sun-bleached sand, khaki, slate blue, faded olive; low saturation but not grey; no vivid primaries, no modern teal-orange grade.
- 材质：sand, sweat, canvas, steel rails, ice, wool, cracked leather; no clean new props.

## 视频提示
- 镜头运动（只选一种）：slow forward tracking behind a walking figure, matching his pace, then stop when he stops.
- 主体运动：a long walk from the horizon toward camera; a hand shading the eyes; a train crossing the frame; almost nothing else.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, minimal motion blur; duration comes from real distance, not slow motion.

## 负面提示
no handheld camera, no fast cutting, no medium-shot dialogue coverage, no warm desert filter, no sunset postcard light, no voice-over psychology, no modern glass or plastic, no digital sharpness, no aerial drone reveal, no romantic resolution, no centered hero portrait, no crowded foreground.

## 一致性锚点
- 色彩：sun-bleached sand, khaki, slate blue; low saturation, hard sun.
- 镜头：28–40mm wide and 100–150mm close-up, nothing comfortable in between; .
- 光线：single hard key, long shadows, one window shaft indoors.
- 构图：low or high horizon, figure small on the line, deep measurable space.
- 材质：sand, sweat, canvas, steel, ice, wool.
- 禁止漂移：no teal-orange grade, no golden-hour glow, no drone shot, no modern vehicles, no clean digital skin, no medium two-shot.
