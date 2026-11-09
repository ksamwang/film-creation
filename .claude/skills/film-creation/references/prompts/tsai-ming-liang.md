---
name: tsai-ming-liang
title: 蔡明亮 Tsai Ming-liang
style_file: ../directors/tsai-ming-liang.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, bare Taipei apartment or flooded corridor, fixed extreme wide-angle full shot, low light from a single practical source, subject centered or pressed against the frame edge, damp stained walls, mattress, leaking water, cool cyan-grey, mould green and sodium yellow, oppressive stillness, minimal, no camera movement.

## 图像提示
- 主体 / 场景：a man sitting on a mattress in an empty room with water pooling on the floor; a woman alone in a corridor; a figure at the edge of a ruined space; the room is a resident, not a set.
- 景别 / 构图：full shot, fixed, subject centered or pressed to the frame edge; wide-angle slight distortion makes the body small.
- 镜头 / 焦段：wide-angle, deep focus, static.
- 光线：low illumination, practical sources only, no dramatic key, no fill.
- 色彩：cyan-grey, mould green, sodium yellow — three hues maximum.
- 材质：water, damp wall, mattress, tile, peeling paint, stains.

## 视频提示
- 镜头运动（只选一种）：completely static; the camera never follows and holds after the subject leaves the frame.
- 主体运动：sitting, lying down, eating, walking slowly, sleeping; the body occupies space, no performed emotion.
- 时长 / 帧率 / 运动模糊：40–60 seconds in one take, 24fps, no motion blur.

## 负面提示
no score, no shortened cut to fix pacing, no psychological flashback or voice-over, no close-up explaining emotion, no erotic spectacle, no camera following the subject, no character naming their loneliness, no clean bright art direction, no handheld, no fast cutting, no symmetrical advertising composition.

## 一致性锚点
- 色彩：cyan-grey, mould green, sodium yellow; three hues maximum, dirty and cold.
- 镜头：wide-angle, deep focus, fixed.
- 光线：low-level practical source, no fill, damp falloff.
- 构图：full shot, subject centered or pressed to the edge, room given equal weight.
- 材质：water, damp wall, mattress, tile, peeling paint.
- 禁止漂移：no bright clean interior, no music, no camera movement, no glamorous ruin, no fast cut.
