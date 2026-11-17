# 表演指导：写给模型的戏

模型的表演有两种默认，方向相反。一种是**标签化**：难过就流泪，生气就皱眉瞪眼，坏人就冷笑。另一种是**呆**：只给了动作、没给意图时，人物照着动作做完就停，听的人一动不动，整段像默剧。

所以写表演要做三件事：

1. **写清这一拍人物要什么、对谁做**。
2. **写出可见的行为和情绪变化的方向**：从什么变成什么，因为什么。情绪词可以写，但只作表演标注，不能单独出现。
3. **按强度档位（§2）决定外放多少**，再封住这一档里模型的错误演法。

克制不是默认值。传奇、古装、短剧的重逢、诀别、哀求，该喊就喊，该哭就哭。表演的判断原则在 `craft/performance/index.md`，互动与档位见 `craft/performance/06-interaction.md`；这份文件是写进提示词时的词库。

每条四个字段：**写法**、**防什么误读**、**用在**、**别这样写**。

---

## 1. 戏的骨架

### 一拍一个意图 One intention per beat

**写法**：

```text
Beat 1 (0–4s): she wants him to leave without a scene.
Beat 2 (4–8s): she realises he is not leaving; she wants to end this herself.
```

**防什么误读**：整段只写一种情绪，模型演成一条直线；一镜里塞三种情绪，模型演成一团。

**用在**：时长超过 5 秒、情绪有变化的镜头。意图写「她要什么」，不写「她是什么情绪」。

**别这样写**：she feels sad, then angry, then hopeful——三个标签，没有原因。

### 情绪三件套 Behaviour + meaning + not

**写法**：

```text
His thumb keeps rubbing the edge of the ticket (behaviour). He is deciding whether
to give it to her (meaning). He is not nervous and not shy; he is weighing it (not).
```

**防什么误读**：只写行为，模型可能读成另一种情绪；只写情绪，模型会演得夸张。三件一起写，意思就钉住了。

**用在**：每个情绪关键点。这是 `video-prompt/index.md` 的第 4 条总规则。

**别这样写**：只写 nervously 一个副词。

### 信息差 Who knows what

**写法**：

```text
She knows the money is gone. He does not know she knows. So she is gentle with him,
and he is relaxed.
```

**防什么误读**：模型让所有人都表现得「知道剧情」：被骗的人提前警觉，骗人的人提前心虚。

**用在**：悬疑、反转、隐瞒、讽刺。信息差的写法见 `writing/intent.md`。

**别这样写**：写出剧情背景，却不写此刻谁知道、谁不知道。

### 情绪轨迹 From → to, because

**写法**：

```text
Liancheng hears her name and freezes; she does not turn yet (0–2s). She turns her
head slowly, disbelief first: eyes searching, lips parted (2–4s). When she sees it
is really him, her face breaks: mouth trembling, tears welling, then she calls out (4–6s).
```

**防什么误读**：只写一个情绪，模型从头到尾挂着同一张脸；只写结果，变化会一下跳过去，像换了一张图。

**用在**：每个情绪转折的镜头。写清起点、触发、终点，以及每一段的微表情（Seedance 2.5 官方指南：写情绪随时间的变化，并配上每次变化的微表情）。

**别这样写**：she is shocked and then happy——两个标签，中间没有过程。

### 动作与反应 Action → reaction

**写法**：

```text
Qiaosheng grabs the chain and pleads (0–3s). The guard on frame right shoves his chest
with the iron gauntlet; Qiaosheng stumbles back a step, still holding the chain (3–5s).
The second guard tightens his grip and steps in beside the first (5–6s).
```

**防什么误读**：每个人各演各的，台词或动作打出去，没有人接；或者对方的反应和触发同时发生，看起来像预先排好的。

**用在**：所有两人以上的镜头。每个动作后面写出对方被改变的样子，反应比触发晚半拍。镜头里每个人都有一句指令，不动也要写「不动，只看着他」。原则见 `craft/performance/06-interaction.md`。

**别这样写**：they argue——不写谁先出手，谁被逼退。

### 地位 Status

**写法**：

```text
The judge does not move; he looks at Qiaosheng for a long beat before speaking.
Qiaosheng's hands keep tightening on Liancheng's sleeve; his eyes go from the judge's
face to his hands and back.
```

**防什么误读**：模型让所有人用同一种姿态站着，权力关系读不出来。

**用在**：审讯、求情、对峙、上下级。地位高：静止、视线慢、不怕停顿；地位低：手上找事、看对方的脸、身体前倾。一场里地位交换了，就是转折。

**别这样写**：he looks powerful / she looks submissive。

---

## 2. 强度档位与反误读

先选档位，再选写法。档位按类型给默认，按场切换：同一部片子，铺垫用写实，峰值用戏剧化。档位要写进剧本场表，分镜和提示词都沿用。

| 档位 | 什么时候用 | 看起来像什么 | 提示词怎么写 |
|---|---|---|---|
| 克制 | 生活流、悬疑铺垫、压着不说的戏 | 情绪在身体里，脸上只漏一点 | 用下面第一张表；最后加一句 nuanced and realistic, never exaggerated |
| 写实 | 大多数剧情戏 | 正常外放：会笑出声、会红眼眶、会提高声音 | 行为 + 情绪轨迹 + 台词的表演标注（§4）；不加 not-crying 一类的封锁 |
| 戏剧化 | 传奇、古装、聊斋、爱情和短剧的重逢、诀别、哀求、狂喜、暴怒 | 喊名字、哭出声、扑上去、跪下 | 用下面第二张表；动作要有重心和接触，声音性反应写进台词（§4） |

强度词（intense、hysterical、撕心裂肺）会让模型把眼睛画得发光或变形。写戏剧化时，用具体的身体动作承担强度，再加一句 eyes natural, no glow（Seedance 2.5 官方指南）。

**克制档：模型演成情绪标签时的改法**

| 想要的 | 模型的默认 | 写法 |
|---|---|---|
| 压着的愤怒 | 皱眉、瞪眼、咬牙、喊 | stillness; jaw set; breathing slows; voice lower and even; not shouting, not frowning |
| 克制的悲伤 | 泪流满面、抽泣 | eyes glassy but no tears fall; swallows; looks away to something ordinary; not crying |
| 尴尬 | 夸张的挠头、脸红、做鬼脸 | a smile held a beat too long; eyes search for somewhere to land; not comedic mugging |
| 害怕 | 尖叫、瞪大眼、捂嘴 | goes very still; shoulders rise slightly; breath held; eyes track the sound; not screaming |
| 心动 | 害羞捂脸、甜笑 | looks, looks away, looks back; small involuntary smile that she suppresses; not giggling |
| 得意 | 冷笑、挑眉、斜眼 | relaxed shoulders; a small private smile to himself; not smirking at camera |
| 释然 | 大口呼气、仰头闭眼 | shoulders drop a centimetre; hands unclench; a short breath out through the nose; not a dramatic sigh |
| 震惊 | 张嘴、后退、捂嘴 | the action stops mid-way; eyes stay on the thing; no gasp; not stepping back |
| 冷漠 | 面无表情的僵硬 | continues what she was doing; answers without looking up; face relaxed, not frozen |
| 虚伪的友善 | 坏人式的笑 | warm and easy on the surface; smile reaches the mouth only; not villainous, not menacing |

**戏剧化档：峰值场的写法**

| 想要的 | 模型容易演成 | 写法 |
|---|---|---|
| 重逢 | 两人站定相视微笑，或者一冲就抱住，中间没有过程 | freezes, disbelief first, then calls his name, voice breaking; runs, the last steps uneven; they collide, her weight hitting his chest, his arms closing late |
| 哀求 | 站着说台词，手垂着 | grabs the chain with both hands, knees bending toward the ground, voice rising and cracking on the last word; looks from one guard's face to the other |
| 诀别 | 安静流一滴泪 | holds on a beat too long, fingers sliding off one by one; a sob escapes before she can stop it; turns away, shoulders shaking |
| 狂喜 | 露齿大笑、举手欢呼 | laughs and cries at once, hand over mouth, then grabs the other person's arms and shakes them |
| 暴怒 | 瞪眼、龇牙、全身发抖 | slams the cup down so it cracks, steps in close, voice dropping then exploding on one word; the other person flinches |

**防什么误读**：克制档的表是模型最常见的情绪标签化表演；戏剧化档的表，是峰值被压平、或者演成一个定格姿势。

**用在**：写 THE BEAT 和 ACTING 段时，先按档位挑表，再组合写法；克制档的「not ...」放在 THE BEAT 或 negative 里。

**别这样写**：intense, emotional, powerful performance——这些词既不说明档位，也不说明动作，只会把画面推向标签化。

---

## 3. 眼睛

### 视线目标 Eyeline target

**写法**：

```text
She looks at his hands, not his face. At 3s her eyes lift to his face for one second,
then drop back to his hands.
```

**防什么误读**：模型让人物直视对方或平视前方。视线落在哪，是表演里信息量最大的部分。

**用在**：所有有两人以上的镜头；反应镜（`storyboard/shot-functions.md` 反应）。

**别这样写**：she looks at him meaningfully。

### 不看镜头 No eye contact with the lens

**写法**：

```text
Nobody looks into the lens at any point. Her eyeline stays just off the camera's left
edge, toward where he sits.
```

**防什么误读**：模型非常容易让人物突然直视镜头，尤其在近景和镜头开头结尾。

**用在**：所有叙事镜头（除非有意打破第四面墙）。长提示词里写在 ACTING 段，必要时进总锁。

**别这样写**：只在 negative 里写 looking at camera，正文不给视线目标。

### 眨眼与凝视 Blinks

**写法**：

```text
Natural blinking at a normal rate. During the long look at 4–7s she does not blink;
she blinks once, slowly, as she turns away.
```

**防什么误读**：模型的人物要么不眨眼（像蜡像），要么眨得机械。不眨眼的那几秒本身就是表演。

**用在**：所有近景。凝视的时候，用「这几秒不眨」来加压。

**别这样写**：不写眨眼，导致整段像照片。

---

## 4. 嘴与说话

### 只有说话的人动嘴 Only the speaker's lips move

**写法**：

```text
Only Wen's lips move when he speaks. Jia listens with her mouth closed; she does not
mouth along, does not murmur.
```

**防什么误读**：多人画面里所有人一起动嘴，或者听的人在默念。这是多人对白最常见的失败。

**用在**：所有两人以上、有台词的镜头。关键时标 CRITICAL，并进总锁。另见 `references/drama/07-segment-prompt.md` 的口型部分。

**别这样写**：只写台词，不写谁在说、谁闭嘴。

### 台词的表演标注 Delivery cue

**写法**：

```text
Qiaosheng (choking, faster with each word, hands still on the chain): "Let me pass...
I beg you, let me pass! She is the one I came for!"
```

**防什么误读**：只给台词原文，模型用平均语气念出来，脸也跟着平；在台词里逐字加语气，有的模型会把标注当字幕画出来。

**用在**：每句台词。格式是「角色（语气、节奏、正在做的动作）：台词」（Seedance 2.5 官方格式「角色台词（情绪）：内容」）。语气写声音怎么变：哽咽、越说越急、压低、最后一个字破音。说话期间不要再写点头、转头，这类动作会和口型抢（Seedance 社区经验）。先配音再生成时，同样的标注写进语音模型的音频标签，见 `references/aigc/workflow.md`。

**别这样写**：Qiaosheng: "Let me pass."——没有语气，也没有他在做什么。

### 声音性反应 Vocal reactions

**写法**：

```text
Liancheng gasps, a short sharp intake of breath; then a sob breaks out of her before
she can speak. Qiaosheng laughs once through his tears.
```

**防什么误读**：模型的人物只在有台词时出声，其余时间是哑的；情绪最满的时候反而没有声音，像默剧。

**用在**：惊、哭、笑、喘、喊名字。声音性反应也算对白，写进分镜的台词 / 声音栏，计入「默剧检验」（`references/writing/dialogue.md` §0）。克制档才改成屏住呼吸。

**别这样写**：she reacts emotionally——不写发出什么声音。

### 没说出口的话 Words held back

**写法**：

```text
She opens her mouth to answer, stops, and closes it again. No sound comes out.
She looks down.
```

**防什么误读**：模型会把「欲言又止」演成说了半句话，或者无声地说完一整句。

**用在**：犹豫、压抑、权力关系里的退让。

**别这样写**：she almost says something。

### 说话时身体在做什么 Business while speaking

**写法**：

```text
He says the line while folding the shirt, not looking at her. He keeps folding after
the line ends.
```

**防什么误读**：模型的人物说话时一动不动，正对对方，像在念稿。

**用在**：日常对白。一边做事一边说，台词才像生活里说的话。

**别这样写**：he says calmly——副词代替行为。

---

## 5. 身体

### 微动作 Micro-actions

**写法**：

```text
Small, contained movements only: she turns the ring on her finger once; her weight
shifts from one foot to the other; she tucks a strand of hair behind her ear.
```

**防什么误读**：模型的身体表演偏大：手势夸张、走来走去。

**用在**：等待、对峙、倾听。一镜选一两个微动作，不要列一串。

**别这样写**：列五六个小动作，模型会全部做一遍，像在抽搐。

### 停住 Freeze mid-action

**写法**：

```text
She is reaching for the cup when he says her name. Her hand stops in the air,
an inch from the cup, and stays there.
```

**防什么误读**：模型演「震惊」时会加后退、捂嘴。真实的反应往往是动作停住。

**用在**：听到坏消息、被抓住、意识到真相。

**别这样写**：she is shocked。

### 呼吸 Breath

**写法**：

```text
Her breathing is visible in her shoulders: quick and shallow at first, slowing down
by the end of the shot.
```

**防什么误读**：人物像不呼吸。呼吸的变化是情绪变化最可信的外在表现。

**用在**：情绪近景、动作之后、等待结果。

**别这样写**：heavy breathing（模型会演成喘气）。

### 倾听 Listening

**写法**：

```text
While she talks, he listens: still, eyes on her, a small nod at 3s, no other movement.
He is taking it in, not waiting for his turn to speak.
```

**防什么误读**：听的人要么完全僵住，要么在做与戏无关的动作。

**用在**：反应镜、过肩镜里前景的人。听的人要被那句话改变：写清听到哪个词时他变了、变成什么（手松开、呼吸停住、眼眶红了）。听者和说话的人写在同一条 prompt 里；台词说到一半，可以把镜头留在听的人脸上。

**别这样写**：he reacts——不写怎么反应。

---

## 6. 群像与非主角

### 背景人物的行为 Background behaviour

**写法**：

```text
The other passengers keep to themselves: one reads, one sleeps against the window,
one scrolls a phone. None of them look at the couple. Nobody reacts to the argument.
```

**防什么误读**：模型的背景人物会集体看向主角，或者全部一起做同一个动作。

**用在**：公共空间里的私人戏。人群调度见 `video-prompt/one-take.md` 人群一节。

**别这样写**：busy background——模型会让背景很忙，抢走注意力。

### 儿童与动物 Children and animals

**写法**：

```text
The child is genuinely distracted, playing with the zip of her coat, only half
listening. She does not look at the adults when they argue.
```

**防什么误读**：模型的孩子像小大人：表情成熟，精准地配合剧情。

**用在**：家庭戏。孩子和动物写得越「不配合」，越真实。

**别这样写**：the child looks sad, understanding everything。

---

## 7. 常见问题

| 问题 | 原因 | 改法 |
|---|---|---|
| 演得像肥皂剧 | 只写了情绪词、副词，没写档位 | 选档位；换成行为 + 情绪轨迹，克制档加「不是什么」 |
| 呆、像默剧 | 只写动作没写意图；没写听者；把峰值场也压成了克制 | 写这一拍要什么、对谁做；加动作 → 反应；峰值改戏剧化档，加声音性反应 |
| 人物直视镜头 | 没给视线目标 | 写看谁、看哪；ACTING 段写不看镜头 |
| 两个人一起动嘴 | 没写谁闭嘴 | 只有说话的人动嘴；进总锁 |
| 像蜡像 | 没有眨眼、呼吸、微动作 | 自然眨眼 + 一个微动作 + 呼吸 |
| 被骗的人提前知道 | 没写信息差 | 写谁知道、谁不知道 |
| 背景人物看主角 | 默认围观 | 写他们各自在做什么、不看主角 |

## 来源

见 `video-prompt/sources.md`。
