# 摄影机行为：把摄影机写成一个人

运镜的名字（推、摇、跟、环绕）在 `camera/lexicon-move.md`。这份文件解决另一个问题：**在长提示词里，怎么让模型照你的意思去动摄影机，而不是给出它的默认运动。**

模型的默认是「有一个看不见的稳定器，一直在缓慢漂移」。不管你写的是固定还是手持，它都容易往这个默认滑。对付它有两个办法：

1. **把摄影机写成一个有身体、有反应、有动机的操作员**：他站在哪、跟着谁、什么时候反应慢半拍、什么时候停下。模型对「人怎么拿机器」的理解，比对运镜术语的理解稳得多。
2. **把不动写死**：静止不是「不写运动」，而是明确写出不漂、不呼吸、不微推。

每条四个字段：**写法**（英文提示词片段）、**防什么误读**、**用在**、**别这样写**。

---

## 1. 静止

### 锁死的固定机位 Locked-off

**写法**：

```text
Locked-off on a tripod. The frame does not move at all: no drift, no slow push,
no micro-shake, no reframing. Only the people move inside the frame.
```

**防什么误读**：模型把 static shot 理解成「几乎不动」，加一点缓慢推近或漂移，画面像在呼吸。

**用在**：对白、观察、喜剧（构图本身就是笑点时）、需要后期拼接或合成的镜头。

**别这样写**：只写 static camera；或者在同一段又写了 cinematic movement。

### 全段静止、单镜例外 All locked except one

**写法**：

```text
CAMERA: Every shot is locked-off on a tripod, except shot 4.
Shot 4 only: a slow push-in from medium to close-up over 4 seconds, starting when
she stops talking, ending on her eyes.
```

**防什么误读**：多镜头段落里只给某一镜写了运动，模型把运动传染给所有镜头。

**用在**：整场固定、只在情绪转折那一镜动一下（`storyboard/breakdown.md` 场 5 的 5-11 就是这样）。

**别这样写**：把例外写在逐镜时间线里却不在 CAMERA 段声明，模型以为全段都在推。

---

## 2. 手持：写成操作员

### 贴身跟随的操作员 Operator on the shoulder

**写法**：

```text
Handheld, an operator walking half a step behind her right shoulder, matching her pace.
When she stops, the camera overshoots slightly and settles. When she turns her head,
the operator reacts a beat late.
```

**防什么误读**：只写 handheld，模型给出两种极端：几乎不动，或者剧烈晃成灾难片。

**用在**：紧张的跟随、纪实感、人物在陌生空间里移动。

**别这样写**：shaky cam、chaotic handheld——模型会加夸张抖动，脸都看不清。

### 呼吸式手持 Breathing handheld

**写法**：

```text
Handheld but almost still: the operator stands braced, the frame breathing slightly
with their breath, a gentle sway of a few pixels. No sudden moves.
```

**防什么误读**：想要「活着的静止」（比固定多一点人味），模型要么锁死，要么晃。

**用在**：亲密对白、情绪近景、纪实风格的静态镜头。

**别这样写**：subtle handheld 不加任何参照——「多 subtle」模型无从判断。

### 反应慢半拍 Late reaction

**写法**：

```text
The camera does not know what will happen. When the glass falls, the operator whips
toward the sound a moment after it hits the floor, losing focus briefly, then finding it.
```

**防什么误读**：模型的摄影机总是「预知」：动作还没发生，镜头已经在等着。纪实感正来自摄影机的不预知。

**用在**：突发事件、伪纪录片、追逐里的意外。

**别这样写**：the camera captures the moment perfectly——这就是预知。

### 操作员的视线 Operator's attention

**写法**：

```text
The operator is watching the boy, not the mother. Even while she speaks, the frame
favours him, drifting back to his face whenever he moves.
```

**防什么误读**：手持镜头里谁说话就对准谁，失去视点。写清操作员关心谁，镜头就有了立场。

**用在**：视点要跟某个人、但他不说话的戏（观众站在他这一边）。

**别这样写**：同时写「跟着她」和「捕捉每个人的反应」。

---

## 3. 有动机的运动

### 跟着动作开始和停下 Motivated start and stop

**写法**：

```text
The camera holds still until he stands. As he rises, it rises with him, stopping
exactly when he is fully upright. It does not move again.
```

**防什么误读**：模型的运动从第 0 帧开始、到最后一帧还在动，和画面里的动作无关。

**用在**：所有运动镜头。运动要有起点（谁的动作触发）和终点（停在哪）。

**别这样写**：the camera slowly moves up——没有起止，模型均速动满全程。

### 推近要有落点 Push with a destination

**写法**：

```text
A slow push-in, starting at 1s from a medium shot, ending at 4s on a close-up of
her hands on the letter. The push stops; the last second is still.
```

**防什么误读**：推近不停，最后一帧还在推，接下一镜时运动断掉。

**用在**：揭示、情绪加压、注意力引导。

**别这样写**：dramatic push-in——模型会推得过快过深。

### 揭示的路径 Reveal path

**写法**：

```text
The camera starts on the kettle in close-up, then pans right slowly, following the
steam, until the woman sitting at the table enters frame. It stops with her centred.
```

**防什么误读**：揭示镜头里，被揭示的东西从第一帧就在画里，揭示失效。

**用在**：先物后人、先局部后整体、悬疑的延迟信息。

**别这样写**：revealing the woman——不写她一开始在画外。

### 平行跟随的距离 Fixed distance tracking

**写法**：

```text
Tracking alongside her at a constant distance of about two metres, camera at her
shoulder height, keeping her in a medium shot the whole way. The background slides
past; her size in frame never changes.
```

**防什么误读**：跟随镜头里人物忽大忽小（摄影机速度和人不同步）。

**用在**：走路对白、平行追逐、人物穿过空间。

**别这样写**：dynamic tracking shot。

---

## 4. 焦段、视野与机位

### 焦段写成视野 Lens as field of view

模型对 mm 数字的理解不稳，**同时写数字和视野效果**。焦段的作用与可靠性见 `camera/lexicon-shot.md` 焦段一节；这里是写进提示词时的对照：

| 焦段（全画幅等效） | 大约水平视野 | 提示词里同时写 |
|---|---|---|
| 18–24mm | 约 74°–90° | wide, deep space, things near the lens look large, walls lean slightly |
| 28–35mm | 约 54°–65° | moderate wide, the room and the person both read |
| 40–50mm | 约 40°–48° | natural perspective, like standing in the room |
| 75–85mm | 约 24°–27° | tight, face flattering, background soft and close |
| 100–135mm | 约 15°–20° | compressed, background flattened right behind the subject |
| 200mm 以上 | 约 10° 以下 | extreme compression, distant layers stacked into one plane |

视野数值是 36mm 宽画幅的近似值，用来帮助选择，不必写进提示词。

**写法**：

```text
85mm equivalent: tight, the face flattering, the dark office behind her soft and
pressed close.
```

**防什么误读**：只写 close-up，模型用广角贴近拍，脸变形；只写 85mm，透视效果不到位。

**用在**：每个有景别要求的镜头。

**别这样写**：焦段和景别矛盾（24mm tight portrait）；同一镜写两个焦段。

### 焦段锁 No zoom, no breathing

**写法**：

```text
Focal length is fixed within each shot: no zoom, no lens breathing, the size of the
background does not change unless the camera physically moves.
```

**防什么误读**：模型在镜头中段偷偷变焦，背景忽大忽小。

**用在**：所有不需要变焦的镜头；长提示词里写一次，在 LENS 段。

**别这样写**：只写 no zoom，又在逐镜里写 the frame tightens on her（模型会用变焦去实现）。

### 机位高度 Camera height

**写法**：

```text
Camera at the eye level of a seated person, about 1.1 metres, level, no tilt.
```

**防什么误读**：模型默认站立的人的眼平。人物坐着时，镜头就成了俯视，关系被改写。

**用在**：坐着的对白、儿童、动物、地面上的动作。机位高度的意义见 `camera/lexicon-shot.md` 角度一节。

**别这样写**：只写 eye level，却不写谁的眼平。

### 焦点行为 Focus behaviour

**写法**：

```text
Shallow focus on her eyes. When he enters behind her at 3s, the focus stays on her;
he remains a soft shape until he speaks at 5s, then the focus shifts to him over
half a second.
```

**防什么误读**：模型的焦点要么全清，要么随机转焦。焦点转移本身是一种剪辑，写清触发和速度。

**用在**：前后景关系、注意力转移、两人同框不切镜。

**别这样写**：rack focus between them——不写何时、为什么、多快。

---

## 5. 风格化的摄影机

### 监控视角 Surveillance view

**写法**：

```text
A fixed high-angle security camera view from the corner of the ceiling, wide lens with
slight barrel distortion, no camera movement at all. Flat, slightly greenish image.
No timestamp, no on-screen overlay.
```

**防什么误读**：模型会自动加时间戳和 REC 字样（属于画面文字），也会让监控镜头运动。

**用在**：悬疑、证据画面、冷观察。

**别这样写**：CCTV footage——模型会加满屏界面元素。

### 第一人称 First person

**写法**：

```text
Point of view: we are him. His own hands enter frame from the bottom as he reaches for
the door. The view moves with a walking rhythm, slight up-and-down with each step.
We never see his face.
```

**防什么误读**：模型把 POV 拍成第三人称的过肩，或者把「他」画进画面。

**用在**：主观镜头、视线对象（`storyboard/shot-functions.md`）。

**别这样写**：POV shot of the room——不写身体的参照，模型拍成普通空镜。

### 车载与固定在身体上 Mounted camera

**写法**：

```text
Camera rigidly mounted on the car's dashboard, facing the driver. The car moves; the
camera does not move relative to the car. The street slides past the side windows.
```

**防什么误读**：车内镜头里摄影机自己在车里飘，像无人机在车厢里。

**用在**：车内对白（`storyboard/scene-types.md` 车内戏）、身体固定的主观眩晕感。

**别这样写**：只写 inside a moving car。

---

## 6. 常见问题

| 问题 | 原因 | 改法 |
|---|---|---|
| 全段都在缓慢漂移 | 没有写死静止；或某一镜的运动传染了 | CAMERA 段写全段静止 + 例外；静止写「no drift, no push」 |
| 手持晃成一团 | 写了 shaky / chaotic | 写操作员的身体和反应，给出幅度参照 |
| 运动和动作无关 | 没写起止 | 写触发动作和停点 |
| 推近推过头 | 没写落点 | 写起止景别和时间 |
| 脸变形 | 广角拍特写 | 焦段 + 视野效果一起写 |
| 坐着的人被俯拍 | 默认站立眼平 | 写「坐着的人的眼平」 |
| 摄影机像在预知 | 模型默认完美构图 | 写反应慢半拍、短暂失焦 |

## 来源

见 `video-prompt/sources.md`。
