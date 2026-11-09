---
name: charlie-chaplin
title: 查理·卓别林 Charlie Chaplin
style_file: ../directors/charlie-chaplin.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Silent-era black-and-white film still, a small tramp in a worn bowler hat and too-tight jacket, full body centered in a proscenium-wide shot, flat high-key frontal lighting, hard leather shoes and a bamboo cane, deep focus, visible floor, fine 35mm grain, gentle pathos, theatrical, no sepia.

## 图像提示
- 主体 / 场景：a tramp with a bowler hat, toothbrush mustache, tight jacket, baggy trousers and oversized shoes, alone on a plain street, in a factory, or at a prison gate.
- 景别 / 构图：full body, centered, symmetrical proscenium; feet, hands and cane inside the frame; visible floor; no close-up.
- 镜头 / 焦段：35–50mm, deep focus, camera 4–6 m away at chest height.
- 光线：flat high-key frontal light from above the lens; minimal shadow; side-backlight only for the final silhouette.
- 色彩：black and white, hard tonal separation; clean highlights; the dark suit keeps its texture.
- 材质：35mm grain, worn wool, hard leather, bamboo cane, brick, metal gears, bread.

## 视频提示
- 镜头运动：locked-off static camera; no dolly, no zoom, no handheld; only a horizontal pan if he crosses the frame.
- 主体运动：walk with turned-out feet, trip, recover, tip the hat; repeat one gesture three times, the third time deformed.
- 时长 / 帧率 / 运动模糊：6–8 seconds, 24fps, slight step-printed blur on fast movement.

## 负面提示
no close-up fragmentation of the body, no shallow depth of field, no sepia or warm nostalgia filter, no handheld camera, no cut on the punchline, no modern dialogue, no pitiful poverty imagery, no dolly-in for emotion, no rapid montage, no clean digital sharpness.

## 一致性锚点
- 色彩：black and white, hard tone, clean highlights, textured darks.
- 镜头：35–50mm deep focus, full-body distance.
- 光线：flat frontal high-key, single soft top key, no dramatic side light.
- 构图：centered proscenium, full body, visible floor.
- 材质：35mm grain, worn wool, hard leather, bamboo, brick.
- 禁止漂移：no color, no modern clothing, no handheld, no lens flare, no digital skin.
