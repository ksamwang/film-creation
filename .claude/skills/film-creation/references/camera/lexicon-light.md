# 光的词典：人物光型、光源动机、时段与调性

字段与可靠性分级见 `camera/index.md`。光为什么这样用（看见、看不见、怀疑看见的）见 `craft/visual/04-light.md`；色温与色板见 `craft/visual/05-color.md`。本篇只管「叫什么、怎么写、能不能出」。

**写光的四条规则**

1. 按顺序写：**动机 → 方向 → 硬度 → 光比 → 色温**（`craft/visual/04-light.md`）。`A single desk lamp at frame right throws hard warm light across his face; the far side falls into deep shadow.`
2. **一个主光**。辅光只负责让该看见的看见，不能形成第二个方向。
3. **光是场景级的决定**：写进场景参考图和风格句，同一场逐字复用；单镜换光必须有画内事件（开灯、云遮日）。
4. 写光的**后果**（阴影落在哪、哪半边脸暗），不只写光型的名字。名字模型认得，但常只给个大概。

**短剧**：光不在分镜枚举里。整部剧的光写进画风句（`references/drama/10-look.md`「媒介 → 线条/渲染 → 光 → 色 → 质感」），每个场景的光写进场景图；分镜 `text` 里只写有动机的光变化。非写实画风不写写实摄影词，光只写主光源和方向。

---

## 1. 人物光型

人物光型是摄影的通行叫法（行业惯例），都由主光相对人脸的位置决定。三点照明模型（主光、辅光、轮廓光）见《镜头的语法》3.3。

### 伦勃朗光 Rembrandt
- **写法**：`Rembrandt lighting: a single soft key from high frame left; the right cheek in shadow except for a small triangle of light under the eye.` B: `rembrandt lighting, triangle of light on shadow cheek`
- **作用**：立体、庄重、有心事；经典的戏剧人像光。
- **用 / 不用**：沉思、独白、肖像式的人物亮相；喜剧和明快场景太重。
- **生成**：稳。写出「暗侧脸颊上的三角形光斑」比只写名字准。

### 蝴蝶光 Butterfly / Paramount
- **写法**：`Butterfly lighting: the key light high and directly in front of her face, a small butterfly-shaped shadow under the nose, cheekbones sculpted.` B: `butterfly lighting, frontal high key light`
- **作用**：美化、光鲜、明星感；脸对称、皮肤平滑。
- **用 / 不用**：女主亮相、广告感、霸总剧的精致人像；需要阴暗或真实感时不用。
- **生成**：稳。

### 环形光 Loop
- **写法**：`Loop lighting: soft key slightly to one side and above; the nose shadow falls in a small loop toward the cheek.` B: `loop lighting`
- **作用**：自然、亲切，最日常的人像光，比伦勃朗光轻。
- **用 / 不用**：都市剧、对话戏的默认人像光。
- **生成**：稳；常常就是模型的默认结果。

### 分割光 Split
- **写法**：`Split lighting: hard light from directly frame left; exactly half his face lit, the other half in black shadow.` B: `split lighting, half face in shadow`
- **作用**：双面性、内心分裂、危险；黑色电影的标志。
- **用 / 不用**：反派、秘密、道德抉择的一刻；用多了观众会觉得廉价。
- **生成**：稳。

### 宽光 / 窄光 Broad / Short
- **写法**：宽光 `The key light falls on the side of her face turned toward the camera.`；窄光 `The key light falls on the side of her face turned away from the camera; the near cheek is in shadow.` B: `broad lighting` / `short lighting`
- **作用**：宽光让脸显得宽、开放、明亮；窄光让脸显得瘦、立体、有神秘感。
- **用 / 不用**：同一个人物在不同处境下切换：坦白时宽光，隐瞒时窄光。
- **生成**：定帧。模型常分不清朝向镜头的是哪一侧，先出关键帧确认。

### 轮廓光 / 逆光 Rim / Backlight
- **写法**：`A strong backlight from behind her outlines her hair and shoulders in a thin bright edge, separating her from the dark background.` B: `rim light, backlit hair`
- **作用**：把人物从背景里分离出来（《镜头的语法》3.3 轮廓光）；神圣、回忆、浪漫。
- **用 / 不用**：暗背景前的人物、逆光的告白；正午户外不需要。
- **生成**：稳。容易过度变成整片光晕，写 `thin edge`。

### 剪影 Silhouette
- **写法**：`Silhouette: he stands in the doorway against the bright corridor; his body is a solid black shape, no facial detail.` B: `silhouette against bright background`
- **作用**：隐藏身份、强调姿态；神秘人物出场、结尾的告别。
- **用 / 不用**：要观众读形状不读表情时。需要脸时不用。
- **生成**：稳。参考图生时模型会想把脸画亮，写 `no facial detail`。

### 顶光 Top light
- **写法**：`Hard light from directly overhead; deep shadows in his eye sockets and under his nose and chin.` B: `harsh top light, shadowed eyes`
- **作用**：眼睛藏进阴影，人物不可读、有威胁；审讯室、正午的荒漠。
- **用 / 不用**：审讯、教父式的权力人物；需要读眼神时不用。
- **生成**：稳。

### 底光 Under light
- **写法**：`Light from below, from the phone screen in her hands; the shadows on her face run upward.` B: `underlighting from below`
- **作用**：反自然，恐怖、诡异；或者有动机的屏幕光、篝火光。
- **用 / 不用**：有画内光源（手机、篝火、蜡烛）时自然；没有动机就是恐怖片的手电照脸。
- **生成**：稳。

### 眼神光 Catchlight
- **写法**：`A small bright catchlight in both eyes from the window.` B: `catchlight in eyes`
- **作用**：眼睛有生气。没有眼神光的眼睛显得空洞、死寂（《镜头的语法》6.3 保证眼神光）。
- **用 / 不用**：特写默认要有；刻意去掉用来表示绝望或非人。
- **生成**：稳。

---

## 2. 画内光源（光源动机）

光要有来源：观众能在画面里找到，或能想象到（《导演的摄影课》第六章；`craft/visual/04-light.md`）。

| 光源 | 写法 | 光的性质 | 适合 | 生成 |
|---|---|---|---|---|
| 窗光 | `Soft daylight from a large window at frame left` | 大面积、柔、单侧 | 日戏的默认；都市剧 | 稳 |
| 台灯 / 落地灯 | `A single desk lamp at frame right, warm, hard-edged pool of light` | 小面积、暖、衰减快 | 夜戏、独处、密谋 | 稳 |
| 霓虹 | `Red and blue neon signs outside the window wash across his face` | 饱和、双色、闪烁 | 都市夜、迷离、黑色 | 稳 |
| 屏幕光 | `The cold blue light of the laptop screen on her face, the room dark` | 冷、从下方或正面、会闪 | 深夜工作、偷看、孤独 | 稳 |
| 火光 / 烛光 | `Flickering warm candlelight from below, the edges of the room in darkness` | 暖、闪动、底光 | 古装、仪式、亲密 | 稳；闪烁幅度难控，写 `gentle flicker` |
| 门缝光 | `A thin strip of light from the gap under the door falls across the dark floor` | 细线、对比强 | 悬疑、门外有人 | 稳 |
| 百叶窗光 | `Hard sunlight through venetian blinds casts striped shadows across her face` | 条纹 | 黑色电影、困住、审视 | 稳 |
| 车灯 | `Headlights from a passing car sweep across the bedroom ceiling` | 移动、扫过 | 夜、有人来了、时间流逝 | 视频里定帧 |
| 手电 | `A flashlight beam cuts through the darkness and stops on the drawer` | 硬、窄、移动 | 潜入、搜寻 | 稳 |
| 闪电 | `A flash of lightning briefly lights the whole room` | 一瞬间全亮 | 揭示、惊吓 | 后期：生成暗镜头和亮镜头，剪辑交替 |

---

## 3. 时段与天气

| 名称 | 写法 | 作用 | 生成 |
|---|---|---|---|
| 正午硬光 | `Harsh midday sun, short black shadows directly under them` | 暴露、炎热、无处可躲 | 稳 |
| 黄金时刻 | `Low golden sunlight just before sunset, long shadows, warm glow on skin` | 温暖、怀旧、浪漫、最后的美好 | 稳 |
| 蓝调时刻 | `Blue hour just after sunset: deep blue sky, the first warm windows lit in the buildings` | 过渡、忧郁、冷暖对比 | 稳 |
| 阴天柔光 | `Overcast sky, soft shadowless light, muted colors` | 平静、压抑、真实感 | 稳 |
| 月光夜景 | `Cool moonlight from high frame right, deep blue shadows, faces barely readable` | 夜、秘密 | 稳；易死黑，写清哪里能看见 |
| 雨夜 | `Night rain, wet asphalt reflecting the shop signs, rim light on wet hair` | 都市、情绪、追逐 | 稳 |
| 雾与体积光 | `Shafts of light through the haze from the high windows` | 神圣、梦境、空间感 | 稳；全片都有会像 MV |

时段写进场景级设定：同一场的几个镜头必须是同一个时段，否则剪在一起会跳（`craft/visual/05-color.md`）。

---

## 4. 整场调性

| 调性 | 写法 | 作用 | 来源 |
|---|---|---|---|
| 高调 High key | `High-key lighting: bright, even, few shadows, low contrast` | 喜剧、日常、安全、广告感 | 《导演的摄影课》第六章 6.5 |
| 低调 Low key | `Low-key lighting: most of the frame in shadow, a single hard source, high contrast` | 惊悚、黑色、悬疑、秘密 | 《导演的摄影课》第六章 6.5 |
| 明暗对照 Chiaroscuro | `Strong chiaroscuro: faces emerge from deep black, a single warm source` | 古典、宗教感、道德冲突 | 行业惯例 |
| 平光 Flat | `Flat frontal light, no modeling, shadows almost absent` | 冷漠、监控感、荒诞；或刻意的漫画感 | 行业惯例 |

调性是**整场甚至整片**的决定，不是单镜随机。写进场景 token 或画风句（`references/drama/10-look.md`）。

---

## 5. 光的变化（视频）

| 变化 | 写法 | 作用 | 生成 |
|---|---|---|---|
| 开灯 / 关灯 | `She switches on the lamp; warm light fills the corner of the room.` | 进入 / 结束、揭示 | 定帧：首尾帧锁住亮前与亮后 |
| 云遮日 | `A cloud passes over the sun; the bright courtyard dims to gray.` | 情绪转阴、不祥 | 定帧 |
| 车灯扫过 | 见上表 | 有人来了 | 定帧 |
| 闪烁 | `The fluorescent tube overhead flickers twice.` | 不安、故障、恐怖 | 生成闪烁不稳，幅度乱；后期调亮度更可控 |
| 日转夜 | `Time-lapse from afternoon to night`（无固定人物） | 时间流逝 | 见 `lexicon-move.md`「延时」 |

光变一定要有画内事件触发。没有触发的光变，观众会以为是生成错误。

---

## 6. 失败与修法

| 失败 | 原因 | 修法 |
|---|---|---|
| 均匀的棚拍光，没有方向 | 没写主光 | 写一个有动机的主光和方向 |
| 夜戏一片死黑 | 只写 `dark`、`night` | 写一个画内光源，画面里至少一块亮区；脸的哪一部分能看见 |
| 两个方向的阴影打架 | 写了两个主光 | 只留一个主光；第二个光写成 `faint fill` 或 `rim` |
| 同一场里光每镜不同 | 每镜单独写光 | 光写进场景图和风格句，逐字复用 |
| 光晕、镜头光斑太多 | 写了 `cinematic lighting`、`dreamy` | 删掉形容词，写具体光源和硬度 |
| 光型名字写了但没效果 | 只写名字 | 补后果：阴影落在哪、哪半边脸暗 |

## 来源

见 `camera/sources.md`。
