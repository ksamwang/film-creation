---
name: agnes-varda
title: 阿涅斯·瓦尔达 Agnès Varda
style_file: ../directors/agnes-varda.md
---

> 用法：「风格锚点」可直接放在模式 A 提示词末尾当风格句；「负面提示」和句中的 no ... 只在模型有 negative 参数时使用（模式 B 放进 NEGATIVE），否则改写成正面描述；「视频提示」的镜头运动按图生视频写，文生视频要先补人物位置。见 `../prompting.md`。

## 风格锚点
Cinematic film still, handheld 35mm at the subject's eye height, available daylight, cluttered real location with passers-by and cables left in frame, collage of pink, blue and yellow against faded wall plaster, old clothes and handwritten paper, the photographer's shadow or hand entering the frame, medium close-up, tender, unsentimental, imperfect, alive.

## 图像提示
- 主体 / 场景：an old woman sorting discarded vegetables; a woman walking a beach in a black dress; a wall of handwritten notes; the filmmaker's own reflection in a mirror.
- 景别 / 构图：medium close-up at subject height, asymmetric, clutter and bystanders kept, frame not cleaned; mirror, doorway or mural dividing the space; the camera's own presence visible.
- 镜头 / 焦段：35mm handheld, environment and face in the same frame；《克莱奥》35–50mm with tracking.
- 光线：available light, no studio fill；《克莱奥》controlled light is the exception; imperfect shadows are allowed.
- 色彩：collage pink, blue and yellow that can clash；《克莱奥》black and white with color only in the song sequence.
- 材质：old clothes, sand, peeling plaster, mirror, mural, handwritten paper.

## 视频提示
- 镜头运动（只选一种）：handheld follow at the subject's height; the camera may stop and stare at a face, a hand or a wall; no smooth dolly.
- 主体运动：people walking, talking, working, being interviewed; small unplanned gestures; the subject may look into the camera.
- 时长 / 帧率 / 运动模糊：5–10 seconds, 24fps, natural handheld motion blur, no stabilization, no speed ramp.

## 负面提示
no unified color grade, no hidden camera or invisible crew, no interviewee treated as raw material, no voice-over smarter than the image, no beautiful empty landscape, no sweet string score, no smile close-up, no hug ending, no pink-filter lifestyle vlog, no decorative handwritten font, no warm grade on the black-and-white film.

## 一致性锚点
- 色彩：clashing pink / blue / yellow; or pure black and white with color only in the song.
- 镜头：35mm handheld, （散文片 1.37–）.
- 光线：available light, imperfect, no fill.
- 构图：asymmetric, clutter retained, camera's own shadow or hand in frame, subject at eye height.
- 材质：old clothes, sand, peeling plaster, mirror, handwriting.
- 禁止漂移：no drone, no stabilized gimbal, no HDR, no vintage filter, no clean minimalist set.
