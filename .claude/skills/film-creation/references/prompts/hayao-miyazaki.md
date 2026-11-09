---
name: hayao-miyazaki
title: 宫崎骏 Hayao Miyazaki
style_file: ../directors/hayao-miyazaki.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic animation still, hand-drawn cel animation over watercolor backgrounds with visible paper grain, saturated layered greens and blues each with its own color temperature, deep receding space, wind bending grass hair cloth and smoke in one direction, soft natural daylight with cloud shadows moving across the land, an inhabitable cluttered interior of wood iron and steam, hard clean foreground lines, curious, warm, alive.

## 图像提示
- 主体 / 场景：a girl on a rooftop above a sprawling hand-painted town; a boiler room packed with pipes, coal and steam; a small aircraft over a green valley; a forest spirit at the edge of tall grass.
- 景别 / 构图：extreme wide establishing first, then medium; deep space with foreground, midground and background readable; wind unifies every element; interiors cluttered and lived-in.
- 镜头 / 焦段：24–35mm equivalent wide, no wide-angle distortion on faces; tighter lens only for a face.
- 光线：natural daylight, cloud shadows drifting across the ground, no flat uniform light.
- 色彩：saturated but layered, separate color temperature for sky and grass; watercolor washes, no even digital gradient.
- 材质：watercolor paper grain, wood, iron, steam, cloth, hand-painted foliage.

## 视频提示
- 镜头运动（只选一种）：one long lateral move that reveals the landscape instead of cutting; or a low glide over grass and rooftops; no shaky handheld.
- 主体运动：wind moves hair, grass, smoke and flags together; flight with weight and inertia, clumsy takeoff and landing; running with clear direction.
- 时长 / 帧率 / 运动模糊：4–8 seconds, 24fps, slight smear on fast flight.

## 负面提示
no 3D-rendered smoothness replacing hand-drawn lines, no uniform gradient skies, no photoreal foliage, no villain monologue justifying himself, no rapid-cut flight montage, no voice-over explaining the world, no protagonist awakening to one-shot the enemy, no postcard nature, no ending that solves everything, no character stating the theme, no lens flare, no shallow depth-of-field bokeh, no vector-clean edges.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：saturated layered greens and blues, one temperature per plane.
 - 镜头：24–35mm equivalent wide.
 - 光线：natural daylight with moving cloud shadow.
 - 构图：deep space, wide establishing first, a single wind direction across all elements.
 - 材质：watercolor paper, hand-drawn line, wood, iron, steam.
- 禁止漂移：no 3D or CGI sheen, no uniform gradient, no vector-clean edges, no photoreal texture, no modern city, no flat anime filter.
