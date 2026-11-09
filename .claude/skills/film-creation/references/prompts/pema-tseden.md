---
name: pema-tseden
title: 万玛才旦 Pema Tseden
style_file: ../directors/pema-tseden.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, Tibetan plateau village, low-saturation earth yellow, muted crimson and grey blue, flat frontal medium shot at eye level, subject centered and facing the camera in a static frame, natural window light and bare bulb, whitewashed mud wall, plastic sheeting, worn sweater, 35–50mm lens, documentary stillness, no spectacle.

## 图像提示
- 主体 / 场景：an old herdsman and a young monk bargaining across a table in a whitewashed room; a man on a motorcycle stopped on a dirt road beside power poles; a woman hanging laundry against a mud wall.
- 景别 / 构图：medium shot and full shot, frontal, subject centered with near-thangka frontality, background of white wall, grassland or prayer flags; no close-up, the figure does not fill the frame.
- 镜头 / 焦段：35–50mm, eye level, static.
- 光线：natural window light indoors; bare bulb and stove fire at night; no shaped key light, no fill.
- 色彩：low saturation; earth yellow, Tibetan red, grey blue; the sky must not read as vivid blue.
- 材质：mud wall, plastic sheeting, worn sweater, motorcycle, prayer flags handled and dirty.

## 视频提示
- 镜头运动（只选一种）：static locked-off camera at eye level; the only permitted move is a slow lateral pan during silence, never a push-in.
- 主体运动：riding a motorbike, herding sheep, walking a mountain road, handing over documents, bargaining; small gestures, no emotional display.
- 时长 / 帧率 / 运动模糊：10–20 seconds, 24fps, natural motion blur only, no slow motion.

## 负面提示
no postcard grassland, no horizon pinned to the rule of thirds, no pristine landscape without power poles, plastic sheeting or dirt roads, no mystical glow, no ethereal atmosphere, no ritual staged as spectacle, no glamorized religious imagery, no fluent urban styling, no tearful close-up, no handheld shake for realism, no saturated turquoise sky, no voice-over explaining the era, no resolved reconciliation ending.

## 一致性锚点
- 色彩：low-saturation earth yellow, Tibetan red, grey blue; sky held back from vivid blue.
- 镜头：35–50mm, eye level, medium shot as default.
- 光线：window light, bare bulb, stove fire; no shaped key.
- 构图：frontal and centered, near-thangka frontality, background wall or grassland.
- 材质：mud wall, plastic sheeting, worn sweater, motorcycle, used prayer flags.
- 禁止漂移：no tourism-postcard horizon, no clean new props, no mystical haze, no drone landscape.
