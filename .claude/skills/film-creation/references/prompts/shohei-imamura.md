---
name: shohei-imamura
title: 今村昌平 Shohei Imamura
style_file: ../directors/shohei-imamura.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Japanese lower-depths naturalism, camera dropped to knee height, handheld 28mm wide angle close to bodies and clutter, people and animals sharing the same muddy ground, crowded wet hovel with laundry, crates and chickens, hard available daylight and dim underexposed interiors, desaturated earth brown and green, grime on the lens, raw, unpolished, alive.

## 图像提示
- 主体 / 场景：a fisherman gutting a catch beside a pig; a family eating at a low table with laundry hanging overhead; a woman carrying a child through a muddy yard; chickens crossing the doorway.
- 景别 / 构图：medium-close and close, crowded and asymmetric, bodies pressed among objects; full shot only to establish the living environment; no clean negative space.
- 镜头 / 焦段：28–35mm wide, slight distortion close to faces, knee-height camera.
- 光线：available light only, hard outdoors, dim and underexposed indoors, no fill, no rim.
- 色彩：earth brown, moss green, ochre; low saturation, underexposure allowed.
- 材质：mud, water, grass, rough planks, animal fur, sweat, grime on the lens.

## 视频提示
- 镜头运动（只选一种）：handheld follow at knee height, unsteady and searching; no gimbal smoothness.
- 主体运动：people working, eating, fighting, carrying animals; bodies pushing through clutter; someone glances at the lens.
- 时长 / 帧率 / 运动模糊：3–6 seconds, 24fps, natural handheld blur.

## 负面提示
no beautified poverty, no moral halo on the poor, no clean symmetrical composition, no music telling the audience how to feel, no avoidance of bodily dirt, no literary dialogue, no decorative animal inserts, no polite observational distance, no gimbal-smooth camera, no saturated pastoral color, no studio lighting, no tasteful minimalism, no shallow-focus poverty portrait.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：earth brown / green / ochre, low saturation, underexposed.
 - 镜头：28–35mm, knee height, handheld.
 - 光线：available only, hard outdoors, dim indoors.
 - 构图：crowded and asymmetric, bodies among objects, no clean space.
 - 材质：mud, water, planks, fur, grime.
- 禁止漂移：no clean digital skin, no drone, no color grade, no modern appliances, no tidy set dressing, no shallow-focus portrait, no studio backdrop.
