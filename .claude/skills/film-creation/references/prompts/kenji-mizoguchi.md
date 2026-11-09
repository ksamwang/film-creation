---
name: kenji-mizoguchi
title: 沟口健二 Kenji Mizoguchi
style_file: ../directors/kenji-mizoguchi.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Japanese period tragedy, one continuous lateral tracking shot along a scroll-like horizontal axis, deep focus holding foreground, middle and far planes, a woman walking at the lower edge of the frame, vast wall, sky and mist above her, layered doorways, curtains and trees opening the space, soft fog-diffused light with no hard shadow, muted earth yellow indigo and dark red, silk and water, restrained, fated.

## 图像提示
- 主体 / 场景：a woman in kimono walking the full length of a corridor; a man crossing a foggy market and shrinking into the crowd; a mother and child at the edge of a field.
- 景别 / 构图：medium-long to long shot, figure pressed to the lower edge, large headroom of wall, sky or mist; a horizontal scroll axis with destinations left and right; deep focus; no centered single portrait.
- 镜头 / 焦段：35–50mm deep focus, camera slightly above seated height and below standing height.
- 光线：soft and foggy, low contrast, no hard edge; lantern or window light diffused through paper.
- 色彩：monochrome greys, or earth yellow, indigo and dark red; no vivid contrast.
- 材质：silk with visible folds, wood, paper, water, mist.

## 视频提示
- 镜头运动（只选一种）：one slow lateral track that follows the walking figure and never closes in; no cut inside the scene.
- 主体运动：a woman walks the full corridor, turns out of frame and re-enters from the other side; a man diminishes into a crowd; columns and curtains pass between lens and subject.
- 时长 / 帧率 / 运动模糊：8–12 seconds as a single take, 24fps, slight natural blur on the walking figure.

## 负面提示
no shot-reverse-shot, no push-in during a woman's suffering, no fast cutting, no handheld camera, no modern psychological dialogue, no decorative kimono-and-fog postcard, no ending in which a woman is rescued, no fragmenting one scene into separate spaces, no hard contrast film-noir light, no centered symmetrical single portrait, no close-up of tears, no shallow depth of field.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：greys, or earth yellow / indigo / dark red, low contrast.
 - 镜头：35–50mm deep focus, one scene one take.
 - 光线：soft fog-diffused, low ratio, no hard edge.
 - 构图：horizontal scroll, figure at the lower edge, headroom of wall and sky.
 - 材质：silk folds, wood, paper, water, mist.
- 禁止漂移：no drone, no handheld, no shallow focus, no modern costumes, no teal-and-orange, no crisp digital fog, no centered portrait.
