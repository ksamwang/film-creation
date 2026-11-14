# 物理与反 AI 质感

观众说一段视频「一看就是 AI」，指的通常不是画面不清楚，而是两类问题：

1. **物理发飘**：东西没有重量，动作没有惯性，人走路不落地，水像果冻，布料像塑料。
2. **质感太干净**：皮肤磨皮、表面无瑕、光线完美、所有东西都在最佳位置。

这两类问题都不能靠「realistic」「high quality」解决。要写**具体物件的具体物理**，和**这个空间里真实会有的不完美**。

每条四个字段：**写法**、**防什么误读**、**用在**、**别这样写**。

---

## 1. 重量与惯性

### 有重量的物件 Weight

**写法**：

```text
The suitcase is heavy: she has to lean back to lift it, it swings slightly as it comes
off the floor, and lands on the bed with a dull thump that bounces the mattress.
```

**防什么误读**：模型的物件没有重量，人单手拎起箱子像拎空纸盒。

**用在**：任何人和物件的交互。写**人的身体怎么对重量做出反应**，比写物件本身更有效。

**别这样写**：a heavy suitcase——只给形容词，不给身体反应。

### 惯性与停止 Inertia

**写法**：

```text
He shoves the door; it swings wide, hits the wall, and bounces back a little before
coming to rest half-open.
```

**防什么误读**：模型的运动在终点「刹住」，没有过冲和回弹。

**用在**：门、抽屉、摆动的灯、急停的人和车。

**别这样写**：the door opens——只写结果。

### 人的落地与重心 Footfall and balance

**写法**：

```text
Each step lands heel first and her weight transfers fully onto that foot. On the wet
stairs she slows, her hand finding the rail.
```

**防什么误读**：模型的人走路滑行、脚不落地、重心不跟着脚走。

**用在**：走路、跑、上下楼梯、在不平的地面上。

**别这样写**：she walks naturally。

---

## 2. 材料

### 液体 Liquid

**写法**：

```text
He pours too fast; the water rises to the rim and a little spills over, running down
the side of the glass and pooling on the table.
```

**防什么误读**：模型的液体像果冻，倒水不溅，杯里的水不晃，溢出的水凭空消失。

**用在**：倒水、碰杯、打翻、雨、眼泪（眼泪要写从哪流到哪）。

**别这样写**：pours water elegantly。

### 布料 Fabric

**写法**：

```text
Her linen shirt is creased from the day, the sleeve catching at the elbow when she
reaches. The coat is heavy wool; it swings late behind her when she turns.
```

**防什么误读**：模型的衣服像塑料或者像刚熨过，动作时布料不跟随。

**用在**：所有人物镜头。写面料（亚麻、羊毛、尼龙）比写颜色更能决定它怎么动。

**别这样写**：flowing dress——模型会让裙子飘得像在风洞里。

### 头发 Hair

**写法**：

```text
Her hair is tied back but a few strands have come loose; they stick to her damp
forehead and do not move.
```

**防什么误读**：模型的头发要么像头盔一样不动，要么在室内无风飘动。

**用在**：近景、动作戏、雨戏。写清有没有风，头发才知道该不该动。

**别这样写**：hair flowing in the wind（室内）。

### 烟、蒸汽与灰尘 Smoke, steam, dust

**写法**：

```text
Steam rises from the bowl in a thin column, bending away when she breathes out.
Dust drifts slowly in the window light; it is only visible inside the beam.
```

**防什么误读**：模型的烟雾是装饰性的、到处都是，不和光、气流互动。

**用在**：营造空气感、显示光束、显示时间流逝。

**别这样写**：atmospheric fog everywhere。

### 玻璃、镜面与倒影 Glass and reflections

**写法**：

```text
The window reflects the room faintly; her reflection is dimmer than she is and moves
exactly with her. Beyond the glass, the street is dark.
```

**防什么误读**：模型的倒影和本体不同步，或者倒影里多出别人，或者镜子里的人物长相漂移。

**用在**：车窗、镜子、橱窗、水面。倒影是多余人物和动作错乱的高发区，复杂的话改成避开反射的机位。

**别这样写**：dramatic reflection shot——让倒影成为主体，风险最高。

---

## 3. 接触

### 手与物件 Hands on objects

**写法**：

```text
Her fingers wrap fully around the mug handle; the knuckles whiten slightly as she
grips. When she lets go, the mug stays exactly where it was.
```

**防什么误读**：手和物件穿插、手指数目变化、松手后物件漂移或消失。

**用在**：所有手部动作。手部近景尽量一镜一个简单动作（拿起、放下），复杂的手部操作（打结、弹琴）高风险。

**别这样写**：her hands move skilfully over the keyboard——复杂手部动作 + 无具体动作。

### 人与人的接触 Touch between people

**写法**：

```text
He puts a hand on her shoulder; her cardigan dents under his fingers. She does not
lean into it.
```

**防什么误读**：模型的身体接触没有压力，像两张图层叠在一起；或者两个人的手臂融合。

**用在**：拥抱、握手、拉扯、扶。写接触点的变形（布料凹陷、皮肤被按压）。

**别这样写**：they embrace passionately——大幅度、多肢体接触，融合风险高。

### 物件不变形 Object permanence

**写法**：

```text
Objects keep their shape, number and position: the two cups stay two cups, the book
stays closed on the desk unless someone opens it. Nothing morphs, duplicates or
passes through anything else.
```

**防什么误读**：模型的物件在镜头中途变形、复制、消失、穿模。

**用在**：长提示词的 PHYSICS 段，写一次。最重要的道具在总锁里再写一次具体状态。

**别这样写**：只在 negative 里写 morphing。

---

## 4. 反 AI 质感

### 皮肤 Skin

**写法**：

```text
Natural skin: visible pores, slight unevenness of tone, a little shine on the nose
and forehead, fine lines around the eyes when she smiles. No airbrushing.
```

**防什么误读**：模型默认磨皮、蜡像脸、完美无瑕的肤色。

**用在**：所有人物近景。写实画风必写；动画画风按风格写。

**别这样写**：flawless skin、beautiful face——会把脸推向 AI 网红脸。

### 环境的使用痕迹 Signs of use

**写法**：

```text
The kitchen is lived in: a tea towel thrown over the oven door, a chipped mug,
water marks around the tap, a calendar a month out of date.
```

**防什么误读**：模型的空间像样板间：干净、对称、没有人生活过。

**用在**：所有室内场景。两三个具体的痕迹胜过「messy」。

**别这样写**：messy room——模型会堆满杂物。

### 不完美的光 Imperfect light

**写法**：

```text
The light is uneven: the far corner falls into darkness, the lamp's shade throws
a hard edge across the wall, and her face is slightly underexposed on the shadow side.
```

**防什么误读**：模型的光完美均匀，每个人都被打亮，没有死黑和过曝。

**用在**：写实画风的所有镜头。光的写法见 `camera/lexicon-light.md`。

**别这样写**：perfect cinematic lighting。

### 镜头质感 Lens character

**写法**：

```text
Slight softness toward the frame edges, gentle highlight bloom around the lamp,
fine grain in the shadows. Not digitally sharp.
```

**防什么误读**：模型的画面锐利到每根头发都清楚，像游戏渲染。

**用在**：要实拍质感时。和风格段一起写，不要和 8K / ultra detailed 同时出现。

**别这样写**：sharp, highly detailed, 8K。

### AI 质感速查 AI tells

**写法**：

```text
Avoid the AI look: no waxy skin, no glossy plastic surfaces, no perfectly symmetrical
faces, no overly saturated colours, no glowing rim light on everyone, no floating
camera drift.
```

**防什么误读**：这些是观众一眼认出 AI 的标志。

**用在**：放在 ATMOSPHERE 段末尾或 negative 里，只选和这场戏相关的几条。

**别这样写**：整份照抄进每条提示词——与这场戏无关的条目只会稀释注意力。

---

## 5. 常见问题

| 问题 | 原因 | 改法 |
|---|---|---|
| 东西像没重量 | 只写形容词 | 写人的身体怎么对重量反应 |
| 动作急停 | 没写惯性 | 写过冲、回弹、停下的过程 |
| 水像果冻 | 没写液体行为 | 写溅、晃、流到哪 |
| 衣服像塑料 | 没写面料 | 写面料和褶皱，写它怎么跟随动作 |
| 手指乱、穿模 | 复杂手部动作 | 一镜一个简单动作；写接触点 |
| 像样板间 | 默认干净 | 写两三个具体使用痕迹 |
| 脸像蜡像 | 默认磨皮 | 写毛孔、油光、细纹；删掉 flawless |

## 来源

见 `video-prompt/sources.md`。
