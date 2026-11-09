---
name: martin-scorsese
title: 马丁·斯科塞斯 Martin Scorsese
style_file: ../directors/martin-scorsese.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 24–35mm wide angle, handheld at eye level inside a crowd, saturated red blue and green night, neon signage and practical car lights, smoke, street grime, off-balance crowded framing, foreground shoulders blocking the frame, visible 35mm grain, kinetic, guilty, confessional.

## 图像提示
- 主体 / 场景：a cab driver alone at the wheel on a wet neon street; a group of men at a bar table, all talking at once; a boxer in the ring under flashbulbs. The subject is surrounded, never isolated against a clean background.
- 景别 / 构图：medium close-up inside a crowd; off-balance, crowded, non-symmetrical; foreground shoulders and heads cut the frame; no clean single.
- 镜头 / 焦段：24–35mm wide angle, handheld; long lens only to isolate a character from the group.
- 光线：neon sign, storefront, headlights, practical interior lamps; darks retained, no even fill, no studio key.
- 色彩：saturated red, blue and green in night exteriors; film grain visible; no pastel grade.
- 材质：smoke, wet glass, neon tube, old brick, scuffed bar wood, street signage.

## 视频提示
- 镜头运动（只选一种）：handheld follow through a crowd — the camera stays at eye level and pushes in when someone speaks.
- 主体运动：characters talk over each other, walk through a back corridor, gesture broadly; the camera catches a look that was not planned.
- 时长 / 帧率 / 运动模糊：6–12 seconds, 24fps, slight handheld motion blur; keep the frame breathing, never locked.

## 负面提示
no steadicam smoothness, no symmetrical clean framing, no orchestral score cueing emotion, no complete redemption arc, no bloodless violence, no artificial period filter, no flat even lighting, no empty negative space, no digital skin, no static tripod framing, no polite non-overlapping dialogue staging, no cool blue-only grade.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：saturated red blue green night with 35mm grain, 24–35mm handheld at , neon and practical sources with retained darks, crowded off-balance framing with foreground obstruction, smoke and wet glass.
- 禁止漂移：no anamorphic clean look, no teal-orange blockbuster grade, no tripod symmetry, no drone, no digital sharpness, no period costume-drama polish.
