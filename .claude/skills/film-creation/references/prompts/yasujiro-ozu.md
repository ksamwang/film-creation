---
name: yasujiro-ozu
title: 小津安二郎 Yasujiro Ozu
style_file: ../directors/yasujiro-ozu.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Japanese family drama, camera fixed at tatami height about seventy centimetres, low and level, frontal symmetrical composition, figures seated to one side, the other side left as doorway, shoji screen or courtyard, layered interior frames, soft even diffuse light with no hard shadows, warm low-key wood beige grey and deep blue, tatami and cotton, still, polite, quietly dissolving.

## 图像提示
- 主体 / 场景：an elderly couple seated on tatami in an otherwise empty room; a daughter serving tea at a low table; a father and daughter with a sake bottle between them; clothes folded on the floor.
- 景别 / 构图：fixed full shot showing the whole room and the relation of people to furniture; frontal, symmetrical, figure on one side, empty door or window or wall on the other; layered door frames; no off-center handheld framing.
- 镜头 / 焦段：50mm prime at the eye level of a kneeling person, about 70cm; never raised, never lowered mid-scene.
- 光线：even diffuse daylight, no hard shadow, no rim light; interiors evenly lit.
- 色彩：warm and low — wood, beige, grey, deep blue; kimono almost the same value as the wall.
- 材质：tatami, shoji paper, wooden posts, cotton fabric, old household objects.

## 视频提示
- 镜头运动（只选一种）：static, locked off; no pan, tilt, dolly or follow; changes of view come only from cuts.
- 主体运动：slow seated gestures — pouring sake, folding clothes, bowing; a person exits frame and the camera holds on the empty room.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, no motion blur; hold three seconds after the exit.

## 负面提示
no moving camera, no pan or dolly, no handheld, no shot-reverse-shot with matched eyelines, no high angle, no camera height change within a scene, no push-in at a wedding or funeral, no cut immediately after a character exits, no music explaining sadness, no character saying "I am lonely", no reconciliation ending, no hard side light or rim light, no saturated color, no shallow-focus glamour portrait, no slow-cinema emptiness without composition.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：warm low saturation — wood, beige, grey, deep blue.
 - 镜头：50mm, tatami height about 70cm, static.
 - 光线：even diffuse, no hard shadow, no rim.
 - 构图：frontal symmetry, figure to one side, empty frame on the other, layered doorways.
 - 材质：tatami, shoji paper, wood, cotton.
- 禁止漂移：no handheld, no drone, no modern apartment, no LED white, no teal-and-orange, no shallow bokeh, no camera height drift, no Western living room.
