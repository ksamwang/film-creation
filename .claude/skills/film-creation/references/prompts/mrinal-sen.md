---
name: mrinal-sen
title: 姆里纳尔·森 Mrinal Sen
style_file: ../directors/mrinal-sen.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Grainy black-and-white Bengali political modernism, 1970s Calcutta, handheld 28–50mm, available window and street light, underexposed shadows with texture, frontal flat compositions, people standing in rows facing the camera, dust sweat cotton and old newspaper, freeze-frame, documentary urgency, no beautiful poverty.

## 图像提示
- 主体 / 场景：an unemployed clerk, a student, a villager standing in a cramped office or rubble-strewn lane, several people behind him facing the lens like a roll call.
- 景别 / 构图：hard cut between close-up and extreme wide, no medium transition; frontal, flat, tableau-like; figures in rows, camera at chest height.
- 镜头 / 焦段：28–50mm wide, close enough to crowd the body with walls; long lens only for spying into a rich man's window.
- 光线：available light only — window, streetlamp, kerosene; allow underexposure and blocked shadows, no fill.
- 色彩：coarse black and white, heavy grain; later color films use ochre, grey-green, rust red, low saturation.
- 材质：dust, sweat, cotton, old newspaper, concrete, cheap paper.

## 视频提示
- 镜头运动：handheld whip pan, one move only, sweeping across a crowd and stopping on a face or a number.
- 主体运动：people stand still and speak to the lens; someone turns away mid-sentence; no choreographed movement.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, coarse grain, smear on the pan, no slow motion.

## 负面提示
no beautiful poverty, no sympathetic close-up, no classical continuity, no sentimental score, no soft fill light, no warm nostalgia, no clean digital image, no single omniscient narrator, no closed family ending.

## 一致性锚点
- 色彩：coarse black and white, heavy grain, crushed but textured shadows.
- 镜头：28–50mm handheld, chest height.
- 光线：available window and street light, underexposed, no fill.
- 构图：frontal tableau, rows of people, direct address, no frame-within-frame comfort.
- 材质：dust, sweat, cotton, newspaper, concrete.
- 禁止漂移：no digital clarity, no warm sepia, no shallow bokeh, no smooth gimbal, no modern glass architecture.
