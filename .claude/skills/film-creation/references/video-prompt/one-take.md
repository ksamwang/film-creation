# 一镜到底与调度：摄影机路径和人群

一镜到底是提示词里最难的形式。多镜头段落可以靠切点重置一切；一镜到底没有切点，摄影机的位置、人物的位置、光的变化都要连续，任何一处漂移观众都看得见。

对模型来说，一镜到底的难点是：**它不知道摄影机下一秒该去哪。** 只写「一镜到底跟着她穿过餐厅」，模型会给出一段漫无目的的漂移。要写的是一条**路径**：摄影机经过哪些点、在每个点看到什么、为什么从这里移到那里。

运镜本身的写法与可靠性见 `camera/lexicon-move.md` 长镜头一条；拆法上的取舍见 `storyboard/three-ways.md`。

---

## 1. 路径设计

**第一步：定路点**

把一镜到底拆成 3–6 个**路点**（waypoint）。每个路点写：

| 字段 | 内容 |
|---|---|
| 时间 | 摄影机到达这个点的时间码 |
| 位置 | 摄影机在空间里的位置和高度 |
| 构图 | 这一刻画面里是谁、什么景别 |
| 看到什么 | 观众在这一刻得到的信息 |
| 动机 | 是什么让摄影机离开这里、去下一个点 |

动机是关键。摄影机的每一次移动，都要由**画面里的东西**触发：一个人走开、一个声音、一个视线。没有动机的移动，就是模型默认的漂移。

**第二步：写交接**

两个路点之间，摄影机从**跟一个人**换到**跟另一个人**的那一刻叫交接。交接写清三件事：交出的人往哪走、接手的人从哪来、两人在画面里擦肩的那一刻摄影机做什么。

```text
At 9s the waiter passes the bride's mother coming the other way. The camera lets the
waiter go out of frame left and turns with the mother, following her now.
```

**第三步：写空间和光的变化**

摄影机穿过不同空间时，光、声音、人的密度都会变。在路点里写清楚，模型才不会把三个空间渲染成同一种光。

**第四步：写节奏**

一镜到底也有节奏：快走、停顿、慢慢靠近。路点之间的时间不要平均分配；在信息最重要的路点上停留更久。

**第五步：控制长度**

- 一次生成的长度受模型上限限制（多数 10–15 秒）。更长的一镜到底要分段生成、用首尾帧续接（`references/aigc/workflow.md`），接缝藏在擦过前景遮挡物或快速横摇的那一刻。
- 路点越多，漂移风险越大。单次生成 3–4 个路点比较稳。

---

## 2. 人群调度

### 人群分层 Crowd in layers

**写法**：

```text
Three layers of people: in the foreground, two cooks working at the counter who never
look up; in the middle, waiters crossing left and right at a steady pace; at the far end,
a dishwasher with her back to us.
```

**防什么误读**：模型的人群要么是一堵站着的墙，要么全体随机走动；路径被人挡住。

**用在**：餐厅、街道、聚会、车站。按前景、中景、背景写人在做什么。

**别这样写**：a busy crowd。

### 人群让路 Crowd makes way

**写法**：

```text
As the camera moves through, people step aside naturally to let the waiter pass —
they do not notice the camera. Nobody looks into the lens.
```

**防什么误读**：摄影机穿过人群时，路人看向镜头或者被摄影机「穿过」（穿模）。

**用在**：所有摄影机在人群中移动的镜头。

**别这样写**：the camera weaves through the crowd——没写人群怎么反应。

### 人群的方向 Crowd direction

**写法**：

```text
The guests in the hall are all facing the stage, frame right. Only the bride, near the
door, has turned the other way, looking back at the kitchen doors.
```

**防什么误读**：人群朝向随机，主角没有被区别出来。让人群朝一个方向，主角朝另一个方向，观众的眼睛自然落在主角身上。

**用在**：要在人群中找出一个人的时候。

**别这样写**：the bride stands among the guests。

### 人群的反应 Crowd reaction

**写法**：

```text
When the tray crashes at 14s, the nearest three guests turn toward the sound; the rest
of the hall, further away, keeps talking for another second before the noise reaches
them, then a wave of heads turns.
```

**防什么误读**：模型的人群对事件的反应整齐划一，所有人同时转头，像约好的。

**用在**：意外事件、宣布、闯入。反应从近到远传开。

**别这样写**：everyone turns to look。

---

## 3. 示例：婚宴后厨到宴会厅（重型档片段）

**这场戏**：婚宴进行中。服务员小陈端着蛋糕从后厨出来，蛋糕里藏着新郎准备的戒指。新娘不知道。一镜到底 15 秒，从后厨跟着小陈，推开双开门进入宴会厅，镜头放开小陈，找到站在门边、回头张望的新娘。

**路点**：

| 时间 | 位置 | 构图 | 看到什么 | 动机 |
|---|---|---|---|---|
| 0s | 后厨，蛋糕前，胸口高度 | 小陈中景，双手端着蛋糕 | 他小心翼翼，蛋糕顶上的小盒子 | 他转身走 |
| 0–6s | 后跟，半步距离 | 他的背和肩，后厨在两侧滑过 | 后厨的忙乱，没有人注意他 | 他走向双开门 |
| 6–8s | 双开门 | 他用背顶开门，镜头跟进 | 光从冷白变成暖黄，声音变吵 | 门打开 |
| 8–11s | 宴会厅入口，摄影机停住 | 小陈从画右走远，宾客朝向舞台 | 宴会厅的规模 | 小陈走出画面，新娘在门边 |
| 11–15s | 慢慢左摇、轻推 | 新娘中近景 | 她回头望着后厨的门，不知道 | 结束 |

**提示词片段**（只列路径相关段落；其余段落按 `video-prompt/anatomy.md` 写）：

```text
EDIT: Single continuous shot, 15 seconds, no cuts.

CRITICAL — the camera is one operator moving through real space. It never jumps,
never teleports, never passes through people or walls.

CAMERA PATH:
0s — The camera is at chest height in the hotel kitchen, facing Chen, a young waiter
  in a white jacket. He holds a two-tier cake on a tray with both hands, a small velvet
  box on top. He is already turning away.
0–6s — The camera follows half a step behind his right shoulder as he walks the length
  of the kitchen. Cooks work on both sides, heads down; a porter crosses behind him.
  Chen walks carefully, the tray level. The camera matches his pace exactly.
6–8s — Chen reaches the double doors and pushes one open with his back, turning
  sideways to protect the cake. The camera follows him through the doorway.
  As it passes through, the light changes from cold kitchen white to warm amber,
  and the sound opens up from clattering pans to a hall full of voices.
8–11s — Just inside the hall the camera stops and holds. Chen keeps walking away,
  frame right, weaving between round tables toward the stage. All the guests face
  the stage, frame right. The camera lets him go.
11–15s — The camera pans slowly left, away from Chen, and drifts in slightly to find
  the bride standing near the door, frame centre, medium close-up. She has turned
  away from the stage and is looking back at the kitchen doors, curious. She does not
  see the cake. The camera settles and holds still on her for the last second.

CROWD: Guests are seated and talking, faces toward the stage. Waiters cross at a
steady pace. People step aside naturally for Chen. Nobody looks into the lens.
Nobody reacts to the camera.

LOCKS:
- One continuous shot, no cuts.
- The cake stays level and intact the whole time; the box stays on top.
- Chen exits frame right at about 11s and does not return.
- The bride is the only guest facing away from the stage.
- No music: the only sound is the hall's voices and cutlery.
```

**为什么这样写**：

- **每段路径都写了动机**：他转身、他走、门开了、他走出画面。摄影机从不自己决定去哪。
- **交接在 8–11s**：摄影机停住、让小陈离开，再摇向新娘；比在人群中硬转更稳。
- **门是光和声音的分界**：写出变化，模型才不会把后厨和宴会厅渲染成同一种光。
- **新娘是唯一背对舞台的人**：人群朝向制造对比，最后一个路点不用推得很近，观众也能找到她。
- **最后一秒静止**：给剪辑留落点，也方便续接下一段。

---

## 4. 常见问题

| 问题 | 原因 | 改法 |
|---|---|---|
| 摄影机漫无目的漂 | 没写路径 | 拆成路点，每段写动机 |
| 人物在路径中途位置跳 | 路点太多；交接没写 | 减到 3–4 个路点；写清交接 |
| 摄影机穿过人和墙 | 没写物理限制 | 写「一个操作员在真实空间里移动」 |
| 路人看镜头、挡路 | 没写人群反应 | 写人群让路、不看镜头 |
| 三个空间同一种光 | 没写变化 | 在路点里写光和声音的变化 |
| 长度超过模型上限 | 一次写太长 | 分段生成，首尾帧续接，接缝藏在遮挡处 |

## 来源

见 `video-prompt/sources.md`。
