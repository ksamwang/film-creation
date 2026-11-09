---
name: jacques-tati
title: 雅克·塔蒂 Jacques Tati
style_file: ../directors/jacques-tati.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, extreme deep-focus wide shot on 18–25mm, three layers of action in one frame, a figure stumbling in the foreground, two people talking mid-ground, a door closing by itself in the background, flat diffuse daylight with no shadows, cool grey-blue glass and aluminium, polished floor, deadpan, geometric, gag at the frame edge.

## 图像提示
- 主体 / 场景：a tall awkward man in a raincoat at a glass office entrance; a modern apartment where chairs fold by themselves; tourists crossing a polished lobby.
- 景别 / 构图：wide or full shot, deep focus, three depth planes active at once, gag placed at the frame edge or in the background, focus deliberately dispersed.
- 镜头 / 焦段：18–25mm wide-angle, everything sharp front to back, no long lens, no close-up.
- 光线：flat diffuse daylight or broad fluorescent, no shadows, no dramatic side light; light creates no mood.
- 色彩：《游戏时间》cool grey-blue glass；《我的舅舅》saturated red and green plastic against warm brown old quarter.
- 材质：glass, aluminium, plastic, polished floor, old brick, modern furniture.

## 视频提示
- 镜头运动（只选一种）：fixed camera at standing eye height, set back half a step; a pan may only bring a new figure into frame, never point at the joke.
- 主体运动：choreographed, step-counted bodies, precise but half a beat off; several independent actions in three planes.
- 时长 / 帧率 / 运动模糊：10–20 seconds, 24fps, minimal motion blur, no speed ramp.

## 负面提示
no close-up on the gag, no cartoon sound effects, no unnatural foley, no dialogue carrying emotion, no camera move that points at the joke, no inner monologue or psychology, no cutting within one space, no warm grade on the glass city, no modern architecture as villain lair, no slapstick exaggeration, no shallow depth of field.

## 一致性锚点
- 色彩：cool grey-blue glass; or saturated red-green plastic against warm brown.
- 镜头：18–25mm, deep focus, or .
- 光线：flat diffuse, no shadows, no side light.
- 构图：full shot, three depth planes, gag at the edge or background, focus dispersed.
- 材质：glass, aluminium, plastic, polished floor, old brick.
- 禁止漂移：no drone, no handheld, no shallow bokeh, no teal-orange grade, no neon, no anamorphic flare.
