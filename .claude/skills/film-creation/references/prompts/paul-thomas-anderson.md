---
name: paul-thomas-anderson
title: 保罗·托马斯·安德森 Paul Thomas Anderson
style_file: ../directors/paul-thomas-anderson.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, anamorphic widescreen, low camera angle, 35–50mm lens, staged Steadicam tracking through a real room, visible tungsten practical lamps, warm amber-brown 1970s palette or cool green-cream 1950s palette, wood paneling, carpet, pool water, film grain, bodies with weight, power written in who holds frame center.

## 图像提示
- 主体 / 场景：a performer or salesman mid-address in a wood-paneled room; two men across a table, one leaning in; a woman in a workroom lit by one lamp; a pool at night.
- 景别 / 构图：medium close-up and close-up on bodies with weight — sweat, breath, fabric folds; room and furniture stay legible behind the figure; the powerful sit at frame center, the failing are pushed to the edge or out.
- 镜头 / 焦段：35–50mm, wide for long-take rooms; 75–85mm only when someone is seen through.
- 光线：visible tungsten practicals as the key; window light as supplement; cold white only for institutional spaces; no sourceless soft light.
- 色彩：1970s orange-brown, or 1950s cool green and cream; per-film temperature, no single global filter.
- 材质：wood, carpet, pool water, wallpaper, fabric, sweat, 35mm grain.

## 视频提示
- 镜头运动（只选一种）：choreographed Steadicam follow — enter the door, circle the table, settle where the power settles.
- 主体运动：talking over each other, cooking, tailoring, swimming, performing; bodies doing real work, blocking planned in advance.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, minimal blur; hold the take through the discomfort instead of cutting.

## 负面提示
no handheld shake, no improvised camera, no cut to close-up at the emotional peak, no voice-over explaining relationships, no sourceless soft beauty lighting, no sepia nostalgia filter, no symmetrical static staging, no clean digital sharpness, no background reduced to bokeh.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：amber-orange and brown, or cool green and cream; medium saturation, film contrast.
- 镜头：35–50mm, wide for long takes.
- 光线：visible tungsten sources, window fill, no even wash.
- 构图：low angle, figure and room in the same frame, power holder centered.
- 材质：wood, carpet, pool water, wallpaper, fabric, film grain.
- 禁止漂移：no handheld documentary shake, no modern LED white, no digital skin, no empty minimalist interiors, no present-day devices.
