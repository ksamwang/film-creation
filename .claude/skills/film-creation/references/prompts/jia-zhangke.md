---
name: jia-zhangke
title: 贾樟柯 Jia Zhangke
style_file: ../directors/jia-zhangke.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Chinese county town, mid-long shot from across the street, figure standing at the edge of the frame or with their back to camera, loose composition with a power line, billboard or plastic stool intruding in the foreground, grey-yellow and grey-green low saturation, natural light from existing fixtures with dirty shadows, roller shutter, wall tile, plastic sheeting, rebar, a construction site rather than nostalgia, 35–50mm, plain, unstaged.

## 图像提示
- 主体 / 场景：a young man waiting outside a shuttered shop; workers eating at a plastic table beside a demolition site; a woman on a ferry; a family in a tiled living room with the TV on.
- 景别 / 构图：mid-long shot, figure at frame edge or back turned; one or two obstructions always in the foreground; loose, unstaged, no centered portrait.
- 镜头 / 焦段：35–50mm, observing from across the street, never in the face.
- 光线：natural and existing light only; interior lamps as they are; darks allowed to be dirty, never lifted.
- 色彩：grey-yellow, grey-green, low saturation; no nostalgia filter.
- 材质：roller shutters, wall tiles, plastic sheeting, old sofa, rebar, billboard.

## 视频提示
- 镜头运动（只选一种）：static camera at passerby eye height with a slow pan to sweep the era's traces; after the subject exits frame, hold without following.
- 主体运动：walking past, waiting, eating, smoking, riding a scooter; everyday duration, no designed beat.
- 时长 / 帧率 / 运动模糊：10–20 seconds, 24fps, no speed ramps, no motion-blur styling.

## 负面提示
no nostalgia filter, no county town as spectacle, no sad strings for the poor, no camera hunting for beauty, no explanatory voice-over, no character stating the theme, no star faces, no every-shot-static long take, no handheld, no HDR, no drone aerial.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：grey-yellow and grey-green, low saturation; 35–50mm; natural existing light with dirty darks; fixed passerby height, edge framing, foreground clutter; roller shutter, tile, plastic, rebar.
- 禁止漂移：no warm filter, no LED clean white, no drone, no modern glass towers, no digital skin.
