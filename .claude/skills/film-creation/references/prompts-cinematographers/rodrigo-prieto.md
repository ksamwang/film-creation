---
name: rodrigo-prieto
title: 罗德里戈·普列托 Rodrigo Prieto
style_file: ../cinematographers/rodrigo-prieto.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, handheld medium close-up, camera pressed close behind a shoulder, mixed color temperature — tungsten amber against cool daylight, culturally specific streets and rooms, visible skin texture and sweat, 35–50mm spherical lens, shallow but not empty depth, practical lamps and neon in frame, medium-high contrast, 35mm grain, intimate, immediate, unglamorous.

## 图像提示
- 主体 / 场景：a person inside a crowded market, a family kitchen, a motel room, or a car at dusk; the place carries a specific culture and class.
- 景别 / 构图：medium close-up and close-up, subject off-center, framed through a doorway, car window, or the gap between shoulders; foreground obstruction allowed.
- 镜头 / 焦段：35–50mm spherical, 85mm for close-ups; shallow depth that still keeps the room readable.
- 光线：practical sources — window, tungsten lamp, neon, headlights; mixed color temperatures left uncorrected, medium-high ratio.
- 色彩：tungsten amber, daylight cyan, ochre, earth yellow, mist green; regional palette, medium saturation, dirt retained.
- 材质：film grain, sweat, dust, worn fabric, peeling paint, real street surfaces.

## 视频提示
- 镜头运动（只选一种）：handheld follow, camera breathing behind the subject.
- 主体运动：the subject walks through a crowd or turns to speak; people pass between camera and subject.
- 时长 / 帧率 / 运动模糊：8–20 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no unified teal-orange LUT, no even beauty lighting, no gimbal-smooth replacement for handheld, no subject detached from cultural environment, no cold white LED washing out tungsten, no symmetrical crowd composition, no shallow depth turning background into color blocks, no slow-motion emotion, no clean digital skin.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：tungsten amber against daylight cyan, ochre and earth; 35–50mm; mixed practical light; off-center through frames; grain and sweat.
- 禁止漂移：no unified grade, no studio fill, no gimbal glide, no fashion lighting, no modern glass skyline.
