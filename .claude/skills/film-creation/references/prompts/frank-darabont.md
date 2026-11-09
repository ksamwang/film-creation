---
name: frank-darabont
title: 弗兰克·达拉邦特 Frank Darabont
style_file: ../directors/frank-darabont.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Classical American prison drama, warm amber window light against grey-blue shadow, eye-level static two-shot, 35mm lens, stone walls and iron bars in the foreground, rain on the yard, worn books and uniforms, soft halation, fine film grain, restrained, humanist, no stylization.

## 图像提示
- 主体 / 场景：two men in prison uniforms sitting on a cell bunk or at a long wooden table, a guard standing at the edge of frame, rain on the window.
- 景别 / 构图：medium two-shot at eye level; stable horizontal lines; doorframe or bars as a straight frame; no tilt.
- 镜头 / 焦段：35–50mm for the two-shot, 85mm for the single close-up; shallow but readable depth.
- 光线：one motivated source — barred window, bare bulb, yard sun; warm key on one side of the face, cool shadow on the other; visible falloff.
- 色彩：warm amber, grey-blue shadow, faded olive uniforms; golden only in memory; no teal-orange grade.
- 材质：stone, rusted iron, rain, worn paper, wool uniforms, scarred wood.

## 视频提示
- 镜头运动：one slow dolly in, about ten percent over the shot; no handheld, no zoom, no crane.
- 主体运动：a man looks up from a table, hands still, then speaks; the other man listens without moving.
- 时长 / 帧率 / 运动模糊：8–10 seconds, 24fps, natural motion blur, no speed ramp.

## 负面提示
no handheld camera, no Dutch angle, no high-angle judgment of the prisoner, no cold teal grade, no even fill light, no cutaway reaction shots during dialogue, no on-screen violence, no voice-over explaining the theme, no digital sharpness, no glossy prestige lighting.

## 一致性锚点
- 色彩：warm amber key, grey-blue shadow, olive and stone grey, low saturation.
- 镜头：35–50mm two-shot, 85mm close-up.
- 光线：single motivated window or bulb, hard falloff, rim from behind.
- 构图：eye-level, stable horizontals, bars or doorframe in foreground.
- 材质：stone, iron, rain, paper, wool, wood.
- 禁止漂移：no modern glass architecture, no LED white, no handheld shake, no digital skin, no teal-orange blockbuster grade.
