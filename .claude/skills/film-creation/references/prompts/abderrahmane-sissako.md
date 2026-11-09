---
name: abderrahmane-sissako
title: 阿布德拉曼·西萨科 Abderrahmane Sissako
style_file: ../directors/abderrahmane-sissako.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, a mud-walled courtyard in Timbuktu at late afternoon, a man seated on a mat pouring tea, camera at seated eye level across the threshold, street and desert held outside the frame, earth-yellow walls, grey-blue cloth, low hard sunlight casting long shadows, fine dust, a tin teapot, 35mm, static, quiet, everyday, power waiting off-screen.

## 图像提示
- 主体 / 场景：a man pouring tea in a courtyard, a woman washing clothes by a basin, a boy sitting at the doorway; a football match with no ball; a radio on a shelf, a poster on a wall.
- 景别 / 构图：medium-wide, seated or standing eye level; figure inside the doorway or against the courtyard wall; the frame edge holds street or desert; no close-up until someone crosses the threshold.
- 镜头 / 焦段：35mm for the wide; 85mm only for the teapot, the cup, the hand at the threshold; deep, calm focus.
- 光线：natural light; hard midday or long late-afternoon shadows; no fill, no diffusion.
- 色彩：earth yellow, grey-blue, white; low saturation, no monochrome; one colored garment identifies the person.
- 材质：sand, dust, cloth, corrugated iron, tin teapot, enamel cups.

## 视频提示
- 镜头运动（只选一种）：static camera at seated height, held for the whole shot; no push-in.
- 主体运动：tea is poured in a slow continuous arc; a hand washes cloth; someone crosses the threshold and only then does the frame change; a song is sung to its end.
- 时长 / 帧率 / 运动模糊：10–15 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no battle scene, no psychological backstory for armed men, no cartoon evil, no score inciting anger or pity, no handheld shake, no fast cutting, no hero speech, no timeless utopian village, no victory for occupier or residents, no poetic empty silence, no high-angle view, no exotic desert postcard.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：earth yellow, grey-blue, white / 35mm wide, 85mm detail, / natural, hard noon, long dusk / seated eye level, static, doorway framing / sand, dust, cloth, tin, enamel.
- 禁止漂移：no drone desert aerials, no modern glass, no saturated orange grade, no clean digital skin, no handheld urgency.
