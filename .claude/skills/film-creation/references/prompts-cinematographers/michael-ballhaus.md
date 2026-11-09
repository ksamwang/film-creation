---
name: michael-ballhaus
title: 迈克尔·鲍尔豪斯 Michael Ballhaus
style_file: ../cinematographers/michael-ballhaus.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 35mm, eye-level camera one and a half meters from the body, 32mm lens, a slow 360-degree dolly orbit around two people in a furnished interior, tungsten practical lamps visible in frame, warm amber and faded green, to contrast, mirrors and doorways doubling the room, dark wood and velvet, fine grain, theatrical, enclosed, unbroken.

## 图像提示
- 主体 / 场景：two or three people talking in a lived-in room — a nightclub back office, a postwar apartment, a restaurant banquette; furniture and mirrors are part of the drama.
- 景别 / 构图：medium and knee-up medium-wide; figures off-center, framed by a doorway or reflected in a mirror; walls crop the edges of the frame.
- 镜头 / 焦段：25–40mm prime, eye level, slight wide-angle, deep enough to read the room.
- 光线：visible practical lamps — table lamp, wall sconce, stage footlight; warm 3200K key from three-quarter side, –, background one to two stops down.
- 色彩：tungsten amber, dark red, faded green, muted brown; no saturated primaries.
- 材质：dark wood, velvet, old wallpaper, glass, cigarette smoke, worn upholstery.

## 视频提示
- 镜头运动（只选一种）：slow 360-degree dolly orbit on a circular track, returning to the starting point.
- 主体运动：two people turn, sit, lean across a table; the camera keeps its distance and circles them.
- 时长 / 帧率 / 运动模糊：20–40 seconds, 24fps, natural motion blur, no slow motion, no cut inside the orbit.

## 负面提示
no handheld shake, no drone orbit, no telephoto isolation of a face, no high angle looking down, no even fill lighting, no cool blue night, no symmetrical centered portrait, no modern glass architecture, no zoom, no cut inside the circle.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：tungsten amber and faded green; 25–40mm; visible practicals at –; doorway and mirror framing; wood, velvet, smoke.
- 禁止漂移：no LED white, no teal-orange grade, no drone move, no clean digital interior, no handheld.
