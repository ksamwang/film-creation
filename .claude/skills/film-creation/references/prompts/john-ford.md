---
name: john-ford
title: 约翰·福特 John Ford
style_file: ../directors/john-ford.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 35mm, eye-level camera fixed like a bystander in the crowd, low horizon and a vast sky, a small figure framed inside a doorway, monument valley sandstone, dust, wooden porch, natural light, hard noon or long dusk, muted ochre and grey-blue, classical, communal, elegiac.

## 图像提示
- 主体 / 场景：a rider standing in a cabin doorway while a family sits at the table inside; a cavalry column crossing a plain; a town street with a porch and a church. The community is in the frame; the loner is at its edge.
- 景别 / 构图：medium long shot and long shot; vertical door and window frames, horizontal horizons and fences; monument-scale landscape, human small; no close-up for emotion.
- 镜头 / 焦段：35–50mm; camera at the eye level of a person standing in the crowd, not below or above.
- 光线：natural light only — hard noon, long dusk; no studio softness, no rim-light glamour.
- 色彩：earth ochre, grey-blue, dark red; muted, no high saturation; black and white for the dust-bowl passages.
- 材质：weathered wood door, porch boards, sandstone, dust, leather tack, wool uniforms; no smooth modern material.

## 视频提示
- 镜头运动（只选一种）：static camera — it does not move; riders, wagons or a crowd pass through the frame.
- 主体运动：a group rides or walks across the frame; the protagonist stands still at the doorway and does not follow them; at the end he turns and the frame holds on the people inside.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, classical continuous motion, no blur, no speed ramp.

## 负面提示
no fast cutting, no shaky handheld, no psychological monologue staging, no postcard filter, no sepia, no close-up close on tears, no camera following the hero out of frame at the end, no anonymous faceless attackers, no hero given a seat at the family table, no jokes played as gags, no dutch angle, no modern lens flare, no saturated sky.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：ochre and grey-blue muted, 35–50mm at eye level, hard natural light, doorway and low horizon with a small figure, weathered wood and dust.
- 禁止漂移：no anamorphic western pastiche, no drone landscape, no teal-orange grade, no handheld, no centered hero portrait, no modern costumes.
