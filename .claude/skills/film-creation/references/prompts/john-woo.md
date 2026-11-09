---
name: john-woo
title: 吴宇森 John Woo
style_file: ../directors/john-woo.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic heroic-bloodbath film still, candlelit church with stained glass and drifting smoke, two men in long coats back to back, symmetrical low-angle medium shot, warm gold against cold blue, hard backlight rimming the figures, white doves, wax candles, one slow-motion beat, operatic, reverent, baroque.

## 图像提示
- 主体 / 场景：two gunmen in long coats inside a church, a killer and a cop facing each other; candles, a Virgin statue, drifting smoke; a man loading a pistol beside a stained-glass window.
- 景别 / 构图：medium and medium close-up, symmetrical, low angle, two-shot; props block half the body; figure made taller than life.
- 镜头 / 焦段：wide-angle close coverage and long-lens close-up, compressed then expanded.
- 光线：hard backlight, smoke, candlelight; deep shadow, no even fill.
- 色彩：warm gold against cold blue, split within the frame; no unified midtone grade.
- 材质：smoke, wax, stained glass, trench coats, white feathers.

## 视频提示
- 镜头运动（只选一种）：one slow low-angle orbit around the two figures during the ritual moment; no handheld.
- 主体运动：lighting a cigarette, handing over a gun, pushing a door, leaping, falling; gestures held and posed, then one burst of gunfire.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps base with a single 48fps slow-motion beat; motion blur only inside that beat.

## 负面提示
no unmotivated slow motion, no doves in every scene, no ironic anti-hero deconstruction, no realistic gore or forensic detail, no hero escaping unharmed, no handheld gunfight, no woman reduced to waiting only, no dialogue explaining brotherhood, no even studio fill, no desaturated realistic warfare.

## 一致性锚点
- 色彩：warm gold versus cold blue, split lighting, high contrast.
- 镜头：wide-angle close work plus long-lens close-up.
- 光线：backlight, smoke, candle flames, deep shadow.
- 构图：symmetrical, low angle, two-shot, props blocking half the body.
- 材质：smoke, wax, stained glass, trench coats, doves.
- 禁止漂移：no handheld shake, no digital-clean gunfire, no tactical realism, no muted grey grade.
