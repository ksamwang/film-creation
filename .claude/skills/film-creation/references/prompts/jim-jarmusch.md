---
name: jim-jarmusch
title: 吉姆·贾木许 Jim Jarmusch
style_file: ../directors/jim-jarmusch.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, fixed wide shot held at human eye level, figure placed slightly below center with large empty air above, 35–50mm lens, flat available light from a bulb or window, no dramatic shadow, low-saturation blue, green and brown or grainy black and white, old car, cheap jacket, wall graffiti, patient, deadpan, unglamorous.

## 图像提示
- 主体 / 场景：two people sharing a motel room or a car; a man alone at a diner counter; an empty street with one streetlamp; a musician with an instrument in a bare room.
- 景别 / 构图：fixed full shot, figure slightly below center, lots of air above; off-balance but calm; nobody is centered, the center stays empty.
- 镜头 / 焦段：35–50mm, rarely long lens; distance between person and environment stays readable.
- 光线：flat available light — a bulb, a window, a streetlamp; no dramatic shadow, no motivated beauty.
- 色彩：early black and white; later low-saturation blue, green, brown; never saturated.
- 材质：old car, cheap jacket, worn diner booth, wall graffiti, cigarette smoke, cheap coffee cup.

## 视频提示
- 镜头运动（只选一种）：locked static frame, holding a few seconds after the subject walks out of shot.
- 主体运动：sitting, smoking, drinking coffee, walking slowly, waiting; no plot-driven action.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, no motion blur; let the pause run past comfort.

## 负面提示
no handheld energy, no fast cutting, no dramatic lighting, no saturated color, no non-diegetic score swell, no postcard America, no centered hero portrait, no punchline framing, no shallow-focus emotional close-up.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：desaturated blue, green, brown; or monochrome; low contrast.
- 镜头：35–50mm, fixed.
- 光线：flat available light, no dramatic shadow.
- 构图：human eye level, figure low-center, large empty space.
- 材质：old car, worn fabric, graffiti, smoke, film grain.
- 禁止漂移：no drone shots, no neon glamour, no clean digital sharpness, no modern luxury interiors, no music-video slow motion.
