---
name: larry-fong
title: 拉瑞·方 Larry Fong
style_file: ../cinematographers/larry-fong.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, anamorphic, 35mm grain, a single hard top-light raking across the body, deep black background, no fill except negative fill, figure centered against empty sky or smoke, amber and steel-blue palette, crushed blacks, desaturated midtones, dust and rain in the air, hard rim on shoulders, poster-like graphic composition, retro 1970s genre film, monumental, still.

## 图像提示
- 主体 / 场景：a lone warrior, detective or soldier standing in smoke, rain or dust; a vast empty landscape or a black soundstage void behind them.
- 景别 / 构图：wide or medium-wide, dead center or low angle, strong verticals, figure small against a large negative space; horizon very low or very high.
- 镜头 / 焦段：27mm Primo or 35–50mm anamorphic; long lens for compressed landscapes.
- 光线：one hard source from top or behind, –, black background, rim on shoulders, a small eye light inside the silhouette.
- 色彩：amber, steel blue, blood red; crushed blacks, desaturated midtones, no pastel.
- 材质：dust, ash, rain, smoke, metal, leather, wet skin, anamorphic flare.

## 视频提示
- 镜头运动（只选一种）：slow vertical crane rise, revealing the figure against sky or smoke, then a hard stop.
- 主体运动：a figure stands still while cape, coat or smoke moves in the wind.
- 时长 / 帧率 / 运动模糊：4–8 seconds, 24fps base with a 50–100fps speed ramp, crisp edges, no handheld.

## 负面提示
no soft frontal fill, no even skin tones, no handheld shake, no grey-blue desaturated wash, no naturalistic window logic, no wide-angle distortion, no rescued shadows, no pastel palette, no documentary realism, no modern LED white, no clean digital skin.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：amber, steel blue and blood red; 27mm or 35–50mm anamorphic; one hard top/back source at –; centered graphic frame; dust, smoke and wet metal.
- 禁止漂移：no soft key, no handheld, no teal-orange LUT, no daylight naturalism, no clean plastic surfaces.
