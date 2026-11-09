---
name: film-creation
description: AIGC 创作参考包，供 LLM 在用户提出故事、角色、镜头序列、图像/视频提示词、资产与一致性（参考图、角色表）、声音与剪辑、竖屏短剧（立项、分集大纲、剧本、角色场景拆解、分镜、片段提示词）需求时调用。内置 6 个 AIGC 方法模块、竖屏短剧生产标准、125 位导演、29 位摄影指导，以及按模型类型区分的两种提示词写法（自然语言 + 参考图 / token 块）。默认输出 AIGC 产物；实拍只在用户明确要求时回答。
---

# AIGC 创作参考包

这是一份给 LLM 用的参考包 + 路由手册。默认用于 AI 图像/视频作品，不用于实拍。

LLM 的职责：**判断请求类型 → 读对应文件 → 按需要提问 → 输出 AIGC 产物。**

## 包里有什么

- `references/craft/` — 6 个 AIGC 方法模块
- `references/drama/` — 竖屏短剧：生产标准（字段契约）+ 立项到成片的写法
- `references/directors/` + `references/cinematographers/` — 视觉参考
- `references/aigc/` — 提示词两种模式、资产与一致性
- `templates/` — concept、scene-to-shots、shot prompt、资产卡、character sheet、edit-sound、AI prompt；短剧模板

## 默认输出

- 概念 / beat sheet
- 镜头序列
- 图像 / 视频提示词（按目标模型选模式）
- 资产卡、参考图规格、角色表
- 剪辑 / 声音方案

**不输出**：剧组、演员排练、选角、预算、排期、通告、灯具型号、轨道、现场录音——除非用户明确要求实拍。

## 请求路由表

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 概念 | `craft/story/index.md` | 一句话 + beat sheet |
| 角色 / 人物 | `craft/performance/index.md` + `templates/character-sheet.md` | 资产卡 + 角色表提示词 |
| 镜头序列 / 分镜 | `craft/staging/index.md` + `craft/visual/index.md` | shot list + 提示词 |
| 图像 / 视频提示词 | `aigc/prompt-syntax.md` | 按模式出提示词 |
| 资产一致性 / 参考图 | `aigc/assets.md` + `templates/asset-tokens.md` | 资产卡 + 参考图规格 |
| 声音 / 剪辑 | `craft/sound/index.md` + `templates/edit-sound.md` | 声音分工 + 剪辑方案 |
| 风格参考 | `references/index.md` + `references/taxonomy.md` | 2–3 个参考 + 视觉基元 |
| 迭代 / 交付 | `craft/production/index.md` | 镜头数 / 迭代预算 / 交付 |
| 短剧：立项 / 题材 | `references/drama/index.md` → `drama/01-premise.md` | 立项设定 setting |
| 短剧：出海 / 海外市场 | `drama/01-premise.md` + `drama/09-overseas.md` | 本地化的立项设定 |
| 短剧：分集大纲 / 付费点 | `references/drama/index.md` → `drama/02-season.md` | 分集大纲 outline |
| 短剧：单集剧本 | `references/drama/index.md` → `drama/03-episode.md` + `drama/04-script.md` | 结构化剧本 script |
| 短剧：角色 / 场景拆解、造型图 | `references/drama/index.md` → `drama/05-breakdown.md` | 拆解 breakdown + 造型图规格 |
| 短剧：分镜 | `references/drama/index.md` → `drama/06-storyboard.md` | 分镜 segments（按 `drama/standard.md` 字段） |
| 短剧：片段提示词 / 口型 / 站位问题 | `drama/07-segment-prompt.md` | 编译后的片段提示词，问题回分镜改 |
| 短剧：成片 / 配乐字幕 / 质检 | `drama/08-cut-qc.md` | 成片方案 + 质检结论 |
| 短剧：字段 / JSON / 对接平台 | `drama/standard.md` | 按标准字段落表 |
| 明确要实拍 | 先说明本包默认不做实拍；按需给通用建议 | — |

## 短剧另有标准

竖屏短剧按 `references/drama/standard.md` 的字段出稿，面向多参考图、原生出声、多镜头一次生成的视频模型。与下面的通用规则冲突时，**短剧以 `references/drama/` 为准**。

宿主平台或工具已经规定了输出格式（比如某个阶段要求返回指定 JSON）时，**格式以平台为准**，本包只提供写法；不要改字段名、不要加平台没要的字段。一次只读当前阶段需要的 1–2 篇。

## 使用原则

1. **默认 AIGC**；不主动给实拍方案。
2. **先判断请求类型**，不要一套流程套所有人。
3. **需要时才问**，最多 3 个关键问题；目标模型不明时按模式 A 写，必要时附模式 B。
4. **每条建议必须落到 AIGC 产物**：concept、beat、shot、提示词、资产、剪辑/声音。
5. **引用导演/摄影时给视觉基元**，不给剧组职位。

## 导演 / 摄影怎么用

1. 先问「这个作品需要什么视觉」，再选参考。
2. 1 位主参考 + 0–1 位副参考。
3. 只取 2–3 条视觉约束（一个机位、一个光源、一个色彩关系），转成提示词。
4. 「反向约束」改写成正面描述；模型有 negative 参数时再放进 negative。
5. 不在提示词里写导演名字；用视觉基元。

## AIGC 提示规则

先选模式（详见 `aigc/prompt-syntax.md`）：

- **模式 A（默认）**：大语言模型编码的图像/视频模型（Seedance、Kling、Veo、Wan、Hailuo、GPT-Image、Nano Banana、Flux 等）。
- **模式 B**：CLIP 系模型（SD / SDXL 及微调）或用户要求 token 写法。

通用：

1. 具体胜过形容：一个机位、一个光源、一个材质；不写 `cinematic / 8K / masterpiece`。
2. 风格放最后，8–15 个视觉基元；不写导演名。
3. 不写画幅、分辨率、时长参数；交给工具。
4. 一致性先靠参考图，再靠首帧续接，文本锁兜底（`aigc/assets.md`）。

模式 A：

5. 自然语言，按时间顺序写；一镜 2–3 个动作。
6. 空间写画面左右、机位前后、接触点；情绪写成可见动作。
7. 有参考图时正文不重复外貌，写清每张图是谁。
8. 正面描述；否定只进 negative 参数或工具约定的约束句。

模式 B：

9. token 块、`|` 分隔；一个提示一个主语；词序即权重。
10. 正向只写肯定，否定进 NEGATIVE；token 逐字复用；图生视频只写运动。

## 质量门

- 故事：概念 → beat → 镜头，能一条线走通。
- 视觉：每个镜头有理由，能转成提示词。
- 调度：镜头顺序成立，轴线/方向可读。
- 表演：写成微动作，不写形容词。
- 声音：对白、环境、事件、音乐、沉默分工清楚，写明哪些由模型原生出、哪些后期做。
- 资产：每个反复出现的人物/场景/道具有资产卡与参考图（或文本锁）。
- 提示：模式选对；无画幅/平台参数/导演名；模式 A 无否定堆叠，模式 B 正向无否定、NEGATIVE 是具体失败模式。

## 文件地图

- `references/craft/` — 6 个 AIGC 方法模块（index + 子文件）
- `references/drama/` — 竖屏短剧：`drama/index.md` 路由、`drama/standard.md` 字段契约、01–09 分阶段写法、`drama/sources.md`
- `references/aigc/prompt-syntax.md` — 两种提示词模式与失败模式
- `references/aigc/assets.md` — 资产卡、参考图与一致性
- `references/index.md` — 125 导演 + 29 摄影总表
- `references/taxonomy.md` — 风格族谱
- `references/mixing.md` — 视觉混搭 + 导演 × 摄影
- `references/prompting.md` — 档案 → 提示词的转换规则
- `references/directors/<slug>.md` — 导演档案
- `references/prompts/<slug>.md` — 导演提示参考
- `references/cinematographers/<slug>.md` — 摄影档案
- `references/prompts-cinematographers/<slug>.md` — 摄影提示参考
- `templates/` — concept / scene-to-shots / shot prompt / asset tokens（资产卡）/ character sheet / edit-sound / AI prompt；短剧 drama-bible / drama-outline / drama-episode / drama-breakdown / drama-storyboard
