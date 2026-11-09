---
name: wally-pfister
title: 沃利·菲斯特 Wally Pfister
style_file: ../cinematographers/wally-pfister.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic anamorphic film still, hard low-key noir lighting, deep crushed blacks, a single hard key and a strong backlight rim, steel-blue night city against warm tungsten interiors, rain and smoke in the air, low camera angle, 35mm grain, IMAX-scale wide shots, graphic, severe, morally weighted.

## 图像提示
- 主体 / 场景：a solitary figure on a rain-soaked city street, in a glass office, or against a dark institutional corridor.
- 景别 / 构图：wide establishing shot or tight medium; figure off-center, negative space left black, foreground columns or rain.
- 镜头 / 焦段：35–50mm anamorphic for space; 75–100mm for close-ups; low angle.
- 光线：hard off-screen key plus strong rim, ratio or more; blacks near pure black, highlights held on streetlamps and rain.
- 色彩：steel blue, cyan-grey, amber tungsten; low saturation, two-temperature contrast.
- 材质：rain, smoke, wet glass, concrete, wool overcoat, polished metal.

## 视频提示
- 镜头运动（只选一种）：slow dolly in.
- 主体运动：the figure stands still or turns slowly; rain, smoke, and coat fabric carry the motion.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no even fill light, no soft key, no three-point lighting, no flat grey shadows, no neon collage, no shallow background, no LED white light, no warm nostalgia filter, no handheld shake, no low-contrast grade, no daylight brightness.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：steel blue and amber, low saturation, deep black; 35–50mm anamorphic; hard key at ; figure off-center in black negative space; rain, smoke, wet glass.
- 禁止漂移：no LED white, no teal-orange LUT, no daytime exposure, no soft beauty light, no shallow depth of field.
