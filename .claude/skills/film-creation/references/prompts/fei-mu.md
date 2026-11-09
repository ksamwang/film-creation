---
name: fei-mu
title: 费穆 Fei Mu
style_file: ../directors/fei-mu.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1940s Chinese small town, desaturated blue-grey and earth yellow with one candle-warm accent, natural window light, one side of the face in shadow, deep focus, door and window frames splitting the composition, figure and wall each half the frame, peeling plaster, damp brick, old timber, cotton cloth, 35mm film grain, academy ratio, restrained, still, wide negative space.

## 图像提示
- 主体 / 场景：a wife and her returned old friend standing at opposite ends of a courtyard; a family seated in a dim front room; a lone man at a threshold.
- 景别 / 构图：medium-wide to medium, deep space with a front room and a back room; doorframe or window lattice cuts the frame; figure and wall each take half; large negative space; no centered hero shot.
- 镜头 / 焦段：35–50mm, deep focus at f/4 or deeper, eye level.
- 光线：natural window light, side-back direction, half the face in shadow, no fill; night scenes lit by candle only, never bulbs.
- 色彩：near-monochrome blue-grey; colour passages low saturation — blue-grey, earth yellow, one candle warm.
- 材质：peeling plaster, damp brick, old timber, cotton cloth, paper windows.

## 视频提示
- 镜头运动（只选一种）：slow lateral tracking that trails half a beat behind the walker, stops when the subject stops, never pushes in.
- 主体运动：walking through a courtyard, sitting down, turning away; hands on knees, eyes elsewhere; the largest outburst is turning and leaving.
- 时长 / 帧率 / 运动模糊：8–12 seconds, single take, 24fps, minimal motion blur, no speed ramps.

## 负面提示
no close-up tears, no fast cutting inside an argument, no villain dialogue framing, no musical cue telling the audience to feel sad, no handheld, no zoom, no ruin postcard, no symmetrical centered hero shot, no modern glass, no digital sharpness, no warm sepia nostalgia filter, no characters speaking their real feelings aloud, no resolution or break-up ending.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：blue-grey and earth yellow, low saturation, one candle accent; 35–50mm deep focus; natural window light, side-back, half-face shadow; door and window frames halving the frame, figure at the threshold; peeling plaster, damp brick, old timber, cotton.
- 禁止漂移：no modern glass, no LED white, no clean digital skin, no crane or drone, no telephoto compression.
