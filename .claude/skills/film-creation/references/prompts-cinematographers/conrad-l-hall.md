---
name: conrad-l-hall
title: 康拉德·L·霍尔 Conrad L. Hall
style_file: ../cinematographers/conrad-l-hall.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 35mm, a soft window key from the side, a large dark room falling away into black, one face emerging from shadow, 75–150mm long lens, to contrast, slate grey, amber and bone white, a single warm accent, smoke and rain on glass, faint 1/8 Black ProMist diffusion, painterly, quiet, elegiac, held.

## 图像提示
- 主体 / 场景：a solitary man or woman in a dim room — a bedroom, a kitchen at night, a rain-streaked window; the room is mostly dark.
- 景别 / 构图：medium close-up or close-up, off-center, a large dark field around the face, a bright window rectangle in the background.
- 镜头 / 焦段：75–150mm long lens, shallow depth, background compressed to a tone.
- 光线：one soft side key from a window or bounced source, –, gentle rim, eyes protected, dark background.
- 色彩：slate grey, amber, bone white; a single warm accent (a lamp, a red object); no saturated primaries.
- 材质：smoke, rain, glass, dust, fabric, skin with visible texture but softened.

## 视频提示
- 镜头运动（只选一种）：very slow dolly push-in toward the eyes.
- 主体运动：a person turns slowly toward the window or lowers their head; almost still.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, natural motion blur, no handheld, no speed ramp.

## 负面提示
no flat frontal key, no saturated primary colors, no background as bright as the face, no fast cutting, no handheld, no digital sharpness, no grey silhouettes, no cool white LED, no hard shadow across the eyes, no modern glass architecture.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：slate grey, amber, bone white plus one warm accent; 75–150mm; soft side window key at –; off-center face in a dark field; smoke, rain and soft skin.
- 禁止漂移：no flat fill, no primary palette, no handheld, no clean digital sharpness, no HDR lift.
