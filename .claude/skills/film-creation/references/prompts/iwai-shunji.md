---
name: iwai-shunji
title: 岩井俊二 Shunji Iwai
style_file: ../directors/iwai-shunji.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, a snowfield at dusk, a girl in a dark coat standing far off, backlit by a low overexposed sky with one specific pale sun, 35mm wide, vast negative space, cream-white and faded pink memory palette, blown highlights, a lace curtain in the near foreground, soft film grain, a letter read to someone absent, tenderness already turning into recollection.

## 图像提示
- 主体 / 场景：a girl standing alone in a snowfield or wheat field; a hand holding an envelope near a window; a classroom lit by green fluorescent tubes; a figure cycling past a corridor window; a CRT monitor or miniDV camera on a desk.
- 景别 / 构图：extreme wide landscape or extreme close-up of a hand, ear, envelope; no stable medium two-shot; composition either leaves vast empty space or pushes the object to the frame edge.
- 镜头 / 焦段：24–35mm for snowfield and wheat field; 85–135mm for hands, ears, envelopes; long lens isolates the media object.
- 光线：backlight first; window, snowfield, sea, corridor window as a specific source; highlights may blow out, but never without a source.
- 色彩：memory set — cream white, pale green, faded pink; present set — cold cyan, fluorescent green, screen blue; do not blend the two in one shot.
- 材质：lace curtain, plastic raincoat, CRT monitor, miniDV tape, school desk, snow.

## 视频提示
- 镜头运动（只选一种）：slow lateral tracking at walking pace alongside the subject; no push-in, no handheld unless the shot is explicitly DV.
- 主体运动：a girl walks through snow, breath visible, holding a letter; a hand turns an envelope; a figure cycles away from camera; no running in slow motion.
- 时长 / 帧率 / 运动模糊：6–8 seconds, 24fps, gentle natural blur, no slow motion, no speed ramp.

## 负面提示
no backlight with cherry blossoms, white dress and piano all at once, no overexposure without a specific light source, no face-to-face confession spoken to completion, no push-in on a reunion, no piano while a character cries, no lyrical score over violence, no clean bright classroom, no slow-motion running or falling sakura, no sweet unrequited love without misrecognition or cost, no adult explaining youth.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：cream white, pale green, faded pink, or cold cyan and screen blue / 24–35mm wide, 85–135mm detail, or / backlight with a named source, blown highlights allowed / vast negative space or extreme close-up, no medium two-shot / lace, plastic raincoat, CRT, miniDV.
- 禁止漂移：no modern smartphone, no crisp 4K digital skin, no drone snowscape, no warm golden filter, no music-video gloss.
