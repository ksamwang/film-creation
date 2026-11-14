# 配方：打斗 / 动作

## 这场戏要什么

观众要读到：**谁占上风**、**每一击的结果**、**局势在哪一下翻转**。打斗是一场没有台词的对话：每个回合都有出招、接招和结果。

**生成层面的现实**：两个人肢体接触、快速交手，是视频模型最容易崩的内容——手脚穿模、多出肢体、脸在动作中漂移。所以打斗配方的核心是**拆**：每镜只做一个动作，接触的瞬间用剪辑完成，不让模型生成完整的交手过程。这和书里「剪在高峰瞬间、删掉不提供新信息的过程」是同一个原则（《电影语言的语法》第 2 章）。

## 默认序列：一个回合（7 镜，约 15 秒）

| # | 景别 / 角度 / 运动 | Q | 生成 | 时长 |
|---|---|---|---|---|
| 1 | 全景，平视，固定 | 两人的距离和架势 | 场景图 + 两人参考，关键帧先行 | 2–3 s |
| 2 | 中景 A：出招的起势 | 谁先动 | 首帧生视频，只做起势 | 1–2 s |
| 3 | 插入特写：拳 / 刀 / 脚的轨迹 | 攻击 | 首帧生视频或首尾帧；单一动作 | 1 s |
| 4 | 中景 B：格挡或被击中的结果 | 结果 | 首帧生视频，从受力开始 | 1–2 s |
| 5 | 低角度 B 反击：起身、反扣 | 翻转 | 首帧生视频 | 2 s |
| 6 | 慢动作峰值：一击命中的瞬间 | 决定性的一下 | 首帧生视频，正常速度生成，后期放慢 | 2 s |
| 7 | 全景或俯拍：一方倒地，另一方站着 | 回合结果 | 首帧生视频 | 2–3 s |

**排法要点**

- **出招和结果分两镜**：A 挥拳在一镜，B 被击中在下一镜；接触点藏在剪辑里。这是动作片的传统做法，也正好绕开模型的弱点。
- 全景（1、7）每个回合至少出现一次，让观众知道两人的位置关系；只有近景的打斗观众会看不懂。
- 权力变化用角度表现：占上风的一方仰拍，处下风的一方俯拍；翻转时交换（`camera/intent.md`「权力反转」）。
- 慢动作只给一个回合的峰值，整场慢动作等于没有峰值。

## 示例（模式 A）

场景：地下停车场。顾言的保镖拦住林晚的哥哥林泽。

```text
1 | Full shot at eye level, static: the bodyguard at frame left and Lin Ze at frame right face each other three meters apart between two parked cars; fluorescent light overhead.
2 | Medium shot of the bodyguard: he steps forward and draws his right fist back. Static.
3 | Insert, slightly low: the fist swings from frame left toward the camera. One fast motion.
4 | Medium shot of Lin Ze: his forearm is already up, the impact snaps his head slightly to frame right; he slides back half a step.
5 | Low angle medium shot: Lin Ze straightens, grabs the bodyguard's wrist with both hands and twists it outward.
6 | Medium close-up: Lin Ze's elbow drives into the bodyguard's ribs; the bodyguard folds forward.
7 | High angle full shot, static: the bodyguard on one knee by the car door, Lin Ze standing over him, breathing hard.
```

第 6 镜生成正常速度，剪辑时放慢峰值那 10–15 帧。

## 变体

### 一对多
- 中心人物固定在画面中心，对手轮流从画面边缘进入；每个对手一个回合，一个回合 2–3 镜。
- 远景先交代所有人的位置，之后每个回合前回一次远景。

### 武器
- 刀剑、棍棒的轨迹用插入特写；兵器接触的火花和声音在后期加。
- 枪战：开枪（枪口特写）→ 结果（命中、玻璃碎）→ 反应，三镜一组；枪口火光生成不稳，后期补。

### 长镜头打斗
- 走廊式的一镜到底：横移跟随，人物在纵深里推进。
- 生成做不出完整长镜头，拆成多段续接，接点藏在人物从镜头前挡过或镜头被撞的瞬间（`camera/lexicon-move.md`「长镜头」）。

### 余波
- 打斗结束后的固定长镜头：喘息、血迹、碎掉的东西。很多时候余波比打斗本身更有分量，也最容易生成。

## 竖屏 / 短剧

- 竖屏打斗以中景和中近景为主，全景只用来交代开打和结束。
- 短剧的打斗常常是「一招制敌」：起势 → 一击 → 对方倒地 → 主角整理袖口，4 镜就够；重点在旁观者的反应镜，见 `reversal.md`。
- 枚举：`full` + `static`；`medium` + `handheld`；`extreme_close` 做插入；慢动作在成片阶段做，不进片段提示词。

## 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 手脚穿模、多出一条胳膊 | 一镜里完成了接触 | 出招和结果拆两镜；接触在剪辑里发生 |
| 两人在交手中换脸 / 互换衣服 | 两人近距离纠缠 | 每镜只让一人是正脸；纠缠镜头放宽到全景 |
| 动作软绵绵 | 动作写得抽象（「激烈地打斗」） | 写具体动作：哪只手、从哪到哪、打到哪 |
| 动作被压成半秒一个 | 一镜写了太多动作 | 一镜一个动作，最多两个 |
| 观众看不懂谁赢了 | 只有近景 | 每个回合至少一个全景 |

## 可借的档案

- `directors/king-hu.md`：剪在动作的起点和终点，跳过中间过程——正好适合生成。
- `directors/john-woo.md`：慢动作 + 对称构图的枪战峰值。
- `directors/park-chan-wook.md`：横移的走廊打斗长镜头。
- `directors/takeshi-kitano.md`：省略暴力过程，只给之前的静止和之后的结果。
- `directors/akira-kurosawa.md`：动作前的长时间对峙，一击决胜负。

## 来源

见 `camera/sources.md`。
