---
name: bi-gan
title: 毕赣 Bi Gan
style_file: ../directors/bi-gan.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, damp southern Chinese town of Kaili, 24–35mm wide lens close behind the subject's head, long unbroken take changing time inside the frame, green and blue with mold stains, old half-broken neon, practical corridor and car light keeping density in the shadows, fog placed behind the figure not in front, water dripping and pooling, moldy wall, stained ceiling, 16mm-like grain, humid, dreamlike.

## 图像提示
- 主体 / 场景：a man walking into a tunnel; a woman singing in a rundown KTV; a clock on a moldy wall; a figure crossing a wet bridge at night.
- 景别 / 构图：medium and full shot inside the long take; close-up only for hands and clocks; asymmetric, following the figure, deep space with fog behind.
- 镜头 / 焦段：24–35mm wide, distorting person and space together.
- 光线：practical only — corridor bulb, headlights, flashlight; keep density in the darks, no even fill.
- 色彩：green, blue, mold stains, old neon that looks half broken; each light source keeps its own colour, no global green filter.
- 材质：moldy walls, water stains, old clothes, wet floor, film grain.

## 视频提示
- 镜头运动（只选一种）：one continuous take following behind the head at shoulder height, moving with the subject; no cut, no orbit, no rise in the same prompt.
- 主体运动：slow, delayed reactions; walking, wading, climbing, carrying, looking for a door; every dream has one measurable physical action.
- 时长 / 帧率 / 运动模糊：20–40 seconds single take, 24fps, natural motion blur, no speed changes.

## 负面提示
no long take as mere duration, no global green filter, no poetic voice-over explaining the image, no weightless dream, no imitation dialect accent, no clocks as stickers, no rain in every scene, no actor “performing poetry”, no fast cutting, no HDR, no drone.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：green, blue and mold with old neon; 24–35mm; practical light, dense darks; follow behind the head, asymmetric depth, fog behind the figure; mold, water stain, old cloth, film grain.
- 禁止漂移：no global green filter, no clean digital, no HDR, no drone, no fast cut.
