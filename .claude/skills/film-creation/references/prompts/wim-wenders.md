---
name: wim-wenders
title: 维姆·文德斯 Wim Wenders
style_file: ../directors/wim-wenders.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, road movie stillness, a figure seen from behind at the edge of a wide horizontal frame, horizon line cutting through the body, vast empty space left unfilled, motel window, railway, sky, flat eye-level 35mm lens holding its distance, natural dawn light mixed with motel neon, saturated green magenta and blue, glass, worn photograph, neon tubing, 35mm grain, quiet, wandering, tender.

## 图像提示
- 主体 / 场景：a man in a worn jacket seen from behind, a child beside him, a woman behind one-way glass; motel room, gas station, railway siding, empty road, diner at dusk.
- 景别 / 构图：wide or medium-wide, horizontal; the horizon passes through the figure; large areas left empty — sky, wall, parking lot; the character often faces away from camera.
- 镜头 / 焦段：35–50mm, eye level or slightly low, two to four meters, like someone walking alongside rather than judging; landscape not compressed.
- 光线：natural dawn and dusk, window light, mixed with practical neon; no studio evenness.
- 色彩：by film — saturated green, magenta and blue like over-developed memory; or black and white that turns to color only when feeling begins; always sourced from signage, neon, daylight.
- 材质：asphalt, plate glass, faded photographs, cassette tape, neon tubing, cheap motel fabric.

## 视频提示
- 镜头运动（只选一种）：long static hold; if it moves, a lateral track at walking pace, or one slow push in only at the moment the character finally sees something.
- 主体运动：sitting, smoking, looking out a window, walking slowly away; small gestures, long pauses.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural motion blur, time allowed to accumulate.

## 负面提示
no scenic road-trip montage, no voice-over explaining loneliness, no witty literary dialogue, no warm sentimental grade, no drone landscape beauty, no symbolic American iconography, no happy reunion, no tearful close-up, no restless handheld camera, no glossy car commercial, no fast cutting.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：green, magenta, blue sourced from neon and signs; 35–50mm; natural dawn/dusk window light; horizontal frame with horizon through the body and empty space; glass, photograph, neon.
- 禁止漂移：no teal-orange blockbuster grade, no golden nostalgia, no centered hero portrait, no drone aerials, no crowded urban montage, no modern LED white.
