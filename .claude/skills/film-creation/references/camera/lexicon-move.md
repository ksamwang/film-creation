# 运动词典：运镜、航拍与穿越、速度与时间、复合运动

字段与可靠性分级见 `camera/index.md`。运动怎么设计（起幅—触发—落幅、运动动机）见 `craft/staging/03-camera-movement.md`；本篇只管「叫什么、怎么写、能不能出」。

**运动句：六项写全**

模型最常见的运动毛病是两种：不知道推到哪（停在半路，或一直漂），不知道多快（给一个中速漂移）。一句运动按下面六项写，缺哪项补哪项：

| 项 | 写什么 | 不写会怎样 | 例 |
|---|---|---|---|
| 起幅 | 运动开始时的景别和主体位置 | 模型自选起点，和上一镜接不上 | `Starting on a medium shot of her at the counter,` |
| 运动 | 一种运动加方向 | 方向随机，或换成别的运动 | `the camera pushes in` / `pans left` |
| 速度 | `slow` / `steady` / `sudden`，需要时写加速、减速 | 中速漂移；停的时候一顿 | `slowly, easing to a stop` |
| 幅度 | 走多远、转多少 | 运动过度或不够 | `about two steps` / `a quarter turn` |
| 落幅 | 运动结束时的画面 | 停在半路，或落幅之后继续漂 | `until her eyes fill the frame` |
| 动机 | 什么让它动：人物走动、一声响、一个视线 | 像无人机在漂（`craft/staging/03-camera-movement.md`） | `as he steps through the door` |

```text
Starting on a medium shot of her at the counter, the camera slowly pushes in about two steps as he steps through the door behind her, easing to a stop when her eyes fill the frame.
```

模式 B 用 `MOTION:` 块，六项各一格：`MOTION: slow push-in | start medium on C1 at counter | about two steps | trigger C2 enters behind | end close-up on C1's eyes`。

**另外三条**

1. **一次生成一种运动意图。** 一个主运动，最多加一个为了让主体留在画框里的补偿运动：跟着人横移时顺势摇向他、升起时俯下去看住他（§6）。两种各自独立的运动（推近 + 横摇 + 变焦）会让脸和墙一起变形，拆成两镜。
2. **主体运动和摄影机运动分开写。** 先写人怎么动，再写摄影机怎么动，各一句；混在一句里，模型常把人物的动作安到摄影机上。
3. **首帧生视频只写运动和动作，不复述画面。** 单段 3–5 秒最稳，更长就拆镜或续接；运动强度参数和首帧的限制见 §7（`references/aigc/workflow.md`）。

---

## 1. 固定与摇

### 固定机位 Static / locked-off
- **写法**：`Static camera, locked off; only she moves.` B: `static shot, locked camera`
- **作用**：画框成了舞台，观众看人物在框里做什么；冷静、客观、喜剧的节奏感。
- **用 / 不用**：对话、需要读表演的镜头、默认值。人物也不动时，镜头会像照片——给环境运动（烟、窗帘、车流）。
- **生成**：稳。不写时很多模型会自己加轻微推近，要固定就明写。
- **短剧**：`static`

### 横摇 Pan
- **写法**：`The camera pans slowly left from the window to the door as she walks across the room.` B: `slow pan left`
- **作用**：机位不动，转头换关注点；跟着走动的人，或把两样东西连起来（《镜头的语法》5.2；《电影镜头入门》Step1）。
- **用 / 不用**：窄空间里换关注点；有人物或视线带着摇。没动机的空摇像监控录像。
- **生成**：稳。摇得太快会糊、背景会抖，写 `slow`。
- **短剧**：`pan`

### 竖摇 Tilt
- **写法**：`The camera tilts up slowly from his muddy boots, past the rifle strap, and stops on his face.` B: `slow tilt up, feet to face`
- **作用**：自下而上揭示身份或体量（脚 → 脸、楼底 → 楼顶）；自上而下表示坠落或看向地面。
- **用 / 不用**：人物出场、建筑体量；竖屏里竖摇比横摇更合适，画面本身是纵向的。
- **生成**：稳。
- **短剧**：`tilt`

### 甩镜 Whip pan
- **写法**：`A sudden whip pan to the right, the image smearing into motion blur, landing on the man at the door.` B: `whip pan, motion blur`
- **作用**：注意力被猛地拽走；速度、惊吓、喜剧；也是常用转场（《电影镜头入门》Step6「快速摇摄」）。
- **用 / 不用**：两人之间的快节奏抢白、突然的声响；用多了像 MV。
- **生成**：后期。生成里常被画成普通慢摇。生成两段稳定镜头，剪辑时在接点加模糊甩动。
- **短剧**：落 `pan`，在 `text` 里不写甩镜，交给成片阶段。

---

## 2. 推、拉与变焦

### 推近 Push in / dolly in
- **写法**：`The camera slowly pushes in from a medium shot to a close-up of her face as she reads the letter.` B: `slow dolly in, medium to close-up`
- **作用**：观众和人物的距离缩短——注意、领悟、压力在增加（《电影镜头设计》第十二章）。
- **用 / 不用**：人物意识到什么、做出决定、被逼近。推近必须揭示更多（表情、道具）；没新信息只显得慢（《镜头的语法》6.21：推拉要有动机）。
- **生成**：稳。最可靠的运镜之一。
- **短剧**：`push_in`

### 拉远 Pull out / dolly out
- **写法**：`The camera slowly pulls back from her face until she is small in the empty hall.` B: `slow dolly out, close-up to wide`
- **作用**：离开人物——孤立、结束、真相显露后的「原来如此」。
- **用 / 不用**：场尾、段落结束、揭示人物处境。
- **生成**：稳；拉出来的新空间是模型编的，要和场景资产一致时**定帧**：先出落幅帧走首尾帧。
- **短剧**：`pull_out`

### 后拉揭示 Pull-back reveal
- **写法**：`Start tight on the cracked watch in her hand, then pull back slowly and steadily until the whole rooftop edge and the city below are in frame.` B: `slow pull-back reveal, detail to wide`
- **作用**：先给细节，后给处境；落幅改变了起幅的意义（《电影镜头入门》Step4「后拉揭示」）。
- **用 / 不用**：揭示地点、危险、人群、身份反转。落幅必须有新信息。
- **生成**：定帧。起幅、落幅各出一张关键帧，走首尾帧。

### 变焦 Zoom
- **写法**：`A slow optical zoom in on the man across the square; the perspective stays flat, the camera does not move.` B: `slow zoom in, static camera`
- **作用**：和推近不同：机位不动，只是视角变窄，透视不变、背景一起放大。感觉是「被看」「被盯上」，偏纪录、偏 70 年代（《导演创作完全手册》29.12.7 变焦特写与推摄特写；《镜头的语法》6.20）。
- **用 / 不用**：远处的观察、监视、纪录感。要表达靠近人物的情感，用推近。
- **生成**：定帧。很多模型把 zoom 画成推近，区分不了；对透视要求高时，生成固定机位的长焦画面，后期裁切放大。
- **短剧**：`zoom`

### 急推 Crash zoom / snap zoom
- **写法**：`A sudden snap zoom onto his shocked face.` B: `crash zoom`
- **作用**：一下子扎进去——震惊、喜剧重音、类型片的强调（《电影镜头入门》Step6「快速变焦推摄」）。
- **用 / 不用**：反转瞬间、喜剧节拍。正剧慎用。
- **生成**：后期。生成一个高清晰度的固定镜头，剪辑时 4–6 帧内裁切放大，加一点运动模糊，比生成稳得多。
- **短剧**：落 `zoom`；竖屏短剧的「打脸」反转常用，成片阶段做。

### 希区柯克变焦 Dolly zoom
- **写法**：`Dolly zoom over three seconds: the camera moves slowly back while zooming in, so his face stays the same size while the corridor behind him stretches away.` B: `slow dolly zoom, vertigo effect`
- **作用**：人物不动，世界在变形——眩晕、顿悟、恐惧袭来（《电影镜头入门》Step4「眩晕」）。
- **用 / 不用**：一部片一次，留给最大的心理冲击。
- **生成**：定帧，多数模型做不准。近似做法：生成一段拉远镜头，后期逐帧放大让脸保持同样大小，背景就会向前压。仍不成立就改用推近 + 声音处理。
- **短剧**：落 `push_in` 或 `pull_out`，效果在成片阶段做。

---

## 3. 移动与跟随

### 横移 Lateral tracking / trucking
- **写法**：`The camera tracks sideways to the right at her walking pace, parallel to her as she passes the shop windows, and stops with her at the last one.` B: `lateral tracking right, walking pace`
- **作用**：和人物并行；扫过一排东西（人群、货架、废墟）让观众逐个看过去。
- **用 / 不用**：开阔空间；窄空间换用摇。
- **生成**：稳。
- **短剧**：`tracking`

### 后跟 Follow from behind
- **写法**：`The camera follows close behind him at shoulder height, matching his slow steps down the dark corridor, and stops when he stops at the door.` B: `follow shot from behind, walking pace`
- **作用**：观众跟着他进入未知；他看到的我们同时看到（《电影镜头入门》Step4「跟拍」）。
- **用 / 不用**：进入新空间、走向冲突；要看表情时改前引。
- **生成**：稳；背面镜头身份难辨，前面先有一镜正面锚定。
- **短剧**：`tracking`

### 前引 Leading shot
- **写法**：`The camera moves backward ahead of her at her walking pace as she walks toward it, keeping her in a steady medium shot until she stops.` B: `leading shot, camera retreating, walking pace`
- **作用**：边走边看表情；人物在推着画面前进。
- **用 / 不用**：走路对话、带着情绪前进；人物直奔镜头且镜头加速后退，就是 `craft/staging/03-camera-movement.md` 里的「反推镜头」，一场只放一次。
- **生成**：稳。
- **短剧**：`tracking`

### 环绕 Orbit / arc
- **写法**：`The camera arcs slowly halfway around the couple as they kiss, the city lights sliding behind them.` B: `slow 180-degree orbit`
- **作用**：时间被拉长、人物成为世界中心；浪漫、胜利、迷失（《电影镜头入门》Step4「环绕」）。
- **用 / 不用**：关系的高峰、人物觉醒的一刻。对话中环绕会越轴，观众方向感会乱。
- **生成**：稳（半圈以内）。整圈环绕时脸和背景易漂，**定帧**，或拆成两段半圈。
- **短剧**：`orbit`

### 升 Crane up
- **写法**：`The camera cranes slowly up and away from her as she stands alone in the square, until the whole square is visible and she is a small dot in the middle.` B: `slow crane up, rising away`
- **作用**：离开人物、上升到俯视——结局、孤立、命运；《电影镜头入门》Step3 专讲升降的情感表达。
- **用 / 不用**：场尾、片尾；从人物上升到环境。
- **生成**：稳。
- **短剧**：`crane`

### 降 Crane down
- **写法**：`The camera cranes steadily down from the rooftops into the narrow street, settling at eye level just as he steps out of the door.` B: `steady crane down to eye level`
- **作用**：从世界进入个人——开场、把观众带进故事。
- **生成**：稳。
- **短剧**：`crane`

### 搜索式上升 Searching crane
- **写法**：`The camera rises slowly over the crowded hall, drifting until it finds her in the far corner.` B: `rising crane, searching the crowd`
- **作用**：先给群体，再在群体中找到一个人（《电影镜头入门》Step3「搜索式升降机上升运动」）。
- **生成**：定帧。「找到她」的落点要准，用首尾帧。

### 手持 Handheld
- **写法**：`Handheld camera, slight natural shake, staying close behind her shoulder as she pushes through the crowd.` B: `handheld, subtle shake`
- **作用**：在场、紧张、纪录感；镜头像一个跟着跑的人（《镜头的语法》5.2；《导演的摄影课》第七章：手持、移动车、斯坦尼康传达的信息不同）。
- **用 / 不用**：争吵、追逐、慌乱、纪实；用作「电影感」装饰会让观众晕。抖动要有级别：`subtle` / `restless` / `violent`。
- **生成**：稳；抖动幅度控制差，写级别词，过度抖动时加 `smooth, gentle sway`。
- **短剧**：`handheld`

### 稳定跟随 Steadicam / gimbal
- **写法**：`Smooth floating steadicam move at walking pace, gliding behind him through the kitchen and out into the dining room, where it settles on the long table.` B: `steadicam, smooth gliding, walking pace`
- **作用**：既跟随又平滑，像一个无形的观察者在漂；长镜头的主要方式。
- **用 / 不用**：穿过多个空间、梦境感、群戏巡游；紧张场面换手持。
- **生成**：稳。
- **短剧**：落 `tracking`

### 身体固定 Body-mount / snorricam
- **写法**：`The camera is rigidly fixed to his chest, facing him; his face stays locked in the center while the street lurches behind.` B: `snorricam, body-mounted`
- **作用**：人物稳、世界晃——醉、恐慌、药物、失控。（行业惯例）
- **用 / 不用**：主观失控的一两个镜头。
- **生成**：定帧。模型常把它画成普通跟拍，先出关键帧再写「脸固定在画面中心、背景摇晃」。

### 横滚 Roll / barrel roll
- **写法**：`The camera slowly rolls 90 degrees as she falls asleep, until the room is on its side.` B: `camera roll, rotating frame`
- **作用**：世界翻转——失重、坠落、梦、迷失。（行业惯例）
- **生成**：定帧，小角度较稳；整圈翻滚后期旋转画面更可控。

### 长镜头 / 一镜到底 Long take / oner
- **写法**：按段写，每段一个运动：`Continuing the same shot, the camera follows her up the stairs...`
- **作用**：时间不被剪断，观众被困在现场（《电影镜头入门》Step4「长镜头」）。
- **用 / 不用**：要观众感到「没有退路」时用；单纯炫技会拖节奏。
- **生成**：定帧 + 续接。单次生成时长有限，拆成多段续接，每段第一句接住上一段的结束状态；接点藏在遮挡（人从镜头前走过、穿过门框）或甩镜里。越接越漂，段数尽量少（`references/aigc/workflow.md`）。

---

## 4. 航拍与穿越

### 航拍拉升 Aerial rise / pull-away
- **写法**：`Aerial shot rising slowly and straight up from the car on the empty road until the whole forest surrounds it.` B: `slow drone ascent, top-down reveal`
- **作用**：从个人到环境；孤立、结局、规模。
- **生成**：稳。模型很擅长航拍。
- **短剧**：落 `crane`

### 飞越 Flyover
- **写法**：`A slow aerial flyover above the rice terraces at dawn, moving forward toward the village.` B: `aerial flyover, forward`
- **作用**：建立地理与规模；开场、转场（《电影镜头入门》Step4「飞越」）。
- **生成**：稳。人物在画面中很小时身份不必一致，适合文生视频。
- **短剧**：落 `tracking`

### 航拍俯冲 Aerial dive
- **写法**：`The drone dives fast down the side of the tower toward the street, slowing and leveling out just above the crowd.` B: `fast drone dive, level out above crowd`
- **作用**：冲进事件现场；速度、危险。
- **生成**：稳；接近地面后人物会糊，落幅放在人群不在个人。

### FPV 穿越 FPV dive and weave
- **写法**：`FPV drone shot, fast and close: diving off the cliff, skimming the water, then weaving between the boats.` B: `FPV drone, fast, low, weaving`
- **作用**：极速与身体感；动作、体育、开场冲击。（行业惯例）
- **用 / 不用**：一个片段一次；对白戏不用。
- **生成**：稳（简单路径）。穿过狭窄障碍时障碍物会变形或被穿模，**定帧**：首尾帧锁住两侧。

### 穿越固体 Push through
- **写法**：`The camera pushes slowly forward through the rain-streaked window into the room and stops on her at the table.` B: `slow push through window, end on her`
- **作用**：从外到内，打破空间边界——窥视、进入内心（《电影镜头入门》Step4「穿越固体」）。
- **用 / 不用**：外景 → 内景的段落开头；穿过钥匙孔、屏幕、眼睛也是这一类。
- **生成**：定帧。首帧是外侧、尾帧是内侧，走首尾帧；穿越瞬间常出现溶化，可接受时就保留，否则在玻璃处硬切。

---

## 5. 速度与时间

### 升格慢动作 Slow motion
- **写法**：`In slow motion, the glass slips from her fingers and shatters; droplets hang in the air.` B: `slow motion, high frame rate`
- **作用**：时间被放大——冲击、美、创伤的一瞬（《电影镜头入门》Step8「慢动作、快动作」）。
- **用 / 不用**：一个动作的峰值几秒；整段慢动作会稀释。
- **生成**：稳；但模型的「慢动作」常是整体变慢、细节变糊。要精确的慢，生成正常速度后用插帧放慢。

### 快动作 Fast motion
- **写法**：生成正常速度，剪辑时加速；提示词不写。
- **作用**：时间被压缩——喜剧、日常的重复、忙乱。
- **生成**：后期。

### 变速 Speed ramp
- **写法**：生成正常速度，剪辑时在动作峰值前后加速 → 减速。
- **作用**：动作片的节拍感：快进 → 峰值慢放 → 恢复。（行业惯例）
- **生成**：后期。提示词里写 `speed ramp` 常造成速度乱跳（`craft/staging/03-camera-movement.md` 的失败模式）。

### 延时 Time-lapse / hyperlapse
- **写法**：`Time-lapse of clouds racing over the city as day turns to night, lights flicking on across the buildings.` B: `time-lapse, day to night`
- **作用**：时间流逝、季节变化、城市节奏；移动延时（hyperlapse）是边移动边延时。
- **生成**：稳（无固定人物时）。人物在延时里会换脸、换衣服，有固定人物时拆成几张定帧图做硬切。

### 定格 Freeze frame
- **写法**：生成正常镜头，剪辑时停在某一帧；提示词不写。
- **作用**：把一瞬变成判词——人物介绍、喜剧重音、结尾（《电影镜头入门》Step7「定格」）。
- **生成**：后期。

### 子弹时间 Bullet time
- **写法**：`Time freezes mid-jump; he hangs in the air while the camera orbits slowly around him, dust suspended.` B: `bullet time, frozen moment, orbiting camera`
- **作用**：时间停止、空间可以绕着看——超能力、决定性瞬间。（行业惯例）
- **用 / 不用**：一部片最多一次。
- **生成**：定帧。先出凝固瞬间的关键帧，再用首帧生视频写「主体不动、镜头环绕半圈」；主体常会继续动，写清 `completely still`。

### 倒放 Reverse motion
- **写法**：生成正常镜头，剪辑时倒放；提示词不写。
- **作用**：时间倒流、回忆、超现实。
- **生成**：后期。生成「倒着发生」的动作通常不成立；挑倒放后看起来仍合理的动作（碎片聚合、水回到杯中）。

---

## 6. 复合运动与微运动

复合运动只有一种写得稳：一个主运动，加一个让主体留在画框里的补偿运动。补偿运动不改变这一镜的意图，观众感觉到的仍然是一种运动。两种各自有意图的运动叠在一起，拆成两镜。

### 跟摇 Pan to follow
- **写法**：`She crosses the room from the window to the door; the camera stays in place and pans slowly with her, keeping her in a medium shot, and stops as she reaches the door.` B: `static position, pan to follow, medium shot`
- **作用**：机位不动，镜头头部跟着人转。观众在原地看着人物走过去，空间被一点点扫出来（《镜头的语法》5.2）。
- **用 / 不用**：窄空间里人物移动；走位短的对话。人物要走很远，换成横移或后跟。
- **生成**：稳。写清人物从哪到哪，摄影机「在原地」。
- **失败**：摄影机跟着人一起平移，变成横移。写 `stays in place`。
- **短剧**：`pan`

### 移动加摇 Track and pan
- **写法**：`The camera tracks slowly right along the market stalls while panning left to keep him centered as he walks past it, ending on his back as he moves away.` B: `lateral track right with compensating pan, subject centered`
- **作用**：摄影机横移，镜头同时转向主体，人物始终在画框中间，背景快速换过去。视差强，空间显得深（行业惯例）。
- **用 / 不用**：人物和摄影机擦肩而过；在人群、货架、柱廊之间穿行。
- **生成**：稳（主体在中间时）。写出「摇是为了让他留在中间」，模型更容易当成一个动作做。
- **失败**：主体滑出画框，或背景扭曲。缩短幅度，或改成单纯的横移。
- **短剧**：`tracking`

### 升俯 Crane with tilt
- **写法**：`The camera cranes slowly up while tilting down, keeping her centered below as she sits alone on the steps, until it looks almost straight down on her.` B: `crane up with tilt down, subject held in frame`
- **作用**：升起时俯下去看住人物，视平线在变，人物越来越小却一直在画框中心。观众从她身边退到她头顶（《电影镜头入门》Step3）。
- **用 / 不用**：场尾、孤立、俯瞰命运。反过来是降仰：从高处降下来时抬头看住人物，常用在出场。
- **生成**：稳。单纯写 `crane up` 时人物容易出画，这样写更稳。
- **失败**：摄影机只俯不升，或只升不俯，人物出画。两个动作写在同一句，写清「保持她在中心」。升多高用画面里的参照物写（`from her eye level up past the top of the window frame`），不写米数，模型不认米数。
- **短剧**：`crane`

### 环绕推近 Arc in
- **写法**：`The camera arcs a quarter turn around him while slowly pushing in, from a medium side view to a close-up of his face as he realizes.` B: `quarter arc with slow push-in, medium to close-up`
- **作用**：一边绕一边靠近，背景在转，人物在变大。比单纯推近多了一层「世界在他周围转」的感觉，常用在领悟和决定的一刻（行业惯例）。
- **用 / 不用**：人物觉醒、决定、关系翻转的一拍。对话中途用会越轴。
- **生成**：稳（四分之一圈以内）；半圈以上加推近，脸会漂，定帧。
- **失败**：绕得太多、脸变形。限幅：`a quarter turn`。
- **短剧**：`orbit`

### 推近转焦 Push with rack focus
- **写法**：`The camera slowly pushes in on the letter on the table; as it settles, the focus shifts from the letter to her face in the doorway behind.` B: `slow push-in, rack focus foreground to background`
- **作用**：先靠近一个东西，再把注意力交给后面的人。一个镜头完成「这个东西 → 这个人」的交接（《电影镜头设计》12.4 移动兴趣中心）。
- **用 / 不用**：物件和人物的关系；揭示谁在看。
- **生成**：定帧。焦点转移的时机模型控制不准。三种做法按稳妥程度：推近和转焦分成两镜（第二镜锁死机位只转焦，用第一镜的尾帧做首帧）；首尾帧，首帧焦点在物件、尾帧焦点在人；后期做焦点切换（生成两条焦点不同的同构图素材，剪辑里叠化）。
- **失败**：两处一直都清楚，或焦点来回跳。写清「推近停下之后」才转焦。
- **短剧**：`push_in`，焦点写进 `text`。

### 垂直升降 Pedestal
- **写法**：`The camera rises straight up, level and without tilting, from the height of the child's eyes to the height of the adults' faces.` B: `pedestal up, level, no tilt`
- **作用**：只换高度、不换角度：从孩子的视平线升到大人的视平线，从桌面升到人脸。视平线的变化本身就是信息（行业惯例）。
- **用 / 不用**：视角交换（孩子和大人）、从物件升到人物。
- **生成**：定帧。模型常把它做成竖摇或升俯；用首尾帧锁住两个高度的平视画面。
- **失败**：变成仰拍或俯拍。写 `level, without tilting`。
- **短剧**：`crane`

### 微推 Creep in
- **写法**：`An almost imperceptible push-in over the whole shot, the frame tightening by only a few percent while she listens.` B: `very slow creep in, barely perceptible`
- **作用**：观众察觉不到摄影机在动，只觉得压力在慢慢增加。是对话和反应镜里最常用的「静中有动」（行业惯例）。
- **用 / 不用**：倾听、沉默、反应镜、呼吸镜；想要画面活一点又不想要运镜存在感时用。滑轨式的小幅横移见 `camera/lexicon-gear.md` 滑轨微移。
- **生成**：稳。写清「几乎看不出」和幅度，否则会变成普通推近。
- **失败**：推得太多。写 `only a few percent` 或 `barely`。
- **短剧**：`push_in`

### 不能叠的组合

| 组合 | 为什么不行 | 改法 |
|---|---|---|
| 推近 + 横摇 + 变焦 | 三种运动各有意图，透视和画框一起乱，脸和墙一起变形 | 拆成两镜，或只留推近 |
| 推近 + 变焦（不是希区柯克变焦） | 模型分不清两种放大，透视乱跳 | 只写一种 |
| 环绕 + 猛烈手持 | 方向感完全丢失 | 环绕用稳定器；手持另起一镜 |
| 升降 + 横滚 | 人物和地平线一起转，模型常把人画歪 | 横滚单独一镜，或后期旋转 |
| 甩镜 + 任何运动 | 甩镜本来就在后期做 | 生成两段稳定镜头，剪辑加甩动 |

---

## 7. 图生视频：运动强度与首帧

首帧生视频（图生视频）时，运动受两样东西限制：平台的运动强度参数，和首帧本身的构图。

**运动强度参数**

不少平台有一个控制「画面动多少」的参数，名字各不相同（运动强度、动态程度、motion strength、motion bucket 等），有的版本没有。用法：

| 档位 | 适合 | 风险 |
|---|---|---|
| 低 | 微推、呼吸镜、静物、风吹头发 | 写了运镜也可能几乎不动 |
| 中 | 走路、慢推、跟摇、横移 | 多数镜头的默认 |
| 高 | 奔跑、打斗、航拍、FPV | 脸和手容易变形，背景会扭 |

- **参数和文字同向。** 文字写 `slow push-in`、参数开到高，画面会乱动；参数开到低、文字写 `fast FPV dive`，画面基本不动。先定这一镜要多少运动，两边一起调。
- 参数控制不了方向和落点，方向和落点仍然靠运动句的六项。
- **画面里所有在动的东西都算进运动量**：摄影机、人物、环境（烛影、风、雨、人群）。一镜里摄影机在升、窗外烛影在晃，参数取低到中，环境运动写成轻微的（`the candlelight flickers faintly`）；动的东西越多，参数越低，靠文字里的速度词压。
- 平台没有这个参数时，用速度词和幅度词代替（`slowly`、`barely`、`a few steps`）。

**首帧限制运动**

| 运动 | 首帧要满足 | 不满足会怎样 |
|---|---|---|
| 推近 | 落点在首帧里已经看得见、够清楚（要推到脸上，首帧里脸不能太小、太糊） | 推到最后是一张糊脸 |
| 拉远、后拉揭示 | 拉出来的空间是模型编的；要和场景资产一致，就用首尾帧 | 空间和场景资产对不上 |
| 横移、跟随 | 运动方向那一侧留出空间；人物朝向和运动方向一致 | 人物撞出画框，或往反方向走 |
| 环绕 | 主体四周的空间要能被看见（首帧不能是贴墙的特写） | 背景是编的，越绕越漂 |
| 升降 | 落幅高度用首帧里看得见的参照物写（升到窗框顶、降到桌面高度）；一次升降不超过一层楼的高度差 | 透视在中途溶化 |

- **景别跨度和时长匹配。** 3–5 秒能稳定地从中景推到近景；从全景推到大特写，换首尾帧或拆两镜。
- **首尾帧只走得通一种运动。** 两帧之间透视差太大，模型会用溶化代替运动；起幅和落幅要是同一种运动能连起来的两张画面（`references/aigc/workflow.md`）。
- 首帧已经决定了景别和构图，提示词里只写运动和动作，不复述画面（本篇开头「另外三条」）。

---

## 8. 短剧 `move` 枚举对照

| 枚举 | 本篇条目 |
|---|---|
| `static` | 固定机位 |
| `push_in` | 推近（也承接希区柯克变焦的近似）、推近转焦、微推 |
| `pull_out` | 拉远、后拉揭示 |
| `pan` | 横摇、甩镜（甩镜在成片做）、跟摇 |
| `tilt` | 竖摇 |
| `tracking` | 横移、后跟、前引、稳定跟随、飞越、移动加摇 |
| `orbit` | 环绕、子弹时间、环绕推近 |
| `crane` | 升、降、搜索式上升、航拍拉升、升俯、垂直升降 |
| `handheld` | 手持 |
| `zoom` | 变焦、急推（急推在成片做） |

短剧标准规定运镜**只放枚举字段、不写进 `text`**，枚举之外的值会被丢弃（`references/drama/standard.md`）。所以枚举里没有的运动，`move` 填最接近的值；靠后期完成的（甩镜、急推、变速、定格、希区柯克变焦的近似）记进成片方案（`references/drama/08-cut-qc.md`），不进片段提示词。宿主平台不受此限时，按本篇写法写进提示词。

## 来源

见 `camera/sources.md`。
