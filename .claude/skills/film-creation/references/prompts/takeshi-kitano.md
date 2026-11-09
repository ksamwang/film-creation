---
name: takeshi-kitano
title: 北野武 Takeshi Kitano
style_file: ../directors/takeshi-kitano.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Japanese minimalist crime drama, figures held small against a wide flat horizon, two-thirds of the frame left empty as sea or sky, fixed frontal 35mm deep focus keeping person and background equally sharp, flat overcast light with no modeling, cool blue grey white with a single small red accent, clean concrete and asphalt, no decoration, silent, deadpan, withheld.

## 图像提示
- 主体 / 场景：two men sitting on a beach, neither speaking; a man alone at the end of a pier; a child and an adult walking a long empty road; a bare concrete wall with one figure leaning on it.
- 景别 / 构图：full shot and medium, subject centered or pushed to one edge, background sea, sky, wall or road; only person, void and horizon; large blank area; props only if they carry the story.
- 镜头 / 焦段：35–50mm deep focus, no long-lens compression; person and background separated but both sharp.
- 光线：flat, overcast, no dramatic contrast, no rim light.
- 色彩：blue, grey, white, one small red accent; no warm nostalgia.
- 材质：sea, sky, asphalt, concrete wall, clean uncluttered surfaces.

## 视频提示
- 镜头运动（只选一种）：completely static frontal; the camera does not follow anyone who leaves frame.
- 主体运动：a figure walks out of frame; two people sit motionless; a sudden burst of violence occurs off-screen.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, minimal blur; hold the final shot one beat too long.

## 负面提示
no on-screen violence process, no long-lens compression, no dialogue explaining motive, no push-in at an emotional moment, no handheld camera, no fast cutting, no score under the whole film, no audible sobbing, no cool-gangster styling, no camera following the subject, no shallow depth of field, no warm filter, no dramatic chiaroscuro, no crowded set dressing.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：blue / grey / white plus one small red accent.
 - 镜头：35–50mm deep focus, fixed frontal.
 - 光线：flat overcast, no modeling.
 - 构图：person / void / horizon, large empty space, subject at center or edge.
 - 材质：sea, sky, asphalt, concrete.
- 禁止漂移：no drone, no handheld, no neon, no shallow bokeh, no warm grade, no busy set dressing, no lens flare.
