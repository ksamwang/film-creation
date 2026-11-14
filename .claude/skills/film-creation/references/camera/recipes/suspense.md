# 配方：悬疑与揭示

## 这场戏要什么

悬疑的核心是**信息差**。先决定观众比人物知道得多还是少：

- **观众知道得多（悬念）**：观众看到了桌下的炸弹，人物不知道。紧张来自等待。镜头要把危险**给观众看**，再回到毫不知情的人物。
- **观众知道得少（惊奇 / 谜）**：观众和人物一样不知道门后是什么。紧张来自未知。镜头要**藏住**信息，只给人物的视线和反应。

两种拍法相反，混用会两头落空。一场戏先选一种。

镜头工具：主观镜头让观众和人物共享未知（《电影镜头入门》Step5 视点技巧；《电影镜头设计》第十六章）；后拉揭示和延时揭示让新信息在镜头里出现（《电影镜头入门》Step4「后拉揭示」「延时揭示」）；焦点转移让注意力在一个镜头里交接（`camera/lexicon-shot.md`）。

## 默认序列 A：潜入与发现（观众知道得少，7 镜）

| # | 景别 / 角度 / 运动 | Q | 生成 | 时长 |
|---|---|---|---|---|
| 1 | 远景，人物在门口，固定；画面大部分是暗的空间 | 她要进入哪里 | 场景图 + 人物参考，关键帧先行 | 3 s |
| 2 | 后跟：跟在她肩后进入房间，缓慢 | 我们和她一起看 | 首帧生视频 | 4 s |
| 3 | 主观镜头：手电光或视线扫过房间 | 她在找什么 | 首帧生视频；光的移动比镜头运动更稳 | 3 s |
| 4 | 中近景，她停住，视线落在画外某处 | 她看到了什么——先不给观众看 | 首帧生视频 | 2 s |
| 5 | 插入特写：证据（照片、血迹、打开的抽屉） | 发现 | 关键帧，字和细节在图阶段做对 | 2 s |
| 6 | 特写反应：她的脸 | 意义落到人物身上 | 首帧生视频，无台词 | 2–3 s |
| 7 | 回到远景，或她背后的门口出现一个人影 | 新威胁 / 新问题 | 首帧生视频；人影可以不清楚 | 3 s |

**排法要点**

- 第 4 镜**先给反应、后给证据**：观众先看到她看见了什么，再看到是什么。延迟就是悬念。
- 主观镜头前后都要有「她在看」的镜头夹住（4 → 5 → 6），否则观众不知道这是谁的眼睛。
- 黑暗里的空间要有可读的轮廓：一个光源（手电、门缝、窗外路灯），其他地方暗下去（`craft/visual/04-light.md`）。
- 最后一镜留一个问题，不要把所有信息都给完。

## 默认序列 B：危险在场（观众知道得多，6 镜）

| # | 景别 / 角度 / 运动 | Q | 生成 | 时长 |
|---|---|---|---|---|
| 1 | 中景，人物在做日常的事（倒茶、看手机） | 毫不知情 | 首帧生视频 | 3 s |
| 2 | 插入特写：危险（杯里的药、门外的人、松动的刹车） | 观众知道了 | 关键帧 | 2 s |
| 3 | 中景，人物继续，离危险更近一步 | 等待 | 首帧生视频 | 3 s |
| 4 | 前景遮挡：透过百叶 / 门缝看她，长焦 | 有人在看 | 首帧生视频，固定或慢变焦 | 3 s |
| 5 | 特写：她的手伸向杯子 | 拉长的瞬间 | 首帧生视频，可放慢 | 2–3 s |
| 6 | 打断或得手：电话响 / 她喝下 | 释放或爆发 | 首帧生视频 | 2 s |

**排法要点**

- 危险镜头（2）要尽早给，越早给，等待越长。
- 之后在人物和危险之间交替，每次回到人物，她都离危险近一步。
- 节奏和追逐相反：镜头越来越**长**，而不是越来越短。

## 示例（模式 A，序列 A）

场景：深夜，林晚潜入顾言的书房。

```text
1 | Wide shot, static: the study door at frame right opens a crack; Lin slips in, a dim strip of hallway light behind her; the rest of the room is dark.
2 | Following shot close behind Lin's shoulder, slow and steady: she moves past the bookshelves toward the desk, the beam of her phone light leading the way.
3 | Point-of-view shot: the phone light sweeps slowly across the desk, papers, a closed laptop, and stops on a half-open drawer.
4 | Medium close-up of Lin, lit from below by the phone; she stops, her eyes fixed on something below frame. Static.
5 | Insert: inside the drawer, a hospital report with her mother's name on it, the date circled in red ink.
6 | Close-up of Lin, static: her breath stops; the light in her hand trembles slightly.
7 | Wide shot, static: behind Lin, the study door, which she had left open a crack, is now fully open; the hallway is empty.
```

## 变体

### 惊吓 Jump scare
- 慢节奏、长镜头、环境声逐渐消失 → 突然的硬切 + 巨响。
- 惊吓靠剪辑和声音，不靠画面：生成一个安静的镜头和一个「东西出现」的镜头，在剪辑里制造突然性。
- 一场最多一次，紧接着给一个「虚惊」或真威胁的结果。

### 跟踪
- 长焦远距离 + 前景遮挡（车窗、人群、报摊），交叉剪接被跟踪者偶尔回头。
- 被跟踪者回头时，跟踪者正好被路人挡住——遮挡就是剪辑点。

### 真相揭示
- 后拉揭示：从一个细节拉开，落幅改变了整件事的意义（`camera/lexicon-move.md`「后拉揭示」，首尾帧）。
- 或者焦点转移：前景的物证从虚到实，后景的嫌疑人从实到虚。

## 竖屏 / 短剧

- 竖屏的上下纵深适合悬疑：门在画面上方、人物在下方；人影从画面顶端出现。
- 证据插入镜（照片、聊天记录、报告）在短剧里很常见：字一定在图阶段做对，视频只给一个缓推；字还是变形就后期贴图。
- 枚举：`medium_close` + `static`（反应）；`extreme_close` + `push_in`（证据）；`pov` + `pan`（扫视）。

## 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 黑暗里什么都看不清 | 没写光源，或整个画面欠曝 | 写一个有动机的光源，画面里至少一块亮区 |
| 主观镜头里出现了她自己 | 模型把「她在看」画成了第三人称 | 主观镜头写 `from her eyes, she is not visible`，定帧 |
| 证据上的字乱码 | 视频模型画不好字 | 图阶段生成并修正，视频运动小；不行就后期贴 |
| 悬念不紧张 | 危险没有先给观众看 | 序列 B：危险插入镜放在前面 |
| 惊吓不吓人 | 惊吓之前节奏不够慢、声音不够静 | 之前加长镜头，抽掉环境声 |

## 可借的档案

- `directors/alfred-hitchcock.md`：先把炸弹给观众看——悬念与惊奇的经典区分。
- `directors/david-fincher.md`：冷静、精确、几乎不动的机位，让细节自己发出威胁。
- `directors/bong-joon-ho.md`：空间的上下层次（地下室、楼梯）承担危险。
- `directors/denis-villeneuve.md`：大面积暗部与远景里的小人物。
- `cinematographers/gordon-willis.md`：让脸沉进暗部，只露一部分。

## 来源

见 `camera/sources.md`。
