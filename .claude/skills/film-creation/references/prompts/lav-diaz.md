---
name: lav-diaz
title: 拉夫·迪亚兹 Lav Diaz
style_file: ../directors/lav-diaz.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, black and white, deep-focus 35mm wide shot, tiny human figures lost in a vast rain-soaked landscape, sky and mud filling most of the frame, overcast natural light, no fill, single practical source at night, heavy grey tonal range, wet earth and corrugated iron, static camera at human height, figures walking a real distance, documentary gravity, no grain nostalgia.

## 图像提示
- 主体 / 场景：a man walking a long road through rain; a mother waiting outside a government office; a boat crossing a wide river; a group standing in mud.
- 景别 / 构图：wide or extreme wide; figures deep in the frame, small as punctuation; large sky, earth and water; no foreground decoration.
- 镜头 / 焦段：35mm wide-angle prime, deep focus, no compression of sky and ground.
- 光线：overcast natural light; at night one practical source; blacks allowed to go solid, no rim light.
- 色彩：black and white, hard grey range; color reserved only to separate the present from history, never nostalgia.
- 材质：wet earth, rain, corrugated iron, plastic sheeting, old documents, coconut grove.

## 视频提示
- 镜头运动（只选一种）：static camera at human height or slightly low, no follow.
- 主体运动：one person walks the full distance toward and past the camera; the camera neither follows nor pushes in.
- 时长 / 帧率 / 运动模糊：30–60 seconds or platform maximum, 24fps, no motion blur, no speed ramp.

## 负面提示
no nostalgic sepia, no decorative film-grain filter, no dramatic climax inside the long take, no score replacing rain, no reaction shots during speeches, no subtitle cards explaining plot, no poetic poverty, no close-up forcing emotion, no steadicam follow, no shallow depth of field, no clean digital monochrome.

## 一致性锚点
- 色彩：black and white, hard grey range; color only for the present.
- 镜头：35mm wide-angle, deep focus.
- 光线：overcast natural light; single practical source at night; solid blacks.
- 构图：wide or extreme wide, figures small and off-center, sky / earth / water dominant, eye level or slightly low.
- 材质：rain, mud, corrugated iron, plastic sheeting, old documents.
- 禁止漂移：no drone establishing shot, no golden-hour glow, no handheld shake, no modern glass towers, no HDR.
