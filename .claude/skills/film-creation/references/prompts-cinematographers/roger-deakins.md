---
name: roger-deakins
title: 罗杰·迪金斯 Roger Deakins
style_file: ../cinematographers/roger-deakins.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Precise large-format digital frame, one motivated source, deep negative fill, a figure reduced to silhouette against a bright exterior, strict horizon and verticals, muted grey-blue and earth palette with a single sodium-orange accent, wide 40mm lens, symmetrical negative space, fog or dust in the air, clean deep blacks, controlled, exact, quiet.

## 图像提示
- 主体 / 场景：a lone figure crossing a vast landscape, an empty room, a corridor or a trench; the place matters more than the face.
- 景别 / 构图：wide to extreme wide, one-point or centered composition, strict horizontals, large negative space, figure very small.
- 镜头 / 焦段：35mm or 40mm, deep focus, no compressed telephoto unless the landscape demands it.
- 光线：single window, sky, streetlamp or practical; heavy negative fill; silhouette against a bright field; highlights held.
- 色彩：desaturated grey-blue, earth ochre, dark green, one warm sodium accent.
- 材质：fog, dust, rain, snow, wet stone, practical bulbs, real locations.

## 视频提示
- 镜头运动（只选一种）：slow dolly push along a fixed axis, no handheld, no zoom.
- 主体运动：a figure walks steadily through the space and stops at the edge of frame; the camera keeps its measured pace.
- 时长 / 帧率 / 运动模糊：8–20 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no handheld shake, no unmotivated camera movement, no multiple key lights, no teal-orange grade, no shallow depth of field by default, no Dutch angle, no golden-hour cliché, no unexplained light source, no crowded foreground, no digital-clean HDR skin.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：grey-blue earth palette, 35–40mm, single source with negative fill, horizon and negative space, fog and dust.
- 禁止漂移：no handheld, no zoom, no neon, no drone-only aerial, no orange-teal LUT.
