# 构图词典：位置、线条、层次、画框

字段与可靠性分级见 `camera/index.md`。构图为什么重要、取景句的四项写法（placement、angle、layer、horizon）见 `craft/visual/02-composition.md`；本篇只管「叫什么、怎么写、能不能出」。

**写构图的三条规则**

1. 用**画面方位**写位置：`at the right third`、`in the lower left corner`、`centered`，不写「在旁边」。
2. 一镜只用一个构图手法说话。中心对称 + 框中框 + 引导线叠在一起，画面会像海报，不像电影。
3. 构图在**图像阶段**定。关键帧先行时，构图在首帧里就已经确定了；视频提示只写运动，并给运动留出空间（`references/aigc/workflow.md`：要推镜就构图稍宽，人要出画就在走向那侧留空）。

**生成总体判断**：静态构图在图像阶段大多**稳**；视频里人物一动，构图就会变。精确构图一律关键帧先行。

---

## 1. 位置

### 中心构图 Centered
- **写法**：`She stands dead center in the frame, the corridor symmetrical around her.` B: `centered composition`
- **作用**：稳定、正式、对质；人物是这个世界的中心。也可以是困住：四面八方都一样。
- **用 / 不用**：宣告、仪式、对峙、喜剧的正面构图；日常对话里一直居中会显得呆板。
- **生成**：稳。模型本来就爱居中——想要偏边构图时反而要明写。

### 三分法 Rule of thirds
- **写法**：`He sits on the left third of the frame, the window and the city filling the right two-thirds.` B: `rule of thirds, subject on left third`
- **作用**：自然、平衡、有呼吸感；把空间留给人物看向的方向或环境（《镜头的语法》2.1 九宫格定律）。
- **用 / 不用**：大多数镜头的默认值。要强调稳定或对称时改中心构图。
- **生成**：稳。写清哪一侧、空出来的部分是什么。

### 视线留白 Lead room / look room
- **写法**：`Close-up of her looking toward frame right; her face sits on the left third, open space in front of her eyes.` B: `lead room on the right`
- **作用**：人物看向哪边，哪边就留空，观众跟着她的视线（《镜头的语法》2.1、6.10）。
- **用 / 不用**：默认要留。刻意反过来——人物看向画框边缘、背后留大片空白——会制造压迫或「有东西在背后」的不安（`camera/intent.md`「不安」）。
- **生成**：稳；模型常把脸居中，要写清脸在哪一侧。
- **短剧**：正反打的两个单人镜，视线留白方向相反。

### 头顶留白 Headroom
- **写法**：`A small margin of space above her head, eyes at the upper third line.` B: `tight headroom` / `generous headroom`
- **作用**：头顶留白太多，人物显得渺小、往下沉；太少或切掉头顶，显得压迫、亲密（《镜头的语法》2.1、6.14）。
- **用 / 不用**：同一场的小景别镜头统一头顶留白，逐字复用（`craft/visual/02-composition.md`）。特写切掉头顶、保留眼睛和嘴，是强烈情绪的常用做法。
- **生成**：稳。

### 上半部原则
- **写法**：`The important object sits in the upper half of the frame.`
- **作用**：观众的视线先落在画面上半部，重要的被摄对象放在那里（《镜头的语法》6.12）。
- **短剧**：竖屏下方约 20% 被字幕和平台界面挡住，脸和关键动作放在中上部（`references/drama/06-storyboard.md`）。

---

## 2. 线条与形状

### 对称 Symmetry
- **写法**：`Perfectly symmetrical frame: the hallway, the doors on both sides and the chandelier mirrored around the center line; he stands at the far end.` B: `symmetrical composition, one-point perspective`
- **作用**：秩序、控制、仪式感；也可以是荒诞——太完美的世界。
- **用 / 不用**：权力空间（宫殿、法庭、董事会）、有意的风格化；打破对称的那一镜就是事件。
- **生成**：稳。

### 引导线 Leading lines
- **写法**：`The railway tracks run from the bottom corners of the frame toward her small figure at the vanishing point.` B: `leading lines toward subject`
- **作用**：用画面里的线（路、栏杆、走廊、桌沿）把视线引到主体（《电影镜头入门》Step2「视线引导」）。
- **用 / 不用**：远景里主体很小时；主体已经很大时不需要。
- **生成**：稳。

### 对角线 / 斜线 Diagonals
- **写法**：`The staircase cuts diagonally across the frame from lower left to upper right; she climbs along it.` B: `strong diagonal composition`
- **作用**：动感、不稳定、冲突；水平线和垂直线是静止，斜线是运动（《镜头的语法》3.1 斜线法）。
- **用 / 不用**：动作、追逐、对峙；平静的场景用水平线。
- **生成**：稳。

### 地平线高低 Horizon placement
- **写法**：低地平线 `A very low horizon: the sky fills four-fifths of the frame above the small rider.`；高地平线 `A high horizon: the plowed field fills almost the whole frame, the sky a thin strip at the top.` B: `low horizon` / `high horizon`
- **作用**：低地平线——天空压倒一切，自由或渺小；高地平线——大地压倒一切，劳作、困住、沉重（《镜头的语法》3.1 地平线）。
- **用 / 不用**：远景必须决定地平线放哪，不要默认放在正中间。
- **生成**：稳。

### 三角形构图 Triangle
- **写法**：`The three of them form a triangle: the father standing at the apex in the back, the two children seated at the lower corners.` B: `triangular grouping`
- **作用**：稳定的多人关系；顶点上的人是这一拍的中心（《电影镜头入门》Step2「三人、四人构图」；`recipes/dialogue-group.md`）。
- **生成**：稳；人越多越要参考图分配身份。

---

## 3. 层次与纵深

### 前景 / 中景 / 后景
- **写法**：`Three layers: a blurred teacup in the foreground at frame left, her face sharp in the middle ground, the door at the back where he stands, soft.` B: `foreground element, subject midground, figure in background`
- **作用**：把二维画面变成空间；前后景之间可以有戏剧关系（前景的人不知道后景发生的事）（《镜头的语法》3.1；《电影镜头入门》Step2「层次」「多层次的情节」）。
- **用 / 不用**：需要空间感、需要两个信息同时在画面里时。竖屏尤其依赖纵深。
- **生成**：稳（图像）；视频里前后景都有人时，后景的人常常变形，景深写清谁实谁虚。

### 纵深调度 / 平面调度
- **写法**：纵深 `He walks from the far end of the room straight toward the camera, growing from a small figure to a close-up.`；平面 `Everyone stands in a line parallel to the camera, like figures on a flat stage.`
- **作用**：纵深调度让人物在画面里改变大小，权力随距离变化；平面调度像舞台、像画，冷静或荒诞（《电影镜头入门》Step2「纵深舞台调度，平面舞台调度」；《电影镜头设计》第十三章）。
- **生成**：纵深运动定帧（首尾帧锁住远近两个位置）；平面调度稳。

### 前景遮挡
- 见 `lexicon-shot.md`「遮挡偷窥」「前景虚化」。

---

## 4. 画框

### 框中框 Frame within a frame
- **写法**：`She is framed by the doorway, the dark walls of the hallway around the bright door like a picture frame.` B: `frame within frame, doorway`
- **作用**：困住、隔离、被观看；门、窗、镜子、车窗把人物框起来（《电影镜头入门》Step2「内部画框」）。
- **用 / 不用**：人物被困、被监视、和另一个人隔开（一人一个框）；开放的自由场景不用。
- **生成**：稳。框必须是场景里存在的东西，写进场景图。

### 封闭式构图 Closed frame
- **写法**：`Everything the scene needs is inside the frame; the walls close in on all four sides, nothing leads out.` B: `closed composition`
- **作用**：画框就是世界的边界，人物逃不出去；精心安排、形式感强（《电影镜头设计》第十五章）。
- **用 / 不用**：室内戏、受困、权力的控制。
- **生成**：稳。

### 开放式构图 Open frame
- **写法**：`She is cut by the right edge of the frame, the street continuing beyond it; people pass in and out of the shot.` B: `open composition, subject cut by frame edge`
- **作用**：画框外还有世界，生活在继续；纪实感、随意、不受控制（《电影镜头设计》第十五章）。
- **用 / 不用**：街头、纪实、混乱；精确的权力场景用封闭式。
- **生成**：稳；模型倾向把人物完整放进画框，要明写「被画框边缘切掉」。

### 负空间 Negative space
- **写法**：`A vast empty white wall fills most of the frame; he sits small in the lower right corner.` B: `negative space, small subject`
- **作用**：孤独、空虚、等待；空的部分也是内容（`camera/intent.md`「孤独」）。
- **用 / 不用**：人物孤立、失去、沉默的一拍；连续使用会让节奏变慢。
- **生成**：稳；模型爱往空处加东西，写清空处是什么（一面墙、一片天）。

### 空画面 / 出画
- **写法**：`He walks out of frame at the left; the camera holds on the empty kitchen.`
- **作用**：人走了，空间留下；结尾、告别、离开后的余波。也是天然的剪辑点（`craft/staging/04-coverage.md`）。
- **生成**：稳。人物出画后画面常继续「生成」新东西，写 `the empty kitchen, nothing moves`。

---

## 5. 竖屏构图

- **纵深代替横向**：两人前后站、上下错落，不左右排开（`references/drama/06-storyboard.md` 第 4 节）。
- **上下三分**：脸放在上三分之一线，下三分之一留给字幕区。
- **竖线和竖向空间**：门框、楼梯、电梯、高楼在竖屏里天然好用；竖摇比横摇合适。
- **框中框**更容易：竖屏本身就像一扇门。
- **中心构图**更常用：竖屏左右窄，三分法的偏移空间有限。

## 6. 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 所有镜头都居中 | 没写位置 | 写画面方位：`on the left third` |
| 空出来的地方被塞满东西 | 只写了「留白」 | 写空处是什么：一面墙、一片天、空走廊 |
| 头被切掉、手被切掉 | 没写头顶留白和手的位置 | `full head in frame, hands visible`（`craft/visual/02-composition.md`） |
| 构图在视频里跑掉 | 文生视频没有首帧 | 关键帧先行；视频只写运动，运动幅度小 |
| 构图手法太多，像海报 | 同时用了几种 | 一镜只用一种 |
| 背景里的东西从头上长出来 | 没检查主体和背景的关系 | 换背景、换机位，或浅景深虚化 |

## 来源

见 `camera/sources.md`。
