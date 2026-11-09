---
name: film-creation
description: AIGC 创作参考包，供 LLM 在用户提出故事、角色、镜头序列、图像/视频提示、资产一致性、声音与剪辑需求时调用。内置 6 个 AIGC 方法模块、125 位导演、29 位摄影指导与注意力友好的 token 规则。默认输出 AIGC 产物；实拍只在用户明确要求时回答。
---

# AIGC 创作参考包

这是一份给 LLM 用的参考包 + 路由手册。默认用于 AI 图像/视频作品，不用于实拍。

LLM 的职责：**判断请求类型 → 读对应文件 → 按需要提问 → 输出 AIGC 产物。**

## 包里有什么

- `references/craft/` — 6 个 AIGC 方法模块
- `references/directors/` + `references/cinematographers/` — 视觉参考
- `references/aigc/` — token 语法、文本资产
- `templates/` — concept、scene-to-shots、shot prompt、asset tokens、character sheet、edit-sound、AI prompt

## 默认输出

- 概念 / beat sheet
- 镜头序列
- 图像 prompt token
- 视频 motion token
- 资产 token / 角色表
- negative token
- 剪辑 / 声音方案

**不输出**：剧组、演员排练、选角、预算、排期、通告、灯具型号、轨道、现场录音——除非用户明确要求实拍。

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
| 明确要实拍 | 先说明本包默认不做实拍；按需给通用建议 | — |

## 使用原则

1. **默认 AIGC**；不主动给实拍方案。
2. **先判断请求类型**，不要一套流程套所有人。
3. **需要时才问**，最多 3 个关键问题。
4. **每条建议必须落到 AIGC 产物**：concept、beat、shot、token、资产、negative、剪辑/声音。
5. **引用导演/摄影时给视觉 token**，不给剧组职位。

## 导演 / 摄影怎么用

1. 先问“这个作品需要什么视觉”，再选参考。
2. 1 位主参考 + 0–1 位副参考。
3. 只取 2–3 条视觉约束（一个机位、一个光源、一个色彩关系），转成 token。
4. 用「反向约束」做 negative。
5. 不在 prompt 里堆导演名字；用视觉基元。

## AIGC 提示规则

1. 一个提示一个主语。
2. 正向只写肯定；否定全部进 NEGATIVE。
3. 戒连接词：不写 and / with / while / then；用 `|` 分块。
4. 词序即权重：主体 → 环境 → 镜头 → 光色 → 风格。
5. 控制预算：核心 30–60 词，风格 8–15 个概念。
6. 一致性靠文本 token 锁：同一角色/场景逐字复用；不用参考图。
7. 不写画幅；不做平台参数；不绑定模型。
8. 图像与运动分离：视频提示只写运动/镜头/时长。

## 质量门

- 故事：概念 → beat → 镜头，能一条线走通。
- 视觉：每个镜头有理由，能转成 token。
- 调度：镜头顺序成立，轴线/方向可读。
- 表演：写成微动作，不写形容词。
- 声音：有环境/事件/音乐/沉默的分工。
- 风格：反向约束转成 negative。
- 提示：正向无否定；NEGATIVE 非空；无画幅/平台参数。

## 文件地图

- `references/craft/` — 6 个 AIGC 方法模块（index + 子文件）
- `references/aigc/prompt-syntax.md` — token 语法与失败模式
- `references/aigc/assets.md` — 文本资产 token 与一致性
- `references/index.md` — 125 导演 + 29 摄影总表
- `references/taxonomy.md` — 风格族谱
- `references/mixing.md` — 视觉混搭 + 导演 × 摄影
- `references/prompting.md` — 档案 → token 的转换规则
- `references/directors/<slug>.md` — 导演档案
- `references/prompts/<slug>.md` — 导演提示参考
- `references/cinematographers/<slug>.md` — 摄影档案
- `references/prompts-cinematographers/<slug>.md` — 摄影提示参考
- `templates/` — concept / scene-to-shots / shot prompt / asset tokens / character sheet / edit-sound / AI prompt
- `../../../DESIGN.md` — 设计说明
