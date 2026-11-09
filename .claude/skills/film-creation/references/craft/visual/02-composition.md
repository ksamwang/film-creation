# 画幅内的构图

## 核心判断

构图是在固定矩形里分配注意力：第一眼看谁、第二眼看哪、什么被挤出画外。AIGC 里构图不是后期裁切，而是提示里的位置 token；模型默认把主体放中间，所以“偏离中心”必须显式写，并配 negative。

## 书里的原则

《镜头的语法》把取景拆成三个可测量：头顶留白、视线留白、九宫格。头顶留白过多会让脸下沉，过少会切额头；宁可少留。正反打之间要保持一致，否则剪起来跳。AIGC 对应写法是 `generous headroom` 或 `tight headroom`，同一场所有镜头用同一词。视线留白是人物看向画外时眼睛前方的空间，小景别尤其要留，写成 `looking off-frame | negative space ahead of gaze`。九宫格把画面三等分，主体放交点或正中，二选一；prompt 写 `rule-of-thirds placement` 或 `centered composition`，不要两者都写。

摄影角度分水平与垂直：正面、四分之三侧面、侧面、背面，越转越少信息、越多态度；平视、俯拍、仰拍改变权力而不改变景别。写成 `frontal | three-quarter | profile` 与 `eye level | low angle | high angle`，每个角度要能说出给了谁权力。

第三维靠前景、中景、后景分层，以及重叠、相对大小、透视、焦点、空气感。AIGC 里用遮挡 token 造纵深：`foreground shoulder silhouette | midground subject | background doorway`，并且前景要暗、要虚，否则抢戏。对话双人优先过肩，面向镜头者占三分之二、背向者三分之一，写成 `over-the-shoulder | 2/3 frame on facing actor`。

安全框和清场在生成里变成 margin 与 negative：主体四周留边，边缘不放关键信息；背景不要亮窗、不要从头顶长出的物体、不要开着的电视。

## AIGC 执行

- SHOT 块写四项：placement（centered / off-center / rule-of-thirds）、angle、layer（foreground obstruction / deep staging）、horizon（low / high）。
- 小景别统一头顶留白词，同一场逐字复用；不要这镜 `tight`、下镜 `generous`。
- 需要过肩时把前景写进主体块：`foreground shoulder, dark, out of focus`。
- 重要对象放画面上半部：`subject in upper half of frame`，因为观众先扫上方。
- NEGATIVE 写具体失败：`cropped head | cut-off hands | subject touching frame edge | background clutter | bright window | object growing from head | unmotivated dutch angle`。

## 检查清单

- [ ] 主体在九宫格交点还是中央？只选了一个吗？
- [ ] 头顶留白与相邻镜头一致吗？
- [ ] 人物看向画外时，视线前方有空间吗？
- [ ] 机位高度是选的吗？它给了谁权力？
- [ ] 双人镜头是过肩还是并排？前景抢戏吗？
- [ ] 画面有前中后三层吗？还是所有人站一排？
- [ ] 主体离画框边缘够远吗？交付裁切安全吗？
- [ ] 背景有亮窗、杂物、头顶长物吗？

## 常见错误

| 错误做法 | 后果 | 替代做法 |
|---|---|---|
| 只写 `beautiful composition` | 模型给平均中心构图 | 写 placement + angle + layer |
| 头顶留白每镜不同 | 正反打剪辑跳 | 同场统一 headroom 词 |
| 前景过肩太亮 | 抢主体注意力 | 写 `dark, out of focus` |
| 主体贴边 | 裁切时被切掉 | `subject with margin`，重要信息内缩 |
| 无理由荷兰角 | 像失误而非失衡 | 有动机才写，否则 negative |

## 与风格层接口

导演档案的构图项只取一两项可执行约束，例如“低机位、人物压画面上半部、前景肩背常驻”，转成固定 SHOT 子块与 negative。构图还决定镜头序列的呼吸：宽构图建立空间，紧构图制造压迫；同一场不要两种构图逻辑打架。资产 token 里的场景陈设要为构图留层：前景有可遮挡物，后景有可引导的门口或窗。

## 来源

见 `craft/sources.md#visual`；逐条章节见 `craft/visual/_sources.md`。
