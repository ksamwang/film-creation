# 声音与台词：写进提示词的声音

能出声音的视频模型，会在你不写的地方自己补声音：配乐、氛围音乐、夸张的音效、没人说的话。声音写得越具体，它自作主张的空间越小。

声音分工的判断（视点声、画外音、静默、音乐、对白）在 `craft/sound/`；口型容量与模型差异在 `references/drama/07-segment-prompt.md` §4–§5。这份文件是写进提示词时的词库。

每条四个字段：**写法**、**防什么误读**、**用在**、**别这样写**。

---

## 1. 画内声

### 只写画内声 Diegetic only

**写法**：

```text
AUDIO: Diegetic sound only — only what exists in this room. No music, no score,
no musical stings, no ambient soundtrack.
```

**防什么误读**：模型把「气氛」理解成配乐，紧张的戏自动加低音铺底。

**用在**：所有不需要模型生成音乐的镜头（多数情况，音乐后期做）。和硬约束呼应。

**别这样写**：tense atmosphere sound——模型会加音乐。

### 房间音 Room tone

**写法**：

```text
Room tone: the low hum of the fridge and a clock ticking somewhere off-screen.
Traffic outside is faint and constant.
```

**防什么误读**：不写房间音，模型要么完全静音（像断了声音），要么填满杂乱环境声。

**用在**：所有室内镜头。写一两个持续的声源就够。

**别这样写**：ambient sounds——模型随意加声音。

### 声音落在时间点上 Sound cues on the timeline

**写法**：

```text
At 2.5s, the kettle clicks off. At 4s, a car door slams outside; she glances toward
the window.
```

**防什么误读**：声音和动作不同步，或者声音被「平均」铺在整段里。

**用在**：动作有声音的瞬间、声音触发反应的瞬间。写在逐镜时间线里，和动作同一行。

**别这样写**：把所有声音堆在 AUDIO 段，不和时间对应。

### 声音的距离 Perspective

**写法**：

```text
His footsteps start far down the corridor, faint and echoing, growing closer and
drier as he approaches.
```

**防什么误读**：模型的声音没有空间感，远处和近处一样响。

**用在**：人物走近走远、隔墙的声音、电话里的声音。视点声的判断见 `craft/sound/01-perspective.md`。

**别这样写**：footsteps——不写距离和变化。

### 画外声 Off-screen sound

**写法**：

```text
From the next room, off-screen, a television plays indistinctly; no words can be
made out. Nobody in frame reacts to it.
```

**防什么误读**：模型把画外声的来源画进画面，或者让画内人物对它做出反应。

**用在**：扩展空间、暗示别人的存在、制造悬念（`craft/sound/02-offscreen.md`）。

**别这样写**：写一句可辨认的画外台词，模型会让画面里有人对口型。

---

## 2. 台词

### 原语言台词 Lines in the original language

**写法**：

```text
At 3s he says, in Mandarin: "你先吃吧，我不饿。" — quiet, looking at the table.
```

**防什么误读**：提示词用英文写、台词也翻成英文，生成出来是英文口型或英文语音，和中文配音对不上。

**用在**：所有台词。提示词主体可以用英文，台词保留成片的语言，用引号写原文，标明语言。

**别这样写**：He says that she should eat first because he isn't hungry——转述，模型不知道说什么。

### 台词三要素 Who, when, how

**写法**：

```text
Speaker: the grandmother. Time: 5.0–7.5s. Delivery: slow, flat, without looking up
from her knitting.
```

**防什么误读**：不写说话人，模型把台词给错的人；不写时间，台词和动作打架；不写说法，模型演得戏剧化。

**用在**：每一句台词。说法写行为（不抬头、边做事边说），不只写语气词。

**别这样写**：angrily / sadly 一个副词。

### 一镜一个说话人 One speaker per shot

**写法**：

```text
Shot 3 has one line, spoken by Ming. Shot 4 has one line, spoken by Lan.
Never two people speaking in the same shot.
```

**防什么误读**：一镜两人对话，口型落错人、两人同时动嘴。

**用在**：多人对白的分镜和提示词都按这条拆（`references/drama/04-script.md` §3）。确实要同框对话时，让说话的人正脸、听的人侧脸或背对。

**别这样写**：把一来一回写在同一镜。

### 台词时长 Line length fits the shot

**写法**：

```text
The line is 10 characters; at a natural pace it takes about 2.5 seconds.
The shot is 4 seconds, leaving a beat before and after.
```

**防什么误读**：镜头比台词短，模型赶词或吞掉半句。

**用在**：写提示词前核对：中文约 4–5 字 / 秒，加 1–2 秒余量（各模型的实测容量见 `references/drama/07-segment-prompt.md` §4）。这句不写进提示词，是写之前的检查。

**别这样写**：在 2 秒的镜头里放一句 20 个字的台词。

### 画外延续的台词 Voice carrying over

**写法**：

```text
He is off-screen. His voice continues from the previous shot: "照着念就行。"
On screen, she listens; her lips stay closed.
```

**防什么误读**：模型把画外台词放到画内人物嘴上。

**用在**：台词落在听者脸上的反应镜（`storyboard/breakdown.md` 第五步）。

**别这样写**：只写台词，不写说话人在画外、画内的人闭嘴。

### 低语、喊与哭腔 Voice quality

**写法**：

```text
She whispers, barely voiced, her lips hardly moving. / He calls out across the yard,
raising his voice to be heard, not screaming.
```

**防什么误读**：模型的「喊」变成尖叫，「低语」变成正常说话。

**用在**：需要特殊音量和音色的台词。给出参照（为了让人听见 / 不让旁边的人听见）。

**别这样写**：screams / yells——除非真的要尖叫。

---

## 3. 静默

### 写出来的静默 Scripted silence

**写法**：

```text
After her line: silence. Only the hum of the fridge for two full seconds. Nobody speaks,
no music enters.
```

**防什么误读**：模型讨厌空白，静默的地方会被补上音乐或台词。

**用在**：转折之后、关键台词之后、结尾（`craft/sound/03-silence.md`）。

**别这样写**：不写，指望模型留白。

### 声音抽空 Sound drop-out

**写法**：

```text
At 3s, as she reads the message, the room tone fades away completely; for two seconds
we hear only her breathing. At 5s the room returns.
```

**防什么误读**：模型做不出主观的声音变化，会理解成音频故障。

**用在**：主观时刻、震惊。生成里不稳定，多数情况后期做更可靠；写进提示词时同时准备后期方案。

**别这样写**：dramatic silence——模型会加一个戏剧性的音效。

---

## 4. 速度与声音

### 慢动作的声音 Slow motion and sound

**写法**：

```text
Generate at normal speed with natural sound. Slow motion will be applied in the edit.
```

**防什么误读**：要慢动作时，模型连声音一起放慢，台词变成低沉拖长的怪声；或者画面慢了声音没慢，对不上。

**用在**：所有需要慢动作的镜头。画面后期变速（`storyboard/pacing.md` §6），声音后期单独处理（常见做法是抽掉现场声、只留一个放大的细节声或音乐）。

**别这样写**：在提示词里写 slow motion 又写台词。

---

## 5. 音乐（确实需要时）

### 画内音乐 Source music

**写法**：

```text
A radio on the counter plays an old song quietly; it is part of the room, slightly
tinny, and stays at the same volume throughout. No other music.
```

**防什么误读**：画内的收音机变成了全片配乐，音质干净、音量随剧情起伏。

**用在**：音乐属于场景的时候（收音机、街头艺人、婚礼）。写清来源、音质、音量不变。音乐的判断见 `craft/sound/04-music.md`。

**别这样写**：romantic music plays——模型直接加配乐。

---

## 6. 常见问题

| 问题 | 原因 | 改法 |
|---|---|---|
| 自动加了配乐 | 写了气氛词；没封住 | 只写画内声 + 硬约束列全同义词 |
| 口型落错人 | 一镜两个说话人；没写谁闭嘴 | 一镜一个说话人；听的人闭嘴 |
| 台词说不完 | 镜头太短 | 按字数算时长，留余量 |
| 台词变成英文 | 提示词翻译了台词 | 台词保留原文，标明语言 |
| 静默被填满 | 没写静默 | 写出静默和持续的房间音 |
| 慢动作声音怪 | 生成时写了慢动作 | 正常速度生成，后期变速 |

## 来源

见 `video-prompt/sources.md`。
