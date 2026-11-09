---
name: walter-salles
title: 沃尔特·萨列斯 Walter Salles
style_file: ../directors/walter-salles.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, camera at the same height as the characters, 35–50mm lens, figures framed with their real environment still legible behind them, natural daylight and available interior lamps, regional palette — grey-blue northeast station, Andean earth yellow, Amazon green — dust, asphalt, worn car, threadbare clothing, on the road, quiet, observational.

## 图像提示
- 主体 / 场景：two people sharing the front seat of a truck; a woman writing letters at a station counter; a boy asleep against a bus window; a roadside shrine in dry country.
- 景别 / 构图：wide and full shot to establish geography, close-up for faces and hands; subject and environment share the frame, background not blurred, subject neither centered nor pinned to the edge; road scenes shot side-on so the viewer looks the same direction as the characters.
- 镜头 / 焦段：35–50mm, occasional long lens; wide only for road panoramas, never distorting a face.
- 光线：natural daylight, window light and existing interior lamps; big lights only for night; no dramatic shadow.
- 色彩：regional — grey-blue northeast, Andean earth yellow, Amazon green; no single global grade.
- 材质：asphalt, dust, rusted car, worn fabric, wooden counters, road film grain.

## 视频提示
- 镜头运动（只选一种）：side-tracking shot from a moving vehicle at the characters' speed.
- 主体运动：sitting in a car, looking out of a window, walking to a bus, handing over an object; natural, unhurried.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, mild documentary motion blur; let a silent exchange run without cutting.

## 负面提示
no sweeping drone aerials, no postcard landscape, no savior framing, no voice-over history lesson, no sentimental score swell, no glamour lighting, no poverty as backdrop, no hugging resolution, no saturated travel-brochure color.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：regional triad, low-medium saturation, no unified filter.
- 镜头：35–50mm, road / interior.
- 光线：natural daylight and available lamps, no dramatic shadow.
- 构图：eye level, background legible, side-on road framing.
- 材质：asphalt, dust, rust, worn fabric, film grain.
- 禁止漂移：no drone shots, no teal-orange grade, no clean digital skin, no luxury vehicles, no travel-agency glow.
