---
name: edward-yang
title: 杨德昌 Edward Yang
style_file: ../directors/edward-yang.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic urban film still, 1990s Taipei office or apartment, fixed wide-angle deep-focus shot, figures separated by glass partitions and window frames, cool grey-blue fluorescent light, flat overhead illumination, architectural lines cutting across faces, symmetrical framing, analytic, precise, no handheld, city as grid.

## 图像提示
- 主体 / 场景：a family at a dinner table in a glass-walled apartment; office workers divided by partitions; a teenager in a school corridor; two people in the same frame but unable to reach each other.
- 景别 / 构图：medium-wide and full shot, symmetrical, framed, deep focus; architectural lines slice across the face; person and space carry equal weight.
- 镜头 / 焦段：wide-angle, deep depth of field, static.
- 光线：flat fluorescent overhead; domestic warmth flattened by daylight tubes; no soft warm key.
- 色彩：cool grey-blue for offices, hospitals and night; warm only at home but held flat; no unified midtone.
- 材质：glass, curtain wall, corridor tile, neon, office partitions.

## 视频提示
- 镜头运动（只选一种）：fixed camera, one slow lateral pan to re-frame the group; never a push-in or handheld.
- 主体运动：people talking, arguing, moving between rooms, sitting in separate compartments; restrained gestures, no big emotional display.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, no stylized motion blur.

## 负面提示
no handheld shake, no warm nostalgia filter, no postcard city skyline, no score judging the characters, no sentimental close-up, no content-free poetic dialogue, no coincidence resolving threads, no violence as spectacle, no shallow focus, no soft warm fill.

## 一致性锚点
- 色彩：cool grey-blue, fluorescent-flat; warm domestic light held down.
- 镜头：wide-angle, deep focus.
- 光线：flat overhead fluorescent, visible fixtures, minimal fill.
- 构图：symmetrical, glass and frame divisions, lines crossing the face, person and space equal.
- 材质：glass, curtain wall, corridor tile, neon.
- 禁止漂移：no handheld, no shallow depth, no warm grade, no glass-tower glamour, no emotional close-up.
