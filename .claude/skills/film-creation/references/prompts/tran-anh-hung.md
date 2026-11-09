---
name: tran-anh-hung
title: 陈英雄 Tran Anh Hung
style_file: ../directors/tran-anh-hung.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, humid Indochina interior, wet green foliage and milky white papaya, warm brown wood, striped shadows from a wooden window lattice on a face, medium close-up at seated working height, hands and bowls in the foreground, layered curtain and window frame dividing the space, 35–50mm, natural window light, no fill, steam and oil sheen, tactile, quiet, amber and copper.

## 图像提示
- 主体 / 场景：a young woman preparing green papaya in a wooden house; a cook finishing a copper pot of consommé; a family at a table beside shutters.
- 景别 / 构图：medium close-up, camera at seated or kneeling height, hands and vessels in the foreground, window lattice or curtain layering the frame, subject off-center.
- 镜头 / 焦段：35–50mm, close to the hands, no long-lens voyeurism.
- 光线：natural light through the lattice, real striped shadows, no flat fill; kitchen fire as secondary source.
- 色彩：humid green, milky white, warm wood brown; in the French kitchen amber, copper and white linen; never a saturated “Vietnam filter”.
- 材质：wood, gauze, steam, oil, fruit skin, copper pot, condensation.

## 视频提示
- 镜头运动（只选一种）：slow dolly along a door, window or curtain, joining two rooms in one breath; no handheld.
- 主体运动：one complete household action — chopping, wiping, stirring; the camera stops when the action is finished.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, natural motion blur only, no speed ramp.

## 负面提示
no yellow-green Vietnam filter, no saturated tropical grade, no food as symbol without steam and oil, no voice-over explaining nostalgia, no chopped-up hand action, no music before the sensory sound, no high-angle on servants, no folkloric display, no lifestyle-commercial gloss, no decorative shallow bokeh.

## 一致性锚点
- 色彩：humid green / milky white / warm brown; amber-copper-white for the French kitchen.
- 镜头：35–50mm.
- 光线：window-lattice daylight, striped shadows, no fill.
- 构图：medium close, seated or working height, layered door / window / curtain, hands in foreground.
- 材质：wood, gauze, steam, oil, copper, fruit skin.
- 禁止漂移：no drone, no HDR, no clean digital kitchen, no food-styling gloss, no handheld shake, no saturated green grade.
