---
name: david-fincher
title: 大卫·芬奇 David Fincher
style_file: ../directors/david-fincher.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, cold green-cyan and sodium-yellow palette, hard directional practical light, deep crushed blacks, camera at surveillance height slightly above eye line, subject boxed by a doorframe or monitor frame, center composition deliberately a few centimeters off, 35–50mm lens, glass, brushed metal, rain, screen pixels, controlled, clinical, no comfort.

## 图像提示
- 主体 / 场景：an investigator at a desk of files and monitors; a figure in a corridor seen from its far end; a room reproduced step by step; a face half-eaten by shadow in an interview room.
- 景别 / 构图：medium and close-up, face allowed to be cropped; subject trapped by doorframe, window frame or monitor bezel; center off by a few centimeters; exit kept inside the frame.
- 镜头 / 焦段：35–50mm, 75mm for close-ups; wide only for corridors and surveillance views; fixed distance when following.
- 光线：existing sources only, hard contrast, uneven fill, shadows allowed to swallow half the face; no sourceless soft light.
- 色彩：cold green, cyan-blue, sodium yellow; warm tone only while a character feels safe, pulled away at the loss of control.
- 材质：glass, metal, rain, screen pixels, files, fluorescent surfaces; no soft fabric or warm wood as comfort.

## 视频提示
- 镜头运动（只选一种）：precise slow dolly-in on a locked axis, machine-steady, no drift.
- 主体运动：typing, opening doors, washing hands, refreshing a page, assembling a weapon; exact, repeated, procedural.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, no visible motion blur, no handheld float; violence happens in an omitted cut.

## 负面提示
no handheld shake, no warm nostalgia grade, no jump scare, no sudden loud sting, no slow-motion release of violence, no sourceless soft beauty light, no romantic bokeh, no symmetrical stable centering, no bright even fill, no improvised performance.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：cold green, cyan-blue, sodium yellow, black; low warmth, high contrast.
- 镜头：35–50mm, 75mm close-up.
- 光线：practical sources, hard direction, deep shadows.
- 构图：slightly high, off-center, subject boxed by architecture or monitor.
- 材质：glass, brushed metal, rain, screen pixels, paper files.
- 禁止漂移：no modern phone UI parody, no HDR bloom, no clean showroom lighting, no warm domestic glow.
