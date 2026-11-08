---
name: film-creation
description: 电影与 AIGC 创作参考包，供 LLM 在用户提出故事、剧本诊断、人物表演、场面调度、分镜、声音、视觉设计、风格参考或 AI 图像/视频提示需求时调用。内置 6 个 craft 方法模块、125 位导演、29 位摄影指导与注意力友好的提示规则。
---

# 电影创作参考包

这是一份给 LLM 用的参考包 + 路由手册，不是给用户点的固定流程。

LLM 的职责：**判断请求类型 → 读对应文件 → 按需要提问 → 输出对应粒度的方案。**

## 包里有什么

- `references/craft/` — 6 个方法模块：故事、视觉、调度、表演、声音、制作
- `references/directors/` + `references/cinematographers/` — 125 位导演、29 位摄影指导
- `references/aigc/` — 注意力友好的提示规则、文本资产 token
- `templates/` — treatment、scene card、shot list、asset tokens、AI prompt
- `references/index.md` / `taxonomy.md` / `mixing.md` / `prompting.md` — 检索、族谱、混搭、转换

## 请求路由表

| 用户意图 | 先读 | 输出 |
|---|---|---|
| 故事 / 剧本诊断 | `craft/story/index.md` | 诊断 + 修改建议 |
| 短片 / 长片结构 | `craft/story/index.md` | logline + 结构方案 |
| 人物 / 表演 | `craft/performance/index.md` | 动作表 + 给演员的指令 |
| 人物资产 / 角色表 | `templates/character-sheet.md` + `aigc/assets.md` | trait card + 三面板角色表（单条 prompt） |
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
2. **需要时才问**，最多 3 个关键问题；问题必须改变输出。
3. **先戏后风格**；风格是约束，不是内容。
4. **输出粒度跟用户走**：一句话建议 / 单场方案 / 完整计划 / 分镜 / 提示。
5. **引用导演/摄影时给约束**，不给名字堆砌。

## 导演 / 摄影怎么用

1. 先问“这场戏需要什么”，再选参考。
2. 1 位主参考 + 0–1 位副参考。
3. 只取 2–3 条约束（一个机位、一个光源、一个剪辑规则），不要整套复制。
4. 用「反向约束」当检查表。
5. 不在提示词里堆导演名字；用视觉基元。

## AIGC 提示规则

1. **一个提示一个主语**。
2. **正向只写肯定**；否定全部进 NEGATIVE。
3. **戒连接词**：不写 and / with / while / then；用 `|` 分块。
4. **词序即权重**：主体 → 环境 → 镜头 → 光色 → 风格。
5. **控制预算**：核心 30–60 词，风格 8–15 个概念。
6. **一致性靠文本 token 锁**：同一角色/场景逐字复用同一串 token；不用参考图。
7. **不写画幅**；不做平台参数；不绑定模型。
8. **图像与运动分离**：视频提示只写运动/镜头/时长。

## 输出粒度

- 用户问一句：1–3 段 + 1 条可执行规则。
- 用户问一场戏：scene card + 3–5 个镜头建议。
- 用户问一个项目：treatment + shot list + 声音/视觉注记。
- 用户问提示：token 块 + NEGATIVE；可选给 2 个变体。

## 质量门

- 故事：目标 / 障碍 / 选择 / 转折。
- 视觉：每个镜头有理由。
- 调度：轴线 / 屏幕方向 / 覆盖成立。
- 表演：动词，不是形容词。
- 声音：有沉默 / 画外。
- 风格：反向约束逐条通过。
- 提示：正向无否定；NEGATIVE 非空；无画幅/平台参数。

## 文件地图

- `references/craft/` — 6 个方法模块
- `references/aigc/prompt-syntax.md` — token 语法与失败模式
- `references/aigc/assets.md` — 文本资产 token 与一致性
- `references/index.md` — 125 导演 + 29 摄影总表
- `references/taxonomy.md` — 风格族谱
- `references/mixing.md` — 混搭 + 导演 × 摄影
- `references/prompting.md` — 档案 → token 的转换规则
- `references/directors/<slug>.md` — 导演档案
- `references/prompts/<slug>.md` — 导演提示参考
- `references/cinematographers/<slug>.md` — 摄影档案
- `references/prompts-cinematographers/<slug>.md` — 摄影提示参考
- `templates/` — treatment / scene card / shot list / character sheet / asset tokens / AI prompt / style brief
- `../../../DESIGN.md` — 设计说明
