---
name: wes-anderson
title: 韦斯·安德森 Wes Anderson
style_file: ../directors/wes-anderson.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, perfect central symmetry, camera locked at chest height square to the wall, 35mm lens, flat deep-focus plane, one custom pastel palette per scene — pink, mint green, mustard yellow, brick red — even soft shadowless light, handmade wallpaper, uniforms, model miniatures, handwritten labels, deadpan, melancholy held inside order.

## 图像提示
- 主体 / 场景：a family arranged across a hotel lobby; a boy at a desk with labeled drawers; a concierge in a uniform between two doors; a room shown as four walls and a floor plan.
- 景别 / 构图：medium and full shot at chest height, subject centered, camera perpendicular to the back wall; flat, readable, frame-within-frame from doors and windows; tilt-down only for objects on a table, never for a face.
- 镜头 / 焦段：35mm wide, flat perspective, deep focus; no long-lens compression, no shallow focus.
- 光线：even, soft, nearly shadowless; sadness comes from empty space in the frame, not from darkness.
- 色彩：one custom palette per scene — pink, mint green, mustard yellow, brick red; artificial and consistent, never naturalistic.
- 材质：handmade wallpaper, uniforms, model miniatures, handwritten labels, pastries, old hotel fittings.

## 视频提示
- 镜头运动（只选一种）：slow lateral tracking at chest height, parallel to the wall, camera never tilts.
- 主体运动：walking a straight line, sitting precisely, handing over an object; actors move on marked positions, deadpan, no improvisation.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, no motion blur; cut on the last word rather than follow the movement.

## 负面提示
no handheld camera, no unmotivated zoom, no shallow depth of field, no bokeh background, no uneven natural window shadows, no dirty grunge texture, no fast emotional push-in, no dutch angle, no improvisational blocking, no warm nostalgic haze.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：pink / mint / mustard / brick red, one set per scene, medium-high saturation, low contrast.
- 镜头：35mm, flat plane, deep focus, or chapter.
- 光线：even soft light, almost no shadow.
- 构图：dead center, camera perpendicular to the wall, chest height.
- 材质：handmade wallpaper, uniforms, models, handwritten labels.
- 禁止漂移：no handheld shake, no telephoto compression, no naturalistic dirt, no modern glass architecture, no off-center drift without a story reason.
