---
name: claire-denis
title: 克莱尔·德尼 Claire Denis
style_file: ../directors/claire-denis.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, extreme close-up of skin and sweat in backlight, low camera at floor or bed height, 85mm isolating a shoulder and breath, night exterior lit by neon and dying ember orange, hard practical light with deep colored shadows, uniform fabric and dust, no establishing wide, body cropped by the frame, sensual, tense, unexoticized.

## 图像提示
- 主体 / 场景：a soldier's shoulder in a barracks doorway; a woman standing in a dusty yard at dusk; bodies on a dance floor; a hand against a metal railing.
- 景别 / 构图：extreme close-up of skin, sweat, fabric; or a medium shot with no spatial establishment; body cropped by the frame; low or high angle pressing the body to ground or floating in light.
- 镜头 / 焦段：wide-angle pulls the body into space; 85mm keeps only skin and breath; switch abruptly.
- 光线：practical light and backlight, large interior/exterior ratio, shadows retain color rather than dead black.
- 色彩：colonial white, blood red, earth yellow; night adds neon and dying ember orange, not a warm hearth.
- 材质：skin, sweat, uniform, iron, dust, plastic curtain.

## 视频提示
- 镜头运动（只选一种）：handheld follow synced to desire — press close, then stop dead; move away when violence begins.
- 主体运动：walking, carrying, dancing, lying still; bodies act rather than speak.
- 时长 / 帧率 / 运动模糊：5–10 seconds, 24fps, natural handheld blur, no stabilization, no speed ramp.

## 负面提示
no dialogue explaining colonial history, no music that explains desire, no complete on-screen violence, no anthropological establishing shot, no warm nostalgic grade, no body-as-landscape, no soft-focus eroticism, no voice-over explaining psychology, no dialogue stating relationships, no clean gimbal move, no exotic percussion cue.

## 一致性锚点
- 色彩：white / red / earth yellow; night neon and ember orange.
- 镜头：wide-angle ↔ 85mm.
- 光线：practical plus backlight, big ratio, colored shadows.
- 构图：extreme close-up against a non-establishing medium, low camera, body cropped.
- 材质：skin, sweat, uniform, iron, dust.
- 禁止漂移：no drone, no clean establishing wide, no warm filter, no soft-focus skin, no stabilized gimbal.
