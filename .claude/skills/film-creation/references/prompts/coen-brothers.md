---
name: coen-brothers
title: 科恩兄弟 Coen Brothers
style_file: ../directors/coen-brothers.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, locked static wide shot, figure small in one corner of a large empty space, flat eye-level camera, 35–50mm wide angle with deep focus, source-motivated practical light, no fill in the darks, regional genre texture — snow, cracked wood, highway, cheap wallpaper — muted earth tones, film grain, deadpan, vast indifference.

## 图像提示
- 主体 / 场景：a man in a snowbound parking lot beside a car; a clerk behind a counter and a stranger in front of it; an empty motel room after something happened; a face explaining itself to no one.
- 景别 / 构图：either the wide full shot that makes a person a speck in a corner, or an extreme close-up of a baffled face; no medium-shot transition; large blank space that reads as the universe not answering.
- 镜头 / 焦段：35–50mm wide for the space, extreme close-up for the face; eye-level, never a heroic low angle.
- 光线：motivated practical light, underexposed darks left alone, night not filled in; no showing off.
- 色彩：genre-specific texture rather than one grade — high-contrast noir, western wide sky, saturated musical color; muted earth otherwise.
- 材质：snow, wood, asphalt, cheap wallpaper, motel carpet, bloodstains only after the fact.

## 视频提示
- 镜头运动（只选一种）：locked static frame; the camera does not console or chase.
- 主体运动：one person explaining an already-lost situation to another; talking in circles, polite and lethal; violence kept outside the frame.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, no motion blur; hold past the point where the explanation fails.

## 负面提示
no handheld tension, no slick music-video coverage, no warm filter making absurdity cute, no stylized gore, no omniscient narration that resolves every clue, no heroic low angle, no symmetrical beauty shot, no sentimental redemption ending, no comic mugging.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：muted earth, high-contrast noir, wide-sky western; never one decorative grade.
- 镜头：35–50mm wide, extreme close-up, or .
- 光线：source-motivated, no fill, unglamorous.
- 构图：flat eye level, figure small in a corner, large blank space.
- 材质：snow, wood, asphalt, wallpaper, carpet, film grain.
- 禁止漂移：no drone aerials, no teal-orange blockbuster grade, no modern urban glass, no handsome hero lighting.
