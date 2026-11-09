---
name: emir-kusturica
title: 埃米尔·库斯图里卡 Emir Kusturica
style_file: ../directors/emir-kusturica.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Balkan village wedding in mud and dust, saturated ochre red green and turquoise, a brass band and a pig crossing the foreground, handheld camera at chest height inside the dancing crowd, bare bulbs and firelight, sweat on faces, cheap lace, feathers, animal hair, 24–35mm wide lens, 35mm grain, chaotic, ecstatic, alive.

## 图像提示
- 主体 / 场景：a gypsy brass band, a bride and groom, a smuggler, children and a grandmother; a muddy yard, a wedding tent, a ruined house, a riverbank; at least one animal in the frame.
- 景别 / 构图：medium and medium-wide with two or more planes of action; foreground animal or instrument crossing; close-up only when someone sings or dies. Off-balance, diagonal, crowd filling the corners, something moving at the edge; no clean symmetrical single.
- 镜头 / 焦段：24–35mm wide and close to bodies; 50–85mm for a face; no long telephoto isolating the figure from the chaos.
- 光线：sun, fire, bare bulbs, car headlights; faces shiny with sweat; no soft beauty light.
- 色彩：saturated ochre, red, green, turquoise; warm daylight, firelit night; no desaturated realism.
- 材质：mud, feathers, brass, sweat, cheap lace, animal hair, dust, wet cloth.

## 视频提示
- 镜头运动（只选一种）：handheld circular orbit around the dancing crowd, pushed and jostled by bodies, one continuous move.
- 主体运动：people dancing, a band playing, a pig running between legs, a bride pulled in two directions; the camera is bumped and recovers.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, heavy natural motion blur; never stabilize the shot.

## 负面提示
no clean symmetrical frame, no static crowd, no cute-animal prop, no desaturated realism, no slow-motion heroics, no voice-over history lesson, no tidy ending, no folkloric postcard, no modern interior, no digital smoothness, no shallow beauty focus, no animal as metaphor-only.

## 一致性锚点
- 色彩：saturated ochre, red, green, turquoise; firelight and sweat.
- 镜头：24–35mm wide, 50–85mm face; .
- 光线：sun, fire, bare bulb, headlight; hard and uneven.
- 构图：diagonal, layered, foreground animal or instrument, crowd in all corners.
- 材质：mud, feathers, brass, cheap lace, animal hair, dust.
- 禁止漂移：no clean studio, no desaturated grade, no stabilized gimbal, no modern city, no digital skin, no empty frame.
