# 提示词语法：两种模式

> 提示词是**给模型分配注意力的预算**：每个词都要决定画面里的某样东西。
> 先判断目标模型属于哪一类，再用对应的写法。竖屏短剧另有标准（`references/drama/`），冲突时以那里为准。

## 0. 先选模式

| 看什么 | 模式 A：自然语言 | 模式 B：token 块 |
|---|---|---|
| 文本编码 | 大语言模型（T5-XXL、Qwen、Gemini 等），读得懂句子、顺序、引号 | CLIP 为主，按词袋读，77 token 左右截断 |
| 典型模型 | Seedance、MiniMax Hailuo、Wan、Kling、Veo、Sora；GPT-Image、Nano Banana、Flux、Qwen-Image、Seedream | SD 1.5 / SDXL 及其微调、Midjourney 风格的短词写法、多数 ComfyUI 老工作流 |
| 参考图 | 多张参考图负责身份、地点、风格 | 一般没有，或靠 IP-Adapter / LoRA |
| negative | 多数没有 negative 参数 | 有 negative 输入框 |
| 声音 | 视频模型常能原生出对白和环境声 | 无 |

**默认用模式 A。** 只有目标明确是 CLIP 系模型、或者用户要求 token 写法时才用模式 B。不知道是哪个模型时按 A 写，同时给出 B 的版本。

两种模式共通的原则：

1. **具体胜过形容**：一个机位、一个光源、一个材质，胜过 `cinematic, stunning, masterpiece`。
2. **不写画幅、分辨率、时长参数**：这些在工具的参数面板里设，写进正文会冲突或被忽略。
3. **不写导演名**：把导演风格拆成可见的视觉基元（见 `references/prompting.md`）。
4. **概念越多越平均**：同时写赛博朋克、巴洛克、极简，得到的是四不像。风格 8–15 个概念以内。
5. **想要什么写什么**：正面描述目标效果，比写「不要」可靠。

## 1. 模式 A：自然语言

### 为什么

大语言模型编码器读得懂语法：先后（先推门，再抬头）、因果（因为风大，衣角往后飘）、空间关系（她在画左，桌子在两人之间）、引号里的台词。这些信息在 token 块里会丢。

### 结构

按「主体 → 动作 → 环境 → 镜头 → 光色 → 质感」写成几句话。视频按时间顺序写，多镜头视频按「镜头 1、镜头 2」分段。

```text
A woman in her thirties in an emerald cheongsam stands still in a cramped noodle shop at midnight, rain streaking the window behind her.
Medium close-up at eye level on a 50mm lens, framed through the doorframe in the foreground.
The only light is a red neon sign outside, leaving half her face in shadow; steam and cigarette smoke hang in the air.
Muted emerald, crimson and amber, with soft 35mm film grain.
```

视频（文生视频或参考图生视频）：

```text
She lifts the cigarette, takes one slow drag, then turns her head toward the door as a bell rings.
The camera drifts slowly closer, handheld, following the turn.
```

### 规则

1. **一句一件事，按顺序写**：一个镜头 2–3 个动作；写多了会被压成半秒一个、叠在一起。
2. **空间写清楚**：左右用画面方位（画左 / frame left），前后用相对机位的前景 / 背景，人和锚点的关系写接触点（「右手搭在椅背上」比「站在椅子旁边」稳）。
3. **情绪写成可见的动作**：「下巴绷紧，盯了两秒才移开视线」，不写「她很难过」。
4. **有参考图时不重复外貌**：身份交给图，文字只写这一镜的动作、状态和取景；重复外貌会和图打架（见 `assets.md`）。
5. **台词放引号里，说清谁说、什么语气**；一镜一个说话人。
6. **否定只在两处出现**：模型有 negative 参数时放进 negative；工具约定的固定约束句（如「音频里不要有背景音乐」）。正文里不堆「不要模糊、不要变形」。
7. **长度看信息量**：图像 40–120 词，单镜视频 60–150 词；每个词都要落到画面上，没有可删的修饰。

## 2. 模式 B：token 块

### 为什么

CLIP 系编码器按词袋读：冗余词平均分走注意力；否定词会强化它否定的概念（`no gun` 反而容易出枪）；超长部分直接截断。

### 结构

写块，不写句子。每块只放同类信息，用 `|` 分隔概念：

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

词序：`SUBJECT → identity → wardrobe → action → ENVIRONMENT → SHOT → LIGHT → COLOR → TEXTURE → STYLE`。主体最前，风格最后，避免风格压过主体。

### 规则

1. **一个提示一个主语**：CLIP 分不清两个人的属性，会混脸、换衣服；多人物分开生成再合成。
2. **正向只写肯定**：`calm face`，不写 `not sad`；`empty street`，不写 `no people`。
3. **否定全部进 NEGATIVE**，写具体失败模式，6 项左右。
4. **不用连接词**：不写 `and / with / while / then`；用 `|`。
5. **一个概念一个词**：不堆 `beautiful, gorgeous, stunning`。
6. **词序即权重**：先调词序，不靠括号堆权重。
7. **控制预算**：核心 30–60 词 + 风格 8–15 个概念。
8. **图生视频只写运动**：首帧已经承担身份、场景和风格，运动提示只写动作、运镜、时长。

## 3. 同一镜头，两种写法

**模式 A**：
> A lonely woman in a cheongsam walks slowly through a cramped noodle shop at midnight, smoking. The camera follows her from behind, handheld, at shoulder height. Red and green neon from the street cuts through the steam; half her face stays in shadow. Muted emerald and crimson, soft film grain.

**模式 B**：
```text
SUBJECT: 30s woman | cheongsam | dark hair | smoking | walking slowly
ENVIRONMENT: cramped noodle shop | midnight | steam
SHOT: medium shot | from behind | shoulder height | handheld
LIGHT: practical neon | low key | half-face shadow
COLOR: emerald | crimson | amber
NEGATIVE: clean symmetrical | even studio light | modern glass | digital sharpness
```

**两种都错的写法**：
> Cinematic masterpiece, beautiful woman, Wong Kar-wai style, 8K, HDR, ultra detailed, no modern things, 2.39:1.

## 4. 失败模式

| 症状 | 原因 | 修法 |
|---|---|---|
| 风格像通用「电影感」 | 只写 `cinematic` / 导演名 | 换成一个机位、一个光源、一个材质 |
| 画面过饱和、过锐 | `HDR`、`8K`、`sharp` 堆叠 | 删掉；写具体胶片、镜头、光比 |
| 主体变弱、画面平均 | 风格词太多 | 删风格词，主体前置 |
| 不要的东西反而出现 | 正文里写了否定 | 改成正面描述；有 negative 参数就移过去 |
| 人物脸、衣服和参考图不一样（A） | 文字又描述了一遍外貌 | 删外貌，只写动作和状态 |
| 两个人脸混在一起（B） | 一个 CLIP 提示写了两个角色 | 分开生成、合成；或换成支持多参考图的模型 |
| 动作挤成一团、跳帧（A） | 一镜写了太多动作 | 一镜 2–3 个动作，或拆镜 |
| 人站错侧、隔桌变同侧（A） | 只写了关系，没写机位前后 | 左右写画面方位，前后写前景 / 背景 |
| 首帧很好，一动就崩（图生视频） | 运动提示重复描述画面，或和首帧矛盾 | 只写运动、运镜、时长 |
| 中景出成远景（A） | 只有地点参考、没写取景 | 写「切在腰部，脸在上三分之一」，或给首帧 |

## 出图前检查

两种模式都查：

- [ ] 确认了模式（模型类型、参考图、negative 参数）？
- [ ] 没有画幅、分辨率、`--ar`、导演名、`masterpiece / 8K / HDR`？
- [ ] 风格不超过 15 个概念，每个都落到可见的东西上？

模式 A：

- [ ] 动作按顺序写，一镜不超过 2–3 个动作？
- [ ] 空间写了画面左右、机位前后、接触点？
- [ ] 有参考图时，正文没有重复外貌？
- [ ] 正文没有否定堆叠；否定只在 negative 参数或工具约定的约束句里？

模式 B：

- [ ] 只有一个主语？
- [ ] 正向没有 no / not / without，没有 and / with / while？
- [ ] NEGATIVE 约 6 项，都是具体失败模式？
- [ ] 图生视频的运动提示只写运动？
