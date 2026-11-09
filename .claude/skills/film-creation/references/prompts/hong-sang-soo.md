---
name: hong-sang-soo
title: 洪常秀 Hong Sang-soo
style_file: ../directors/hong-sang-soo.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, deadpan Korean everyday comedy, flat available window light with blown-out highlights, static eye-level long lens, a man and a woman seated off-center with empty space between them, cheap plastic tablecloth and soju bottles, loose framing, natural color, awkward pause held.

## 图像提示
- 主体 / 场景：a film director and a younger woman at a cafe table with half-finished soju glasses; two people in winter coats walking a wet beach; a man talking too much while the woman looks at the window.
- 景别 / 构图：medium and medium wide; figures pushed to one side, large negative space, no symmetry, empty chair or table edge allowed to dominate; reframe rather than cut.
- 镜头 / 焦段：long end of a zoom, 85–200mm equivalent, compressing subject into the background so they cannot escape it.
- 光线：available light only, flat; window light may blow out; no shaping, no rim light, no fill.
- 色彩：natural everyday color, mildly cool; black-and-white only as a whole-film exception, never mixed within a shot.
- 材质：plastic tablecloth, soju bottle, concrete wall, wet coat, umbrella, old bookshop shelves.

## 视频提示
- 镜头运动（只选一种）：one slow zoom in (or out), mechanical and even, no cut, no track.
- 主体运动：small and unplanned — raising a glass, glancing away, an awkward laugh, a hand pushed through hair; no staged gesture.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, no motion blur, zoom speed constant.

## 负面提示
no dramatic event to drive the scene, no witty one-liners or aphorisms, no moral verdict from the camera, no zoom as showmanship, no polished lighting, no self-flattering male artist, no simple replay of a repeated scene, no black-and-white-plus-drinking cliché, no symmetrical composition, no score, no shallow-focus beauty shot.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：natural muted color, 85–200mm long lens; flat available window light with allowed overexposure; off-center figures with wide negative space; plastic tablecloth, soju bottle, concrete, wet coat.
- 禁止漂移：no cinematic teal grade, no anamorphic flare, no dolly or handheld drift, no glossy production design, no symmetry, no subtitle-style text in frame.
