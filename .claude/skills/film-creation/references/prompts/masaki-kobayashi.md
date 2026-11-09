---
name: masaki-kobayashi
title: 小林正树 Masaki Kobayashi
style_file: ../directors/masaki-kobayashi.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, black-and-white 1960s Japan, a wide symmetrical interior of a samurai house, tatami geometry, shoji screens, figures placed on precise marks, deep focus, hard directional light and deep shadow, Tohoscope, 35mm lens, static camera, severe, theatrical, ritualistic, dust or snow in the air.

## 图像提示
- 主体 / 场景：a ronin kneeling at the center of a bare reception room; elders seated behind a screen; a lone figure at a gate in falling snow.
- 景别 / 构图：wide shot, symmetrical, frame-within-frame through shoji and posts, deep foreground and background; no close-up.
- 镜头 / 焦段：35–50mm, deep focus, entire room readable from front tatami to rear wall.
- 光线：hard directional light through paper screens, deep shadow, silhouettes; no soft fill.
- 色彩：black and white, high contrast, retained paper texture in the whites; no sepia.
- 材质：tatami, wood grain, paper shoji, armor lacing, white sand, snow, blood.

## 视频提示
- 镜头运动：static camera for the entire shot; no movement.
- 主体运动：formal, restrained — kneeling, bowing, drawing a sword slowly, then a sudden clumsy strike.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, minimal motion blur, no speed ramp.

## 负面提示
no handheld camera, no zoom, no crying close-up, no glamorous swordplay, no naturalistic improvisation, no sepia or warm tone, no explanatory voice-over, no sympathetic authority, no single-shot reverse angles, no soft fill light.

## 一致性锚点
- 色彩：black and white, high contrast, paper-white highlights, crushed blacks.
- 镜头：35–50mm deep focus.
- 光线：hard directional light, shoji silhouette, deep shadow.
- 构图：symmetrical, geometric marks, threshold in frame, figures small in the room.
- 材质：tatami, wood, paper, armor lacing, snow, blood, film grain.
- 禁止漂移：no color grade, no warm lantern light, no handheld drift, no modern architecture, no digital sharpness.
