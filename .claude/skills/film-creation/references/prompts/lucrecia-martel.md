---
name: lucrecia-martel
title: 卢奎西亚·马特尔 Lucrecia Martel
style_file: ../directors/lucrecia-martel.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, a sweltering Salta afternoon, a middle-class family crushed around a plastic table, 100mm telephoto compressing shoulders and heads, top of frame cropping a forehead, damp moss-green wall, mildew yellow, faded pink, diffuse light through a gauze curtain, skin slick with sweat, blurred garden green behind, soft grain, someone off-frame is being ignored.

## 图像提示
- 主体 / 场景：women half-lying beside a green pool while children watch from the water; a family lunch where a maid passes in the next room, only partly visible; a car stopped on a rain-dark road, the event itself outside the frame.
- 景别 / 构图：medium close-up and close-up; heads or half-bodies cropped by the frame; figures pushed to the edges; a group that occludes itself rather than posing; foreground gauze, table edge or curtain blocking half a face.
- 镜头 / 焦段：85–135mm telephoto; background compressed into a wash of green or white; shallow but not glamorous focus.
- 光线：diffused, never direct; through louvered blinds, gauze curtains, water reflection; humid, slightly dim.
- 色彩：moss green, mildew yellow, faded pink, hospital white; desaturated by moisture, no clean primaries.
- 材质：sweat, water, mud, tile, plastic tablecloth, damp fabric.

## 视频提示
- 镜头运动（只选一种）：slow lateral drift at seated height, as if the camera is looking at the wrong thing; no push-in.
- 主体运动：people talk without fully facing each other, fan themselves, reach across the table; a child or dog draws the camera's attention away from the speaker; no dramatic gesture.
- 时长 / 帧率 / 运动模糊：6–8 seconds, 24fps, soft natural motion blur, no slow motion.

## 负面提示
no establishing wide shot of the location, no high-angle or overhead view, no clean symmetrical family portrait, no glossy green art-film filter, no orchestral cue telling us danger, no servants framed as victim posters, no centered composition, no crisp digital skin, no clear face-forward speech staging, no awakening moment for the middle class.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：moss green, mildew yellow, faded pink, hospital white / 100mm, / diffused through blinds, gauze, water / chest-shoulder height, cropped heads, figures at edges / sweat, water, mud, tile, plastic.
- 禁止漂移：no drone or aerial, no clean modern interiors, no saturated emerald filter, no sharp digital texture, no heroic close-up.
