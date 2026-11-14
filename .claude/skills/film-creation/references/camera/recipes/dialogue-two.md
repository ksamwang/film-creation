# 配方：双人对话

## 这场戏要什么

观众要读到三件事：两人**在哪、怎么相对**；每句话**落在谁身上**；关系**在哪一句变了**。

最常见的失败是「逐句正反打」：谁说话切谁，镜头一直在追台词，关系的变化反而看不见。正确做法是先找出关系改变的那一句，镜头只在那里变（《电影语言的语法》第 2 章动作与反应；《电影镜头设计》第九章对话场景的调度）。

**轴线**：两人视线连成一条线，所有机位放在线的同一侧。A 一直在画左朝右看，B 一直在画右朝左看（`craft/visual/01-shot-grammar.md`）。

## 默认序列（6 镜，约 25 秒）

| # | 景别 / 角度 / 运动 | Q | 生成 | 时长 |
|---|---|---|---|---|
| 1 | 远景或中景双人，平视，固定 | 在哪、怎么相对 | 场景主图 + 两人参考图，关键帧先行 | 3 s |
| 2 | 过肩中近景：越过 B 看 A，固定 | A 说了什么 | 首帧生视频，口型给 A | 4–6 s |
| 3 | 过肩中近景：越过 A 看 B，固定 | B 怎么接 | 同上，口型给 B；角度与 2 对称 | 4–6 s |
| 4 | 中近景单人 A，缓推 | 转折句落在 A 身上 | 首帧生视频 | 4 s |
| 5 | 特写 B，固定 | B 的反应：谁变了 | 首帧生视频，无台词 | 2–3 s |
| 6 | 回到双人，固定或缓拉 | 关系变化后的新位置 | 首帧生视频；位置与 1 不同（有人站起、走开、靠近） | 3 s |

**排法要点**

- 2、3 是一对，焦段、高度、景别完全对称（《镜头的语法》6.11）；不对称就成了「一方占优」的声明。
- 转折前用过肩（两人连在一起），转折后用干净单人（不带对方肩膀），距离感由此出来。
- 反应镜（5）比台词镜更重要：剪辑点落在反应峰值，不落在台词结束。
- 1 和 6 的双人镜要能对比：同一机位，人物位置变了，观众一眼看出关系变了。

## 示例（模式 A）

场景：深夜厨房。顾言要林晚签离婚协议，林晚拿出他出轨的证据。

```text
1 | Medium wide two-shot at eye level, static: Lin stands at frame left by the counter, Gu sits at frame right at the kitchen table, the agreement between his hands.
2 | Over Lin's soft, dark shoulder at frame left: Gu at frame right looks up at her and slides the agreement across the table. Static. Gu speaks: "Sign it. The house is yours."
3 | Over Gu's shoulder at frame right: Lin at frame left looks down at the paper, then back at him. Static.
4 | Medium close-up of Lin, clean single, no shoulder in frame; the camera slowly pushes in as she places a phone face-up on the agreement. Lin speaks: "Whose earring was in my jewelry box?"
5 | Close-up of Gu, static: his eyes drop to the phone and stay there; his jaw tightens.
6 | Same medium wide two-shot as shot 1, static: Gu now stands, one step back from the table; Lin has not moved.
```

## 变体

### 走着说 Walk and talk
- 前引中景双人，两人并肩走向镜头，镜头匀速后退（`camera/lexicon-move.md`「前引」）。
- 转折时一人停下，镜头随另一人再走两步才停——停下的人被留在后景。
- **生成**：一段走路 + 对白最多 5–6 秒；长对话拆成多段续接，每段第一句接住上一段的步伐和位置。

### 隔物对话
- 两人之间有桌子、栏杆、玻璃、车窗。物件是关系的形状：每次景别收紧，物件仍留在画面里。
- 写清物件在两人之间、在机位前后：`the glass partition between them, Lin on the near side with her back to the camera`。

### 电话 / 视频通话
- 一人一个空间，平行剪辑；两边视线方向相反（A 朝右、B 朝左），观众才会读成在对话。
- 屏幕里的脸单独生成，后期合成到手机上更稳；直接生成「屏幕里的人」常常脸糊、字乱。

### 审问 / 不平等对话
- 一方高（站）一方低（坐），过肩镜高低对应：审问者的过肩略俯，被审者的过肩略仰。
- 审问者可以走动、绕到背后；被审者固定。镜头跟着权力移动。

## 竖屏 / 短剧

- 双人不左右排开，改前后纵深：前景过肩放在画面下角，对方在中景偏上（`references/drama/06-storyboard.md` 第 4 节）。
- 6 镜可以装进一个 15 秒片段的前半，或者合并成 4 镜：双人建立 → 过肩台词 → 单人转折（`push_in`）→ 反应特写。
- 一镜一个说话人；过肩时前景那人背对镜头，口型只会落在对面的正脸上。
- 枚举：`medium` / `over_shoulder` / `medium_close` + `push_in` / `close` + `static`。

## 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 两人左右互换、越轴 | 每镜单独描述，没锁方位 | 每镜都写 `A at frame left, B at frame right`，逐字复用 |
| 口型落在错的人脸上 | 两张正脸同时在画面里 | 过肩时前景背对；反应镜不带台词 |
| 「隔桌相对」画成同一侧 | 只写「隔桌」 | 写清谁在桌子近侧、背对镜头 |
| 过肩的肩膀变成第三个人 | 没说肩膀是谁 | `over Lin's soft dark shoulder`；参考图生时写明前景是 Lin |
| 正反打焦段不一致，脸型变了 | 两镜各写各的 | 固定一句镜头描述，两镜逐字复用 |
| 节奏拖沓 | 逐句切 | 合并台词，只在转折句换镜 |

## 可借的档案

- `directors/asghar-farhadi.md`：对话中的信息差，用纵深和门框管理谁听见了什么。
- `directors/hong-sang-soo.md`：固定双人 + 突然的变焦推近，变焦本身就是评论。
- `directors/eric-rohmer.md`：长时段双人镜头，让言辞和身体距离矛盾。
- `directors/yasujiro-ozu.md`：正面单人、视线略偏镜头，对称正反打。

## 来源

见 `camera/sources.md`。
