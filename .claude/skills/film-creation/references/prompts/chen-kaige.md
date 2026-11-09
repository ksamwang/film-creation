---
name: chen-kaige
title: 陈凯歌 Chen Kaige
style_file: ../directors/chen-kaige.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 20th-century China, low camera angle looking up at a believer, 50–85mm compressing sky, earth and figure into one plane, earth-yellow and blue-grey base with a gold-red ritual accent, hard light through smoke and light shafts, backlit silhouette rather than a lit face, deep stage-like space through a gate or corridor, loess, brick, old opera costume, solemn, theatrical.

## 图像提示
- 主体 / 场景：an opera performer in full stage makeup; a scholar standing on a vast plateau; a figure alone in a palace corridor; a crowd watching a stage.
- 景别 / 构图：wide to establish sky-earth-human layers, then medium to hear the speech; symmetrical deep staging through gate, corridor or stage; solo monologue placed to one side with empty space pressing on him.
- 镜头 / 焦段：50–85mm, compressing sky and ground onto the figure.
- 光线：hard light through smoke with visible shafts; backlight outlines the body, face not fully lit.
- 色彩：earth yellow and blue-grey ground, gold-red for ritual scenes; no candy saturation.
- 材质：loess, brick, old opera costumes, snow, sweat, stage boards.

## 视频提示
- 镜头运动（只选一种）：a crane rising from ground to sky (or descending), or a lateral sweep across a crowd and years; during the monologue the camera is locked off.
- 主体运动：declarative stage movement — turning on a line, kneeling, singing; the body follows the sentence.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, no slow motion unless ritual, no handheld.

## 负面提示
no every-shot-as-poster, no voice-over summarising the theme, no slogan lines without backstory, no history reduced to good versus evil, no overused smoke and light shafts, no monologue over three minutes without action, no worldly happy ending for the idealist, no handheld, no zoom, no modern glass architecture.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：earth yellow and blue-grey with gold-red ritual accent; 50–85mm; hard backlight through smoke; low angle for the believer, deep stage staging; loess, brick, opera costume, snow, sweat.
- 禁止漂移：no modern glass, no LED white, no clean digital face, no handheld, no symmetrical postcard for every shot.
