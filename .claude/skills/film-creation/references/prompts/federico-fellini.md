---
name: federico-fellini
title: 费德里科·费里尼 Federico Fellini
style_file: ../directors/federico-fellini.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s Italian carnival dreamscape, centered radial composition around a circular piazza, crowd filling all four corners, one face pushing out of the mass, saturated red white and gold against cheap painted posters, frontal hard light turning faces into exhibits, night scenes dissolved in fog and backlight, plaster masks, wigs, paper-mâché, wet cloth, 35mm film grain, theatrical, grotesque, tender.

## 图像提示
- 主体 / 场景：a crowd arranged as a ceremony — a piazza, a circus ring, a family dinner, a casting session; a single sweating face squeezed out of the group, not a clean two-shot.
- 景别 / 构图：extreme wide to establish the ritual, then cut straight to a face; no medium-shot bridge. Centered radial composition, crowd fills the corners, face emerges from the mass.
- 镜头 / 焦段：35–50mm wide and close to the bodies; 75–100mm only when the camera stops on one face. Camera at eye level or slightly low, as if standing inside the crowd.
- 光线：frontal hard light that makes the face an exhibit; night scenes in large fog and strong backlight that turn the street into a set.
- 色彩：saturated red, white, gold against cheap poster color; fog blue in night scenes; no naturalistic soft midtones.
- 材质：plaster masks, false hair, paper-mâché, painted canvas flats, wet cloth, condensation, film grain.

## 视频提示
- 镜头运动（只选一种）：slow circular tracking that orbits the crowd, then stops dead on one face and holds.
- 主体运动：people pressing toward the center, gesturing broadly, turning to the lens; the stopped face holds still while the crowd keeps moving.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, natural motion blur, no step-printing.

## 负面提示
no soft focus, no warm nostalgia filter, no sepia, no even fill light, no naturalistic muted midtones, no generic circus collage of clowns and brass bands, no grotesque-for-shock, no dehumanized spectacle bodies, no clean symmetrical two-shot, no handsome idealized director stand-in, no dream-haze overlay, no resolved ending tableau.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：saturated red-white-gold with fog blue at night; 35–50mm wide; frontal hard key; centered radial crowd with the face emerging; plaster, wig, painted canvas.
- 禁止漂移：no even studio lighting, no soft beauty light, no clean modern interiors, no digital skin, no tasteful muted palette, no empty frame without a crowd.
