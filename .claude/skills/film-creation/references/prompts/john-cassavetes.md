---
name: john-cassavetes
title: 约翰·卡萨维茨 John Cassavetes
style_file: ../directors/john-cassavetes.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, handheld 16mm frame pressed close to a face, the face filling most of the image, background falling out of focus or blocked by a shoulder, available bulb or window light with unmodified grain in the shadows, unstable off-balance framing, sweat, smoke, cheap furniture, wrinkles, raw, exhausted, on the edge of breaking.

## 图像提示
- 主体 / 场景：a couple arguing across a cluttered kitchen table; a woman singing in a bar; friends crowded into a small apartment; a face caught between crying and laughing.
- 景别 / 构图：close-up and medium close-up, face filling the frame, background blocked or soft; subject may be cut in half by the frame edge; deliberately unbalanced, no clean composition.
- 镜头 / 焦段：35–50mm, close and very close; wide-angle distortion on a face is kept, not corrected.
- 光线：available light only — bulb, window, stage light; shadows keep their grain; no fill, no beauty light.
- 色彩：early black and white with coarse grain; later natural color, never a warm nostalgic grade.
- 材质：sweat, cigarette smoke, cheap furniture, wrinkles, 16mm grain, worn clothing.

## 视频提示
- 镜头运动（只选一种）：handheld follow, dragged by the actors, allowed to be blocked, lose focus and lag behind.
- 主体运动：arguing, overlapping speech, dancing, singing, breaking down; actors move freely and interrupt each other.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural handheld motion blur; do not cut away from the awkward silence.

## 负面提示
no stabilizer, no polished symmetrical composition, no soft beauty lighting, no score cue telling the audience to cry, no clean digital skin, no balanced two-shot, no tidy blocking, no shallow-focus glamour, no resolved ending frame.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：monochrome 16mm or ungraded natural color; high grain, no warm filter.
- 镜头：35–50mm, close-up dominant.
- 光线：available light, unmodified shadows.
- 构图：unstable, face-centered, subject may be cut off.
- 材质：sweat, smoke, wrinkles, worn fabric, 16mm grain.
- 禁止漂移：no gimbal smoothness, no HDR, no digital clarity, no modern apartment interiors, no fashion lighting.
