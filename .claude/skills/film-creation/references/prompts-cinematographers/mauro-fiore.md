---
name: mauro-fiore
title: 毛罗·菲奥雷 Mauro Fiore
style_file: ../cinematographers/mauro-fiore.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Saturated digital action film still, hard low-angle sunlight, strong rim light, deep clean blacks, orange amber and cyan and magenta color blocks, wide 24mm lens close to the body, kinetic framing, anamorphic flare, sweat and metal, high contrast, fine digital grain, graphic, muscular, poster-like.

## 图像提示
- 主体 / 场景：a body in motion on a street, rooftop, desert, or aircraft deck; environment readable as a stage for action.
- 景别 / 构图：wide action master or tight medium; subject centered or on a third, background divided into color blocks, foreground occlusion.
- 镜头 / 焦段：18–35mm wide-angle for action; 50–85mm for portraits; slight edge stretch allowed.
- 光线：hard side or back sun, fire, neon, practical lamps; ratio –; highlights may clip.
- 色彩：saturated orange, cyan, magenta, gold; clean blacks, strong separation, no grey wash.
- 材质：metal, glass, sweat, smoke, dust, fine digital grain.

## 视频提示
- 镜头运动（只选一种）：low-angle tracking shot following the body.
- 主体运动：running, turning, or stepping into frame; the camera keeps pace with the torso.
- 时长 / 帧率 / 运动模糊：4–8 seconds, 24fps, strong natural motion blur, no slow-motion hero shot.

## 负面提示
no desaturated grey, no muted palette, no telephoto compression, no soft fill light, no dirty shadows, no unmotivated orbit, no blue-orange LUT, no flat lighting, no clean digital skin, no empty frame, no static camera.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：saturated orange, cyan, magenta; 18–35mm wide; hard rim at –; centered or third-placed body with color-blocked background; metal, sweat, grain.
- 禁止漂移：no grey LUT, no soft beauty light, no long-lens distance, no HDR clean skin, no pastel palette.
