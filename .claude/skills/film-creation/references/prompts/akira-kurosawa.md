---
name: akira-kurosawa
title: 黑泽明 Akira Kurosawa
style_file: ../directors/akira-kurosawa.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, epic historical action, three planes of depth held in one frame: a figure's back of head in the foreground, bodies and movement in the midground, mountain or storm sky behind, compressed by a long lens, low angle against hard outdoor sunlight, rain, mud and torn armor, wind pulling cloth sideways, high-contrast black and white, academy ratio, tense, elemental, human against weather.

## 图像提示
- 主体 / 场景：a lone swordsman at one end of a muddy village road, villagers behind him; foot soldiers advancing through driving rain; a general on a rise above a burning plain.
- 景别 / 构图：full shot or extreme wide with three planes in one frame — foreground back of a head, midground action, distant mountain or sky; figures at opposite frame edges with empty space between; no shot-reverse-shot for a standoff.
- 镜头 / 焦段：50–200mm long lens compressing the three planes; camera below eye level for the hero, above for the battlefield.
- 光线：hard direct outdoor sun; rain, snow, dust and smoke cut the light into layers; no soft studio light.
- 色彩：high-contrast monochrome, deep blacks and blown highlights; in color, large flat blocks per faction, no delicate midtones.
- 材质：mud, dented armor, cracked wood, fire, rain, dirty cloth.

## 视频提示
- 镜头运动（只选一种）：slow lateral track following the direction of force — running men, horses, slanting rain; no handheld, no zoom.
- 主体运动：crowds moving as one body, a charge across the frame, wind tearing at banners and clothes; freeze only at the moment of decision.
- 时长 / 帧率 / 运动模糊：3–5 seconds, 24fps, natural motion blur; no slow motion except a single decisive strike.

## 负面提示
no handheld camera, no zoom lens, no duel in clear weather, no shot-reverse-shot in a standoff, no POV shot during action, no slow motion except the decisive blow, no crowd used as background texture, no villain psychology monologue, no victory without cost, no clean studio lighting, no rain-and-slow-motion sword commercial look, no low angle as simple hero worship, no shallow-focus bokeh portrait.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：high-contrast black and white; in color, flat faction blocks, no subtle grading.
 - 镜头：50–200mm, low and high angle paired, ( after 1958, late color).
 - 光线：hard sun, weather used as light layers.
 - 构图：three planes, opposing figures at the frame edges, empty center.
 - 材质：mud, armor, wood, fire, rain.
- 禁止漂移：no clean digital mud, no wire-fu floating, no teal-and-orange, no modern armor, no drone shot, no shallow-focus hero portrait, no glossy rain.
