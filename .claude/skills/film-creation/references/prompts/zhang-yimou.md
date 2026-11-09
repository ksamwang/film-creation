---
name: zhang-yimou
title: 张艺谋 Zhang Yimou
style_file: ../directors/zhang-yimou.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, one dominant colour per scene — saturated red, black, gold or pure grey — symmetrical composition locked to a central axis of gate, road or queue, arrays of lanterns, drums or banners filling the frame, extreme wide shot making the figure a small block of colour, hard backlight rimming dust and smoke, 24–35mm keeping verticals straight, ritual, geometric, severe.

## 图像提示
- 主体 / 场景：a bride under a sedan chair; rows of lanterns in a courtyard; a single figure crossing a vast loess field; an archer formation on a wall.
- 景别 / 构图：extreme wide to establish scale plus extreme close-up on hand, eye or sweat; symmetric central axis of door, road or queue; arrays fill the frame; the figure sits on the axis or is cut by it.
- 镜头 / 焦段：24–50mm, straight verticals, no long-lens compression.
- 光线：hard light, backlight rim, dust and smoke make the beam visible; never flatten daylight or lose shadow.
- 色彩：one dominant hue per scene — red, red-and-black, black-white-grey, gold; no second competing colour.
- 材质：red cloth, silk, loess, snow, blood, rain, lacquered lanterns.

## 视频提示
- 镜头运动（只选一种）：lateral tracking across the array, or a dolly through a gate into the power centre, or a crane up reducing the figure to a point.
- 主体运动：synchronized group action — carrying, beating drums, kneeling, marching; individual gesture compressed, then released in one movement.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, slow motion only for one ritual action per scene, otherwise crisp.

## 负面提示
no red-and-gold for every film, no folk ritual forced into a contemporary urban story, no slow motion as a substitute for emotion, no symmetrical postcard, no moral awakening for power, no crowd used as wallpaper, no voice-over explaining symbols, no flat daylight without shadow, no handheld, no zoom.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：one dominant hue per scene with arrays; 24–35mm; hard backlight with dust; symmetric central axis, extreme wide plus extreme close; red cloth, silk, loess, snow, lantern.
- 禁止漂移：no candy-colour multicast, no modern glass, no LED white, no handheld documentary look, no scattered random crowd.
