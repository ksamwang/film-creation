---
name: eric-rohmer
title: 埃里克·侯麦 Éric Rohmer
style_file: ../directors/eric-rohmer.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, quiet French interior, medium two-shot across a table, 50mm at seated eye height, fixed camera or an almost imperceptible push, soft window daylight plus a table lamp, no dramatic side fill, books and wine glasses on a cloth, muted seasonal color, plain, talkative, restrained, unglamorous.

## 图像提示
- 主体 / 场景：two people talking across a dinner table; a woman alone at a beach-house window; a man and woman walking in a garden; a room with books and a folded newspaper.
- 景别 / 构图：medium shot and medium close-up, shot/reverse-shot by conversational turn, plain centered framing that does not interrupt speech; subject seated.
- 镜头 / 焦段：50mm, no compression, background readable, not dissolved into bokeh.
- 光线：window daylight plus practical table lamp; no dramatic side light; nothing stylized.
- 色彩：《慕德家一夜》black and white; later seasonal — summer white, autumn brown, winter grey; color marks time, never a postcard.
- 材质：books, tablecloth, wine glasses, summer clothes, sand, apartment furniture.

## 视频提示
- 镜头运动（只选一种）：fixed; the camera sits at the table and does not comment.
- 主体运动：talking, listening, gesturing for emphasis, standing to go to the window; no big physical action.
- 时长 / 帧率 / 运动模糊：8–15 seconds per conversational turn, 24fps, no motion blur, no speed ramp.

## 负面提示
no music punctuating conversation, no reaction close-up mid-speech, no camera commentary or comic insert, no debate-club rhetoric, no color flashback in the black-and-white film, no author's-eye-view, no causal explanation for coincidence, no postcard seasonal grade, no glamorous styling, no dramatic side light.

## 一致性锚点
- 色彩：black and white; or summer white / autumn brown / winter grey, muted.
- 镜头：50mm, （《慕德家一夜》）.
- 光线：window daylight plus table lamp, no side fill.
- 构图：medium shot/reverse-shot, table height, plain and non-intrusive.
- 材质：books, tablecloth, wine glasses, summer clothes, sand.
- 禁止漂移：no handheld, no drone, no shallow bokeh, no warm Instagram grade, no luxurious set, no music-video movement.
