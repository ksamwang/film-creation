---
name: george-miller
title: 乔治·米勒 George Miller
style_file: ../directors/george-miller.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, a rusted convoy tearing across an orange desert at noon, a war rig centered in frame like a totem, 24mm wide lens mounted low on the hood, hard directional sun, orange-red fire and chrome silver, dust and petrol haze, readable silhouettes against the sky, high contrast, every body braced, no soft light.

## 图像提示
- 主体 / 场景：a war rig and escort vehicles in a desert chase; a mechanic hanging from a moving car; a young warrior with a shaved head and grease on her face; a faction camp built from scrap, fuel and bone.
- 景别 / 构图：wide panoramic action or extreme close-up (an eye, a wound, a wheel); subject centered like a totem; negative space only to signal imbalance; silhouettes must stay readable.
- 镜头 / 焦段：21–35mm wide, close to the vehicle; 65–85mm only for a static extreme detail; no long telephoto inside action.
- 光线：hard, directional, single-source; noon sun or firelight; no diffusion, no soft box, no rim-light beauty.
- 色彩：coded by faction — orange-red for fire, cold blue for night, chrome silver for machinery, green for oasis; high contrast.
- 材质：rusted iron, leather, petrol, sand, sweat, chrome, torn fabric.

## 视频提示
- 镜头运动（只选一种）：low tracking shot mounted on the vehicle, moving with the convoy; no static shot, no crane.
- 主体运动：a car swerves, a body braces against the roll cage, a wheel throws sand, a hand reaches for a lever; impact has a visible consequence; no speech.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, strong directional motion blur, no slow-motion lyricism.

## 负面提示
no incoherent shaky blur, no action without geography, no speech mid-combat, no even soft lighting, no symmetrical negative-space poster, no consequence-free violence, no sympathetic villain backstory, no slow-motion lyricism, no telephoto compression in action, no women only as rescued, no smooth digital CGI plastic.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：orange-red, cold blue, chrome silver, green / 21–35mm wide, / hard directional sun or fire / center-framed subject, readable silhouette / rust, leather, petrol, sand, sweat.
- 禁止漂移：no drone aerials, no clean futuristic white, no soft beauty filter, no weightless bodies, no HDR video-game gloss.
