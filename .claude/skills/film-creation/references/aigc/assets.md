# 文本资产与一致性

> 竖屏短剧（多参考图、原生出声的视频模型）按 `references/drama/` 写，与本文件冲突时以那里为准。

> 没有参考图，一致性只能靠**逐字复用的 token**。

## 资产层是什么

AIGC 项目里，先定义三类资产：

- **人物**：C1 / C2
- **场景**：S1 / S2
- **道具**：P1 / P2

每个资产只写一次，形成一条固定 token 字符串；之后每个镜头**原样粘贴**，不改写、不换同义词、不重新描述。

## 人物 token

字段顺序：

```text
年龄 | 体型 | 脸型 | 眼睛 | 发型 | 肤色 | 服装 | 配饰 | 疤痕/纹身 | 姿态 | 表情
```

例：

```text
C1: 30s East Asian woman | slim | sharp jaw | narrow eyes | shoulder-length black hair | pale skin | grey wool coat | black turtleneck | worn leather bag | scar above left eyebrow | upright | neutral
```

## 人物角色表

人物资产使用固定的三面板角色表格式，完整规范见 `templates/character-sheet.md`。

- 每个角色一张 3:2 三面板表，不先做单独的正面全身定妆图。
- 左：正面全身，无头；颈根以上 = `#D9D9D9`。
- 中：背面全身，头可见，无脸。
- 右：3/4 头肩特写；全表只有这一张脸。
- 目标格式固定；怎么生成由 LLM 决定，skill 不规定执行步骤。

## 场景 token

```text
地点 | 年代 | 建筑 | 材质 | 色板 | 光源 | 时间 | 天气 | 尺度 | 关键陈设
```

例：

```text
S1: cramped 1970s Hong Kong noodle shop | tiled floor | fluorescent tube | red plastic stools | steam | wet window | night | narrow
```

## 道具 token

```text
名称 | 材质 | 尺寸 | 磨损 | 颜色 | 功能 | 使用方式
```

例：

```text
P1: worn brass lighter | scratched | 6cm | warm metal | right hand
```

## token 锁

- 同一角色/场景，**逐字复用**同一串 token。
- 不改写、不换同义词、不删修饰。
- 一个提示只放一个资产；多人物分开写。
- 漂移时用同一 token 块重生成，不要改词。
- token 越短越稳；只保留决定身份的词。

## 镜头组合

```text
STYLE: ...（导演/摄影的视觉 token）
SUBJECT: C1 | 动作
ENVIRONMENT: S1 | 时间 | 天气
SHOT: 景别 | 机位 | 焦段 | 构图
LIGHT: ...
COLOR: ...
TEXTURE: ...
NEGATIVE: ...
```

- 身份/场景用资产 token；文字只写动作、景别、机位、光变。
- 不要在文字里重复脸和衣服；重复会与 token 打架。
- 视频提示只写运动/镜头/时长；不重复静态描述。

## 限制

纯文本一致性是弱一致性。模型仍可能漂移；token 锁只能降低概率，不能保证。要更强的一致性，需要参考图或训练身份——本包不展开。

## 检查清单

- [ ] 每个角色/场景/道具有固定 token？
- [ ] token 逐字复用，没有改写？
- [ ] 一个提示只有一个资产？
- [ ] 多人镜头分开写？
- [ ] 视频提示只写运动？
- [ ] 漂移时用同一 token 重跑，而不是改词？
