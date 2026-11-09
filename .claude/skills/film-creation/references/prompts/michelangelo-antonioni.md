---
name: michelangelo-antonioni
title: 米开朗基罗·安东尼奥尼 Michelangelo Antonioni
style_file: ../directors/michelangelo-antonioni.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, modernist alienation, wide 28mm deep focus, a lone figure pressed to the edge of the frame, two-thirds white wall glass and concrete, asymmetric negative space, back turned to camera, flat overcast light with no direction, desaturated grey-green and industrial red, fog, bare unfinished apartment, 35mm grain, emptied, suspended, cold.

## 图像提示
- 主体 / 场景：a bourgeois couple or a single woman in a bare modernist apartment, a port, a factory edge, a fogbound street; they stand apart and look in different directions.
- 景别 / 构图：wide shot first, architecture occupying two-thirds of the frame, the figure pushed to an edge or a corner; asymmetric, negative space, a corridor ending in one window. No face-first framing.
- 镜头 / 焦段：28–35mm wide with deep focus, people and building equally sharp; camera slightly above or below eye level at 5–8 meters.
- 光线：flat, diffuse, directionless overcast light; no dramatic contrast, no pools of shadow.
- 色彩：desaturated grey-green, concrete grey, industrial red as an environmental stain; or coarse black and white where rock and sea read harder than skin.
- 材质：white plaster, plate glass, raw concrete, unfinished surfaces, fog, dust on sills.

## 视频提示
- 镜头运动（只选一种）：static camera; at most a very slow lateral drift that reveals more empty space, never a push-in.
- 主体运动：figures drift, sit, smoke, look away; one person walks out of frame mid-conversation and the camera does not follow.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, minimal motion blur, long held stillness.

## 负面提示
no suspense plotting, no murder-mystery framing, no close-up emotional rescue, no dramatic chiaroscuro, no musical score, no neat symmetrical advertising composition, no sterile white-gallery emptiness, no fashion-editorial detachment, no explanatory dialogue scene, no character with a clear goal, no reconciled ending, no glossy architectural render.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：grey-green and concrete with industrial red; 28–35mm deep focus; flat overcast; asymmetry with building at two-thirds; plaster, glass, fog.
- 禁止漂移：no warm wood interiors, no golden-hour romance, no centered hero framing, no shallow-focus portrait, no modern glass towers with clean LED light, no crowd spectacle.
