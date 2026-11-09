# 提示词语法（注意力友好）

> 竖屏短剧（多参考图、原生出声的视频模型）按 `references/drama/` 写，与本文件冲突时以那里为准。

> 提示词不是“描述画面”，是**给注意力分配预算**。

## 为什么必须像写代码

主流文生图/文生视频的文本编码器（CLIP / T5）和生成主干都靠注意力分配权重。三个直接后果：

1. **冗余词分走注意力**：一个 50 词的句子里，真正决定画面的可能只有 8 个词；其余词在平均注意力，主体变弱。
2. **否定不会被执行**：模型不会“不要红色”，只会强化“红色”这个概念。`no gun` 往往更容易出现枪。
3. **概念越多越平均**：同时写赛博朋克、蒸汽朋克、巴洛克、极简，模型给出的是四不像的平均值。

## token 块

不要写句子，写块。每块只放同类信息，用 `|` 分隔概念：

```text
STYLE: 1990s Hong Kong | emerald green | crimson neon | tungsten practicals | smoke | 35mm grain
SUBJECT: 30s woman | cheongsam | dark hair | standing still
ENVIRONMENT: cramped noodle shop | midnight | rain
SHOT: medium close-up | eye level | 50mm | doorframe foreground
LIGHT: practical neon | low key | half-face shadow
COLOR: emerald | crimson | amber | mixed tungsten-neon
TEXTURE: smoke | rain | wet glass | film grain
MOTION: slow handheld drift | follow from behind | 4s | 24fps
NEGATIVE: clean symmetrical | even studio light | modern glass | digital sharpness | warm filter
```

## 词序

通用顺序：

```text
SUBJECT → identity → wardrobe → action → ENVIRONMENT → SHOT → LIGHT → COLOR → TEXTURE → STYLE
```

- **主体最前**：模型先决定画谁/画什么。
- **风格最后**：避免风格 token 压过主体。
- **视频**：首帧图承担身份/场景/风格，`MOTION` 放最前，文字不重复画面。

## 八条硬规则

1. **一个提示一个主语**：一个人物、一个场景、一个物品；多人物分开写。
2. **正向只写肯定**：`calm face`，不写 `not sad`；`empty street`，不写 `no people`。
3. **否定全部进 NEGATIVE**：包括“不要运镜”“不要现代建筑”“不要 HDR”。
4. **戒连接词**：不写 `and / with / while / then / because / as if`；用 `|` 或逗号。
5. **一个概念一个词**：不许 `beautiful, gorgeous, stunning` 同义堆叠。
6. **词序即权重**：最重要的放最前；先改词序，不要靠括号堆权重。
7. **控制预算**：核心 30–60 词 + 风格 8–15 个概念；超过就删。
8. **不写画幅**：画幅由用户/工具设定；不写 `2.39:1` 或 `--ar`。

## 失败模式

| 症状 | 原因 | 修法 |
|---|---|---|
| 主体变弱、画面平均 | 风格词太多 / 一个提示多个主语 | 删风格词、拆主语、主体前置 |
| 不要的东西反而出现 | 正向里写否定 | 移到 NEGATIVE，正向改肯定 |
| 两个人脸混在一起 | 同一提示描述两个角色 | 分开生成、分层合成 |
| 每张图衣服不一样 | 只靠文字描述服装 | 用固定资产 token 逐字复用 |
| 视频首帧很好，一动就崩 | 视频提示重复描述了画面 | 只写运动/镜头/时长 |
| 风格像通用“电影感” | 只写 `cinematic` / 导演名 | 换成一个机位、一个光源、一个材质 |
| 画面过饱和/过锐 | `HDR`、`8K`、`sharp` 堆叠 | 删掉；用具体胶片/镜头/光比 |

## 正反例

**反例（散文 + 否定 + 连接词）**：
> A lonely woman in a cheongsam moving through a cramped noodle shop, with neon lights and smoke, and the camera follows her from behind while she smokes, no clean composition, no modern glass.

**正例（token 块）**：
```text
SUBJECT: 30s woman | cheongsam | dark hair | smoking
ENVIRONMENT: cramped noodle shop | midnight | rain
SHOT: medium close-up | eye level | 50mm | doorframe foreground
LIGHT: practical neon | low key | half-face shadow
COLOR: emerald | crimson | amber
MOTION: slow handheld drift | follow from behind | 4s
NEGATIVE: clean symmetrical | even studio light | modern glass | digital sharpness
```

## 出图前检查

- [ ] 只有一个主语？
- [ ] 正向没有 no / not / without / avoid？
- [ ] 没有 and / with / while / then？
- [ ] STYLE 不超过 15 个概念？
- [ ] 没有画幅 / `--ar`？
- [ ] NEGATIVE 至少 6 项，且是具体失败模式？
- [ ] 图像提示与运动提示分开？
- [ ] 身份/场景靠固定 token，而不是靠重复形容词？
