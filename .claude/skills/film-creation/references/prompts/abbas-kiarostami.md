---
name: abbas-kiarostami
title: 阿巴斯·基亚罗斯塔米 Abbas Kiarostami
style_file: ../directors/abbas-kiarostami.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Iranian minimalist realism, distant 50–135mm long lens compressing a zigzag dirt road, a tiny figure on a khaki hillside, olive trees, dust, hard midday sun or long dusk shadows, low saturation ochre and grey-green, camera fixed inside a car window frame, no score.

## 图像提示
- 主体 / 场景：a man in a car on a hill road, camera in the passenger seat, dust on the windscreen; a child running up a terraced path between olive trees; a lone figure digging on a bare slope at noon.
- 景别 / 构图：extreme wide and wide — the figure is a dot; road or path forms a zigzag or S-curve; frame divided by car door, window pillar or rear-view mirror; negative space dominates.
- 镜头 / 焦段：50–135mm long lens compressing the distant road; 35mm wide only inside the car.
- 光线：natural only — hard noon sun, long dusk shadows; no fill, no diffusion, no shaping.
- 色彩：ochre, dust yellow, grey-green, olive; low saturation, minimal grading.
- 材质：dust, gravel road, olive leaves, dry grass, old car upholstery, plastic chair.

## 视频提示
- 镜头运动（只选一种）：static locked-off camera on the hillside or road edge; it holds the empty landscape after the subject walks out of frame.
- 主体运动：walking, waiting, getting out of a car, digging, driving; long approach over distance; the subject may leave frame and the camera keeps holding the empty road.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, no motion blur, no cut on action.

## 负面提示
no shot-reverse-shot explaining dialogue, no close-up for sentiment, no music explaining emotion, no resolved ending, no polished production design, no camera smarter than the character, no meta-cinema as gimmick, no fast cutting, no aerial drone shots, no warm nostalgia grade, no symmetrical tourist landscape.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：ochre, dust yellow, olive, grey-green, low saturation; 50–135mm; natural hard light, no fill; tiny figure on a zigzag road, car-window framing; dust, gravel, olive leaf, plastic seat.
- 禁止漂移：no drone aerials, no golden-hour postcard grade, no shallow-focus portrait, no modern city glass, no HDR, no added music or voice-over narration.
