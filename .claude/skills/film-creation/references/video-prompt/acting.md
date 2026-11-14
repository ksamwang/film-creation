# 表演指导：写给模型的戏

模型的表演默认是**放大**：难过就流泪，生气就皱眉瞪眼，开心就露齿大笑，坏人就冷笑。这些是它在训练数据里见得最多的「情绪标签」。真实的戏往往相反：情绪越大，动作越小。

所以给模型写表演，核心不是「写出情绪」，而是**写出可见的行为，同时封住模型对这种情绪的默认演法**。表演的判断原则在 `craft/performance/index.md`；这份文件是写进提示词时的词库。

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

---

## 2. 反误读：常见情绪的默认与改法

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

**防什么误读**：表里左列是模型最常见的情绪标签化表演。

**用在**：写 THE BEAT 和 ACTING 段时，按表里的写法组合；「not ...」放在 THE BEAT 或 negative 里。

**别这样写**：intense, emotional, powerful performance——这些词会把一切往左列推。

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

**用在**：反应镜、过肩镜里前景的人。

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
| 演得像肥皂剧 | 写了情绪词、副词 | 换成行为 + 不是什么 |
| 人物直视镜头 | 没给视线目标 | 写看谁、看哪；ACTING 段写不看镜头 |
| 两个人一起动嘴 | 没写谁闭嘴 | 只有说话的人动嘴；进总锁 |
| 像蜡像 | 没有眨眼、呼吸、微动作 | 自然眨眼 + 一个微动作 + 呼吸 |
| 被骗的人提前知道 | 没写信息差 | 写谁知道、谁不知道 |
| 背景人物看主角 | 默认围观 | 写他们各自在做什么、不看主角 |

## 来源

见 `video-prompt/sources.md`。
