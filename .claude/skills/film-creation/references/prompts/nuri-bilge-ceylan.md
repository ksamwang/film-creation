---
name: nuri-bilge-ceylan
title: 努里·比格·锡兰 Nuri Bilge Ceylan
style_file: ../directors/nuri-bilge-ceylan.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Anatolian slow cinema, 50–135mm long lens, two figures small in a vast snowfield or a large dark room, low-saturation ochre, slate blue and snow white, window light as key with the face left dark in backlight, near-static long take, wool coats, mud, wood, silence.

## 图像提示
- 主体 / 场景：two men talking in a snowbound village at dusk; a couple in a hotel room, one at the window with their back turned; a teacher walking a muddy road under a low sky.
- 景别 / 构图：wide and extreme wide — figures occupy a corner, environment holds most of the frame; two-shot preferred over singles; a window or doorway keeps the listener in frame.
- 镜头 / 焦段：50–135mm, compressing figure into snow, mud or wall so they sit on the same plane.
- 光线：natural window light as key; warm interior against cold exterior; backlit faces left dark and unreadable.
- 色彩：low saturation — ochre, slate blue, snow white, weathered wood brown.
- 材质：snow, mud, wet wool coat, old plaster, mist, bare wood, fogged glass.

## 视频提示
- 镜头运动（只选一种）：extremely slow push-in, so gradual it reads as a static frame until the subject moves.
- 主体运动：talking, turning to the window, standing, sitting back down, walking into snow; every thirty seconds someone changes position.
- 时长 / 帧率 / 运动模糊：20–60 seconds (segment into 10-second generations), 24fps, no motion blur, no cuts inside the conversation.

## 负面提示
no score for sentiment, no fast cutting, no character stating the theme, no landscape postcard, no reconciliation ending, no static long take without blocking, no snow as pretty backdrop, no silence as empty filler, no slow-plus-snow-plus-philosophy festival formula, no drone, no warm golden grade, no shallow-focus close-up.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：low-saturation ochre, slate blue, snow white; 50–135mm; natural window key, backlit dark faces, warm-cool split; figures in a corner, two-shot, environment dominant; snow, mud, wool, old wood, mist.
- 禁止漂移：no teal-orange grade, no drone aerials, no golden-hour glow, no handheld, no modern glass interiors, no shallow depth of field isolating a face, no added music.
