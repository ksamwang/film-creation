# AIGC craft 改写简报

## 目标

6 个模块从“实拍工艺”改成“AIGC 创作”。保留书里的原则与章节出处，删掉剧组执行细节。

**默认只输出 AIGC 产物**：概念、beat、镜头序列、图像 token、视频 motion token、资产 token、negative、剪辑/声音方案。实拍只在用户明确要求时才回答。

## 统一结构

```markdown
# <标题>

## 核心判断
（AIGC 语境：这个主题解决什么问题）

## 书里的原则
（保留书的框架/术语，但翻译成“生成时怎么用”）

## AIGC 执行
（具体到概念/beat、镜头序列、图像 token、视频 motion token、资产 token、negative、剪辑/声音）

## 检查清单
（5–8 问，生成前可勾选）

## 常见错误
（错误做法 → 后果 → 替代做法）

## 与风格层接口
（如何用导演/摄影档案的 token 约束这一层）

## 来源
见 `craft/sources.md#<module>`
```

## 硬规则

- 每篇 800–1500 汉字；模块 4000–6000。
- 每篇至少 2 个书内术语/原则、1 个章节引用（写 `_sources.md`）。
- **禁止写**：给演员指令、排练、选角、剧组、预算、排期、通告、灯具型号、轨道、现场录音。
- 每条规则必须落到以下之一：概念/beat、镜头序列、图像 token、视频 motion token、资产 token、negative、剪辑/声音。
- 书里的原则可以保留，但必须写“在 AIGC 里怎么用”。
- 不复制原文，不长段引用。

## 模块与子文件

### story

| 文件 | AIGC 重点 |
|---|---|
| 01-premise | 一句话概念、第一个镜头、主题写成视觉问题 |
| 02-character | 角色 token、want/need/flaw 转成可观察动作 |
| 03-structure | 30–90 秒的 3–5 个 beat；beat 到镜头的映射 |
| 04-scene | 一场戏 = 一个镜头序列；目标/障碍/转折；视觉叙事 |
| 05-narrative | 视点、叙述者、时间在图像序列里怎么呈现 |

### visual

| 文件 | AIGC 重点 |
|---|---|
| 01-shot-grammar | 景别、主镜头、平行剪辑；转成镜头序列与 token |
| 02-composition | 构图、留白、深度线索；转成图像 prompt |
| 03-lens | 焦段、景深、畸变；转成 token 与后果 |
| 04-light | 光源、方向、硬度、光比；light token，不写灯具 |
| 05-color | 色板、色温、饱和度、hex；色彩一致性 |
| 06-texture | 胶片/数字、颗粒、画幅、介质；表面 token 与 negative |

### staging

| 文件 | AIGC 重点 |
|---|---|
| 01-space | 前景/中景/后景、出入口、纵深；scene token |
| 02-blocking | 人物在画面中的位置与移动；不写演员排练 |
| 03-camera-movement | 运镜类型、动机、单条运动；motion token |
| 04-coverage | 主镜头/插入/反应；镜头序列逻辑，不是多机位 |
| 05-multi-character | 多人同框、特征污染、分开生成/合成 |
| 06-scene-analysis | 一场戏拆成 3–8 个镜头；beat → shot |

### performance

| 文件 | AIGC 重点 |
|---|---|
| 01-given-circumstances | 规定情境 = 生成上下文 token；模型需要知道什么 |
| 02-action | 动词 → 可观察微动作；prompt 写法 |
| 03-rehearsal | 表演 token：视线、呼吸、手、重心、距离；迭代调整 |
| 04-direction | 导演模型，不是导演演员；用 token 调整，不写“更悲伤” |
| 05-casting | 角色设计 token、一致性；不写选角 |

### sound

| 文件 | AIGC 重点 |
|---|---|
| 01-perspective | 声音透视作为后期/生成音频层；不写现场录音 |
| 02-offscreen | 画外声作为设计层 |
| 03-silence | 沉默作为一层 |
| 04-music | 音乐 cue、画内/画外、进出点 |
| 05-dialogue | 对白/旁白/TTS；不写同期声 |

### production

| 文件 | AIGC 重点 |
|---|---|
| 01-breakdown | 概念 → 镜头/资产清单；不写剧组分解表 |
| 02-schedule | 生成顺序、镜头依赖；不写拍摄日 |
| 03-budget | 生成次数、迭代预算、一致性 pass；不写制片预算 |
| 04-short-form | 15–90 秒：一个想法、3–5 beat、6–12 镜 |
| 05-risk | 交付：剪辑、声音、字幕、导出；不写保险/法务 |

## 来源 fragment

每个模块写 `craft/<module>/_sources.md`，格式不变：

```markdown
## <module>

| 概念 / 规则 | 来源 |
|---|---|
| ... | 《书》第 X 章 |
```

最后由主进程合并成 `craft/sources.md`。

## 质量门

- 每篇至少 2 个书内术语；模块至少 5 个。
- 每篇至少 1 个章节引用；模块至少 3 个。
- 没有出处的规则删掉。
- 读起来必须像“AIGC 创作指南”，不能像“剧组工作手册”。
- 每篇最后一节必须说明：这条原则怎么变成 prompt / 镜头 / 资产 / 剪辑。
