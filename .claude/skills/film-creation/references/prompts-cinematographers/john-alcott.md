---
name: john-alcott
title: 约翰·阿尔科特 John Alcott
style_file: ../cinematographers/john-alcott.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Candlelit 35mm frame, a single practical flame as the only source, a warm pool of light falling into absolute black, symmetrical one-point perspective, wide 20mm lens, centered figure on the axis, muted amber and cold window blue, visible film grain, patient, formal, eighteenth-century stillness.

## 图像提示
- 主体 / 场景：a figure standing alone in a symmetrical corridor, ballroom or drawing room, lit only by candles, a window or a single hanging bulb.
- 景别 / 构图：wide to medium-wide, centered, one-point perspective, strict symmetry, long axis leading to a vanishing point.
- 镜头 / 焦段：18–25mm wide-angle, or 50mm f/0.7 for candlelight; deep space, no distortion spectacle.
- 光线：single practical source — candle, window, bare bulb; low key, warm pool surrounded by true black.
- 色彩：amber candlelight, cold window blue, muted earth tones, low saturation.
- 材质：wax, wood, snow, plaster, period fabric, 35mm grain.

## 视频提示
- 镜头运动（只选一种）：extremely slow zoom in along the central axis.
- 主体运动：the figure stands still or walks slowly toward the vanishing point; the room remains symmetrical.
- 时长 / 帧率 / 运动模糊：10–20 seconds, 24fps, standard shutter, minimal motion blur.

## 负面提示
no electric fill on candlelight, no soft diffusion on the flame, no saturated neon, no handheld, no fast pan, no asymmetrical framing, no gray shadows without a source, no fast cutting, no modern LED flat light, no color grade filter.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：amber and cold blue, 18–25mm, single candle or window, symmetrical axis, wax and grain.
- 禁止漂移：no fill light, no handheld, no neon, no modern interior, no lifted blacks.
