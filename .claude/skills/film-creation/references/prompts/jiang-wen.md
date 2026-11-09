---
name: jiang-wen
title: 姜文 Jiang Wen
style_file: ../directors/jiang-wen.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1970s Beijing rooftops or wartime village, 24–35mm wide lens close to the face so it distorts, hard noon sunlight and dust backlight, high-saturation red-yellow-brown in the historical section, desaturated grey-green in the private section, tilted and off-balance framing, half a face blocked, sweat-stained uniform, chipped rifle, open space to run through, loud, kinetic, unreliable.

## 图像提示
- 主体 / 场景：young men running across a rooftop at noon; a crowd at a village feast; two men facing off across a table; a figure standing on a city wall.
- 景别 / 构图：wide close-up at 24–35mm pushing into faces; diagonal lines, cut edges, half the face blocked; open space so bodies can run; composition may break the rules but must carry force.
- 镜头 / 焦段：24–35mm for group and confrontation; 50mm for solitude, letting the figure recede from the environment.
- 光线：hard light, straight noon top light not avoided, backlight through dust; night by warm yellow bulbs, never cold blue.
- 色彩：historical sections saturated red, yellow and brown; private sections desaturated grey-green; do not grade the whole film warm orange.
- 材质：sweat-stained uniforms, chipped rifles, cracked bicycle saddles, sorghum, dust.

## 视频提示
- 镜头运动（只选一种）：handheld or Steadicam follow-run, camera inside the group, no cut; keep the subject and at least two other bodies in frame.
- 主体运动：running, shouting, grabbing, laughing, shoving; performances overlap and compete for the frame.
- 时长 / 帧率 / 运动模糊：4–8 seconds for kinetic shots, 10–15 seconds for the static tonal shift, 24fps, real motion blur.

## 负面提示
no oily swagger without a humiliating beat, no woman existing only as spectacle, no fast cutting hiding weak staging, no dialogue as a joke reel, no correct verdict on history, no imitation of the accent, no shouting in every scene, no slow-motion lyricism, no clean digital grade, no symmetrical hero framing.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：saturated red-yellow-brown historical, grey-green private; 24–35mm close wide; hard noon sun and dust backlight, warm tungsten night; diagonal tilted framing, subject on high ground; sweat, chipped paint, sorghum.
- 禁止漂移：no clean HDR, no drone, no modern glass, no cool blue night, no digital skin.
