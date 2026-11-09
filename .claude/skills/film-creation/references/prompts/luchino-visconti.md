---
name: luchino-visconti
title: 卢基诺·维斯康蒂 Luchino Visconti
style_file: ../directors/luchino-visconti.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Italian aristocracy in decline, a vast ballroom with high ceilings and mirrors, figures arranged in depth by rank, gold-brown burgundy black and ivory, long window shafts and candlelight, silk velvet marble crystal silver, 35–50mm deep focus, camera slightly above eye level, slow lateral dolly through rooms, operatic, restrained, suffocating.

## 图像提示
- 主体 / 场景：a prince in a dark suit, a countess in silk, a family seated for dinner, guests at a ball; a palazzo ballroom, an opera box, a hotel lobby, a dining room with too much silver.
- 景别 / 构图：full shot or medium-full first, the room and the hierarchy in one frame; close-up only when the mask cracks. Deep staging, figures placed front/middle/back by rank, doorframes, mirrors and columns dividing the frame; no flat shot-reverse-shot.
- 镜头 / 焦段：35–50mm deep focus so people and architecture stay sharp together; 75–100mm only for a face at the moment of collapse; late-period zoom allowed, but slow.
- 光线：long shafts of window light, candlelight, gaslight; interiors lit like portraits, faces modeled, darks kept; no flat modern white light.
- 色彩：gold-brown, burgundy, black, ivory, faded blue; painterly and heavy, not naturalistic; no pastel, no bright primaries.
- 材质：silk, velvet, marble, crystal, silver, military uniforms, lace, heavy curtains.

## 视频提示
- 镜头运动（只选一种）：slow lateral dolly through the ballroom, passing a servant in the foreground, settling on the seated prince.
- 主体运动：guests turning in a waltz; a servant crossing with a tray; the prince sitting still while the room moves around him.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, minimal blur; the move must feel heavy, as if the camera itself is dressed in period clothes.

## 负面提示
no handheld camera, no fast cutting, no modern jump cut, no warm sepia, no pastel palette, no flat sitcom lighting, no modern furniture, no plastic or glass surfaces, no digital sharpness, no servant-as-decoration, no sympathetic-innocent aristocrat, no close-up that escapes the room, no democratic crowd.

## 一致性锚点
- 色彩：gold-brown, burgundy, black, ivory; heavy, painterly, low-key.
- 镜头：35–50mm deep focus; 75–100mm only for collapse.
- 光线：window shafts and candlelight, portrait modeling, detailed darks.
- 构图：deep staging, doorframes and mirrors, figures ranked front to back.
- 材质：silk, velvet, marble, crystal, silver, uniforms.
- 禁止漂移：no handheld, no modern interior, no daylight sitcom, no pastel, no digital skin, no empty ballroom without servants.
