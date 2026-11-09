---
name: emmanuel-lubezki
title: 艾曼努尔·卢贝兹基 Emmanuel Lubezki
style_file: ../cinematographers/emmanuel-lubezki.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, immersive wide-angle frame, 14–27mm lens, camera inside the action, natural available light, magic-hour sky, low contrast with retained highlights, dust and sweat in the air, earth-brown and grey-green palette, deep space, subject off-center, environment pressing at the edges, 35mm grain, continuous, intimate, unposed.

## 图像提示
- 主体 / 场景：a person moving through a real landscape or crowded interior; the environment is always visible.
- 景别 / 构图：medium to wide, off-center, deep space, foreground objects at the edge; no clean symmetrical portrait.
- 镜头 / 焦段：14–27mm wide-angle, slight distortion, deep focus.
- 光线：available light — window, sky, fire, car headlights; low ratio, retained highlights.
- 色彩：earth brown, grey-green, sky blue; natural, no unified teal-orange grade.
- 材质：dust, sweat, water, fire, leaves, real locations.

## 视频提示
- 镜头运动（只选一种）：handheld or Steadicam follow, camera inside the action, no cut.
- 主体运动：walking, running, turning; the camera follows the body.
- 时长 / 帧率 / 运动模糊：10–30 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no studio lighting, no shot-reverse-shot coverage, no locked-off master with zoom, no teal-orange grade, no shallow depth of field as default, no slow-motion hero shot, no clean symmetrical composition, no digital-clean skin, no artificial haze.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：natural earth palette; 14–27mm; available light; off-center deep space; dust and sweat.
- 禁止漂移：no studio fill, no orange-teal LUT, no drone-only landscape, no clean digital sharpness.
