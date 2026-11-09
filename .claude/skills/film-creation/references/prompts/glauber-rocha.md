---
name: glauber-rocha
title: 格劳贝尔·罗查 Glauber Rocha
style_file: ../directors/glauber-rocha.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, brutal overhead sun with no fill on the face, low camera near the ground looking up so the figure cuts into a huge white sky, 25–35mm wide angle, high-contrast black and white or earth-yellow, blood-red and indigo, dry earth, rock, dead tree, dust, sweat, coarse cloth, handheld frame with aggressive energy, mythic, hungry, confrontational.

## 图像提示
- 主体 / 场景：a peasant or bandit standing against a white sky; a crowd in a village square; a corpse on dry ground seen from above; a preacher addressing the camera directly.
- 景别 / 构图：medium wide and wide, figure treated as a monument; sky and land take most of the frame, the person is small but not weak; low angle, subject pressing into the horizon.
- 镜头 / 焦段：25–35mm wide, person and land pulled into the same frame; no telephoto isolation.
- 光线：harsh sun, no fill, face allowed to burn out; soft light only for the interior of the powerful.
- 色彩：high-contrast black and white by default; color passages use earth yellow, blood red, indigo.
- 材质：dust, sweat, blood, coarse cloth, dry stone, dead wood, film grain.

## 视频提示
- 镜头运动（只选一种）：aggressive handheld push-in toward a face, camera as agitator, never a neutral observer.
- 主体运动：a crowd pressing forward, a speaker turning to the lens, a figure walking against the wind; gestures theatrical and declarative.
- 时长 / 帧率 / 运动模糊：3–6 seconds, 24fps, harsh motion; sudden zoom or cut rather than a smooth move.

## 负面提示
no soft light, no pretty poverty, no smooth continuity editing, no psychological flashback, no neutral observer camera, no clean studio set, no folk culture as decoration, no reconciled final shot, no gentle golden-hour grade.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：monochrome high contrast or earth yellow, blood red, indigo.
- 镜头：25–35mm, low and wide, ( wide passages).
- 光线：overhead sun, no fill, burned-out highlights.
- 构图：sky and land dominate, figure cuts the horizon.
- 材质：dust, sweat, blood, coarse cloth, dry earth, grain.
- 禁止漂移：no drone aerials, no soft-focus humanism, no clean digital color, no modern city, no passive victim framing.
