---
name: luis-bunuel
title: 路易斯·布努埃尔 Luis Buñuel
style_file: ../directors/luis-bunuel.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Surrealist film still played completely straight, symmetrical formal composition, long dining table filling the frame, static eye-level medium-wide, 35–50mm, flat frontal documentary light with no expressionist shadow, warm linen-and-silver bourgeois interior against neutral servants and outdoors, one impossible object placed in plain daylight and never emphasized, polite, dry, quietly blasphemous.

## 图像提示
- 主体 / 场景：a group of well-dressed bourgeois seated at a dinner table; a woman enclosed by church and family in a formal drawing room; servants entering from the frame edge; an animal or object that does not belong.
- 景别 / 构图：default medium-wide including the whole drawing room and every guest; symmetrical, camera stands like a guest, never at the table's center; only a brief close-up when a servant hands something over or the impossible element appears, then immediately back to medium-wide.
- 镜头 / 焦段：35–50mm, whole space intact, no telephoto enlargement of the anomaly.
- 光线：flat, frontal, documentary lighting, evenly lit interior; no expressionist shadow, no spot on the object.
- 色彩：warm tones for bourgeois interiors, neutral tones for servants, peasants and outdoors; class is coded by color temperature.
- 材质：linen tablecloth, silverware, wood, religious fabric.

## 视频提示
- 镜头运动（只选一种）：slow lateral tracking across a table of people, like social observation — no push-in, no crane, no handheld.
- 主体运动：polite eating, passing dishes, ritual gestures, a servant crossing the frame — while the impossible thing happens without anyone reacting.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, no motion blur, deadpan timing with a beat held too long.

## 负面提示
no soft-focus dream haze, no fog, no dream color grade, no "it must be a dream" line, no psychological explanation of quirks, no random weirdness without a target, no camera reacting to the absurd (no push-in, no shake, no score stinger), no glamorized peasants or revolutionaries, no gore or freak-show shock, no moral judgment ending, no close-up emphasizing the impossible object.

## 一致性锚点
- 色彩：warm bourgeois interior / neutral servants and outdoors; class by color temperature.
- 镜头：35–50mm, static medium-wide.
- 光线：flat frontal documentary light, even interior, no expressionist shadow.
- 构图：symmetrical and upright, long dining table filling the frame, camera at guest height.
- 材质：linen, silver, wood, religious fabric.
- 禁止漂移：no dream haze, no surreal CGI glow, no fisheye, no handheld, no modern bourgeois glass apartment, no moralizing close-up.
