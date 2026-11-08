# craft 深度提炼简报

## 目标

把 6 个模块从“通用方法”改成“从 docs 里长出来的方法”。现有 6 篇不再承载正文，改成模块导航索引。

## 结构

```text
craft/
  index.md                 # 顶层导航：6 个模块
  sources.md               # 全局来源表（最后合并）
  story/
    index.md               # 模块导航
    01-premise.md
    02-character.md
    03-structure.md
    04-scene.md
    05-narrative.md
    _sources.md            # 临时来源 fragment，最后合并
  visual/
    index.md
    01-shot-grammar.md
    02-composition.md
    03-lens.md
    04-light.md
    05-color.md
    06-texture.md
    _sources.md
  staging/
    index.md
    01-space.md
    02-blocking.md
    03-camera-movement.md
    04-coverage.md
    05-multi-character.md
    06-scene-analysis.md
    _sources.md
  performance/
    index.md
    01-given-circumstances.md
    02-action.md
    03-rehearsal.md
    04-direction.md
    05-casting.md
    _sources.md
  sound/
    index.md
    01-perspective.md
    02-offscreen.md
    03-silence.md
    04-music.md
    05-dialogue.md
    _sources.md
  production/
    index.md
    01-breakdown.md
    02-schedule.md
    03-budget.md
    04-short-form.md
    05-risk.md
    _sources.md
```

## 子文件要求

- **800–1500 汉字**，只讲一个主题。
- 结构：

```markdown
# <标题>

## 核心判断
（1–3 句：这个主题解决什么问题）

## 书里的方法
（书内框架、术语、步骤；具体到能操作）

## 可执行规则
（3–8 条，每条一句）

## 检查清单
（5–8 问，可勾选）

## 与风格层接口
（如何影响导演/摄影参考、镜头设计或提示词）

## 来源
见 `craft/sources.md#<module>`
```

- 每篇至少 **2 个书内术语**、**1 个章节引用**（写在 `_sources.md`）。
- 不写“要讲好故事”“要有情感”这类通用话。
- 不复制原文，不长段引用；用自己的话提炼。
- 模块 `index.md` 500–800 字：解决什么问题、先读哪篇、子文件一句话说明。

## 来源 fragment

每个模块写 `craft/<module>/_sources.md`：

```markdown
## <module>

| 概念 / 规则 | 来源 |
|---|---|
| 不归点 | 《剧本结构设计》第 5 章 |
| 三角形原理 | 《电影语言的语法》第 4 章 |
```

最后由主进程合并成 `craft/sources.md`。

## 文本来源

`docs/_text/<书名>.txt`，由 `pdftotext -enc UTF-8` 生成。

- 用 `grep -n '第.*章'` 找章节，用 `sed -n 'start,endp'` 抽段。
- 不要整本读入上下文。
- 忽略页眉、页码、OCR 噪声。
- 只有《镜头在说话》本次跳过。

## 模块与书

| 模块 | 书 | 子文件主题 |
|---|---|---|
| story | 剧本结构设计、21天、编剧的策略、从文本到影像、电影叙事学研究 | premise、character、structure、scene、narrative |
| visual | 电影语言的语法、镜头的语法、导演的摄影课、电影照明器材与操作 | shot-grammar、composition、lens、light、color、texture |
| staging | 场面调度、导演创作完全手册、电影镜头设计、电影镜头入门 | space、blocking、camera-movement、coverage、multi-character、scene-analysis |
| performance | 尊重表演艺术、表演的艺术 | given-circumstances、action、rehearsal、direction、casting |
| sound | 视听 | perspective、offscreen、silence、music、dialogue |
| production | 创意制片完全手册、短片的法则 | breakdown、schedule、budget、short-form、risk |

## 质量门

- 模块总字数 4000–6000 汉字。
- 每个子文件 800–1500 汉字。
- 每篇至少 2 个书内术语；模块至少 5 个。
- 每篇至少 1 个章节引用；模块至少 3 个。
- 没有出处的规则删掉。
- 同模块子文件之间不重复。
