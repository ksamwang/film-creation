# 配方：反转 / 打脸

## 这场戏要什么

反转是**权力在一瞬间交换**：被看不起的人亮出身份，嚣张的人当众失势，真相让所有人改变态度。竖屏短剧里这是最高频的爽点（`references/drama/01-premise.md`「获得感」）。

观众要读到四个节拍：

1. **压**：反派嚣张，主角被羞辱。镜头站在反派一边。
2. **亮**：一个信号——一个电话、一份文件、一个人走进来、一句话。
3. **转**：反派的脸变了。这是全场最值钱的镜头。
4. **收**：旁观者的态度变了，主角站在新的位置上。

**核心手法是角度交换**：压的阶段反派仰拍、主角俯拍；转之后反过来（`camera/intent.md`「权力反转」）。没有前面的压，后面的转就不值钱——痛点是爽点的前提（`references/drama/01-premise.md`）。

## 默认序列（8 镜，约 22 秒）

| # | 景别 / 角度 / 运动 | Q | 节拍 | 生成 | 时长 |
|---|---|---|---|---|---|
| 1 | 中景，反派略仰拍，主角在画面边缘 | 谁在上风 | 压 | 场景图 + 人物参考，关键帧先行 | 3 s |
| 2 | 中近景，主角略俯拍，固定 | 主角承受 | 压 | 首帧生视频 | 3 s |
| 3 | 中景：旁观者窃笑、交头接耳 | 众人站在反派一边 | 压 | 首帧生视频；旁观者不进引用 | 2 s |
| 4 | 插入特写或门口远景：信号（来电显示、文件、门被推开） | 局势要变 | 亮 | 关键帧；字在图阶段做对 | 2 s |
| 5 | 特写反派，急推（后期）或缓推 | 反派的脸变了 | 转 | 首帧生视频；表情从得意到僵住 | 3 s |
| 6 | 中近景主角，现在仰拍，缓推 | 主角站起来 | 转 | 首帧生视频 | 3 s |
| 7 | 中景旁观者：笑容消失、退后、低头 | 众人改变态度 | 收 | 首帧生视频 | 2 s |
| 8 | 双人：主角在画面中心偏上，反派在下方或边缘 | 新的位置 | 收 | 首帧生视频；位置与第 1 镜相反 | 4 s |

**排法要点**

- **反派变脸（5）是全场最重要的镜头**：给足 3 秒，表情从得意 → 停顿 → 僵住，写成可见的动作：「笑容停在脸上，嘴角慢慢放下，眼睛盯着手机屏幕」。
- 主角在转的时候**少动**：不需要大笑、不需要喊叫。站起来、整理袖口、看对方一眼，已经足够。
- 旁观者镜头（3、7）成对出现，态度相反。它们让观众确认「所有人都看到了」。
- 第 8 镜的构图和第 1 镜形成对比：位置交换，或者谁在画面上方交换。

## 示例（模式 A）

场景：订婚宴。顾家母亲当众羞辱林晚，林晚的父亲——集团董事长——走进来。

```text
1 | Medium shot, slight low angle on Mrs. Gu at frame left, holding a glass of wine, chin raised; Lin stands at the right edge of the frame, partly cut off. Static.
2 | Medium close-up of Lin from a slight high angle, static: she keeps her eyes down; wine drips from her hair onto her dress.
3 | Medium shot of three guests behind a table, static: they lean toward each other, smiling, one covering her mouth.
4 | Wide shot from inside the hall, static: the double doors at the far end swing open; a gray-haired man in a dark suit stands in the doorway, two assistants behind him.
5 | Close-up of Mrs. Gu, the camera slowly pushing in: her smile stays on her face for a second, then the corners of her mouth drop; her glass tilts in her hand.
6 | Medium close-up of Lin, now from a slight low angle, the camera slowly pushing in: she lifts her head and wipes the wine from her cheek with one finger.
7 | Medium shot of the same three guests, static: the smiles are gone; one sets her glass down and steps back.
8 | Medium two-shot, static: Lin stands at the center of the frame, upper half; Mrs. Gu at the lower left edge, head bowed.
```

第 5 镜可以在成片阶段加急推（4–6 帧裁切放大，`camera/lexicon-move.md`「急推」）。

## 变体

### 身份揭晓
- 信号是一句称呼（「董事长」「少主」）或一个下跪的动作；旁观者的反应镜比主角更重要。
- 自下而上竖摇（鞋 → 西装 → 脸）给揭晓者亮相。

### 证据反转
- 信号是一个屏幕：聊天记录、监控录像、转账记录。屏幕内容单独生成后期贴图，镜头只做缓推（`suspense.md`）。
- 投屏到大屏幕上，全场的人一起看——一个远景就把「所有人都知道了」交代清楚。

### 一句话反转
- 没有外部信号，主角一句话翻盘。这一句给中近景 + 缓推；说完立刻切反派的反应，不要停在主角身上。

### 连环反转
- 每次反转都交换一次角度。第二次反转必须比第一次更大（更高的身份、更多的旁观者），否则是复读（`references/drama/03-episode.md` 回合要有增量）。

## 竖屏 / 短剧

- 一个 15 秒片段装「亮 + 转 + 收」：信号 → 反派变脸 → 主角抬头 → 旁观者，4 镜。「压」放在前一个片段。
- 角度交换在竖屏里更显眼：仰拍时人物头顶贴近画面上沿，俯拍时人物落在画面下半。
- 枚举：压 `medium` + `low`（反派）/ `medium_close` + `high`（主角）；转 `close` + `push_in`（反派）/ `medium_close` + `low` + `push_in`（主角）。急推在成片阶段做。
- 打脸对象必须是主要反派，不是路人（`references/drama/01-premise.md`）。

## 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 反派变脸不明显 | 表情写成「震惊」 | 写成过程：笑容停住 → 嘴角放下 → 视线定住 |
| 主角太夸张 | 写了「得意地大笑」 | 主角少动：抬头、整理衣服、看一眼 |
| 角度交换看不出来 | 仰俯幅度太小 | 写后果：「头顶贴近画面上沿，天花板在身后」 |
| 旁观者抢戏 / 长相乱变 | 旁观者给了引用或正脸太清楚 | 旁观者不进引用，景别放宽，浅景深 |
| 反转不爽 | 前面没有压 | 压的阶段至少两镜：羞辱 + 主角承受 |

## 可借的档案

- `directors/park-chan-wook.md`：复仇的仪式感，构图精确的权力对比。
- `directors/quentin-tarantino.md`：长对话里压抑的张力，一句话后突然爆发。
- `directors/sergio-leone.md`：对峙中的大特写，眼神就是武器。

## 来源

见 `camera/sources.md`。
