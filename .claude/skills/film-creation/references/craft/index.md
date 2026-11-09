# 创作方法导航

6 个模块。每次只读需要的模块和子文件，不要一次加载全部。

| 需求 | 模块 | 先读 |
|---|---|---|
| 故事 / 概念 / beat | `story/` | `story/index.md` |
| 视觉 / 构图 / 光色 / 材质 | `visual/` | `visual/index.md` |
| 镜头序列 / 机位 / 运动 / 群戏 | `staging/` | `staging/index.md` |
| 角色 / 表演 token / 微动作 | `performance/` | `performance/index.md` |
| 声音 / 画外 / 沉默 / 音乐 | `sound/` | `sound/index.md` |
| 镜头数 / 迭代 / 交付 / 短片 | `production/` | `production/index.md` |

每个模块的 `index.md` 会告诉你先读哪一篇。来源表在 `sources.md`。

## 术语与两种模式

模块里的 **token** 指提示词里一个可见的视觉单元（一个动作、一个光源、一个位置），两种模式都适用：模式 A 把它们写成按顺序的句子，模式 B 写成 `|` 分隔的 token 块（`../aigc/prompt-syntax.md`）。代码块里的 `SUBJECT: ... | ...` 是模式 B 的写法，换成模式 A 时内容不变、改成句子。

**NEGATIVE** 列的是这一类镜头的具体失败模式：模式 B 放进 NEGATIVE；模式 A 改写成正面描述，模型有 negative 参数时再放进去。

**一致性**先靠参考图，再靠首帧续接，文本锁兜底（`../aigc/assets.md`）。模块里「逐字复用 token」在有参考图时指资产名、描述与参考图的对应不变。

## 使用顺序

- 先看用户的问题属于哪个模块。
- 读模块 `index.md`，按它的路由读 1–2 个子文件。
- 不要把 6 个模块或一个模块的所有子文件一次性读入。
- 需要跨模块时，先各读一个子文件，再合并。
