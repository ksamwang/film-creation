---
name: ang-lee
title: 李安 Ang Lee
style_file: ../directors/ang-lee.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, restrained family drama, beige grey and navy palette, a single window light from the side, interior corners kept dark, a long dining table with porcelain bowls and rising steam, figures seated in careful social positions, door frames and corridors cutting some of them out of frame, slightly off-axis formal composition, standing eye-level camera, quiet, withheld, polite.

## 图像提示
- 主体 / 场景：a multi-generation family at a long dinner table, the father at the head seat, a son who has just arrived; a widowed father cooking alone in a tight kitchen; a corridor outside a wedding banquet.
- 景别 / 构图：wide or medium-wide full view of the table, seats and dishes readable in one frame; formal near-symmetry with the axis slightly off; door frames and corridor edges block part of the group; no shot-reverse-shot.
- 镜头 / 焦段：35–50mm at standing eye level; 85–135mm compression only for distant, repressed exchanges.
- 光线：window light as the single source, interior not filled, corners left dark; no rim light.
- 色彩：beige, grey and navy as the base; red and gold enter only when desire breaks the surface.
- 材质：porcelain bowls, steam, worn wooden door, heavy curtain, tablecloth with a thin sheen.

## 视频提示
- 镜头运动（只选一种）：static at standing eye level; at most one slow lateral pan to re-read the seating.
- 主体运动：seated, passing dishes, raising a glass, a hand pausing mid-air; someone rises and walks out of frame at the emotional peak.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, minimal motion blur, classical continuity.

## 负面提示
no handheld camera, no zoom lens, no shot-reverse-shot across the dinner table, no close-up push-in at the emotional peak, no tearful close-up, no voice-over explaining cultural difference, no exotic "oriental" music cue, no comic conservative elders, no flat expressionless acting, no centered symmetrical hero framing, no warm nostalgia filter, no high-key even lighting, no fully saturated grade, no resolved reconciliation ending.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：beige / grey / navy base, low saturation; red and gold reserved for loss of control.
 - 镜头：35–50mm, standing eye level, static.
 - 光线：single window source, unfilled interior, dark corners.
 - 构图：formal and slightly off-axis, door frame or corridor cutting the group, table seating readable.
 - 材质：porcelain, steam, worn wood, curtain fabric.
- 禁止漂移：no modern glass office, no LED white, no handheld vérité, no drone shot, no glossy digital skin, no teal-and-orange grade.
