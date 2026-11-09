---
name: lee-chang-dong
title: 李沧东 Lee Chang-dong
style_file: ../directors/lee-chang-dong.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, naturalist Korean social drama, overcast diffused daylight, low-saturation earth yellow and grey-green, 35–50mm at eye level, subject centered yet pressed by walls, wet plastic sheeting and old plaster, no fill light, long unbroken medium shot, quiet moral weight.

## 图像提示
- 主体 / 场景：a woman sitting alone in a church hall after everyone has left; a man eating rice at a folding table in a half-empty room; an old woman looking at the sky beside a plastic greenhouse.
- 景别 / 构图：medium and medium wide; subject near center but compressed by wall, field or rain; door and window frames mark the boundary; when another person is present the face must share the frame with them or with a piece of furniture.
- 镜头 / 焦段：35–50mm standard, eye level; no wide-angle distortion, no long-lens compression except when watching from far off.
- 光线：natural and practical only, overcast preferred, no shaping light, no fill; interior window light left uneven.
- 色彩：low-saturation natural — earth yellow, grey-green, faded denim; never pushed to a single monochrome.
- 材质：old plaster, plastic sheeting, rain, mud, cheap furniture, worn fabric.

## 视频提示
- 镜头运动（只选一种）：static locked-off medium shot for the whole take, no movement; if the subject walks away, the camera stays and lets them leave the frame.
- 主体运动：small and complete — the body finishes a choice inside the take: hesitation, a change of words, a long silence; no big emotional display.
- 时长 / 帧率 / 运动模糊：10–25 seconds, 24fps, no motion blur, no cut inside the emotional turn.

## 负面提示
no long take as showmanship, no scene that exists only to illustrate a social thesis, no music that absolves or convicts the character, no class-symbol characters, no explanation of the mystery, no suffering used as sainthood, no woman as pure victim, no slow-plus-miserable-plus-issue festival formula, no stylized key light, no fast cutting, no saturated color grade.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：low-saturation earth yellow and grey-green, 35–50mm; overcast natural light, no fill; centered subject compressed by door or wall frame; old plaster, plastic sheet, rain, mud.
- 禁止漂移：no teal-orange grade, no golden-hour romance, no handheld urgency, no shallow-focus bokeh portrait, no clean modern interiors, no slow-motion, no voice-over explaining the theme.
