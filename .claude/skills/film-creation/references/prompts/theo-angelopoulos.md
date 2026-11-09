---
name: theo-angelopoulos
title: 西奥·安哲罗普洛斯 Theo Angelopoulos
style_file: ../directors/theo-angelopoulos.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, faded olive-green and ochre, low overcast light, mist and rain, a very wide open landscape cut by a road, railway or river, tiny figures walking along the line, 35–50mm lateral panorama, camera placed ahead of the characters, wet stone and rusted rails, flat contrast, history heavier than the people.

## 图像提示
- 主体 / 场景：refugees or a lone traveller crossing a border station in fog; children walking a railway line; a soldier column on a snow plain. A road, river or track cuts the frame diagonally and the figures follow it.
- 景别 / 构图：extreme wide and wide only; open lines through the frame, figures small, often a third of the frame empty; no emotional close-up, no closed interior composition.
- 镜头 / 焦段：35–50mm; wide lateral framing, long lens only to compress a distant horizon.
- 光线：overcast, fog, rain; low-contrast natural light, no dramatic key, no silhouetted hero.
- 色彩：grey-green, earth ochre, faded blue; low saturation; weather is normal, not special atmosphere.
- 材质：wet stone, rusted rails, snow, peeling station walls, military wool; no clean polished interiors.

## 视频提示
- 镜头运动（只选一种）：slow lateral pan — the camera finds one figure, pans to another who already belongs to a different decade, then stops.
- 主体运动：figures walk along the line and exit the frame; the camera holds on the emptied space until the next group enters.
- 时长 / 帧率 / 运动模糊：40–70 seconds, 24fps, minimal blur; the pan must be slow enough to read two eras inside one move.

## 负面提示
no emotional close-up, no shot-reverse-shot, no flashback marker, no dissolve-to-past, no voice-over explaining the image, no music landing on each emotional beat, no bright saturated colour, no symmetrical closed interior, no background flags and ruins used as set dressing, no fog-as-poetry postcard, no fast cutting, no camera following a character out of frame.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：grey-green and ochre low saturation, 35–50mm lateral wide, flat overcast light, open line cutting the frame with tiny figures, wet stone and rails.
- 禁止漂移：no golden-hour glow, no drone reveal, no handheld, no close-up, no saturated blue sky, no modern city skyline.
