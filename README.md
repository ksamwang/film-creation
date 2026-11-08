# 电影创作参考包 film-creation

一份给 **LLM** 用的创作参考包 + 路由手册。不是用户向导，也不是提示词模板库。

LLM 读到它之后，能判断用户要什么、该读哪一块、给到什么粒度。

## 包里有什么

- **6 个 craft 方法模块**：故事、视觉、调度、表演、声音、制作
- **125 位导演 + 29 位摄影指导**：风格参考档案
- **AIGC token 规则**：注意力友好的提示写法、文本资产 token、固定三面板角色表
- **模板**：treatment、scene card、shot list、character sheet、asset tokens、AI prompt

## LLM 怎么用

1. **判断请求类型**：故事、表演、调度、分镜、声音、视觉、风格、AIGC 提示。
2. **读对应文件**：按下面的路由表。
3. **需要时才问**：最多 3 个关键问题；问题必须改变输出。
4. **按粒度输出**：一句话建议 / 单场方案 / 完整计划 / 分镜 / 提示。

## 请求路由表

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 剧本诊断 | `craft/story/index.md` | 诊断 + 修改建议 |
| 短片 / 长片结构 | `craft/story/index.md` | logline + 结构方案 |
| 人物 / 表演 | `craft/performance/index.md` | 动作表 + 给演员的指令 |
| 调度 / 走位 / 覆盖 | `craft/staging/index.md` | 走位 + 机位 + 覆盖 |
| 分镜 / 镜头设计 | `craft/staging/index.md` + `craft/visual/index.md` | 镜头表 |
| 视觉 / 色彩 / 光线 / 镜头 | `craft/visual/index.md` + 导演/摄影档案 | 视觉方案 + 参考 |
| 声音 | `craft/sound/index.md` | 声音层方案 |
| 制作 / 预算 / 排期 | `craft/production/index.md` | 约束 + 计划 |
| 想要某种风格 | `index.md` + `taxonomy.md` | 2–3 个候选 + 约束 |
| 混搭 | `mixing.md` | 主/副风格 + 冲突规则 |
| AIGC 图像提示 | `aigc/prompt-syntax.md` + `aigc/assets.md` | 图像 token 块 |
| AIGC 视频提示 | `aigc/prompt-syntax.md` + `aigc/assets.md` | 运动 token 块 |
| 已有提示要优化 | `aigc/prompt-syntax.md` | 诊断 + 改写 |

## 使用原则

1. **先判断请求类型**，不要一套流程套所有人。
2. **需要时才问**，最多 3 个关键问题。
3. **先戏后风格**；风格是约束，不是内容。
4. **输出粒度跟用户走**。
5. **引用导演/摄影时给约束**，不给名字堆砌。

## 导演 / 摄影怎么用

- 先问“这场戏需要什么”，再选参考。
- 1 位主参考 + 0–1 位副参考。
- 只取 2–3 条约束（一个机位、一个光源、一个剪辑规则）。
- 用「反向约束」当检查表。
- 提示词里不堆导演名字，用视觉基元。

## AIGC 提示规则

1. 一个提示一个主语。
2. 正向只写肯定；否定全部进 NEGATIVE。
3. 戒连接词：不写 and / with / while / then；用 `|` 分块。
4. 词序即权重：主体 → 环境 → 镜头 → 光色 → 风格。
5. 控制预算：核心 30–60 词，风格 8–15 个概念。
6. 一致性靠文本 token 锁：同一角色/场景逐字复用同一串 token；不用参考图。
7. 人物资产使用固定三面板角色表：`templates/character-sheet.md`（左无头正面、中背面、右 3/4 特写，全表一张脸）。
8. 不写画幅；不做平台参数；不绑定模型。
9. 图像与运动分离：视频提示只写运动/镜头/时长。

## 输出粒度

- 一句提问：1–3 段 + 1 条可执行规则。
- 一场戏：scene card + 3–5 个镜头建议。
- 一个项目：treatment + shot list + 声音/视觉注记。
- 提示：token 块 + NEGATIVE；可选 2 个变体。

## 目录结构

```
.claude/skills/film-creation/
  SKILL.md                  路由手册
  references/
    craft/                  6 个方法模块
      index.md              顶层导航
      sources.md            全局来源表
      story/ visual/ ...    每个模块 index + 子文件
    aigc/                   token 语法、文本资产
    index.md                125 导演 + 29 摄影总表
    taxonomy.md             风格族谱
    mixing.md               混搭 + 导演 × 摄影
    prompting.md            档案 → token 的转换规则
    directors/<slug>.md     125 份导演档案
    prompts/<slug>.md       125 份导演提示参考
    cinematographers/<slug>.md       29 份摄影档案
    prompts-cinematographers/<slug>.md 29 份摄影提示参考
  templates/
    treatment.md
    scene-card.md
    shot-list.md
    character-sheet.md
    asset-tokens.md
    ai-prompt.md
    style-brief.md
DESIGN.md                   设计说明
CRAFT_DEEP_BRIEF.md          方法模块深度提炼简报
DP_BRIEF.md                 摄影指导层简报
tools/                      索引、结构/视觉/提示/重复度检查
```

## 扩展

- 新增导演：复制 `templates/director-entry.md`，按八节填写
- 新增摄影：按 `DP_BRIEF.md` 的 14 节结构
- 调整方法模块：读 `CRAFT_DEEP_BRIEF.md`

全局复用：把 `.claude/skills/film-creation/` 整个复制到 `~/.claude/skills/film-creation/`。

## 数据来源与边界

- 创作方法来自 `docs/` 下的 19 本电影书，经原创提炼；`docs/` 不进入公开仓库。
- 导演/摄影档案依据公开影片与常见影史论述撰写，不收录生平、奖项、票房。
- AIGC 部分只写文本 token 规则；不绑定平台，不使用参考图，不写画幅。

## License

MIT © 2026 Ethan
