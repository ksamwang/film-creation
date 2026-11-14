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

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 概念 | `references/craft/story/index.md` | 一句话 + beat sheet |
| 写台词 / 改对白（太直白、太水、一个腔调） | `references/writing/dialogue.md` | 改后的台词 + 镜头落法 |
| 叙事技巧（伏笔、反转、倒计时、母题…）/ 想让观众爽、笑、哭、怕 | `references/writing/devices.md` 或 `references/writing/intent.md` | 技巧落法 / 情绪机制 + 写法 |
| 按类型写（悬疑、爱情、喜剧、恐怖、犯罪 / 动作、科幻 / 奇幻、家庭、广告） | `references/writing/genres/index.md` → 对应类型 | 类型约定 + beat 表 + 陈词滥调替代 |
| 写一个完整短片剧本 / 要剧本模板 | `templates/script.md`（示例 `references/writing/example.md`） | 片头信息 + beat 表 + 正文 + 台词表 + 检查 |
| 剧本 / beat 哪里不好、怎么改 | `references/writing/doctor.md` | 诊断：最大问题 + 证据 + 修法 |
| 角色 / 人物 | `references/craft/performance/index.md` + `templates/character-sheet.md` | 资产卡 + 角色表提示词 |
| 分镜脚本：一场戏拆几个镜头、每镜拍什么、台词落在谁脸上 | `references/storyboard/breakdown.md`（镜头功能 `references/storyboard/shot-functions.md`，拆法风格 `references/storyboard/three-ways.md`，示例 `references/storyboard/example.md`）+ `templates/storyboard-script.md` | 读戏卡 + 分镜脚本 + 生成清单 |
| 分镜图 / 动态分镜 / 连续性 / 节奏 | `references/storyboard/frames.md`、`references/storyboard/animatic.md`、`references/storyboard/continuity.md`、`references/storyboard/pacing.md` | 分镜图与审图意见 / 动态分镜方案 / 连续性台账与修法 / 节奏表 |
| 镜头序列 / 分镜 | `references/craft/staging/index.md` + `references/craft/visual/index.md` | shot list + prompts |
| 图像 / 视频提示词 | `references/aigc/prompt-syntax.md` | 按模式出提示词 |
| 镜头语言：角度 / 运镜 / 焦段 / 光 / 构图 / 转场怎么写、能否生成 | `references/camera/index.md` 选词典：`lexicon-shot` / `lexicon-move` / `lexicon-light` / `lexicon-frame` / `lexicon-transition` | 取景句 / 运动句 / 光的描述 / 剪辑转场 + 生成方式 |
| 想要某种效果（压迫、孤立、揭示…）不知怎么拍 | `references/camera/intent.md` | 拍法组合 + 示例 |
| 某类场景怎么排镜头（对话、追逐、打斗、悬疑、亲密、蒙太奇、开场结尾、反转打脸） | `references/camera/recipes/index.md` → 对应配方 | 镜头序列 + 逐镜提示词 + 生成方式 |
| 怎么生成 / 用哪种生成方式 / 镜头衔接 | `references/aigc/workflow.md` | 生成方式选择与串联（文生、参考图生、首帧、首尾帧、续接、关键帧先行） |
| 选模型 / 模型能力 | `references/aigc/models.md` | 模型与提示词模式（参考图上限、原生音频、negative 等） |
| 资产一致性 / 参考图 | `references/aigc/assets.md` + `templates/asset-tokens.md` | 资产卡 + 参考图规格 |
| 声音 / 剪辑 | `references/craft/sound/index.md` + `templates/edit-sound.md` | 声音层 + 剪辑方案 |
| 风格参考 | `references/taxonomy.md` 选族 → `references/directors/<slug>.md` 或 `references/cinematographers/<slug>.md`，再读 `references/prompts/` 或 `references/prompts-cinematographers/` 下的同名文件；混搭读 `references/mixing.md` | 2–3 个参考 + 视觉基元 |
| 按地域 / 年代查导演、摄影全表 | `references/index.md`（较大，只在需要全表时读） | 候选名单 |
| 迭代 / 交付 | `references/craft/production/index.md` | 镜头数 / 迭代预算 / 交付 |
| 竖屏短剧：立项 / 题材 | `references/drama/01-premise.md` | 立项设定 setting |
| 竖屏短剧：出海 / 海外市场 | `references/drama/01-premise.md` + `references/drama/09-overseas.md` | 本地化的立项设定 |
| 竖屏短剧：画风 / 漫剧 / 视觉风格 | `references/drama/10-look.md` | 画风设定（含非写实画风） |
| 竖屏短剧：分集大纲 / 付费点 | `references/drama/02-season.md` | 分集大纲 outline |
| 竖屏短剧：单集剧本 | `references/drama/03-episode.md` + `references/drama/04-script.md` | 结构化剧本 script |
| 竖屏短剧：角色 / 场景拆解、造型图 | `references/drama/05-breakdown.md` | 拆解 breakdown + 造型图规格 |
| 竖屏短剧：分镜 | `references/drama/06-storyboard.md` | 分镜 segments |
| 竖屏短剧：片段提示词 / 口型 / 站位 | `references/drama/07-segment-prompt.md` | 编译后的片段提示词，问题回分镜改 |
| 竖屏短剧：成片 / 配乐字幕 / 质检 | `references/drama/08-cut-qc.md` | 成片方案 + 质检结论 |
| 竖屏短剧：字段 / JSON / 对接平台 | `references/drama/standard.md` | 按标准字段落表 |
| 明确要实拍 | 先说明本包默认不做实拍；按需给通用建议 | — |

竖屏短剧第一次进入时先读 `references/drama/index.md`（阶段路由、默认值、与通用规则的差异），产物字段以 `references/drama/standard.md` 为准。

## 使用原则

1. **默认 AIGC**；不主动给实拍方案。
2. **先判断请求类型**，不要一套流程套所有人。
3. **需要时才问**，最多 3 个关键问题。
4. **每条建议落到 AIGC 产物**。
5. **引用导演/摄影时给视觉基元**，不给剧组职位。

## AIGC 提示规则

先按目标模型选模式（`references/aigc/prompt-syntax.md`）：

- **模式 A（默认）**：大语言模型编码的图像/视频模型（Seedance、Kling、Veo、Wan、Hailuo、GPT-Image、Nano Banana、Flux 等）。自然语言按时间顺序写；空间写画面左右和机位前后；有参考图时不重复外貌；正面描述，否定只进 negative 参数。
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
    character-sheet.md      三面板角色表
    asset-tokens.md         资产卡（参考图 + 描述 + token）
    edit-sound.md           剪辑与声音
    ai-prompt.md            AI 生成提示卡
    style-brief.md          AIGC 风格卡
    drama-*.md              短剧：bible / outline / episode / breakdown / storyboard
DESIGN.md                   设计说明
dev-history/                开发过程简报（写作标准、改写简报，供维护者参考）
tools/                      索引、结构/视觉/提示/重复度检查；镜头层、写作层、分镜层检查
```

## 扩展

- 新增导演：复制 `templates/director-entry.md`，按八节填写
- 新增摄影：按 `dev-history/DP_BRIEF.md` 的结构
- 调整方法模块：读 `dev-history/AIGC_CRAFT_BRIEF.md`，改完跑 `python tools/check_craft.py`
- 调整镜头语言查阅层：词典条目按 `references/camera/index.md` 的字段写，配方按 `references/camera/recipes/index.md` 的结构写，改完跑 `python tools/check_camera.py`
- 调整写作查阅层：手法按 `references/writing/dialogue.md`、技巧按 `references/writing/devices.md` 的字段写，类型按 `references/writing/genres/index.md` 的结构写，改完跑 `python tools/check_writing.py`
- 调整分镜查阅层：镜头功能按 `references/storyboard/shot-functions.md` 的字段写，分镜脚本表按 `references/storyboard/breakdown.md` 的九列写（功能取自功能词典，生成栏写可靠性），改完跑 `python tools/check_storyboard.py`

全局复用：把 `.claude/skills/film-creation/` 整个复制到 `~/.claude/skills/film-creation/`。

## 数据来源与边界

- 创作方法来自 `docs/` 下的 19 本电影书，经原创提炼；`docs/` 不进入公开仓库。
- 导演/摄影档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- AIGC 部分按模型类型给两种写法，不绑定某个平台；画幅、分辨率交给工具参数。
- 默认不提供实拍执行方案。

## License

MIT © 2026 Ethan
