---
name: milos-forman
title: 米洛斯·福尔曼 Miloš Forman
style_file: ../directors/milos-forman.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s Czechoslovakia or a 1970s American institution, ordinary non-professional faces crowded in a real room, eye-level medium shot, slightly off-center, overlapping bodies, flat available light, muted grey-brown-green palette, cheap suits and uniforms, 35mm lens, documentary naturalism, awkward, affectionate, comic without punchlines.

## 图像提示
- 主体 / 场景：a shy young man at a village dance; firemen at a raffle table; patients sitting in a circle in a green ward; a small orchestra squeezed into a hall.
- 景别 / 构图：medium shot, faces grouped, foreground body blocking one corner, off-center, crowded; no clean single.
- 镜头 / 焦段：35–50mm, 25mm wide for crowd scenes; slight zoom or pan between faces.
- 光线：flat available light, practical bulbs, fluorescent tubes, no directional beauty light.
- 色彩：muted grey-brown-green; American institutional green and off-white; no warm nostalgia.
- 材质：cheap suits, uniforms, beer glasses, formica tables, linoleum, sheet music, bad wigs.

## 视频提示
- 镜头运动：one handheld drift inside the crowd, following the subject's face, then holding still.
- 主体运动：ordinary social behavior — talking over each other, looking away, laughing a beat too late, reaching for a drink.
- 时长 / 帧率 / 运动模糊：6–12 seconds, 24fps, natural handheld motion blur, no speed ramp.

## 负面提示
no laugh-track timing, no caricature villain, no sentimental score, no glossy period recreation, no symmetrical group portrait, no heroic close-up, no cutting away from embarrassment, no warm nostalgia filter, no spotlight lighting, no staged extras.

## 一致性锚点
- 色彩：muted grey-brown-green / institutional green / off-white, low saturation.
- 镜头：35–50mm, 25mm for crowds.
- 光线：flat available light, practical bulbs and fluorescents, no directional key.
- 构图：eye-level inside the group, off-center, crowded, foreground bodies.
- 材质：cheap suits, uniforms, beer glasses, formica, linoleum, film grain.
- 禁止漂移：no glossy retro color, no modern LED white, no drone shots, no digital skin, no symmetrical staging.
