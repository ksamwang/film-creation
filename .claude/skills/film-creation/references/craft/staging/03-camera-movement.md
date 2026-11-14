# 摄影机运动：反推镜头与运动动机

## 核心判断

运动 token 替观众换一个观看位置，不是制造"电影感"。不改变距离、角度或信息量的运动只是像素在漂。一次生成只承载一种运动，写两个都不成立。运动层只回答：起幅给什么，什么触发，落幅多出什么信息。

## 书里的原则

**建构单位**（《电影镜头设计》12.1）：一个运动镜头分起、转、落三段；起幅独立成立，落幅给出新信息，中间由具体事件触发。AIGC 用法：按时间写三句——起幅是什么、什么触发、落在哪，缺一段就不生成运动。

**移动兴趣中心**（12.4）：在一个运动镜头里把注意力从 A 交给 B，可靠交叉、前景遮挡、焦点或光线。AIGC 用法：用前景擦过交接——`A passer-by crosses close to the lens; when he clears, the focus has moved to Gu.`；不要让模型同时演两段戏。

**反推镜头**（《场面调度：影像的运动》3.5）：主体与摄影机沿同轴反向移动，相对速度加倍，背景透视迅速变化。AIGC 用法：写成 `She walks straight at the camera as it pulls back at her pace; the corridor stretches out behind her.`；一场只放一次，放在关系断裂或追赶的节点。

**后拉揭示**（《电影镜头入门》Step4）：从局部拉到全景，先给细节再给环境。AIGC 用法：`Start close on the cracked watch, then pull back until the whole empty platform is in frame.`起幅和落幅各生成一张关键帧，中间用视频补。

**摇镜、升降、推近的分工**（《电影镜头设计》第 17–20 章）：摇换关注点，升降换视平线与权力，推近换距离与透视。AIGC 用法：窄空间只给摇、俯仰和小幅升降；开阔空间才给横向移动或升降。

## AIGC 执行

图生视频（首帧已定）只写运动、镜头、时长，不重复静态描述；文生或参考图生视频要先写起幅的人物位置，再写运动。模式 A：

```text
Medium shot of Lin at the counter. Gu steps in from frame left; as he does, the camera dollies slowly in until Lin fills the frame in close-up.
```

图生视频只留运动那半句。模式 B：

```text
MOTION: slow dolly-in | start medium on C1 at counter | trigger C2 enters frame-left | end close-up on C1 | 5s | 24fps
```

模式 B 里 `MOTION` 放最前。首尾帧挂同一组 S1、C1 参考图，构图成立后再图生视频；尾帧不成立，运动必收在坏构图上。

一次只给一种运动：推、拉、横移、摇、升降、环绕。`dolly-in + pan + zoom` 会让脸和墙一起变形；复合效果拆两镜。

运动必须有画面内动机：人物走动、门被推开、车辆经过、光线变化。找不到就固定机位，让人物移动。

受限空间用 `slow pan`、`small tilt`、`subtle crane`，不用长距离推近；开阔空间可用 `lateral dolly`、`crane up`、`aerial pull-back`。

时长 3–5 秒；超过 8 秒易漂移。需要更长就拆镜头。失败模式：`warped walls | morphing face | changing wardrobe | speed ramp | shake | multiple camera moves | zoom pulsing`；模式 B 进 NEGATIVE，模式 A 写 `one slow continuous move`。

## 检查清单

- [ ] 运动改变了距离、角度还是信息量？
- [ ] 起幅、触发、落幅是否各有明确内容？
- [ ] 起幅和落幅能否各自成立为好构图？
- [ ] 是否只有一种运动？
- [ ] 运动是否有画面内动机？
- [ ] 反推镜头是否只出现一次？
- [ ] 受限空间是否避免长距离推近？
- [ ] 图生视频是否只写运动；文生视频是否写清起幅位置？

## 常见错误

- 只写"cinematic camera movement"→ 模型随机漂移。改：写运动类型、起幅、触发、落幅。
- 推近但不给新信息 → 观众只感到慢。改：推近必须揭示表情、道具或关系。
- 图生视频重复服装和场景 → 模型重渲染，首帧被覆盖。改：静态信息交给首帧与参考图。
- 一条提示写推近再横移 → 中途变形。改：拆两条，剪辑连接。
- 每个镜头都反推 → 情绪失效。改：一场一次，留给断裂点。
- 长镜头无注意力转移 → 只是拖时间。改：加前景擦过或光线变化。

## 与风格层接口

摄影档案只取一条运动签名：手持漂移、固定机位、缓慢升降，三选一；导演档案只定"何时动"。运动单独成句（模式 B 为 `MOTION` 块），不混进取景。剪辑先看起幅落幅能否接；接不上就是交接没完成，回退固定镜头。各类运镜的写法与生成可靠性见 `references/camera/lexicon-move.md`。

## 来源

见 `craft/sources.md#staging`。
