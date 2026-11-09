---
name: king-hu
title: 胡金铨 King Hu
style_file: ../directors/king-hu.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic wuxia film still, Ming-era timber inn or bamboo forest, layered deep space with foreground branches, mid-ground figures and misted mountains behind, wide static medium-long shot, backlight and fog, earth yellow, ink green and lime white, weathered wood, bamboo, old cloth, poised before motion, 1970s film grain.

## 图像提示
- 主体 / 场景：a swordsman and a swordswoman facing each other across a timber inn; a lone figure at the end of a bamboo corridor; monks and guards distributed through a temple courtyard.
- 景别 / 构图：medium-long and far shot; foreground branches, mid-ground figures, background mist; columns, stairs and doorframes cut the frame; no close-up for emotion.
- 镜头 / 焦段：wide to medium, deep focus, static.
- 光线：backlight through fog, window-lattice light, dark interior; no flat fill on faces.
- 色彩：earth yellow, ink green, lime grey; muted, not vivid.
- 材质：weathered timber, bamboo, brick, old cloth, worn costumes, hanging curtains.

## 视频提示
- 镜头运动（只选一种）：static lock-off through the standoff, releasing into one abrupt whip pan on the strike cue; no continuous movement.
- 主体运动：a cup drops, a curtain lifts, swordsmen hold still then explode into short edited leaps; motion is broken by cuts, not floated on wires.
- 时长 / 帧率 / 运动模糊：3–5 seconds per beat, 24fps, no slow motion.

## 负面提示
no slow-motion combat, no wire-assisted floating replacing editing and blocking, no blood spray or severed limbs, no handheld shake, no modern psychology for villains, no comic relief inside fights, no CGI misty mountains, no invincible hero against numbers, no crisp new costumes, no flat frontal fill lighting.

## 一致性锚点
- 色彩：earth yellow, ink green, lime grey; muted saturation.
- 镜头：wide to medium, deep focus.
- 光线：backlight, fog, window-lattice; faces not evenly lit.
- 构图：three planes — foreground branches, mid-ground figures, background mist; columns cut the frame.
- 材质：weathered timber, bamboo, brick, old cloth.
- 禁止漂移：no wire-fu floating, no digital fog, no glossy new costumes, no modern inn furniture.
