---
name: xie-jin
title: 谢晋 Xie Jin
style_file: ../directors/xie-jin.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, 1960s–1980s rural China, high-key frontal lighting with no hidden shadows, medium shot with faces open to camera, symmetrical staging of a struggle session or a family table, cold grey for the public scene and warm tungsten yellow for the kitchen, 35–50mm at eye level, patches, enamel cups, faded slogans, sweat and dirt visible, direct, unironic.

## 图像提示
- 主体 / 场景：a man and a woman sweeping a stone street under a crowd's gaze; a family at a table with bowls; a woman singing on a stage; a teacher standing on a threshing floor.
- 景别 / 构图：medium shot, frontal, faces turned to camera; key scenes symmetrical — stage above and crowd below, both sides of a table; close-up reserved for eyes and hands, not a full-face crying shot.
- 镜头 / 焦段：35–50mm; 85mm only for the single push-in.
- 光线：high-key and bright, frontal fill, no shadow hiding; the audience must see tears, sweat and dirt.
- 色彩：per-scene, not a global grade — cold grey for struggle and interrogation, warm yellow for kitchen, wedding and rehabilitation; the two may sit next to each other.
- 材质：patches, enamel mugs, old opera costumes, sun-faded slogans, threshing-floor dust, sweat.

## 视频提示
- 镜头运动（只选一种）：one slow push-in from group to face to eyes, then cut; otherwise the camera is static or pans laterally across a crowd.
- 主体运动：sweeping, bowing, shouting, crying aloud, raising a bowl; stage-scale gestures, no small naturalistic hesitation.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, natural motion blur, no speed ramps.

## 负面提示
no cold detached fixed long take of a struggle session, no unblemished dignity in suffering, no ironic music, no purely evil perpetrator, no skipped period markers, no fragmented editing, no supporting character stealing the moral center, no ending without tears, no handheld, no canted angles, no HDR, no desaturated art-house grade.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：cold grey and warm yellow per scene, not a gradient; 35–50mm, 85mm push-in; high-key frontal fill; symmetrical stage and table staging at eye level; patches, enamel, old costume, faded slogan.
- 禁止漂移：no modern LED white, no cool blue moonlight, no drone, no clean digital skin, no desaturated "festival" grade.
