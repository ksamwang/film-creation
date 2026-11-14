# 运动词典：运镜、航拍与穿越、速度与时间

字段与可靠性分级见 `camera/index.md`。运动怎么设计（起幅—触发—落幅、运动动机）见 `craft/staging/03-camera-movement.md`；本篇只管「叫什么、怎么写、能不能出」。

**写运动的四条硬规则**

1. 一次生成一种运动。推近 + 横摇 + 变焦会让脸和墙一起变形；复合效果拆两镜。
2. 写清起点、方向、终点：`slowly pushes in from medium to close-up`，不只写 `push in`。
3. 写速度：`slow`、`steady`、`sudden`。不写时模型常给中速漂移。
4. 首帧生视频只写运动和动作，不复述画面；单段 3–5 秒最稳，更长就拆镜或续接（`references/aigc/workflow.md`）。

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
- **写法**：`The camera tilts up from his muddy boots to his face.` B: `tilt up from feet to face`
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
- **写法**：`Start tight on the cracked watch in her hand, then pull back to reveal she is standing on the edge of the rooftop.` B: `pull-back reveal, detail to wide`
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
- **写法**：`Dolly zoom: the camera moves back while zooming in, so his face stays the same size while the corridor behind him stretches away.` B: `dolly zoom, vertigo effect`
- **作用**：人物不动，世界在变形——眩晕、顿悟、恐惧袭来（《电影镜头入门》Step4「眩晕」）。
- **用 / 不用**：一部片一次，留给最大的心理冲击。
- **生成**：定帧，多数模型做不准。近似做法：生成一段拉远镜头，后期逐帧放大让脸保持同样大小，背景就会向前压。仍不成立就改用推近 + 声音处理。
- **短剧**：落 `push_in` 或 `pull_out`，效果在成片阶段做。

---

## 3. 移动与跟随

### 横移 Lateral tracking / trucking
- **写法**：`The camera tracks sideways to the right, parallel to her as she walks along the shop windows.` B: `lateral tracking shot, moving right`
- **作用**：和人物并行；扫过一排东西（人群、货架、废墟）让观众逐个看过去。
- **用 / 不用**：开阔空间；窄空间换用摇。
- **生成**：稳。
- **短剧**：`tracking`

### 后跟 Follow from behind
- **写法**：`The camera follows close behind him at shoulder height as he walks down the dark corridor.` B: `follow shot from behind`
- **作用**：观众跟着他进入未知；他看到的我们同时看到（《电影镜头入门》Step4「跟拍」）。
- **用 / 不用**：进入新空间、走向冲突；要看表情时改前引。
- **生成**：稳；背面镜头身份难辨，前面先有一镜正面锚定。
- **短剧**：`tracking`

### 前引 Leading shot
- **写法**：`The camera moves backward ahead of her as she walks toward it, keeping her in a steady medium shot.` B: `leading shot, camera retreating`
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
- **写法**：`The camera cranes up and away from her as she stands alone in the square, until the whole square is visible.` B: `crane up, rising away`
- **作用**：离开人物、上升到俯视——结局、孤立、命运；《电影镜头入门》Step3 专讲升降的情感表达。
- **用 / 不用**：场尾、片尾；从人物上升到环境。
- **生成**：稳。
- **短剧**：`crane`

### 降 Crane down
- **写法**：`The camera cranes down from the rooftops into the narrow street, settling at eye level as he steps out of the door.` B: `crane down to eye level`
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
- **写法**：`Smooth floating steadicam move, gliding behind him through the kitchen and out into the dining room.` B: `steadicam, smooth gliding`
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
- **写法**：`Aerial shot rising straight up from the car on the empty road until the whole forest surrounds it.` B: `drone ascending, top-down reveal`
- **作用**：从个人到环境；孤立、结局、规模。
- **生成**：稳。模型很擅长航拍。
- **短剧**：落 `crane`

### 飞越 Flyover
- **写法**：`A slow aerial flyover above the rice terraces at dawn, moving forward toward the village.` B: `aerial flyover, forward`
- **作用**：建立地理与规模；开场、转场（《电影镜头入门》Step4「飞越」）。
- **生成**：稳。人物在画面中很小时身份不必一致，适合文生视频。
- **短剧**：落 `tracking`

### 航拍俯冲 Aerial dive
- **写法**：`The drone dives down the side of the tower toward the street, leveling out just above the crowd.` B: `drone dive, descending fast`
- **作用**：冲进事件现场；速度、危险。
- **生成**：稳；接近地面后人物会糊，落幅放在人群不在个人。

### FPV 穿越 FPV dive and weave
- **写法**：`FPV drone shot, fast and close: diving off the cliff, skimming the water, then weaving between the boats.` B: `FPV drone, fast, low, weaving`
- **作用**：极速与身体感；动作、体育、开场冲击。（行业惯例）
- **用 / 不用**：一个片段一次；对白戏不用。
- **生成**：稳（简单路径）。穿过狭窄障碍时障碍物会变形或被穿模，**定帧**：首尾帧锁住两侧。

### 穿越固体 Push through
- **写法**：`The camera pushes forward through the rain-streaked window into the room, where she sits at the table.` B: `camera passes through window`
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

## 6. 短剧 `move` 枚举对照

| 枚举 | 本篇条目 |
|---|---|
| `static` | 固定机位 |
| `push_in` | 推近（也承接希区柯克变焦的近似） |
| `pull_out` | 拉远、后拉揭示 |
| `pan` | 横摇、甩镜（甩镜在成片做） |
| `tilt` | 竖摇 |
| `tracking` | 横移、后跟、前引、稳定跟随、飞越 |
| `orbit` | 环绕、子弹时间 |
| `crane` | 升、降、搜索式上升、航拍拉升 |
| `handheld` | 手持 |
| `zoom` | 变焦、急推（急推在成片做） |

短剧标准规定运镜**只放枚举字段、不写进 `text`**，枚举之外的值会被丢弃（`references/drama/standard.md`）。所以枚举里没有的运动，`move` 填最接近的值；靠后期完成的（甩镜、急推、变速、定格、希区柯克变焦的近似）记进成片方案（`references/drama/08-cut-qc.md`），不进片段提示词。宿主平台不受此限时，按本篇写法写进提示词。

## 来源

见 `camera/sources.md`。
