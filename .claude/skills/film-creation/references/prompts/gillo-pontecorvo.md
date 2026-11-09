---
name: gillo-pontecorvo
title: 吉洛·蓬泰科尔沃 Gillo Pontecorvo
style_file: ../directors/gillo-pontecorvo.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s black-and-white newsreel, Algiers casbah street, a crowd pressed into a narrow staircase, handheld camera at chest height inside the crowd, hard North African sun and deep shadow, white burnous and khaki uniforms, plaster walls, dust, coarse 16mm grain, urgent, tactical, unsentimental.

## 图像提示
- 主体 / 场景：guerrillas moving through a casbah alley, women carrying baskets, paratroopers at a checkpoint, a cell meeting by bare bulb; a staircase, rooftop, narrow street, interrogation room.
- 景别 / 构图：medium and wide to show the geometry of the street; close-up only for one face in the crowd or a hand placing a charge; no lone-hero portrait. Diagonal, layered composition, foreground crowd, readable exits, high ground and blocked ground visible in the same frame.
- 镜头 / 焦段：28–50mm inside the crowd and the alley; 100–200mm from a rooftop for surveillance and ambush; no shallow beauty focus.
- 光线：available light — hard North African sun, bare bulbs, night flares; faces half in shadow; no studio fill.
- 色彩：black-and-white newsreel grain, hard contrast; later colour uses earth, khaki, dark red; no glamour grade.
- 材质：plaster, stone steps, uniforms, newspapers, megaphones, sweat, dust, coarse wool.

## 视频提示
- 镜头运动（只选一种）：handheld follow through the casbah crowd, matching the pace of the group, no cutaways.
- 主体运动：people climbing stairs, passing a package, running around a corner, stopping at a checkpoint; the group moves as one body.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, natural handheld blur; keep the frame crowded, never isolate the walker.

## 负面提示
no glamorous monochrome, no slow-motion violence, no lone-hero close-up, no cartoon villain, no studio crowd, no clean digital sharpness, no sentimental score, no voice-over explanation, no symmetrical composition, no anonymous masses, no drone beauty shot, no modern city.

## 一致性锚点
- 色彩：black-and-white newsreel, hard contrast, coarse grain; colour only earth, khaki, dark red.
- 镜头：28–50mm crowd and alley, 100–200mm rooftop surveillance; .
- 光线：available hard sun, bare bulb, flare; faces half-lit.
- 构图：diagonal, layered, foreground crowd, exits and high ground readable.
- 材质：plaster, stone, uniforms, newspapers, megaphones, dust.
- 禁止漂移：no colour grade, no shallow focus, no clean digital skin, no modern weapons, no studio set, no hero framing.
