# 配方：三人以上 / 群戏

## 这场戏要什么

观众要知道：**谁和谁站一边**、**谁是这场戏的中心**、**联盟在哪一刻变了**。人越多，越要把人分组，而不是给每个人一样多的镜头。

《电影镜头设计》第十章、第十一章把三人、四人以上的对话调度当成单独问题：三人戏通常是一个三角形，镜头在三角形外围选边；四人以上要先分成几组，每组当成一个「人」来处理。《镜头的语法》6.16 用纵深调度多人镜头，6.17 提醒三人戏的单人镜容易让剪辑看不懂谁在看谁。

**生成层面的硬约束**：同一镜里人越多，脸、服装越容易互串（`craft/staging/05-multi-character.md` 的「特征污染」）。一镜的正脸人数尽量 ≤ 2，参考图张数不能超过模型上限（`references/aigc/models.md`）。

## 默认序列：三人戏（7 镜）

| # | 景别 / 角度 / 运动 | Q | 生成 | 时长 |
|---|---|---|---|---|
| 1 | 远景，略高机位，固定 | 三人的三角形：谁在哪 | 场景图 + 三张人物参考，关键帧先行；最容易崩，多抽几张 | 3 s |
| 2 | 双人：A 与 B 同框，C 在画外 | 哪两人是一边 | 首帧生视频 | 4 s |
| 3 | 单人中近景 C，视线朝 A、B 所在的一侧 | 被排除的人 | 首帧生视频 | 4 s |
| 4 | 过肩：越过 C 看 A | 打破联盟的那句话 | 首帧生视频 | 4–5 s |
| 5 | 特写 B | B 的选择 | 首帧生视频，无台词 | 2–3 s |
| 6 | 新的双人：B 与 C 同框 | 联盟换了 | 首帧生视频；B 的位置或朝向变了 | 4 s |
| 7 | 回到远景 | 三角形的新形状 | 同 1 的机位，人物位置变化 | 3 s |

**排法要点**

- 先用分组镜头（双人 + 单人）表达阵营，再用阵营的变化表达剧情。
- 三人戏的轴线不止一条：每对视线一条轴线。规则是**谁和谁在对话，就守住他们之间的那条轴线**；换说话对象前先回远景或给一个中性镜头（《镜头的语法》6.22 安全越轴）。
- 单人镜的视线方向必须和远景里的位置一致：C 在画右，C 的单人镜就看向画左。

## 示例（模式 A）

场景：家庭饭桌。父亲要把公司交给长子，女儿当场拿出账本。

```text
1 | Wide shot, slightly high, static: a round dinner table; Father at the far side facing the camera, Son at frame left, Daughter at frame right, dishes between them.
2 | Medium two-shot from the right side of the table: Father and Son together, Son leaning toward him, both looking toward frame right where Daughter sits off-screen. Static.
3 | Medium close-up of Daughter at frame right, looking toward frame left; she sets her chopsticks down. Static.
4 | Over Daughter's soft shoulder: Father faces the camera across the table. Daughter speaks: "Before you decide, look at page twelve."
5 | Close-up of Son, static: his smile stays but his eyes go to the ledger.
6 | Medium two-shot from the left side: Father now turned toward Daughter, the ledger open between them; Son is out of frame.
7 | Same wide shot as shot 1: Father's chair angled toward Daughter; Son sits back, alone at frame left.
```

## 变体：四人以上

1. **分组**：把人分成 2–3 组（同一阵营、同一家庭、同一位置），每组一个双人或三人镜头。
2. **中心人物**：选一个人做这场戏的视点，他的单人镜最多、最近；其他人用分组镜头。
3. **纵深代替横排**：前景一组、中景一组、后景一个人；焦点落在谁身上谁是这一拍的中心（`camera/lexicon-shot.md`「深焦」「前景虚化」）。
4. **会议 / 长桌**：机位放在桌子一端做主镜头；单人镜按桌子两侧分成两条轴线，同一侧的人始终朝同一方向看。
5. **宴会 / 人群**：稳定跟随穿过人群，搜索到中心人物；或搜索式上升从人群中找到她（`camera/lexicon-move.md`）。背景人群用文生补，不给参考图。

## 竖屏 / 短剧

- 竖屏装不下横排三人：三人镜改成前景一人背影、中景两人上下错落；或者干脆不做三人同框，用分组双人 + 单人切换。
- 15 秒片段里的引用造型数（含场景）不能超过参考图上限。三人 + 场景 = 4 张；超了就让某个人这段不入画，只在反应镜出现。
- 背景人物（路人、宾客）不进 `@[]` 引用，写成「几位宾客在后景」，由模型生成。

## 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 三张脸互串、服装混在一起 | 一镜正脸太多 | 远景里人物小一点；其他镜头每镜正脸 ≤ 2 |
| 远景里人物位置每次都变 | 没有锁定的远景关键帧 | 远景先出图、定稿，后面所有镜头从它推导方位 |
| 单人镜视线方向错 | 没对照远景位置写 | 每个单人镜写「看向画左 / 画右」，与远景一致 |
| 观众不知道谁在跟谁说话 | 轴线乱跳 | 一组对话守一条轴线；换组前回远景 |
| 背景人群抢戏 | 人群太清楚、动作太多 | 浅景深虚化后景，人群动作写成「低声交谈、几乎不动」 |

## 可借的档案

- `directors/edward-yang.md`：群像里用门框、窗户把人分隔，远景长时段保持。
- `directors/paul-thomas-anderson.md`：稳定跟随穿过人群，一镜里交接多个中心人物。
- `directors/akira-kurosawa.md`：多人构图的纵深分层与几何队形。
- `directors/federico-fellini.md`：宴会、游行式群戏，中心人物在人群中穿行。

## 来源

见 `camera/sources.md`。
