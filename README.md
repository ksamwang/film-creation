# AIGC 创作参考包 film-creation

默认用于 **AI 图像 / 视频作品**，不用于实拍。

LLM 读到它之后，能判断用户要什么、读哪一块、产出一组可直接生成的 AIGC 产物。

## 快速开始

- 「我想做一个 1 分钟 AI 短片，只有一个房间和两个人，帮我出概念和 beat」
- 「设计一个角色，给我资产卡和三面板角色表提示词」
- 「把这场戏拆成 6 个镜头，每镜给图像和视频提示」
- 「这个角色在 10 个镜头里怎么保持一致」
- 「用王家卫 × 卢贝兹基的视觉风格，写雨夜便利店的镜头」
- 「做一部 60 集出海竖屏短剧，先给 3 个方向」「把第 3 集切成 15 秒片段的分镜，输出 JSON」

## 默认输出

- 概念 / beat sheet
- 镜头序列
- 图像 / 视频提示词（按目标模型选模式）
- 资产卡、参考图规格、角色表
- 剪辑 / 声音方案

**不输出**：剧组、演员排练、选角、预算、排期、通告、灯具型号、轨道、现场录音——除非用户明确要求实拍。

## 包里有什么

- **6 个 AIGC 方法模块**：故事、视觉、调度、表演、声音、制作
- **写作查阅层**：对白手法（潜台词、攻防、交代信息、人物声口、节奏、钩子台词、修剪）、叙事技巧（伏笔、反转、倒计时、母题等）、按效果反查（悬念、爽、笑、哭…），以及剧本诊断（六层症状 → 修法）
- **镜头语言查阅层**：景别、角度、焦段、景深、运镜、航拍、速度、光、构图、转场的词典（写法 + 生成可靠性），按目的反查拍法，以及 9 类场景的镜头序列配方
- **竖屏短剧**：生产标准（立项 → 大纲 → 剧本 → 拆解 → 造型图 → 分镜 → 片段提示词 → 成片的字段契约）+ 各阶段写法，见 `.claude/skills/film-creation/references/drama/`
- **125 位导演 + 29 位摄影指导**：视觉基元参考
- **AIGC 提示规则**：两种模式（自然语言 + 参考图 / token 块）、资产卡与一致性分层、三面板角色表
- **生成方式与模型**：文生 / 参考图生 / 首帧 / 首尾帧 / 续接怎么选、怎么串；模型能力卡
- **短剧画风**：写实与漫剧等非写实画风的设定
- **模板**：concept、scene-to-shots、shot prompt、资产卡、character sheet、edit-sound、AI prompt；短剧模板

## 请求路由表

「先读」里的路径都从 `.claude/skills/film-creation/` 算起。

同一请求沾到两行时，按格子里的「→」取舍。

### 故事与写作

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 概念 / 一页 treatment、梗概（story, logline, treatment） | `references/craft/story/index.md` + `templates/treatment.md` | 一句话 + beat sheet / 一页 treatment |
| 写台词 / 改对白：太直白、太水、一个腔调（dialogue） | `references/writing/dialogue.md` | 改后的台词 + 镜头落法 |
| 点名一种叙事技巧：伏笔、反转、倒计时、母题…（foreshadowing, plot twist） | `references/writing/devices.md` | 技巧落法；同时点了类型 → 加读下面类型那一行 |
| 想让观众爽、笑、哭、怕，不知道用什么技巧 | `references/writing/intent.md` | 情绪机制 + 写法 |
| 按类型写：悬疑、爱情、喜剧、恐怖、犯罪 / 动作、科幻 / 奇幻、家庭、广告（genre） | `references/writing/genres/index.md` → 对应类型（广告是 `references/writing/genres/brand.md`） | 类型约定 + 两档结构 + 陈词滥调替代 |
| 写一个完整短片剧本 / 要剧本模板（screenplay, script） | `templates/script.md`（示例 `references/writing/example.md`；先按 `references/writing/genres/index.md` 选类型和时长档） | 片头信息 + beat 表 + 正文 + 台词表 + 检查 |
| 剧本 / beat 哪里不好、怎么改（script doctor） | `references/writing/doctor.md` | 诊断：最大问题 + 证据 + 修法 |

### 角色

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 设计一个角色：人设、欲望、缺陷、弧光（character design） | `references/craft/story/02-character.md` | 人物设定 + 资产卡 |
| 角色跨镜头一致、角色表、脸 / 衣服漂移（character consistency） | `references/craft/performance/05-casting.md` + `references/aigc/assets.md` + `templates/character-sheet.md` | 三面板角色表提示词 + 资产卡 + 漂移修法 |
| 角色怎么演：微动作、表演指导 → 提示词里演得太过走「视频提示词的某一段」 | `references/craft/performance/index.md` | 表演写法 |

### 分镜

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 分镜脚本：把一场戏拆成镜头，几个镜头、每镜拍什么、台词落在谁脸上（scene breakdown, storyboard, shot list） | `references/storyboard/breakdown.md`（镜头功能 `references/storyboard/shot-functions.md`，拆法风格 `references/storyboard/three-ways.md`，场景示例 `references/storyboard/scene-types.md`，全片示例 `references/storyboard/example.md`）+ `templates/storyboard-script.md` | 读戏卡 + 分镜脚本（镜号、功能、景别、角度、运镜、画面、台词、时长、生成）+ 生成清单 `templates/shot-list.md` |
| 镜头策略：覆盖、走位、调度的取舍，不要整场表格（coverage, blocking） → 要整场拆成分镜脚本走上一行 | `references/craft/staging/04-coverage.md` + `references/craft/staging/index.md` + `references/craft/visual/index.md`（读戏 `references/craft/staging/06-scene-analysis.md`，场景卡 `templates/scene-card.md`） | 镜头策略 + 关键镜头 |
| 分镜图：画什么、怎么审（storyboard frames） | `references/storyboard/frames.md` | 分镜图与审图意见 |
| 动态分镜（animatic） | `references/storyboard/animatic.md` | 动态分镜方案 |
| 连续性：人物换边、越轴、方向反、道具 / 服装跳（continuity） | `references/storyboard/continuity.md`；两人对话加 `references/camera/recipes/dialogue-two.md` | 连续性台账与修法 |
| 节奏：剪出来平、拖、赶，镜长怎么排（pacing） | `references/storyboard/pacing.md` | 节奏表 + 改法 |

### 镜头语言

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 镜头语言：景别 / 角度 / 运镜 / 焦段 / 光 / 构图 / 转场怎么写、能否生成（camera movement, framing, lens, lighting） | `references/camera/index.md` 选词典：`references/camera/lexicon-shot.md` / `references/camera/lexicon-move.md` / `references/camera/lexicon-light.md` / `references/camera/lexicon-frame.md` / `references/camera/lexicon-transition.md` | 取景句 / 运动句 / 光的描述 / 剪辑转场 + 生成方式 |
| 想要某种效果（压迫、孤立、揭示…）不知怎么拍 | `references/camera/intent.md` | 拍法组合 + 示例 |
| 某类场景怎么排镜头：对话、追逐、打斗、悬疑、亲密、蒙太奇、开场结尾、反转打脸 | `references/camera/recipes/index.md` → 对应配方 | 镜头序列 + 逐镜提示词 + 生成方式 |

### 提示词与生成

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 图像 / 视频提示词：单镜、基本语法、单镜模板、token 写法（image prompt, SDXL） → 多镜头走下一行 | `references/aigc/prompt-syntax.md` + `templates/ai-prompt.md` | 按模式出提示词 |
| 视频提示词：按分镜脚本写多镜头 / 长提示词，导演 + 摄影 + 场记写进一条（multi-shot video prompt） → 竖屏短剧走「短剧：片段提示词」 | `references/video-prompt/compile.md`（段落 `references/video-prompt/anatomy.md`，档位 `references/video-prompt/index.md`，示例 `references/video-prompt/example.md`、`references/video-prompt/scene-prompts.md`）+ `templates/video-prompt.md` | 生成单位切分 + 逐段提示词（全局段复用、逐镜时间线、总锁、negative） |
| 视频提示词的某一段怎么写，或生成里的某个毛病：人物看镜头 / 演得太过 → 表演；多出路人 / 封不住音乐和字 → 锁；摄影机乱漂 → 摄影机；东西没重量 / AI 感 → 物理；台词 / 画内声 → 声音；一镜到底 / 人群 → 一镜到底。竖屏短剧的口型、站位走「短剧：片段提示词」 | 摄影机 `references/video-prompt/camera-behavior.md`；表演 `references/video-prompt/acting.md`；物理与 AI 感 `references/video-prompt/physics.md`；声音与台词 `references/video-prompt/audio.md`；锁与 negative `references/video-prompt/locks.md`；一镜到底与人群 `references/video-prompt/one-take.md` | 对应段落的提示词写法 |
| 怎么生成：参考图生 / 首帧 / 首尾帧 / 续接，镜头之间怎么接（first/last frame） | `references/aigc/workflow.md` | 生成方式与串联 |
| 选模型 / 模型能力 / 两个模型怎么选（model choice） | `references/aigc/models.md` | 模型与模式 |
| 资产一致性 / 参考图 / 道具与场景锁（reference images） | `references/aigc/assets.md` + `templates/asset-tokens.md` | 资产卡 + 参考图规格 |

### 声音、风格与交付

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 声音 / 配乐 / 剪辑方案（sound design, editing） → 竖屏短剧走「短剧：成片」；只问剪辑节奏走「节奏」 | `references/craft/sound/index.md` + `templates/edit-sound.md` | 声音分工 + 剪辑方案 |
| 导演 / 摄影风格参考、混搭、风格卡（style reference, style brief） → 做广告再加读 `references/writing/genres/brand.md` | `references/taxonomy.md` 选族 → `references/directors/<slug>.md` 或 `references/cinematographers/<slug>.md`，及 `references/prompts/` 或 `references/prompts-cinematographers/` 下同名文件；混搭（含导演 × 摄影）加 `references/mixing.md`；风格卡用 `templates/style-brief.md` | 1 主参考 + 0–1 副参考（或导演 × 摄影）+ 视觉基元 / 风格卡 |
| 迭代 / 预算 / 交付；15–90 秒短片怎么控镜头数 | `references/craft/production/index.md`（预算 `references/craft/production/03-budget.md`，短片 `references/craft/production/04-short-form.md`；生成顺序 `references/aigc/workflow.md`） | 镜头数 / 迭代预算 / 交付 |

### 竖屏短剧

先读 `references/drama/index.md`，产物按 `references/drama/standard.md` 字段出稿。

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 短剧：立项 / 题材 | `references/drama/01-premise.md` + `templates/drama-bible.md` | setting |
| 短剧：出海（台词非中文时也读） | `references/drama/01-premise.md` + `references/drama/09-overseas.md` | 本地化 setting |
| 短剧：画风 / 漫剧 | `references/drama/10-look.md` | 画风设定 |
| 短剧：分集大纲 / 付费点（episode outline） | `references/drama/02-season.md` + `templates/drama-outline.md` | outline |
| 短剧：单集剧本 | `references/drama/03-episode.md` + `references/drama/04-script.md` + `templates/drama-episode.md` | script |
| 短剧：角色场景拆解 / 造型图 | `references/drama/05-breakdown.md` + `templates/drama-breakdown.md` | breakdown + 造型图规格 |
| 短剧：分镜 | `references/drama/06-storyboard.md` + `templates/drama-storyboard.md` | segments |
| 短剧：片段提示词 / 口型 / 站位 | `references/drama/07-segment-prompt.md` | 编译提示词；问题回分镜改 |
| 短剧：成片 / 配乐字幕 / 质检 | `references/drama/08-cut-qc.md` | 成片方案 + 质检 |
| 短剧：字段 / JSON / 对接平台 | `references/drama/standard.md` | 按标准字段落表 |

### 实拍

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 明确要实拍（排期、通告、布光等） | 说明默认不做实拍；用户坚持时，通用的拆解、排期、风险建议取自 `references/craft/production/01-breakdown.md`、`references/craft/production/02-schedule.md`、`references/craft/production/05-risk.md`，换成实拍语境讲 | 简短说明 + 通用建议 |

竖屏短剧第一次进入时先读 `references/drama/index.md`（阶段路由、默认值、与通用规则的差异），产物字段以 `references/drama/standard.md` 为准。

## 使用原则

1. **默认 AIGC**；不主动给实拍方案。
2. **先判断请求类型**，不要一套流程套所有人。
3. **需要时才问**，最多 3 个关键问题。
4. **每条建议落到 AIGC 产物**。
5. **引用导演/摄影时给视觉基元**，不给剧组职位。

## AIGC 提示规则

先按目标模型选模式（`references/aigc/prompt-syntax.md`）：

- **模式 A（默认）**：大语言模型编码的图像/视频模型（Seedance、Kling、Veo、Wan、Hailuo、GPT-Image、Nano Banana、Flux 等）。自然语言按时间顺序写；空间写画面左右和机位前后；有参考图时不重写外貌、只写识别特征锁；正面描述优先，顽固默认集中封住，negative 写这一镜的错误版本；多镜头长提示词见 `references/video-prompt/`。
- **模式 B**：CLIP 系模型（SD / SDXL 及微调）。token 块、`|` 分隔；一个提示一个主语；否定进 NEGATIVE；token 逐字复用；图生视频只写运动。

生成方式见 `references/aigc/workflow.md`，模型能力见 `references/aigc/models.md`。

通用：具体胜过形容；风格放最后、8–15 个视觉基元；不写画幅、分辨率、导演名；一致性先靠参考图，再靠首帧续接，文本锁兜底。竖屏短剧按 `references/drama/standard.md`。

## 目录结构

```
.claude/skills/film-creation/
  SKILL.md                  路由手册
  references/
    craft/                  6 个 AIGC 方法模块
      index.md              顶层导航
      sources.md            全局来源表
      story/ visual/ staging/ performance/ sound/ production/
    writing/                写作查阅层
      index.md              用法与对白总规则
      dialogue.md           对白手法
      devices.md            叙事技巧
      intent.md             按效果反查
      genres/               类型配方（8 类）
      doctor.md             剧本诊断
      example.md            完整示例（初稿 → 诊断 → 改稿）
      sources.md            来源
    storyboard/             分镜查阅层
      index.md              产物关系与总规则
      breakdown.md          拆解七步与分镜脚本格式
      shot-functions.md     镜头功能词典
      three-ways.md         同一场戏的三种拆法
      frames.md             分镜图
      animatic.md           动态分镜
      continuity.md         连续性
      pacing.md             节奏
      scene-types.md        对话 / 动作 / 情绪戏拆解示例
      example.md            全片分镜脚本示例
      sources.md            来源
    video-prompt/           视频提示词层
      index.md              提示词是制作文件；三档长度；总规则
      anatomy.md            十九个段落
      compile.md            从分镜脚本编译；场 5 完整示例
      camera-behavior.md    摄影机写成操作员；焦段与视野
      acting.md             表演指导与反误读
      physics.md            物理与反 AI 质感
      audio.md              声音与台词
      locks.md              锁与 negative
      one-take.md           一镜到底与人群调度
      example.md            全片提示词示例（三层复用）
      scene-prompts.md      轻量 / 标准 / 重型示例
      sources.md            来源
    camera/                 镜头语言查阅层
      index.md              用法与可靠性分级
      lexicon-shot.md       景别、角度、焦段、景深
      lexicon-move.md       运镜、航拍与穿越、速度与时间
      lexicon-light.md      人物光型、画内光源、时段与调性
      lexicon-frame.md      构图：位置、线条、层次、画框
      lexicon-transition.md 转场：剪切、光学、遮挡、匹配与变形
      intent.md             按目的反查拍法
      recipes/              场景手法配方（9 类场景）
      sources.md            来源
    aigc/
      prompt-syntax.md      两种提示词模式与失败模式
      assets.md             资产卡、参考图与一致性
      workflow.md           生成方式的选择与串联（关键帧先行）
      models.md             模型能力卡
    drama/                  竖屏短剧
      index.md              阶段路由与默认值
      standard.md           生产标准（字段契约）
      01-09                 立项 → 成片的分阶段写法（09 出海）
      10-look.md            画风与漫剧（非写实画风）
      sources.md            来源
    taxonomy.md             风格族谱（风格参考先读这里选族）
    index.md                125 导演 + 29 摄影总表（按地域/年代查全表时读）
    mixing.md               视觉混搭 + 导演 × 摄影
    prompting.md            档案 → 提示词的转换规则
    directors/<slug>.md     125 份导演档案
    prompts/<slug>.md       125 份导演提示参考
    cinematographers/<slug>.md       29 份摄影档案
    prompts-cinematographers/<slug>.md 29 份摄影提示参考
  templates/
    treatment.md            AIGC 概念 / beat
    script.md               短片剧本
    scene-card.md           scene to shots
    storyboard-script.md    分镜脚本
    shot-list.md            生成清单（批次、进度、版本）
    video-prompt.md         视频提示词（三层复用、预判误读、自检）
    character-sheet.md      三面板角色表
    asset-tokens.md         资产卡（参考图 + 描述 + token）
    edit-sound.md           剪辑与声音
    ai-prompt.md            AI 生成提示卡
    style-brief.md          AIGC 风格卡
    drama-*.md              短剧：bible / outline / episode / breakdown / storyboard
DESIGN.md                   设计说明
dev-history/                开发过程简报（写作标准、改写简报，供维护者参考）
tools/                      索引、结构/视觉/提示/重复度检查；镜头层、写作层、分镜层、视频提示词层、路由检查
```

## 扩展

- 新增导演：复制 `templates/director-entry.md`，按八节填写
- 新增摄影：按 `dev-history/DP_BRIEF.md` 的结构
- 调整方法模块：读 `dev-history/AIGC_CRAFT_BRIEF.md`，改完跑 `python tools/check_craft.py`
- 调整镜头语言查阅层：词典条目按 `references/camera/index.md` 的字段写，配方按 `references/camera/recipes/index.md` 的结构写，改完跑 `python tools/check_camera.py`
- 调整写作查阅层：手法按 `references/writing/dialogue.md`、技巧按 `references/writing/devices.md` 的字段写，类型按 `references/writing/genres/index.md` 的结构写，改完跑 `python tools/check_writing.py`
- 调整分镜查阅层：镜头功能按 `references/storyboard/shot-functions.md` 的字段写，分镜脚本表按 `references/storyboard/breakdown.md` 的九列写（功能取自功能词典，生成栏写可靠性），改完跑 `python tools/check_storyboard.py`
- 调整视频提示词层：段落按 `references/video-prompt/anatomy.md` 的五个字段写，词库条目按「写法 / 防什么误读 / 用在 / 别这样写」写，完整提示词的 EDIT 时间码要接得上、CRITICAL 不超过 3 处、总锁不超过 8 条，改完跑 `python tools/check_video_prompt.py`
- 调整路由：改 SKILL.md 的 description 或路由表后，同步 README 的路由表，改完跑 `python tools/check_routing.py`（触发词、路径、模板是否都挂上、全部文件是否可达）

全局复用：把 `.claude/skills/film-creation/` 整个复制到 `~/.claude/skills/film-creation/`。

## 数据来源与边界

- 创作方法来自 `docs/` 下的 19 本电影书，经原创提炼；`docs/` 不进入公开仓库。
- 导演/摄影档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- AIGC 部分按模型类型给两种写法，不绑定某个平台；画幅、分辨率交给工具参数。
- 默认不提供实拍执行方案。

## License

MIT © 2026 Ethan
