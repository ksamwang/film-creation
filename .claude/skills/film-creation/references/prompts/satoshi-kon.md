---
name: satoshi-kon
title: 今敏 Satoshi Kon
style_file: ../directors/satoshi-kon.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic animation still, precise hand-drawn psychological thriller, saturated red blue and yellow kept separate per space, flat animation light with a second source from a mirror screen or neon reflection, at least one reflective surface framing the subject, the same composition recurring in another space, hard clean perspective, 24mm wide-angle distortion pressing on the face, unstable, watched, exact.

## 图像提示
- 主体 / 场景：an idol on a stage seen through a television monitor; a woman alone in a bedroom that repeats in three versions; a detective in a corridor of mirrors; a parade of objects flooding a city street.
- 景别 / 构图：medium and close, subject plus screen, mirror or window in the same frame; at least one "being watched" device; the same composition recurs across spaces; full shot only to reveal a whole level of reality.
- 镜头 / 焦段：24–35mm wide with distortion for pressure; 50mm static frontal for the watched moment.
- 光线：flat animation light; reflections and screens supply the second source; no realistic volumetric light.
- 色彩：saturated red, blue and yellow, each space with its own temperature; no unified filter.
- 材质：mirror, glass, screen, neon, tile — every surface able to reflect another space.

## 视频提示
- 镜头运动（只选一种）：one fast push-in or orbit that ends on a reflective surface, handing off to the next space; no smooth neutral dolly.
- 主体运动：a figure runs while the camera turns the other way; a body passes through a mirror seam; a crowd moves as one graphic mass.
- 时长 / 帧率 / 运动模糊：2–4 seconds per shot, 24fps, slight smear only on the match-cut frame.

## 负面提示
no color filter separating dream from reality, no "it was all a dream" ending, no explicit explanation of the boundary, no transition that exists only to show off, no supporting character who exists only as a tool, no slow-motion beautified violence, no passive protagonist waiting to be rescued, no naturalistic handheld, no shallow depth of field, no photoreal 3D, no generic psychedelic swirl, no female lead used as an object of desire.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：saturated red / blue / yellow, one temperature per space, no unified grade.
 - 镜头：24–35mm distorted; 50mm static for the watched moment; .
 - 光线：flat animation light plus a screen or reflection source.
 - 构图：recurring composition, one reflective device in every frame.
 - 材质：mirror, glass, screen, neon, tile.
- 禁止漂移：no unified grade, no realistic bokeh, no 3D render, no generic surrealism, no dream filter, no character design change between spaces.
