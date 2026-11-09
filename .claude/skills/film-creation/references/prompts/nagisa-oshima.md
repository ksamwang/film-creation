---
name: nagisa-oshima
title: 大岛渚 Nagisa Oshima
style_file: ../directors/nagisa-oshima.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Japanese political drama, frontal symmetrical staging like an interrogation, figures at equal height facing the lens, hard theatrical front light, sharp black shadows, enclosed tatami room or prison cell with clear boundaries, medium shot keeping subject and institution in the same frame, dry wood and sweat, high contrast, no softening, cold, confrontational, exposed.

## 图像提示
- 主体 / 场景：two lovers facing each other on tatami, both aware of the lens; a condemned man seated before a tribunal; a shinsengumi captain in a bare barracks room.
- 景别 / 构图：medium and medium-close, frontal and symmetrical, subject and interrogator in one frame, the enclosing boundary visible; no lyrical wide, no naturalistic off-center framing.
- 镜头 / 焦段：35–50mm frontal, minimal compression; camera at the subject's eye height, never above or below.
- 光线：hard frontal stage light, sharp shadows, no fill, no softbox.
- 色彩：high-contrast monochrome; or flesh tone, warm red and dark brown; or desaturated cyan-grey — choose one per project.
- 材质：wood, tatami, blood, sweat; surfaces dry, no wet glossy sheen.

## 视频提示
- 镜头运动（只选一种）：locked static frontal; a single abrupt lateral move or sudden push when the gaze must be forced.
- 主体运动：bodies held still, then a direct turn to the lens; figures arranged in a triangle, the speaker at the apex.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, no motion blur, no smooth easing.

## 负面提示
no beautiful erotic photography, no psychological flashback, no empathic close-up telling the audience whom to side with, no smooth dissolves, no naturalistic conversational acting, no good-versus-evil binary, no redemption ending, no camera hiding behind a character's back, no soft glamour light, no shallow depth of field, no wet glossy skin, no slow-motion violence, no high angle that grants pity.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
 - 色彩：high-contrast monochrome, or one flesh / red / brown palette, or low-saturation cyan-grey.
 - 镜头：35–50mm frontal, equal height.
 - 光线：hard frontal stage light, sharp shadow.
 - 构图：frontal symmetry, closed boundary, oppressor and victim at the same height.
 - 材质：dry wood, tatami, blood, sweat.
- 禁止漂移：no soft focus, no natural window light, no handheld, no modern interior, no aestheticized nudity, no color filter used to separate dream from reality, no slow motion.
