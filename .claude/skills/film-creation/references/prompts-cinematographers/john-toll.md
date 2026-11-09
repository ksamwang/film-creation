---
name: john-toll
title: 约翰·托尔 John Toll
style_file: ../cinematographers/john-toll.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, epic natural-light landscape, anamorphic , long telephoto lens compressing layered ridges, tiny human figure off-center against a vast sky, low horizon, backlit golden grass and drifting dust, sun flaring inside frame, silhouetted bodies with rim light only, wheat-gold and earth-brown palette, high contrast, atmospheric haze, 35mm grain, patient, distant, monumental.

## 图像提示
- 主体 / 场景：a small human figure or a line of riders crossing a real landscape; the land dominates and the person is a moving dark mark.
- 景别 / 构图：extreme wide and wide, low horizon, figure off-center, foreground grass or ridge, layered mountains compressed by a long lens; no centered portrait.
- 镜头 / 焦段：75–300mm telephoto as the primary lens, 35mm only to establish geography; shallow atmospheric layering, not shallow focus.
- 光线：low natural sun in frame, backlight or side-backlight, silhouettes and rim light, sky allowed to blow out.
- 色彩：wheat gold, dry grass green, slate sky, earth brown; color shifts with time of day, no unified teal-orange grade.
- 材质：grass, dust, haze, horse sweat, coarse wool, real terrain.

## 视频提示
- 镜头运动（只选一种）：static camera with a very slow horizontal pan, holding the distant vantage point.
- 主体运动：figures walk or ride across the frame; wind moves the grass and clouds.
- 时长 / 帧率 / 运动模糊：10–20 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no close-up instead of landscape, no centered fully lit face, no even fill light, no drone top-down shot, no uniform orange sunset grade, no shallow depth of field erasing terrain, no slow-motion hero shot, no landscape as empty backdrop, no clean digital sharpness.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：wheat-gold and earth-brown palette; 75–300mm; backlit natural sun; low horizon with tiny off-center figure; grass and dust.
- 禁止漂移：no studio lighting, no teal-orange LUT, no aerial-only landscape, no portrait framing, no modern glass architecture.
