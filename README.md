# AIGC 创作参考包 film-creation

默认用于 **AI 图像 / 视频作品**，不用于实拍。

LLM 读到它之后，能判断用户要什么、读哪一块、产出一组可直接生成的 AIGC 产物。

## 快速开始

- 「我想做一个 1 分钟 AI 短片，只有一个房间和两个人，帮我出概念和 beat」
- 「设计一个角色，给我三面板角色表和固定 token」
- 「把这场戏拆成 6 个镜头，每镜给图像和视频提示」
- 「这个角色在 10 个镜头里怎么保持一致」
- 「用王家卫 × 卢贝兹基的视觉 token，写雨夜便利店的镜头」
- 「做一部 60 集出海竖屏短剧，先给 3 个方向」「把第 3 集切成 15 秒片段的分镜，输出 JSON」

## 默认输出

- 概念 / beat sheet
- 镜头序列
- 图像 prompt token
- 视频 motion token
- 资产 token / 角色表
- negative token
- 剪辑 / 声音方案

**不输出**：剧组、演员排练、选角、预算、排期、通告、灯具型号、轨道、现场录音——除非用户明确要求实拍。

## 包里有什么

- **6 个 AIGC 方法模块**：故事、视觉、调度、表演、声音、制作
- **竖屏短剧**：生产标准（立项 → 大纲 → 剧本 → 拆解 → 造型图 → 分镜 → 片段提示词 → 成片的字段契约）+ 各阶段写法，见 `.claude/skills/film-creation/references/drama/`
- **125 位导演 + 29 位摄影指导**：视觉 token 参考
- **AIGC token 规则**：注意力友好的提示写法、文本资产、固定三面板角色表
- **模板**：concept、scene-to-shots、shot prompt、asset tokens、character sheet、edit-sound、AI prompt

## 请求路由表

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 概念 | `craft/story/index.md` | 一句话 + beat sheet |
| 角色 / 人物 | `craft/performance/index.md` + `templates/character-sheet.md` | 角色 token + 三面板提示 |
| 镜头序列 / 分镜 | `craft/staging/index.md` + `craft/visual/index.md` | shot list + prompts |
| 图像提示 | `aigc/prompt-syntax.md` | 图像 token + negative |
| 视频提示 | `aigc/prompt-syntax.md` | motion token |
| 资产一致性 | `aigc/assets.md` + `templates/asset-tokens.md` | 固定 token |
| 声音 / 剪辑 | `craft/sound/index.md` + `templates/edit-sound.md` | 声音层 + 剪辑方案 |
| 风格参考 | `index.md` + `taxonomy.md` | 2–3 个参考 + 视觉 token |
| 迭代 / 交付 | `craft/production/index.md` | 镜头数 / 迭代预算 / 交付 |
| 竖屏短剧 | `drama/index.md` | setting / outline / script / breakdown / storyboard（按 `drama/standard.md`） |
| 明确要实拍 | 先说明本包默认不做实拍；按需给通用建议 | — |

## 使用原则

1. **默认 AIGC**；不主动给实拍方案。
2. **先判断请求类型**，不要一套流程套所有人。
3. **需要时才问**，最多 3 个关键问题。
4. **每条建议落到 AIGC 产物**。
5. **引用导演/摄影时给视觉 token**，不给剧组职位。

## AIGC 提示规则

1. 一个提示一个主语。
2. 正向只写肯定；否定全部进 NEGATIVE。
3. 戒连接词：不写 and / with / while / then；用 `|` 分块。
4. 词序即权重：主体 → 环境 → 镜头 → 光色 → 风格。
5. 控制预算：核心 30–60 词，风格 8–15 个概念。
6. 一致性靠文本 token 锁：同一角色/场景逐字复用；不用参考图。
7. 人物资产用固定三面板角色表：`templates/character-sheet.md`。
8. 不写画幅；不做平台参数；不绑定模型。
9. 图像与运动分离：视频提示只写运动/镜头/时长。

## 目录结构

```
.claude/skills/film-creation/
  SKILL.md                  路由手册
  references/
    craft/                  6 个 AIGC 方法模块
      index.md              顶层导航
      sources.md            全局来源表
      story/ visual/ staging/ performance/ sound/ production/
    aigc/                   token 语法、文本资产
    index.md                125 导演 + 29 摄影总表
    taxonomy.md             风格族谱
    mixing.md               视觉混搭 + 导演 × 摄影
    prompting.md            档案 → token 的转换规则
    directors/<slug>.md     125 份导演档案
    prompts/<slug>.md       125 份导演提示参考
    cinematographers/<slug>.md       29 份摄影档案
    prompts-cinematographers/<slug>.md 29 份摄影提示参考
  templates/
    treatment.md            AIGC 概念 / beat
    scene-card.md           scene to shots
    shot-list.md            shot prompt list
    character-sheet.md      三面板角色表
    asset-tokens.md         人物/场景/道具 token
    edit-sound.md           剪辑与声音
    ai-prompt.md            AI 生成提示卡
    style-brief.md          AIGC 风格卡
DESIGN.md                   设计说明
AIGC_CRAFT_BRIEF.md         AIGC 模块改写简报
DP_BRIEF.md                 摄影指导层简报
tools/                      索引、结构/视觉/提示/重复度检查
```

## 扩展

- 新增导演：复制 `templates/director-entry.md`，按八节填写
- 新增摄影：按 `DP_BRIEF.md` 的 14 节结构
- 调整方法模块：读 `AIGC_CRAFT_BRIEF.md`

全局复用：把 `.claude/skills/film-creation/` 整个复制到 `~/.claude/skills/film-creation/`。

## 数据来源与边界

- 创作方法来自 `docs/` 下的 19 本电影书，经原创提炼；`docs/` 不进入公开仓库。
- 导演/摄影档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- AIGC 部分只写文本 token 规则；不绑定平台，不使用参考图，不写画幅。
- 默认不提供实拍执行方案。

## License

MIT © 2026 Ethan
