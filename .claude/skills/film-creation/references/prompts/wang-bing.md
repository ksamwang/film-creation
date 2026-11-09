---
name: wang-bing
title: 王兵 Wang Bing
style_file: ../directors/wang-bing.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic documentary still, derelict Chinese factory or bare dormitory, fixed extreme wide shot at eye level, a small figure in a corner swallowed by rusted machinery and concrete, unmodified available light, blown windows and crushed shadows, no fill, ungraded on-site color, 24mm wide lens, coarse 16mm grain, patient, unposed, witness.

## 图像提示
- 主体 / 场景：laid-off workers inside a stripped factory; a lone elderly person on a bare dormitory bed; a laborer mid-task in a coal yard; the environment occupies most of the frame.
- 景别 / 构图：extreme wide and full shot, eye level, subject pushed to a corner or edge; no golden-ratio composition, no heroic centering.
- 镜头 / 焦段：24–35mm wide to normal, fixed, deep focus.
- 光线：available light only; no fill, no shaped key; blown windows and crushed shadows are allowed.
- 色彩：ungraded on-site color, mixed cold and warm; never a uniform "misery grey".
- 材质：rust, coal dust, concrete, plastic sheeting, old quilts, bare wiring.

## 视频提示
- 镜头运动（只选一种）：static lock-off; movement only as a slow follow behind one continuous labor process, never toward a face.
- 主体运动：uninterrupted physical labor, eating, queuing, waiting, smoking; people eventually forget the camera and the everyday returns.
- 时长 / 帧率 / 运动模糊：30–60 seconds, 24fps, natural motion blur only, no stylized blur.

## 负面提示
no voice-over narration, no added score or ambient music bed, no held close-up of weeping, no fast montage compressing time, no fill light on faces, no directed blocking or retakes, no title cards, no uniform misery-grey grade, no poverty aesthetic, no handheld shake, no cutaway to summarizing symbols, no beautified decay.

## 一致性锚点
- 色彩：on-site color, ungraded, cold and warm mixed by location.
- 镜头：24–35mm, fixed, deep focus, or .
- 光线：available light, no fill, blown highlights and crushed shadows permitted.
- 构图：extreme wide, eye level, subject small in a corner, environment dominant.
- 材质：rust, coal dust, concrete, plastic sheeting, old quilts.
- 禁止漂移：no clean digital sharpness, no cinematic teal-orange grade, no drone coverage, no staged poverty.
