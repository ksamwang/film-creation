---
name: carlos-reygadas
title: 卡洛斯·雷加达斯 Carlos Reygadas
style_file: ../directors/carlos-reygadas.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, a Mexican highland before dawn, a heavy man kneeling in wet grass, low 18mm camera at knee height, his body small in the lower third, a huge grey sky and treetops filling the top, unmodified blue-gold dawn, mud, sweat, animal fur, slight wide-angle distortion, coarse grain, devotional patience, nobody in the frame is being judged.

## 图像提示
- 主体 / 场景：a farmer kneeling in a wet field at first light; a city man walking into a mountain village, his body losing its edges in mud and mist; a couple sitting apart in a bare room, neither speaking.
- 景别 / 构图：extreme wide or tight close-up, little in between; figure in the lower third; headroom given to sky, treetops or ceiling; low camera, never looking down.
- 镜头 / 焦段：18–28mm wide with slight distortion; 50mm for skin close-ups; scale difference is the point.
- 光线：natural light only; window light, overcast dawn, late sun; no golden-hour beautification, no fill.
- 色彩：earth yellow, grass green, grey; unmodified dawn and dusk color temperature; no high saturation, no monochrome filter.
- 材质：mud, grass, sweat, animal fur, glass reflection.

## 视频提示
- 镜头运动（只选一种）：static camera fixed low, waiting; no pan, no dolly.
- 主体运动：a man kneels, breathes, waits; wind moves the grass; an animal crosses; someone enters the frame from a distance and keeps walking; no staged emotion.
- 时长 / 帧率 / 运动模糊：10–15 seconds, 24fps, natural motion blur, no slow-motion emphasis.

## 负面提示
no emotional score swell, no clear moral position, no fast cutting in violence or sex, no high-angle or overhead, no golden-hour postcard grade, no professional actor emoting, no explanatory dialogue, no reconciliation ending, no clean digital sharpness, no religious imagery used as an answer.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：earth yellow, grass green, grey / 18–28mm wide, / natural, no fill, no golden hour / low camera, figure lower third, sky headroom / mud, grass, sweat, fur.
- 禁止漂移：no aerial drone, no HDR landscape, no warm filter, no glossy skin, no modern architecture.
