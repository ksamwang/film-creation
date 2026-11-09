---
name: alfonso-cuaron
title: 阿方索·卡隆 Alfonso Cuarón
style_file: ../directors/alfonso-cuaron.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, black-and-white 1970s Mexico City, a domestic corridor with wet terrazzo floor, 24mm wide lens in deep focus, a maid at the far edge of frame carrying laundry, the center held by a doorway into the next room, dust suspended in soft window light, fine grain, the camera about to cross the threshold, institutional space, no cut.

## 图像提示
- 主体 / 场景：a maid carrying laundry through a colonial house, water spreading across the floor; a family car on a dusty highway, the road ahead blocked; a hospital corridor with a nurse at the edge and the ward in the center.
- 景别 / 构图：medium to wide, deep focus so person and architecture are both readable; asymmetrical; subject at the frame edge, center reserved for corridor, water, doorway or road; symmetry only for the institution, never for the character.
- 镜头 / 焦段：21–35mm wide, deep focus; 50mm only for a private close-up; avoid long telephoto in motion.
- 光线：explainable sources only — window, car headlight, fire, sun; soft interior daylight and practical pools.
- 色彩：one code per film; monochrome for the domestic memory (black-and-white), or desaturated grey-green for the dystopian exterior; do not mix.
- 材质：water, dust, glass, concrete, wet floor, worn plaster.

## 视频提示
- 镜头运动（只选一种）：one continuous tracking shot moving through a doorway and handing off to another figure; no cuts, no hidden edits.
- 主体运动：the maid walks, carries, turns; a second person enters and the camera follows them; background action (a car, a crowd, a dog) happens before the subject notices.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural motion blur, no speed ramps.

## 负面提示
no unmotivated camera move, no hidden cuts inside the long take, no score summarizing emotion, no visible villain behind the institution, no total victory, no rapid action cutting, no picturesque poverty, no voice-over explaining class, no telephoto compression during movement, no symmetrical hero framing.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：monochrome or grey-green (choose one per film) / 21–35mm wide, deep focus, / explainable window, headlight, fire, sun / asymmetrical, figure at edge, corridor center / water, dust, glass, concrete.
- 禁止漂移：no drone aerials, no modern glass towers, no LED white, no clean digital skin, no handheld shake.
