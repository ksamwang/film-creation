---
name: diao-yinan
title: 刁亦男 Diao Yinan
style_file: ../directors/diao-yinan.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Chinese city at night, stable camera placed high looking down on a route through an urban village alley, neon zoned into separate red, green and blue pools that never mix, wet ground mirroring the path, hard edge light leaving half the face black, tiled wall, plastic sheeting, old signboard, a second space visible behind a door or window, 35–50mm, deep geometric perspective, cold, fated.

## 图像提示
- 主体 / 场景：a man walking a fixed route through a night-market alley; two people facing each other across a tiled room; a figure at the edge of a lake; a group in a station square.
- 景别 / 构图：medium to wide, symmetrical, frame-within-frame, deep perspective; always a second layer of space behind a door, window or water; the character often seen from behind.
- 镜头 / 焦段：35–50mm; 24–28mm for group staging; keep straight lines and depth.
- 光线：hard, edge-lit, half the face black; smoke used to cut light, not for atmosphere.
- 色彩：neon zoning — red, green and blue each own an area, never blended into party lights; wet ground reflects the route.
- 材质：wall tiles, plastic sheeting, old signboards, rain, ice; at most three art focal points per scene, one of them used or broken.

## 视频提示
- 镜头运动（只选一种）：a slow lateral track or dolly gliding from one space into the next, camera stable, often from a high angle onto the route.
- 主体运动：walking a predetermined path, changing shoes, counting money, lighting a cigarette; precise ritual gestures; violence short and sudden in the middle of the take.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, no motion-blur styling.

## 负面提示
no neon as decoration, no gangster philosophy, no slow-motion violence, no moral ending for a genre film, no shadowless daylight, no art department overwhelming the figure, no every-shot symmetry, no backstory explanation, no handheld, no zoom, no drone, no HDR.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：neon red, green and blue zoned separately over wet ground; 35–50mm; hard edge light, half-black face, smoke cutting light; symmetric frame-within-frame with a second space; tile, plastic, old sign, rain, ice.
- 禁止漂移：no party-neon mix, no HDR, no clean glass towers, no handheld shake, no warm filter.
