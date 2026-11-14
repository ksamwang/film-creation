# 提示词的解剖：十九个段落

一条完整的视频提示词由下面这些段落组成，按顺序排列。不是每条都要写全：轻量档只用其中三四段，重型档全用（档位见 `video-prompt/index.md`）。

每段五个字段：**作用**（替谁说话、防什么误读）、**写法**、**例**、**什么时候省**、**常见错误**。例子是英文提示词片段，因为多数视频模型对英文的结构化长提示词执行更稳；台词保留原语言（见 §17 声音）。中文模型同样适用，把段落标题和内容换成中文即可。

## 排列顺序为什么是这样

```text
剪辑合同 → 硬约束 → 风格 → 戏的意图 → 人数锁 → 资产 → 空间地图 → 首帧
→ 镜头锁 → 摄影机 → 光 → 色 → 空气与质感
→ 逐镜时间线
→ 物理 → 表演 → 声音
→ 总锁 → negative
```

- **先定框架，再填内容。** 模型先知道「这是 5 个镜头、15 秒、硬切」，才不会把 5 个镜头的描述理解成一个镜头里发生的事。
- **先定世界，再写动作。** 人是谁、在哪、光从哪来，都定下来之后，逐镜时间线只需要写「发生了什么」，不用每镜重复环境。
- **最后再锁一次。** 关键不变量在开头说一次，在结尾总锁里再说一次。长提示词中段的信息最容易被稀释。

## 关于「关键」标记与冗余

- **「CRITICAL / 关键」整条提示词最多标 2–3 处。** 处处关键等于没有关键。标给那些一错整条作废的东西：人数、谁说话、不能出现的文字。
- **冗余只给关键不变量。** 人数、轴线、谁坐谁站这类东西，在资产 / 空间、逐镜、总锁里各出现一次是有意的。普通描述不重复，重复会挤掉别的信息。

---

### 剪辑合同 EDIT

**作用**：剪辑的工作。告诉模型这是几个镜头、每镜起止时间、怎么切。不写，模型会把多镜头描述融成一个镜头，或者自己决定切几刀。

**写法**：开头一段写清：镜头数、总时长、每镜时间码、切换方式（hard cut / match cut / 一镜到底无切）、是否实时（真实时间流逝，不跳时）。一镜到底要明确写「single continuous shot, no cuts」。

**例**：

```text
EDIT: 4 shots, 12 seconds total, hard cuts, continuous real time.
Shot 1 0–3s · Shot 2 3–6s · Shot 3 6–10s · Shot 4 10–12s.
```

**什么时候省**：单镜轻量档可以省成一句「single shot, 5 seconds」。

**常见错误**：时间码加起来不等于总时长；镜头数超过模型单次能稳定处理的数量（多数在 3–6 镜，见 `references/drama/06-storyboard.md`）；写了「快速剪辑」却不给时间码，模型自由发挥。

**词库**：一镜到底的路径写法见 `video-prompt/one-take.md`。

### 全片硬约束 GLOBAL RULES

**作用**：封住模型最顽固的默认。配乐、画面文字（字幕、标题、水印、logo）、慢动作，是模型最爱自作主张加的东西。

**写法**：一行一条，每条把同义说法列全。音乐不只写 no music，还要写 no score, no soundtrack, no background music；文字不只写 no text，还要写 no subtitles, no captions, no titles, no watermark, no logo。

**例**：

```text
GLOBAL RULES:
- No music of any kind: no score, no soundtrack, no background music, no musical stings.
- No on-screen text: no subtitles, no captions, no titles, no watermark, no logo.
- Normal speed throughout: no slow motion, no speed ramps.
```

**什么时候省**：模型或平台已有对应参数（音频开关、负面参数框）时，可以只保留提示词里的一句作为兜底；竖屏短剧按 `references/drama/07-segment-prompt.md` 的两条固定约束写。

**常见错误**：只在 negative 参数里写，正文却描述「气氛紧张的音乐」之类自相矛盾的话；同义词列不全，模型换个形式加上（没有字幕，但出现了屏幕上可读的标语）。

**词库**：同义说法的完整清单见 `video-prompt/locks.md` 第 1 节。

### 风格 STYLE

**作用**：摄影 + 调色的总基调。决定画面像什么：实拍质感、动画、某种胶片、某种渲染。

**写法**：先写媒介（photoreal live-action look / 2D animation / stop-motion），再写**画面特征**：反差、暗部、高光过渡、颗粒、肤色质感、锐度。摄影机型号（ARRI Alexa、16mm 胶片）可以作为可选的风格锚点，但优先描述它带来的特征，因为模型对型号的理解不稳定。

**例**：

```text
STYLE: photoreal, naturalistic drama. Soft filmic contrast, gently lifted blacks,
smooth highlight rolloff, fine organic grain, natural skin texture with visible pores.
No HDR look, no oversharpening, no glossy commercial finish.
```

**什么时候省**：参考图已经把风格定死（首帧生视频）时可以缩成一句。

**常见错误**：堆砌「cinematic, masterpiece, 8K, ultra detailed」——不对应任何具体特征，还会把画面推向过度锐化的 AI 质感；风格和资产参考图冲突（参考图是动画，风格写实拍）。

### 戏的意图 THE BEAT

**作用**：导演的工作。告诉模型这场戏在演什么、**不是什么**。模型对情绪的默认是放大：紧张就瞪眼，难过就流泪，坏人就冷笑。写清意图和「不是」，表演才收得住。

**写法**：两三句。这一段的戏剧事实（谁知道什么、谁不知道）、每个人此刻要什么、情绪的强度；然后一句「This is NOT ...」封住最可能的误读。

**例**：

```text
THE BEAT: She has just realised her brother sold their father's watch. She says nothing.
This is a scene of swallowed anger, not an argument. She does not cry, does not raise
her voice, does not confront him. He has no idea she knows.
```

**什么时候省**：纯空镜、纯动作镜头可以省；有人物情绪的镜头不要省。

**常见错误**：只写情绪词（sad, tense）不写强度和「不是」；写了剧情背景却不写此刻的戏（模型不需要知道前三集发生了什么，只需要知道此刻谁知道什么）。

### 人数锁 HEADCOUNT

**作用**：场记的工作。模型非常爱在背景里加人：路人、同事、服务员。人数错了，整条作废。

**写法**：一句话写清画面里的总人数和是谁；空间里本该有人的地方（办公室、街道、餐厅）要明确说空的。这是最值得标「CRITICAL」的一条。

**例**：

```text
CRITICAL — ONLY TWO PEOPLE exist in this scene: the woman and the boy.
The café is closed and empty: no staff, no customers, no passers-by outside the window.
```

**什么时候省**：人群戏不用人数锁，改写人群怎么分布、谁在动、谁不动；单人空间里没有任何可能出现别人的地方时可以省。

**常见错误**：只写 two people 不写背景空；写了「空荡的街道」又写「远处的车流」，模型补上行人。

**词库**：人群的写法见 `video-prompt/one-take.md` 第 2 节。

### 资产 ASSETS

**作用**：美术 / 造型的工作。每张参考图负责什么、不负责什么；人物的识别特征锁；这场戏里的状态。

**写法**：

1. **每张参考图一行，写清它控制什么、不控制什么。** 场景图只管空间和光，不管时间；人物图管脸和服装，不管姿势和表情。不写，模型会照抄参考图里的姿势、表情、时间。
2. **识别特征锁**：2–4 个最容易漂的识别特征（发型轮廓、眼镜、痣、特定服装件），加上明确的「没有」（no scar, no earrings）。**不要重新描述整个外貌**——参考图已经给了，全文重写会和参考图打架。
3. **THIS SCENE**：这场戏里与参考图不同的状态（袖子卷起、头发湿、外套脱了、杯子半满）。

**例**：

```text
ASSETS:
<<<mira>>> — face, hair and wardrobe only. Not her pose or expression.
  Identity lock: shoulder-length black hair with blunt fringe, thin silver hoop in left ear only,
  no glasses, no makeup beyond natural.
  THIS SCENE: cardigan sleeves pushed to the elbows, hair slightly damp.
<<<kitchen>>> — room layout, materials and window position only. Not the time of day:
  in this scene it is night.
```

**什么时候省**：不用参考图的纯文生视频，改为一段简短外貌描述；单人单图的轻量档，缩成一句「<<<x>>> controls face and wardrobe」。

**常见错误**：参考图有了还全文重写外貌（发色写错一个词就漂）；不写参考图「不控制什么」，结果白天的场景图生成了白天；识别特征锁写了十条，模型抓不住重点。参考图的基本用法见 `references/aigc/assets.md`。

### 空间地图 GEOMETRY

**作用**：美术 + 场记的工作。房间的布局、人和物的位置、轴线。多镜头段落里，每镜都要从这张地图里取位置，否则人物会在镜头之间跳位。

**写法**：

- **绝对布局**：门在哪面墙、窗在哪、桌子在哪；
- **相对摄影机的布局**：在主镜头里，谁在画左、谁在画右、谁离摄影机近；
- **哪里有什么、哪里没有**：模型爱补东西，空的地方要说空；
- **轴线**：一句话写死「she is always frame left, he is always frame right」。

**例**：

```text
GEOMETRY: A narrow galley kitchen. Window at the far end, fridge on the left wall,
counter and sink on the right wall. Mira stands at the sink (right side), the boy sits
on a stool by the fridge (left side). Axis: Mira is always frame right, the boy always
frame left, in every shot. Nothing on the counter except a kettle and one mug.
```

**什么时候省**：单人单镜可以省；人物不移动、只有一个机位时可以缩成一句。

**常见错误**：只写「在厨房里」；写了方位但和参考图的空间对不上；反打镜头没写轴线，两人在画面里换边。轴线规则见 `storyboard/continuity.md`。

### 首帧 FIRST FRAME

**作用**：导演的工作。告诉模型第一帧画面是什么样，而且**已经在动作中**。模型默认从静止开始：人物站定、看着前方、然后才开始动，浪费前一两秒，还容易出现「摆拍感」。

**写法**：描述第 0 秒的画面：谁在哪、什么姿势、**正在做什么**（已经在动）。用首帧图生视频时，这段改成「the clip starts exactly on the supplied first frame」，再加一句第一帧之后马上发生什么。

**例**：

```text
FIRST FRAME: Mira is already mid-motion, turning off the tap with her right hand,
head still bowed over the sink. The boy is already looking at her back.
```

**什么时候省**：首帧图已经给定，且动作很简单时。

**常见错误**：首帧写成静态描述（Mira stands at the sink），模型先静止一秒再动；首帧和剪辑合同里第一镜的描述不一致。

### 镜头锁 LENS

**作用**：摄影的工作。每镜的焦段（视角）、机位高度、镜头离人多远。不写，模型默认广角偏中、机位齐眼、变焦漂移。

**写法**：每镜写焦段 + 视角描述（模型对焦段数字理解不稳，同时写视野效果），机位高度（eye level / chest height / low），和人的距离；加一条「no zoom, no focal length change during the shot」。

**例**：

```text
LENS: Shot 1 — 35mm equivalent, moderate wide, camera at chest height, 2 metres from Mira.
Shot 2 — 85mm equivalent, tight, compressed background, eye level.
Focal length is fixed within each shot: no zooming, no breathing.
```

**什么时候省**：轻量档可以并进摄影机一句话里（a static 50mm medium shot）。

**常见错误**：只写「特写」「中景」不写焦段，模型用广角拍特写，脸被拉变形；焦段写了但和景别矛盾（24mm 写成 tight close-up）。焦段与视角的对照见 `camera/lexicon-shot.md` 焦段一节。

**词库**：焦段与视野对照、机位高度、焦点行为见 `video-prompt/camera-behavior.md` 第 4 节。

### 摄影机行为 CAMERA

**作用**：摄影的工作。摄影机怎么动、为什么动、由谁在操作。模型默认是稳定器式的平滑漂移——「一直在缓慢移动」的 AI 感就来自这里。

**写法**：

- **写成操作员的行为**，不只是运动名：「a handheld operator who stays on her shoulder, reacting a beat late when she turns」比「handheld camera」准得多；
- **写静止要明确**：locked-off on a tripod, no drift, no micro-movement；
- **例外镜头单独写**：「all shots locked-off except shot 4, which slowly pushes in」；
- 运动要有**动机**：跟着谁、因为什么开始和停下。

**例**：

```text
CAMERA: All shots are locked-off on a tripod. No drift, no slow push, no gimbal float.
Exception: shot 3 is handheld at shoulder height, the operator breathing slightly,
following the boy as he stands, settling once he stops.
```

**什么时候省**：不能省，至少写一句静止还是运动。不写，模型一定会加漂移。

**常见错误**：写「dynamic camera」「cinematic movement」，模型乱动；一镜里写两种运动（推 + 摇 + 环绕），模型压缩成一团。运镜词汇见 `camera/lexicon-move.md`。

**词库**：操作员式写法的词库见 `video-prompt/camera-behavior.md`。

### 光 LIGHT

**作用**：摄影的工作。光从哪里来、什么颜色、多硬、明暗比例。

**写法**：写**画面里的光源**（台灯、窗、屏幕、路灯）和它们照到哪里；写主光方向、软硬、暗部有多暗。AIGC 只描述画面里看得到的光效，不写怎么打光。

**例**：

```text
LIGHT: Night. The only light is a single pendant lamp over the sink, warm and hard,
throwing Mira's shadow onto the counter. The boy by the fridge sits half in darkness,
lit only by spill. The window is dark blue with no visible street.
```

**什么时候省**：参考图已经给了准确的光，且这场戏光不变化时，缩成一句。

**常见错误**：写「beautiful lighting」「cinematic lighting」；光源和场景图矛盾；多镜头段落里每镜光的方向不一样（反打时光从另一边来）。光效词汇见 `camera/lexicon-light.md`。

### 色 COLOUR

**作用**：调色的工作。画面的色彩构成。

**写法**：用**比例**写主色、辅色、点缀色（例如 70% 暖黄 / 20% 深蓝 / 10% 红），加上饱和度和肤色要求。比例比形容词更容易被执行。

**例**：

```text
COLOUR: 70% warm tungsten amber, 20% deep blue-black shadow, 10% the red of the mug.
Low overall saturation; skin stays natural, not orange.
```

**什么时候省**：风格段已写明调色、且画面没有特别的色彩意图时。

**常见错误**：写「teal and orange」「moody colours」这类套路词，模型直接套 LUT 式滤镜；肤色被主色带偏不写约束。

### 空气与画面质感 ATMOSPHERE

**作用**：摄影 + 特效的工作。空气里有什么（灰尘、蒸汽、雾、雨），以及**防 AI 质感**：过度平滑的皮肤、塑料感的布料、干净到不真实的表面。

**写法**：写这个空间里真实会有的空气介质；写材质的不完美（衣服褶皱、桌面磨痕、玻璃上的指纹）；写一句反 AI 质感的要求。

**例**：

```text
ATMOSPHERE: Faint steam rising from the kettle, catching the lamp light. Worn laminate
counter with scratches, a water ring by the sink. Fabric creases naturally.
No airbrushed skin, no waxy faces, no plastic sheen on surfaces.
```

**什么时候省**：动画、风格化作品按风格需要写；轻量档可省。

**常见错误**：为了「电影感」到处加雾和光束（体积光滥用）；写了防 AI 质感，但风格段又写 ultra detailed / 8K，互相抵消。

**词库**：反 AI 质感词库见 `video-prompt/physics.md` 第 4 节。

### 逐镜时间线 SHOTS

**作用**：导演 + 场记的工作，提示词的主体。每个镜头里按时间发生什么。

**写法**：每镜一段：

1. **镜号、时间码、景别与机位**（和镜头锁一致）；
2. **微动作按时间码排**（0–1.5s 她……；1.5–3s 他……），一镜一个主要动作；
3. **动作要有物理后果**：放下杯子，杯里的水晃；坐下，椅子吱一声往后滑；
4. **声音提示写在镜头里**：「at 2s, the kettle clicks off」；
5. **结束状态**：镜头最后一帧是什么样，方便接下一镜；
6. **台词**：谁说、原文、什么时候说；其他人嘴闭着。

**例**：

```text
SHOT 2 — 3–6s — close-up on Mira, 85mm, eye level.
3.0s: She sets the mug down on the counter; the tea inside sloshes once.
4.0s: Her jaw tightens; she does not look up.
5.0s: Behind her, off-screen, the stool scrapes as the boy shifts.
Ends: Mira still facing the sink, eyes lowered, hands flat on the counter.
```

**什么时候省**：不能省。轻量档就是一镜的时间线。

**常见错误**：一镜写三四个动作，模型压缩成一团（一镜一个动作，见 `references/drama/06-storyboard.md` §2）；只写结果不写过程（她生气了）；不写结束状态，下一镜接不上。

### 物理 PHYSICS

**作用**：特效的工作。重量、惯性、材质的反应。模型的物理常常发飘：杯子没重量，门没惯性，人走路脚不落地。

**写法**：写这场戏里会被观众看到的物理细节：重量（a heavy ceramic mug, set down with a dull knock），惯性（the door swings back and stops against the wall），接触（feet plant firmly, weight shifts）。只写镜头里真的出现的。

**例**：

```text
PHYSICS: The mug is heavy ceramic; it lands with weight, not floating. Liquid moves
with real inertia. Hands make real contact with the counter, fingers pressing slightly.
Objects do not morph, duplicate or pass through each other.
```

**什么时候省**：没有物件交互的对白镜头可以只保留最后一句。

**常见错误**：写一大段通用物理（gravity is realistic），不对应画面里任何一件东西。

**词库**：词库见 `video-prompt/physics.md`。

### 表演 ACTING

**作用**：导演的工作。细到眼睛和嘴的表演指令。

**写法**：

- **情绪三件套**：可见的行为 + 它意味着什么 + 它不是什么（`video-prompt/index.md` 第 4 条）；
- **眼睛**：自然眨眼、视线方向（看谁、看哪里、什么时候移开），**不看镜头**；
- **嘴**：只有说台词的人动嘴；不说话的人嘴闭着，**不默念**；
- **身体**：小动作的幅度（微小、克制），呼吸。

**例**：

```text
ACTING: Restrained, naturalistic. Blinks at a normal rate. Nobody looks into the lens.
Mira's anger shows only as stillness: her shoulders stop moving and her grip on the
mug tightens. It reads as holding back, not as calm. Only the speaking character's
lips move; the listener's mouth stays closed, no silent mouthing.
```

**什么时候省**：无人物镜头省；轻量档并进时间线里。

**常见错误**：写「very emotional」「intense performance」，模型演成肥皂剧；不写不看镜头，人物突然直视观众；不写嘴，两个人都在动嘴。

**词库**：词库与常见情绪的反误读表见 `video-prompt/acting.md`。

### 声音 AUDIO

**作用**：声音的工作。画内声、台词、静默。

**写法**：

- **只写画内声**（diegetic）：这个空间里真实会有的声音，按时间点写；
- **台词保留原语言**，用引号写原文，标明说话人和语言（spoken in Mandarin）；
- **静默要写出来**：「silence except the hum of the fridge」；
- 和硬约束呼应：no music。

**例**：

```text
AUDIO: Diegetic only. Room tone: the low hum of the fridge. At 2s the kettle clicks off.
At 8s the boy says, in Mandarin: "爸的表呢？" — quiet, not accusing.
Mira does not answer. After his line: near silence, only the fridge.
```

**什么时候省**：模型不出声音时可以省（后期配音）；但台词时机还是要写进时间线，表演才对得上。

**常见错误**：台词翻译成英文写，生成的口型和后期配音对不上；写「tense atmosphere sounds」，模型加环境音乐；不写静默，模型填满。声音设计见 `craft/sound/`。

**词库**：词库见 `video-prompt/audio.md`。

### 总锁 LOCKS

**作用**：场记的工作。在结尾把最关键的不变量再列一次。长提示词中段的信息容易被稀释，结尾的重复让它们重新加权。

**写法**：一行一条，5–8 条以内。只放「错了整条作废」的东西：人数、谁坐谁站、谁说话、轴线、道具状态、不能出现的东西。

**例**：

```text
LOCKS:
- Only two people, the whole time.
- Mira never sits; the boy never stands.
- Mira is always frame right, the boy frame left.
- Only one line of dialogue, spoken by the boy.
- No music, no on-screen text.
```

**什么时候省**：轻量档单镜可省。

**常见错误**：把普通描述也放进来，变成第二份提示词；总锁和正文矛盾（正文写他站起来，总锁写他从不站）。

**词库**：选法见 `video-prompt/locks.md` 第 3 节。

### negative

**作用**：这场戏的错误版本。不是通用的「blurry, low quality」，而是**这场戏最可能被生成错的样子**。

**写法**：先想这场戏的三五个「错误版本」——她哭了、他冷笑了、背景出现同事、屏幕上有字、两个人同时说话——写成负面描述。有负面参数框的模型放进参数；没有的写在正文末尾「Avoid: ...」。通用质量词最多保留几个和防 AI 质感相关的。

**例**：

```text
NEGATIVE: Mira crying, tears, shouting, confronting the boy; the boy smirking or
looking guilty; any third person; readable text anywhere; music; slow motion;
smooth floating camera; waxy skin.
```

**什么时候省**：轻量档只保留两三条最可能的错误。

**常见错误**：抄一份万能 negative 清单（extra fingers, bad anatomy, ...），和这场戏无关；正文里写的东西又出现在 negative 里，互相抵消。

**词库**：从错误版本倒推的方法见 `video-prompt/locks.md` 第 2 节。

---

## 四条写法原则

这四条是本层对 `references/aigc/prompt-syntax.md` 单镜规则的扩展；多镜头和长提示词以这里为准。

1. **识别特征锁，不重写外貌。** 有参考图时，不全文重写外貌，但要写 2–4 个最容易漂的识别特征、明确的「没有」（no scar），以及最容易漂的服装件。全文重写会和参考图打架；一句不写，跨镜会漂。
2. **正面描述优先，顽固默认集中封住。** 正文写想要的效果。模型很难改掉的默认（音乐、画面文字、多余的人、稳定器式平滑、AI 质感）放进硬约束和总锁，同义说法列全。negative 写这场戏的错误版本，不写通用清单。
3. **三档长度，按模型和复杂度选。** 轻量 / 标准 / 重型，见 `video-prompt/index.md`。字数区间是社区经验，未经本包实测。
4. **机身型号只做可选锚点。** ARRI Alexa、16mm 这类词可以加，但优先写它们带来的画面特征：微反差、高光过渡、暗部抬起、颗粒。

## 来源

见 `video-prompt/sources.md`。
