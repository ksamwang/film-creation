---
name: film-creation
description: "AIGC 创作参考包，供 LLM 在用户提出故事、角色、镜头序列、图像/视频提示词、资产与一致性（参考图、角色表）、声音与剪辑、竖屏短剧（立项、分集大纲、剧本、角色场景拆解、分镜、片段提示词）需求时调用。内置 6 个 AIGC 方法模块、竖屏短剧生产标准、125 位导演、29 位摄影指导，以及按模型类型区分的两种提示词写法（自然语言 + 参考图 / token 块）。默认输出 AIGC 产物；实拍只在用户明确要求时回答。Triggers: story, storyboard, shot list, image/video prompts, character consistency, reference images, vertical short drama / micro-drama, script, episode outline."
---

# AIGC 创作参考包

默认用于 AI 图像/视频作品。流程：**判断请求类型 → 读路由表的文件 → 按需提问 → 输出 AIGC 产物**：概念 / beat、镜头序列、图像/视频提示词、资产卡与参考图规格、角色表、剪辑/声音方案。不给剧组、排练、选角、预算、排期、通告、灯具、轨道、现场录音，除非用户明确要实拍。

## 路由表

路径从本 skill 根目录算起。

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 概念 | `references/craft/story/index.md` | 一句话 + beat sheet |
| 写台词 / 改对白（太直白、太水、一个腔调） | `references/writing/dialogue.md` | 改后的台词 + 镜头落法 |
| 叙事技巧（伏笔、反转、倒计时、母题…）/ 想让观众爽、笑、哭、怕 | `references/writing/devices.md` 或 `references/writing/intent.md` | 技巧落法 / 情绪机制 + 写法 |
| 按类型写（悬疑、爱情、喜剧、恐怖、犯罪 / 动作、科幻 / 奇幻、家庭、广告） | `references/writing/genres/index.md` → 对应类型 | 类型约定 + beat 表 + 陈词滥调替代 |
| 写一个完整短片剧本 / 要剧本模板 | `templates/script.md`（示例 `references/writing/example.md`） | 片头信息 + beat 表 + 正文 + 台词表 + 检查 |
| 剧本 / beat 哪里不好、怎么改 | `references/writing/doctor.md` | 诊断：最大问题 + 证据 + 修法 |
| 角色 / 人物 | `references/craft/performance/index.md` + `templates/character-sheet.md` | 资产卡 + 角色表提示词 |
| 分镜脚本：一场戏拆几个镜头、每镜拍什么、台词落在谁脸上 | `references/storyboard/breakdown.md`（镜头功能 `references/storyboard/shot-functions.md`，拆法风格 `references/storyboard/three-ways.md`，示例 `references/storyboard/example.md`）+ `templates/storyboard-script.md` | 读戏卡 + 分镜脚本（镜号、功能、景别、角度、运镜、画面、台词、时长、生成）+ 生成清单 `templates/shot-list.md` |
| 分镜图 / 动态分镜 / 连续性 / 节奏 | `references/storyboard/frames.md`、`references/storyboard/animatic.md`、`references/storyboard/continuity.md`、`references/storyboard/pacing.md` | 分镜图与审图意见 / 动态分镜方案 / 连续性台账与修法 / 节奏表 |
| 镜头序列 / 分镜 | `references/craft/staging/index.md` + `references/craft/visual/index.md` | shot list + 提示词 |
| 图像 / 视频提示词 | `references/aigc/prompt-syntax.md` | 按模式出提示词 |
| 镜头语言：角度 / 运镜 / 焦段 / 光 / 构图 / 转场怎么写、能否生成 | `references/camera/index.md` 选词典：`lexicon-shot` / `lexicon-move` / `lexicon-light` / `lexicon-frame` / `lexicon-transition` | 取景句 / 运动句 / 光的描述 / 剪辑转场 + 生成方式 |
| 想要某种效果（压迫、孤立、揭示…）不知怎么拍 | `references/camera/intent.md` | 拍法组合 + 示例 |
| 某类场景怎么排镜头（对话、追逐、打斗、悬疑、亲密、蒙太奇、开场结尾、反转打脸） | `references/camera/recipes/index.md` → 对应配方 | 镜头序列 + 逐镜提示词 + 生成方式 |
| 怎么生成 / 生成方式 / 镜头衔接 | `references/aigc/workflow.md` | 生成方式与串联 |
| 选模型 / 模型能力 | `references/aigc/models.md` | 模型与模式 |
| 资产一致性 / 参考图 | `references/aigc/assets.md` + `templates/asset-tokens.md` | 资产卡 + 参考图规格 |
| 声音 / 剪辑 | `references/craft/sound/index.md` + `templates/edit-sound.md` | 声音分工 + 剪辑方案 |
| 风格参考 | `references/taxonomy.md` 选族 → `references/directors/<slug>.md` 或 `references/cinematographers/<slug>.md`，及 `references/prompts/` 或 `references/prompts-cinematographers/` 下同名文件；混搭加 `references/mixing.md` | 2–3 个参考 + 视觉基元 |
| 迭代 / 交付 | `references/craft/production/index.md` | 镜头数 / 迭代预算 / 交付 |
| 短剧：立项 / 题材 | `references/drama/01-premise.md` | setting |
| 短剧：出海 | `references/drama/01-premise.md` + `references/drama/09-overseas.md` | 本地化 setting |
| 短剧：画风 / 漫剧 | `references/drama/10-look.md` | 画风设定 |
| 短剧：分集大纲 / 付费点 | `references/drama/02-season.md` | outline |
| 短剧：单集剧本 | `references/drama/03-episode.md` + `references/drama/04-script.md` | script |
| 短剧：角色场景拆解 / 造型图 | `references/drama/05-breakdown.md` | breakdown + 造型图规格 |
| 短剧：分镜 | `references/drama/06-storyboard.md` | segments |
| 短剧：片段提示词 / 口型 / 站位 | `references/drama/07-segment-prompt.md` | 编译提示词；问题回分镜改 |
| 短剧：成片 / 配乐字幕 / 质检 | `references/drama/08-cut-qc.md` | 成片方案 + 质检 |
| 短剧：字段 / JSON / 对接平台 | `references/drama/standard.md` | 按标准字段落表 |
| 明确要实拍 | 说明默认不做实拍，按需给通用建议 | — |

`references/index.md`（导演/摄影全表，较大）只在按地域/年代查全表时读。

## 短剧另有标准

短剧产物按 `references/drama/standard.md` 字段出稿；没读过 `references/drama/index.md` 先读它。与通用规则冲突时**以 `references/drama/` 为准**。宿主平台规定了输出格式（如指定 JSON）时**格式以平台为准**：不改字段名、不加平台没要的字段。一次只读当前阶段的 1–2 篇。

## 使用原则

1. 先判断请求类型，不一套流程套所有人；不主动给实拍方案。
2. 需要时才问，最多 3 个关键问题；目标模型不明按模式 A 写，必要时附模式 B。
3. 导演/摄影：先问作品需要什么视觉，选 1 主参考 + 0–1 副参考，只取 2–3 条视觉约束（机位、光源、色彩关系）转成视觉基元；不写导演名、不给剧组职位；「反向约束」改写成正面描述，有 negative 参数再放进去。

## AIGC 提示规则

细则与失败模式见 `references/aigc/prompt-syntax.md`。

- **模式 A（默认）**：大语言模型编码的模型（Seedance、Kling、Veo、Wan、Hailuo、GPT-Image、Nano Banana、Flux 等）。自然语言按时间顺序写，一镜 2–3 个动作；空间写画面左右、机位前后、接触点，情绪写成可见动作；有参考图时不重复外貌，写清每张图是谁；正面描述，否定只进 negative 参数或工具约定的约束句。
- **模式 B**：CLIP 系（SD / SDXL 及微调）或用户要 token 写法。`|` 分隔的 token 块；一个提示一个主语；词序即权重；正向不写否定，否定进 NEGATIVE；token 逐字复用；图生视频只写运动。
- **通用**：具体胜过形容（一个机位、一个光源、一个材质），不写 `cinematic / 8K / masterpiece`；风格放最后，8–15 个视觉基元；不写画幅、分辨率、时长；一致性先靠参考图，再靠首帧续接，文本锁兜底（`references/aigc/assets.md`）。

## 质量门

概念 → beat → 镜头一条线走通；每镜有理由、顺序与轴线可读；表演是微动作不是形容词；对白、环境、事件、音乐、沉默分工清楚，标明模型原生出还是后期做；反复出现的人物/场景/道具有资产卡与参考图（或文本锁）；模式选对，模式 B 的 NEGATIVE 是具体失败模式。

## 文件地图

路由表之外：

- `references/craft/index.md` — 6 个方法模块总导航（story / visual / staging / performance / sound / production）
- `references/writing/index.md` — 写作查阅层：对白手法、叙事技巧、按效果反查、类型配方、剧本诊断
- `references/storyboard/index.md` — 分镜查阅层：拆解七步、镜头数估算、镜头功能词典、三种拆法、场景示例、全片示例、分镜图、动态分镜、连续性、节奏
- `references/camera/index.md` — 镜头语言查阅层：取景 / 运动 / 光 / 构图 / 转场词典、按目的反查、场景配方、可靠性分级
- `references/prompting.md` — 档案 → 提示词的转换；`references/drama/sources.md` — 短剧来源
- `templates/` — treatment、script、scene-card、storyboard-script、shot-list、ai-prompt、style-brief 等；短剧 drama-bible / drama-outline / drama-episode / drama-breakdown / drama-storyboard
