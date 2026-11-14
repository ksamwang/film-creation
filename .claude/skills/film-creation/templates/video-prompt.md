# Video Prompt（视频提示词）

> 按分镜脚本写多镜头视频提示词。方法见 `references/video-prompt/compile.md`，段落见 `references/video-prompt/anatomy.md`，完整示例见 `references/video-prompt/example.md`，三档示例见 `references/video-prompt/scene-prompts.md`。
> 单镜、简单提示词用 `ai-prompt.md`。竖屏短剧的片段提示词以 `references/drama/07-segment-prompt.md` 为准。
> 三层复用：**全片层**全片逐字复用；**场景层**同场同时段逐字复用；**单位层**每条单独写。

## 全片层（写一次，全片复用）

```text
GLOBAL RULES:
- No music of any kind: no score, no soundtrack, no background music, no musical stings.
- No on-screen text: no subtitles, no captions, no titles, no watermark, no logo.
  {Screens / signs / papers in this film show no readable words.}
- Real-time speed throughout: no slow motion, no speed ramps.

STYLE: {medium}. {contrast, blacks, highlight rolloff, grain, skin texture}.
No HDR look, no oversharpening, no glossy commercial finish.

CHARACTERS:
<<<{name}>>> — face, hair and build only. Not pose or expression.
  Identity lock: {2–4 drift-prone features}, {explicit absences: no glasses / no scar}.

ACTING (whole film): {restraint level}. Blinks at a normal rate. Nobody looks into the lens.
Only the speaking character's lips move; listeners keep their mouths closed.
```

## 场景层（每个场景 / 时段写一次）

- 场景 / 时段：
- 本场景的单位：

```text
SCENE ASSETS:
<<<{location}>>> — layout and materials only. Not the time of day. THIS SCENE: {time, weather}.
<<<{name}>>> THIS SCENE: {wardrobe and state in this scene}.
<<<{prop}>>> — {prop look}. THIS SCENE: {state}.

GEOMETRY: {absolute layout: doors, windows, furniture}. {who is where}.
{where nothing / nobody is}.
Axis for every shot: {A} is frame left, {B} is frame right.

LIGHT: {visible sources in frame}, {direction}, {hard / soft}, {how dark the shadows are}.

COLOUR: {N}% {main}, {N}% {secondary}, {N}% {accent}. {saturation}; skin {natural}.

ATMOSPHERE: {air: dust / steam / haze}. {2–3 signs of use}. No airbrushed skin, no waxy faces.

PHYSICS: {weight / inertia / materials that appear in this scene}.
Objects keep their shape, number and position.
```

## 单位层（每条单独写）

### 生成单位

| 项 | 内容 |
|---|---|
| 单位 |  |
| 镜号 |  |
| 总时长（≤ 模型单次上限） |  |
| 档位（轻量 / 标准 / 重型） |  |
| 生成方式（参考图生 / 首帧 / 首尾帧） |  |
| 参考图（≤ 模型上限） |  |
| 不进生成的镜头（后期） |  |

### 读戏摘要

- 本段要推动的变化：
- 谁知道什么：
- 情绪落在哪一格：
- 最可能的误演（NOT）：

### 预判误读

| 方向 | 这一段最可能错成 | 放在哪（CRITICAL / 总锁 / negative） |
|---|---|---|
| 表演 |  |  |
| 人 |  |  |
| 物 |  |  |
| 空间 |  |  |
| 时间与摄影机 |  |  |

### 提示词

```text
EDIT: {N} shots, {T} seconds total, {hard cuts / single continuous shot}, continuous real time.
Shot 1 {0–a}s · Shot 2 {a–b}s · ...

[film layer — paste verbatim]
[scene layer — paste verbatim]

THE BEAT: {the dramatic fact of this unit}. {who knows what}. {intensity}.
This is NOT {the most likely misreading}.

CRITICAL — ONLY {N} PEOPLE: {names}. {places where nobody else is}.

FIRST FRAME: {who is where, already mid-motion}.

LENS: Focal length fixed within each shot, no zoom.
Shot 1 — {mm}, {framing}, {camera height}.
Shot 2 — ...

CAMERA: {all locked-off / moving}. {no drift, no push}. {exceptions: shot N only ...}.

SHOT 1 — {0–a}s — {framing, lens}.
{t}s: {one main action}; {physical consequence}.
{t}s: {name} says, in {language}: "{line}" — {delivery}. Only {name}'s lips move.
Ends: {end state}.

SHOT 2 — ...

ACTING: {behaviour + meaning + not, for this unit}.

AUDIO: Diegetic only. Room tone: {sources}. {timed sound cues}.
{N} lines, in {language}, one speaker at a time. {where the silence is}.

LOCKS:
- Only {N} people, the whole time.
- {who sits / stands}.
- {axis}.
- {prop state}.
- {who speaks}.
- No music, no readable text.

NEGATIVE: {this unit's wrong versions: acting / people / objects / space / time and camera}.
```

### 自检

- [ ] 时间码加起来等于总时长，镜头数和 EDIT 一致
- [ ] 全片层、场景层和同场其他单位逐字一致
- [ ] 每镜的方向词与 GEOMETRY、轴线一致
- [ ] 每句台词有说话人、原文、语言、时间点；其他人嘴闭着
- [ ] 每张参考图写了「只管什么」；识别特征锁不超过 4 条
- [ ] CRITICAL 不超过 3 处；总锁不超过 8 条
- [ ] 正文和总锁、negative 没有矛盾
- [ ] 每一段都能说出「不写这段，模型会在哪里错」
- [ ] 没有 cinematic / masterpiece / 8K 这类不对应任何误读的词

### 生成记录

| 版本 | 改了什么（只改单位层） | 结果 | 采用 |
|---|---|---|---|
| v1 |  |  |  |
