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
- **竖屏短剧**：生产标准（立项 → 大纲 → 剧本 → 拆解 → 造型图 → 分镜 → 片段提示词 → 成片的字段契约）+ 各阶段写法，见 `.claude/skills/film-creation/references/drama/`
- **125 位导演 + 29 位摄影指导**：视觉基元参考
- **AIGC 提示规则**：两种模式（自然语言 + 参考图 / token 块）、资产卡与一致性分层、三面板角色表
- **模板**：concept、scene-to-shots、shot prompt、资产卡、character sheet、edit-sound、AI prompt；短剧模板

## 请求路由表

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 概念 | `craft/story/index.md` | 一句话 + beat sheet |
| 角色 / 人物 | `craft/performance/index.md` + `templates/character-sheet.md` | 资产卡 + 角色表提示词 |
| 镜头序列 / 分镜 | `craft/staging/index.md` + `craft/visual/index.md` | shot list + prompts |
| 图像 / 视频提示词 | `aigc/prompt-syntax.md` | 按模式出提示词 |
| 资产一致性 / 参考图 | `aigc/assets.md` + `templates/asset-tokens.md` | 资产卡 + 参考图规格 |
| 声音 / 剪辑 | `craft/sound/index.md` + `templates/edit-sound.md` | 声音层 + 剪辑方案 |
| 风格参考 | `index.md` + `taxonomy.md` | 2–3 个参考 + 视觉基元 |
| 迭代 / 交付 | `craft/production/index.md` | 镜头数 / 迭代预算 / 交付 |
| 竖屏短剧 | `drama/index.md` | setting / outline / script / breakdown / storyboard（按 `drama/standard.md`） |
| 明确要实拍 | 先说明本包默认不做实拍；按需给通用建议 | — |

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
    aigc/                   两种提示词模式、资产与一致性
    drama/                  竖屏短剧：生产标准 + 分阶段写法
    index.md                125 导演 + 29 摄影总表
    taxonomy.md             风格族谱
    mixing.md               视觉混搭 + 导演 × 摄影
    prompting.md            档案 → 提示词的转换规则
    directors/<slug>.md     125 份导演档案
    prompts/<slug>.md       125 份导演提示参考
    cinematographers/<slug>.md       29 份摄影档案
    prompts-cinematographers/<slug>.md 29 份摄影提示参考
  templates/
    treatment.md            AIGC 概念 / beat
    scene-card.md           scene to shots
    shot-list.md            shot prompt list
    character-sheet.md      三面板角色表
    asset-tokens.md         资产卡（参考图 + 描述 + token）
    edit-sound.md           剪辑与声音
    ai-prompt.md            AI 生成提示卡
    style-brief.md          AIGC 风格卡
    drama-*.md              短剧：bible / outline / episode / breakdown / storyboard
DESIGN.md                   设计说明
dev-history/                开发过程简报（写作标准、改写简报，供维护者参考）
tools/                      索引、结构/视觉/提示/重复度检查
```

## 扩展

- 新增导演：复制 `templates/director-entry.md`，按八节填写
- 新增摄影：按 `dev-history/DP_BRIEF.md` 的结构
- 调整方法模块：读 `dev-history/AIGC_CRAFT_BRIEF.md`，改完跑 `python tools/check_craft.py`

全局复用：把 `.claude/skills/film-creation/` 整个复制到 `~/.claude/skills/film-creation/`。

## 数据来源与边界

- 创作方法来自 `docs/` 下的 19 本电影书，经原创提炼；`docs/` 不进入公开仓库。
- 导演/摄影档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- AIGC 部分按模型类型给两种写法，不绑定某个平台；画幅、分辨率交给工具参数。
- 默认不提供实拍执行方案。

## License

MIT © 2026 Ethan
