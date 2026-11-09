---
name: tian-zhuangzhuang
title: 田壮壮 Tian Zhuangzhuang
style_file: ../directors/tian-zhuangzhuang.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, remote grassland or frontier town, extreme long shot with the human figure small at the edge of the frame, vast grey-green grassland or earth-yellow gobi filling the rest, overcast natural light, no fill, low saturation, loosely composed with uneven negative space, 28–50mm holding the scale of the land, cracked leather boots, worn saddle, peeling painted door, ice river, patient, observational.

## 图像提示
- 主体 / 场景：a herder dismounting and dividing meat; a child crossing a snowfield; a servant kneeling in a palace courtyard; a family standing at a doorway.
- 景别 / 构图：extreme long shot first — person small, landscape dominant; figure may occupy only one corner; loose, off-balance, large empty space; no postcard composition.
- 镜头 / 焦段：28–50mm, holding the scale of the land, no telephoto extraction.
- 光线：natural light only, wait for the sky, overcast preferred; no fill, no artificial source.
- 色彩：low saturation by region — grey-green grassland, earth yellow gobi, faded red palace wall, grey-white snow; do not unify into one “art” tone.
- 材质：cracked boots, polished saddle, peeling painted door, frozen river, worn robe.

## 视频提示
- 镜头运动（只选一种）：static camera for most of the shot, with one slow lateral pan to show the relation between land and person; after the subject exits frame, hold five seconds before cutting.
- 主体运动：complete, unhurried work — dismounting, dividing meat, milking, kneeling, walking a full path.
- 时长 / 帧率 / 运动模糊：12–25 seconds, 24fps, minimal blur, real time.

## 负面提示
no score under emotion, no close-up crying, no explanatory voice-over, no ethnic-minority postcard, no speeding up to please the audience, no modern psychological monologue, no beautiful composition of suffering, no outsider speaking for the local, no handheld, no telephoto extraction, no drone aerial.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：grey-green, earth yellow, faded red and grey-white, low saturation; 28–50mm; overcast natural light, no fill; extreme long shot with figure at the edge or one corner; cracked boots, worn saddle, peeling door, ice.
- 禁止漂移：no warm nostalgia filter, no drone aerial, no HDR, no digital clean skin, no modern clothing.
