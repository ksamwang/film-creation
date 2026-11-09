---
name: quentin-tarantino
title: 昆汀·塔伦蒂诺 Quentin Tarantino
style_file: ../directors/quentin-tarantino.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, low camera angle looking slightly up at the subject, 35–50mm lens, static two-shot with figures pushed to the edges and open space for reaction, visible neon and tungsten sources, hard blacks, chapter-specific palette — desert sand yellow, blood red, faded 1970s amber — leather, wood, film grain, talkative tension, fandom reverence.

## 图像提示
- 主体 / 场景：two figures across a diner booth or bar; a group around a table with drinks; feet, a shoe, a gun, a plate in extreme close-up; a car interior at night.
- 景别 / 构图：static two-shot with figures at the frame edges and the reaction space between them; detail inserts of feet, food, weapons, eyes; no full-body fight choreography.
- 镜头 / 焦段：35–50mm for the room, 75–100mm for inserts; no wide-angle face distortion.
- 光线：neon and tungsten with visible sources; blacks allowed to go very black; not naturalistic.
- 色彩：palette by genre chapter — desert sand, blood red, faded 1970s amber; color as genre label, not mood.
- 材质：35mm film grain, leather, wood, neon tubing, vinyl booths, cheap motel walls.

## 视频提示
- 镜头运动（只选一种）：locked static frame for the whole exchange; the camera does not move even when the violence starts.
- 主体运动：talking, eating, drinking, lighting a cigarette, telling a story with the hands; actors allowed to overlap and steal focus.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, minimal blur; the explosion of action is short and arrives without a preparation shot.

## 负面提示
no handheld realism, no shaky camera, no contemporary smartphones or social media, no gore showcase, no slow-motion cool violence, no score apologizing for violence, no clean digital sharpness, no centered symmetrical dialogue staging, no moral safe exit.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：sand yellow, blood red, faded amber; high contrast, genre-coded.
- 镜头：35–50mm, inserts 75–100mm, ( for 70mm).
- 光线：visible neon and tungsten, hard blacks.
- 构图：low angle, figures off-center at the edges, reaction space open.
- 材质：film grain, leather, wood, neon tubes, vinyl.
- 禁止漂移：no modern digital cleanliness, no smartphone screens, no cool blue teal grade, no drone shots.
