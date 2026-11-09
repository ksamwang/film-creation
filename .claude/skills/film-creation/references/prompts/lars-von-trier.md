---
name: lars-von-trier
title: 拉斯·冯·提尔 Lars von Trier
style_file: ../directors/lars-von-trier.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, artificial confession, a woman's face half a metre from a jittering 28mm handheld lens, frame tilted, background smeared by motion, cold blue and sick green, blown highlights, raw digital noise, or the opposite: a flat frontal stage with chalk lines for walls, centred 50mm, theatrical light falling visibly from above, devotional, punishing, self-indicting.

## 图像提示
- 主体 / 场景：a woman on a bare stage, a mother in a hospital corridor, a bride at a flooded altar; a town drawn in chalk on a black floor, an oil-painted sky, a hospital bed.
- 景别 / 构图：either an uncomfortable close-up at half a metre from the face, off-centre and tilted; or a flat frontal stage composition with no depth, centred and symmetrical. Never naturalistic depth.
- 镜头 / 焦段：handheld 25–35mm wide pressed to the face; static passages at 50–85mm, camera squared to the stage like a painting.
- 光线：natural light that reveals its own arrangement, or theatrical stage light visibly falling from above; never invisible even light.
- 色彩：cold blue, sick green, pure black; abrupt shifts between chapters; no gentle midtones.
- 材质：chalk lines on black floor, flat stage boards, digital noise, oil-painted canvas, hospital linen.

## 视频提示
- 镜头运动（只选一种）：handheld drift that breathes and jitters at half a metre from the face; or a completely locked static stage frame — choose one per shot, never mix.
- 主体运动：a woman walking toward the lens, collapsing, being carried; the body is offered to the camera, not hidden.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps (or 30fps handheld), visible digital motion smear on the handheld passages.

## 负面提示
no woman-as-pure-victim, no gore close-up, no false liberation ending, no handheld shake substituting for staging, no voice-over that explains everything, no decorative religious iconography, no chapter cards as empty provocation, no aestheticized suffering, no ironic distance, no tasteful restraint, no naturalistic depth of field.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：cold blue, sick green, pure black; handheld 25–35mm or static 50–85mm; visible theatrical or natural light; tilted close-up or flat frontal stage; chalk, stage board, digital noise, oil canvas.
- 禁止漂移：no warm palette, no polished Hollywood coverage, no invisible lighting, no shallow beauty bokeh, no stable gimbal, no period realism, no comforting resolution.
