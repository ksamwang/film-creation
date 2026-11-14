# 编译：从分镜脚本到提示词

分镜脚本已经回答了「拍什么」：每镜的功能、景别、角度、运镜、画面、台词、时长。提示词要做的，是把这些决定**翻译**成模型能执行的文字，再**补上**分镜脚本里没写、但模型一定会自己猜的东西：空间、光、人数、表演分寸、不能出现的东西。

翻译是机械的，补充是导演的判断。这份文件按七步走，最后用 `storyboard/breakdown.md` 的场 5 做一条完整示例。

## 字段对应表

| 分镜脚本 | 落到提示词的 | 怎么翻译 |
|---|---|---|
| 场景标题（地点 / 时间） | 资产、空间地图、光 | 场景参考图写「只管什么」；时间写进光 |
| 读戏卡 | 戏的意图 | 「结束时什么变了」「谁知道什么」写成 THE BEAT；情绪曲线决定表演强度 |
| 镜号、时长 | 剪辑合同、逐镜时间码 | 时长累加成时间码；生成单位内重新从 0 计 |
| 功能 | 逐镜时间线里「观众必须读到什么」 | 反应镜 → 写清反应的对象和变化；插入镜 → 写清物件状态；视线对象 → 写清从谁的视线看出去 |
| 景别、角度 | 镜头锁 | 景别 → 焦段 + 距离；角度 → 机位高度 |
| 运镜 | 摄影机行为 | 固定 → locked-off，并写死不漂；缓推 → 写起止和速度 |
| 画面 | 逐镜时间线 | 拆成按时间码排的微动作；补物理后果和结束状态 |
| 台词 / 声音 | 声音 + 逐镜时间线 | 台词原文写进对应镜头的时间点；声音先行写成「上一镜结尾就响」 |
| 生成栏（稳 / 定帧 / 后期） | 决定这镜进不进这次生成 | 「后期」镜不进提示词，或只生成干净底板 |

分镜脚本**不会**写、提示词必须补的：硬约束、风格、人数锁、识别特征锁、空间的「哪里没有什么」、首帧、光、色、空气、物理、表演细节、总锁、negative。

## 第一步：定档位，切生成单位

一场戏很少能一次生成完。先把分镜脚本切成**生成单位**，每个单位写一条提示词。

切分原则（和 `references/drama/06-storyboard.md` 一致）：

- **同一场景、同一时间、同一光线**的连续镜头放在一起；
- 总时长不超过模型单次上限（多数 10–15 秒）；
- 参考图数量不超过模型上限，镜头里出现的人和物都要有图；
- 镜头数控制在模型能稳定处理的范围（多数 3–6 镜）；
- **生成栏写「后期」的镜头单独处理**：屏幕内容、文字特写这类镜头不进生成，或者只生成干净底板再合成；
- 切点优先放在**景别跳变大**的地方，单位之间的接缝不容易被看出来。

然后按 `video-prompt/index.md` 的三档选档位。多镜头对白段落通常是标准档。

## 第二步：写全局段

全局段 = 剪辑合同之外、逐镜时间线之前的所有段落：硬约束、风格、人数锁、资产、空间地图、光、色、空气。

- 来源：全片设定（风格、色彩）、资产库（参考图、识别特征）、场景标题（地点、时间、光源）。
- **同一场戏的所有生成单位，全局段逐字复用。** 只换剪辑合同、首帧、镜头锁、逐镜时间线、总锁里与本段相关的条目。改一个形容词，两段之间的光和人就可能对不上。
- 资产段的 THIS SCENE 写这场戏的状态；跨场变化（换衣服、受伤）在连续性记录里查（`storyboard/continuity.md`）。

## 第三步：从读戏卡写戏的意图

读戏卡的六个问题里，三个直接进 THE BEAT：

- **结束时什么变了** → 这一段要推动的变化（不一定是全场的变化，只写本段的）；
- **观众知道多少 / 谁知道什么** → 写清信息差，表演才有分寸；
- **情绪曲线** → 本段落在哪一格，决定强度。

再加一句「This is NOT ...」，封住模型对这种情绪的默认放大。

## 第四步：从建立镜头画空间地图

- 找分镜脚本里的建立镜头和关系镜头，它们定义了空间。
- 写出：人在哪、门 / 走廊 / 窗在哪（绝对布局），在主机位里谁在画左谁在画右（相对布局），轴线。
- 分镜脚本画面栏里出现的方向词（「看向画右的走廊」「转向画右的顾言」）全部要和地图一致；不一致，先改分镜脚本。
- 写「哪里没有什么」：空的工位、空的走廊。

## 第五步：逐镜翻译

每一行分镜脚本变成一段 SHOT：

1. **时间码**：本单位内从 0 开始累加；每镜比分镜脚本多留的余量（`storyboard/pacing.md` §6）在生成时长里体现，不必写进时间码。
2. **功能 → 观众必须读到什么**：先写这一镜的目的，再写动作。反应镜写「她看见了什么、怎么变」，不只写「她的近景」。
3. **景别 / 角度 / 运镜 → LENS 与 CAMERA**：焦段写进镜头锁；运镜如果全段一致，在 CAMERA 段统一写，逐镜只写例外。
4. **画面 → 微动作**：按时间码拆开，一镜一个主要动作；补物理后果；写结束状态。
5. **台词 / 声音 → AUDIO 与内嵌提示**：台词原文写在说话的时间点，同时写「其他人嘴闭着」；声音先行写在上一镜末尾。

## 第六步：预判误读，写锁和 negative

对每一镜问一句：**模型最可能把这里拍成什么错误的样子？** 把答案写下来，再分三处处理：

| 误读的类型 | 放在哪 |
|---|---|
| 一错整条作废（人数、谁说话、轴线、谁坐谁站） | 标「CRITICAL」+ 总锁 |
| 模型的顽固默认（音乐、文字、漂移、AI 质感） | 硬约束 + 总锁 |
| 这场戏特有的错误演法（哭、冷笑、对质过火） | 戏的意图里的 NOT + negative |

## 第七步：自检

- [ ] 时间码加起来等于总时长？镜头数和剪辑合同一致？
- [ ] 每一镜的方向词都和空间地图、轴线一致？
- [ ] 每句台词标了说话人、原文、时间点？其他人嘴闭着？
- [ ] 每张参考图写了「只管什么」？识别特征锁不超过 4 条？
- [ ] 「CRITICAL」不超过 3 处？总锁不超过 8 条？
- [ ] 正文里有没有和锁、negative 矛盾的句子？
- [ ] 全局段和同场其他单位逐字一致？
- [ ] 每一段都能回答「不写这段模型会在哪里错」？

---

## 示例：场 5 段 B

### 切分

场 5 共 13 镜、约 42 秒（`storyboard/breakdown.md` 分镜脚本）。切成三个生成单位：

| 单位 | 镜头 | 时长 | 内容 | 说明 |
|---|---|---|---|---|
| 段 A | 5-01 – 5-04 | 约 11 s | 发现 | 5-02、5-04 是屏幕内容，生成栏「后期」：只生成 5-01、5-03（屏幕为空白光），屏幕画面另行合成 |
| 段 B | 5-05 – 5-09 | 15.5 s | 来人、对质 | 下面写完整提示词 |
| 段 C | 5-10 – 5-13 | 约 15.5 s | 摊牌、回应 | 复用段 B 的全局段；5-11 林晚不张嘴、顾言台词画外延续 |

段 B 的切点：5-04（屏幕特写）→ 5-05（林晚中近景），景别和内容都跳变，接缝不显。

### 编译过程（段 B）

| 分镜行 | 翻译成 |
|---|---|
| 5-05 反应 · 中近景 · 固定 · 林晚抬头看向画右走廊 · 电梯「叮」先于画面 | 0–2s，50mm；首帧她已经在抬头；叮声在 0s 前已经响起，写成「starts on the tail of a lift chime」 |
| 5-06 视线对象 · 全景 · 固定 · 顾言提两杯咖啡走来 · 脚步声 | 2–5s，85mm 压缩走廊；视线对象 → 写明从林晚的方向看过去；脚步声 |
| 5-07 关系 · 中景 · 固定 · 顾言放下咖啡、林晚侧对镜头 · 顾言台词 | 5–9.5s，35mm；两人同框、轴线写死；台词原文 + 林晚嘴闭着 |
| 5-08 动作 · 近景 · 过肩（顾言）· 林晚转屏幕 · 林晚台词 | 9.5–13s，50mm 过肩；屏幕只有空白光；台词原文 + 顾言嘴闭着 |
| 5-09 反应 · 近景 · 固定 · 顾言看屏幕、笑、放下自己的咖啡 | 13–15.5s，75mm；笑的分寸写成三件套 |

读戏卡给出的信息差（观众知道他改了数据，他不知道她知道）进 THE BEAT；情绪曲线在「冷 → 紧」，所以林晚克制、顾言轻松。

预判的误读：林晚哭或拍桌子；顾言演成反派冷笑；背景里出现加班的同事；屏幕上出现可读的数字；两个人同时动嘴；顾言坐下、林晚站起；林晚喝了咖啡（她不碰咖啡是 B6 的回应，段 C 才发生）；摄影机缓慢漂移。

### 提示词（标准档，约 1300 词）

```text
EDIT: 5 shots, 15.5 seconds total, hard cuts, continuous real time, no time jumps.
Shot 1 0–2s · Shot 2 2–5s · Shot 3 5–9.5s · Shot 4 9.5–13s · Shot 5 13–15.5s.

GLOBAL RULES:
- No music of any kind: no score, no soundtrack, no background music, no musical stings.
- No on-screen text: no subtitles, no captions, no titles, no watermark, no logo.
  The computer monitor shows only a soft blank glow, never readable numbers or words.
- Normal speed throughout: no slow motion, no speed ramps.

STYLE: Photoreal contemporary drama. Soft filmic contrast, gently lifted blacks,
smooth highlight rolloff, fine organic grain, natural skin texture with visible pores.
No HDR look, no oversharpening, no glossy commercial finish.

THE BEAT: Late at night, Lin has just found proof that her manager Gu secretly edited
her report. Gu does not know she knows. He arrives with coffee, friendly and relaxed;
the coffee is a gesture of control dressed as kindness. Lin is cold and controlled.
She asks one quiet, direct question. This is NOT a confrontation scene: Lin does not
cry, does not shout, does not stand up. Gu is pleasant and easy, NOT a villain: no smirk,
no menace.

CRITICAL — ONLY TWO PEOPLE exist in this scene: Lin and Gu. The open-plan office is
completely empty: no colleagues, no cleaner, no figures in the corridor or behind glass.

ASSETS:
<<<lin>>> — Lin's face, hair and wardrobe only. Not her pose or expression.
  Identity lock: straight black hair tied in a low ponytail, thin black-framed glasses,
  no earrings, no visible jewellery.
  THIS SCENE: grey knit cardigan over a white shirt, sleeves pushed to the forearms,
  a few loose strands of hair after a long day.
<<<gu>>> — Gu's face, hair and wardrobe only. Not his pose or expression.
  Identity lock: short side-parted hair, clean-shaven, no glasses, steel wristwatch on left wrist.
  THIS SCENE: navy suit jacket, white shirt, no tie, top button open.
<<<office>>> — room layout, desk arrangement and materials only. Not the time of day:
  in this scene it is night and almost every light is off.
<<<cup>>> — the paper coffee cup design. Gu carries two identical cups.

GEOMETRY: Lin sits at her desk in an open-plan office, facing her monitor. The corridor
leading to the lift is on Lin's right; it runs away from her toward a lift lobby at
the far end. The rows of desks around her are dark and empty. Gu walks up the corridor
and stops standing at the right-hand side of Lin's desk.
Axis, for every shot: Lin is frame left, Gu is frame right. Lin looks frame right to see Gu;
Gu looks frame left to see Lin.

FIRST FRAME: Lin is already lifting her head from the monitor, eyes starting to turn
toward the corridor on her right.

LENS: Focal length is fixed within each shot: no zooming.
Shot 1 — 50mm, medium close-up on Lin, eye level, seated height.
Shot 2 — 85mm, compressed view down the corridor from Lin's desk, the lift lobby flattened
  close behind Gu.
Shot 3 — 35mm, medium two-shot, eye level of a seated person, Lin in profile frame left,
  Gu standing frame right.
Shot 4 — 50mm, over Gu's right shoulder onto Lin; his shoulder soft in the right foreground.
Shot 5 — 75mm, close shot of Gu, eye level of a standing person, background falling soft.

CAMERA: All five shots are locked-off on a tripod. No drift, no slow push, no gimbal
float, no handheld shake.

LIGHT: Night. Lin's desk lamp is the key: warm, low, from frame left, pooling on her desk
and the left side of her face. The monitor adds a faint cool fill on her face. The rest of
the office is dark. The corridor has cold white overhead lights, so Gu walks out of cool
light into the warm pool of the desk lamp as he arrives.

COLOUR: 70% warm lamp amber, 20% blue-grey darkness, 10% cold corridor white.
Low overall saturation; skin stays natural, not orange.

ATMOSPHERE: Still night air, faint steam rising from the coffee cups in the lamp light.
Real office textures: worn desk edge, a stack of printed pages, cable clutter.
No airbrushed skin, no waxy faces, no plastic sheen.

SHOT 1 — 0–2s — Lin, medium close-up, 50mm.
0.0s: The shot starts on the tail of a soft lift chime. Lin's head is already rising
  from the monitor.
1.0s: Her eyes settle on the corridor, frame right. She does not move otherwise.
Ends: Lin still, looking frame right, lips closed.

SHOT 2 — 2–5s — the corridor, 85mm, seen from Lin's desk.
2.0s: Gu is already walking toward camera from the lift lobby, a coffee cup in each hand.
3.0–5.0s: He keeps walking at an easy, unhurried pace, passing under two overhead lights.
  His footsteps are audible on the hard floor.
Ends: Gu in the middle of the frame, still approaching.

SHOT 3 — 5–9.5s — two-shot, 35mm. Lin frame left in profile, seated; Gu enters frame right.
5.0s: Gu steps into frame right and stops beside the desk.
5.5s: He sets one cup down on Lin's desk near her right hand; the lid taps the desk lightly.
6.5s: Gu says, in Mandarin, warm and casual: "还没走？明天汇报别太紧张。"
  Only Gu's lips move. Lin's mouth stays closed. She does not look at the cup.
Ends: Gu standing, his own cup still in his hand; Lin seated, turned slightly toward him.

SHOT 4 — 9.5–13s — over Gu's right shoulder onto Lin, 50mm.
9.5s: Lin takes the edge of the monitor with one hand and turns it toward Gu, frame right.
  The screen shows only a blank glow.
11.0s: Looking up at him, Lin says, in Mandarin, quietly and evenly: "第七页，是你改的？"
  Only Lin's lips move. Gu, seen from behind, does not move his head.
Ends: Lin holding his gaze, hand resting on the monitor edge.

SHOT 5 — 13–15.5s — Gu, close shot, 75mm.
13.0s: Gu glances down at the monitor, frame left, for a moment.
14.0s: A small, easy smile; his shoulders stay relaxed. It reads as a man who thinks this
  is a minor matter, not as guilt and not as a threat.
14.5s: He sets his own cup down on the desk edge.
Ends: Gu looking at Lin, frame left, lips closed, smile fading to neutral.

PHYSICS: The coffee cups are full and have weight; they land with a soft tap, the liquid
does not spill. The monitor turns on its stand with slight resistance. Hands make real
contact with objects. Objects do not morph, duplicate or pass through each other.

ACTING: Restrained, naturalistic. Both blink at a normal rate. Nobody looks into the lens.
Lin's coldness shows only as stillness and a level voice; it reads as control, not calm
and not sadness. Gu is relaxed and friendly throughout. Only the speaking character's
lips move; the listener's mouth stays closed, no silent mouthing.

AUDIO: Diegetic only. Room tone: a faint air-conditioning hum. A soft lift chime at the
very start. Gu's footsteps in shot 2. The cup lid tapping the desk in shot 3. Two lines
of dialogue only, both in Mandarin: Gu's line in shot 3, Lin's line in shot 4. After Lin's
line, near silence.

LOCKS:
- Only two people, the whole time. The office stays empty.
- Lin stays seated in every shot; Gu stays standing in every shot.
- Lin is always frame left, Gu always frame right.
- Lin does not touch or drink the coffee.
- Exactly two lines of dialogue, one each, one speaker at a time.
- No music, no readable text anywhere, including the monitor.

NEGATIVE: Lin crying, tears, shouting, slamming the desk, standing up; Gu smirking,
sneering, looking guilty or angry; Gu sitting down; any third person; colleagues in the
background; readable numbers or words on the screen or papers; both characters talking
at once; music; slow motion; slow camera drift; daylight; waxy skin.
```

### 为什么这样写

- **两条「CRITICAL」**：人数，以及 THE BEAT 里的 NOT 用大写强调。屏幕文字放在硬约束里，因为它在两处会被看到（5-08 和总锁）。
- **冗余只给三件事**：人数（人数锁 + 总锁 + negative）、坐站（空间 + 总锁 + negative）、轴线（空间 + 逐镜方向词 + 总锁）。
- **林晚不碰咖啡写进总锁**：这是段 C 的戏（5-12 她的手停在杯旁），段 B 里她一碰，后面的戏就没了。
- **电梯声先于画面**：分镜脚本写「先于画面」，生成里没办法让声音早于第一帧，所以写成「从叮声的尾音开始」，剪辑时把叮声的前半拖进 5-04 的尾巴。
- **5-08 的屏幕**：生成栏是「稳」，但屏幕内容不可控，所以只要空白光；如果剧情需要观众看清第七页，屏幕画面后期合成。

### 段 A 和段 C

- **全局段**（硬约束、风格、THE BEAT 的人物部分、人数锁、资产、空间地图、光、色、空气、物理、表演）逐字复用段 B。THE BEAT 的情节部分改成本段要推动的变化。
- **段 A**：顾言还没出现。人数锁改成「only one person: Lin」，资产去掉 `<<<gu>>>` 和 `<<<cup>>>`；屏幕在 5-01、5-03 里只有空白光，5-02、5-04 后期合成。
- **段 C**：5-11 林晚近景缓推是 CAMERA 段的唯一例外，单独写「slow push-in over 4.5 seconds」；顾言台词的后半句在画外延续，写成「Gu is off-screen; his voice continues: "汇报的时候，你照着念就行。" Lin's lips stay closed」；5-13 顾言离开后，人数锁仍然有效（不能有别人走进来）。

## 竖屏短剧

竖屏短剧的片段提示词按 `references/drama/07-segment-prompt.md` 的格式和两条固定约束编译。平台允许较长提示词时，可以在那个格式的基础上加入本层的 THE BEAT、人数锁、识别特征锁、总锁和这场戏的 negative；格式本身以 drama/07 为准。

## 来源

见 `video-prompt/sources.md`。
