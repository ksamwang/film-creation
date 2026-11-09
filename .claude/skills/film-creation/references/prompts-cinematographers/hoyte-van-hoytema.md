---
name: hoyte-van-hoytema
title: 霍伊特·范霍伊特玛 Hoyte van Hoytema
style_file: ../cinematographers/hoyte-van-hoytema.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic 65mm film still, large-format IMAX texture, soft overcast daylight, low-saturation steel blue and grey-green palette, warm skin against cold air, visible haze and dust in the beam, wide 40mm lens, small figure against a vast sky, natural window light with detail held in shadow, fine film grain, quiet, monumental, unforced.

## 图像提示
- 主体 / 场景：a lone figure in a real landscape, aircraft cabin, or bare interior; sky, ceiling, or weather always occupies part of the frame.
- 景别 / 构图：wide to medium; figure low in frame, large negative space above, slightly off-center, environment pressing at the edges.
- 镜头 / 焦段：40–65mm large-format spherical; 28mm for the wide establishing shot.
- 光线：overcast daylight or a single window; ratio –; shadow detail retained, highlights just short of clipping.
- 色彩：steel blue, grey-green, concrete grey, warm skin and wood as the only warmth; low saturation, no unified teal-orange grade.
- 材质：haze, dust, condensation, wool, brushed metal, real weather on glass.

## 视频提示
- 镜头运动（只选一种）：slow dolly in.
- 主体运动：the figure turns toward the light, breath visible, coat and hair moving in wind.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no clean digital sharpness, no HDR, no shallow depth of field, no creamy bokeh, no even fill light, no three-point lighting, no teal-orange grade, no pure white sky, no unmotivated handheld shake, no drone-only vista, no plastic skin, no glass skyscrapers.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：steel blue and grey-green with warm skin; 40–65mm large format; overcast window light at –; figure low with sky above; haze, dust, fine grain.
- 禁止漂移：no HDR, no LED white balance, no modern glass architecture, no crisp digital skin, no orange-teal LUT.
