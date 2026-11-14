# 配方：追逐

## 这场戏要什么

观众要始终知道三件事：**谁追谁**、**距离在缩短还是拉开**、**前面有什么障碍**。追逐的紧张来自距离的变化，不来自镜头晃得多厉害。

**方向是追逐的生命线**：逃的人和追的人在屏幕上朝同一个方向跑（比如都从左往右），观众才读得出「在追」。方向一反，观众会以为两人迎面相撞（`craft/visual/01-shot-grammar.md` 屏幕方向）。追逐常用交叉剪接在两条线之间来回（《电影镜头入门》Step7「交叉剪接」）。

## 默认序列（8 镜，约 25 秒）

| # | 景别 / 角度 / 运动 | Q | 生成 | 时长 |
|---|---|---|---|---|
| 1 | 远景，逃者从画左跑向画右，镜头横移跟 | 方向与环境 | 场景图 + 人物参考，首帧生视频 | 3 s |
| 2 | 前引中景：逃者朝镜头跑，镜头后退 | 逃者的脸：恐惧 | 首帧生视频 | 3 s |
| 3 | 后跟：跟在追者肩后 | 追者看到什么（逃者在前方） | 首帧生视频 | 3 s |
| 4 | 远摄压缩：两人在同一画面，追者在后 | 距离有多近 | 关键帧先行，两人同框要锁位置 | 3 s |
| 5 | 主观或中景：前方出现障碍（人群、栅栏、死路） | 新问题 | 首帧生视频 | 2 s |
| 6 | 插入特写：脚、手抓住栏杆、撞翻的东西 | 动作的峰值 | 首帧生视频，动作单一 | 1–2 s |
| 7 | 手持中景：逃者越过障碍或转向 | 怎么解决 | 首帧生视频；动作大，景别放宽 | 3 s |
| 8 | 远景或俯拍：两人的距离结果（甩掉 / 被抓住） | 结果 | 首帧生视频 | 3 s |

**排法要点**

- 远景（1、8）管方向和距离，近景（2、6）管情绪和峰值，中间交替。
- 每 2–3 镜给一个新障碍或新距离信息，否则只是在重复「他在跑」。
- 节奏靠剪辑：镜头越来越短（3 秒 → 2 秒 → 1 秒），不靠每镜都换运镜。
- 剪辑点落在动作上：脚落地、转身、出画（`craft/staging/04-coverage.md`）。

## 示例（模式 A）

场景：夜市。林晚抱着文件逃，两名保镖在追。

```text
1 | Wide shot of the crowded night market, the camera tracking sideways: Lin runs from frame left to frame right through the stalls, clutching a folder to her chest.
2 | Leading medium shot: Lin runs straight toward the camera as it moves backward ahead of her; lantern light streaks across her face; she glances back over her right shoulder.
3 | Following shot close behind the first bodyguard's shoulder, handheld, restless shake: far ahead, Lin's figure weaves between the stalls.
4 | Long telephoto lens from far ahead, compressed: Lin runs toward the camera, the two bodyguards close behind her, the crowd squeezed flat between them.
5 | Medium shot: at the end of the alley, a delivery truck backs across the exit, blocking it.
6 | Insert: Lin's hand slaps onto a stall's metal shelf and swings her body sideways.
7 | Handheld medium wide shot: Lin ducks under the stall's awning and out the other side, oranges spilling across the ground.
8 | High angle wide shot, static: the bodyguards stop at the spilled fruit, looking left and right; Lin is gone.
```

## 变体

### 车辆追逐
- 加两种车载机位：车头对着司机（看脸）、车外低机位贴地横移（看速度）。
- 速度感来自前景擦过（路灯、车流、行人）和远摄压缩，不来自模型画的「高速」。
- 生成：车身外观靠参考图锁定；碰撞和翻滚做不稳，用插入特写 + 声音 + 结果镜代替过程。

### 屋顶 / 跑酷
- 加一个航拍或高机位远景交代高度；跳跃用低角度仰拍，落地用插入特写。
- FPV 跟随跳跃很有冲击力，但人物身份会漂，放在身份已经交代清楚之后（`camera/lexicon-move.md`「FPV」）。

### 慢追 / 跟踪
- 追者不跑，只是跟着：长焦远距离 + 前景遮挡，交叉剪接逃者回头张望。属于悬疑，见 `suspense.md`。

## 竖屏 / 短剧

- 竖屏的横向运动空间窄，追逐改成**纵深方向**：朝镜头跑（前引）、远离镜头跑（后跟）、上下楼梯。
- 一个 15 秒片段只放一个子场景：夜市一段、小巷一段；不要在一个片段里跨两个地点。
- 枚举：`wide` + `tracking`；`medium` + `tracking`；`full` + `handheld`。远摄压缩落 `wide` + `static`，在镜头描述里写「两人在同一画面，追者紧贴在后」。

## 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 两人方向相反，读成迎面 | 每镜各写各的方向 | 每镜都写「从画左跑向画右」或「朝镜头跑」，全场统一 |
| 跑步动作变形、腿打结 | 动作复杂 + 景别太近 | 跑步用中景以上；脚部单独做插入特写 |
| 人物在跑动中换脸 | 运动幅度大、时长长 | 每镜 2–3 秒；脸的镜头用前引（脸稳定朝向镜头） |
| 所有镜头都晃 | 每镜都写手持 | 只在追者视角和越过障碍时用手持，远景固定或平稳横移 |
| 不知道距离多远 | 两人从不同框 | 至少一个两人同框的远摄压缩镜头 |

## 可借的档案

- `directors/george-miller.md`：动作始终保持在画面中心，剪辑再快观众也不丢失焦点。
- `directors/john-woo.md`：慢动作峰值与正常速度交替。
- `directors/johnnie-to.md`：都市夜间的追逐，用空间几何代替快切。
- `cinematographers/hoyte-van-hoytema.md`：实感的车载与贴地机位。

## 来源

见 `camera/sources.md`。
