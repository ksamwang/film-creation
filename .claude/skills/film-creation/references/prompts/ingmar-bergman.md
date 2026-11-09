---
name: ingmar-bergman
title: 英格玛·伯格曼 Ingmar Bergman
style_file: ../directors/ingmar-bergman.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, chamber drama, two faces close together across a bare table, background stripped of decoration, single window light from the left, half of each face falling into darkness, high-contrast black and white, linen, worn wood floor, a glass of water, 50mm framing held, 85mm close-up, deep grain, intimate, severe, unconsoled.

## 图像提示
- 主体 / 场景：a pastor, an actress who has stopped speaking, two spouses in a summer house; a bare room with one table, one window, a bed, a glass; a church, a theatre backstage, a windswept island.
- 景别 / 构图：only two scales — medium holding two or three people, or a close-up filling the frame with a face; no wide establishing shot. Minimal composition, background almost empty.
- 镜头 / 焦段：50mm for the two-shot confrontation, 85–135mm for the face; camera at eye level, starting at two meters and pushing to half a meter.
- 光线：one window as the only source, soft but directional; half the face remains in shadow; no even fill.
- 色彩：black and white with high contrast in the early period; red, white and black in the color period, red like an interior.
- 材质：worn wood floor, linen, faded wallpaper, a glass tumbler, a wall clock, wrinkled sheets.

## 视频提示
- 镜头运动（只选一种）：very slow dolly in toward the face, then stop and hold longer than is comfortable.
- 主体运动：two people seated facing each other, almost motionless; a hand, a swallow, a look away; no blocking.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, minimal motion blur, the hold after the push is the point.

## 负面提示
no sobbing melodrama, no swelling score, no psychological exposition, no scenic landscape, no soft even fill light, no cheap religious consolation, no sudden reconciliation, no theatrical display acting, no modern handheld coverage, no wide establishing shot, no decorative period detail.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：high-contrast black and white, or red-white-black; 50mm two-shot, 85–135mm close-up; single window light with half-face shadow; minimal frame; wood, linen, glass.
- 禁止漂移：no warm color grade, no handheld, no wide landscape, no crowd, no modern apartment, no soft beauty light, no smiling resolution.
