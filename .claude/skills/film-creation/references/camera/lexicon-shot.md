# 取景词典：景别、角度、焦段、景深

字段与可靠性分级见 `camera/index.md`。取景句的固定顺序：**景别 → 角度 → 焦段与透视 → 景深与焦点 → 主体位置**。一镜每项只取一个值。

---

## 1. 景别

景别回答「给多少身体、多少环境」。只写景别名，模型常偏宽；写**切点**更稳（《镜头的语法》1.3–1.4；《电影语言的语法》3.8）。

| 景别 | 写法（模式 A） | 读什么 | 短剧 |
|---|---|---|---|
| 大远景 | `Extreme wide shot: the figure is a small dot against the whole valley.` | 人在世界里有多小；地点、季节、孤立 | `extreme_wide` |
| 远景 | `Wide shot, the whole room visible, both people head to toe in the middle distance.` | 空间地理、谁在哪 | `wide` |
| 全景 | `Full shot including her feet, a little floor below and headroom above.` | 全身姿态、走位 | `full` |
| 中远景（膝上） | `Medium-full shot cut just above the knees.` | 姿态 + 手部动作，西部片的拔枪景别 | 落 `full` |
| 中景 | `Medium shot cut at the waist.` | 动作与手里的东西；对话的默认景别 | `medium` |
| 中近景 | `Medium close-up cut at mid-chest.` | 表情为主、带一点手势 | `medium_close` |
| 特写 | `Close-up, face from chin to just above the hairline.` | 表情、视线 | `close` |
| 大特写 | `Extreme close-up of her eyes only, filling the frame edge to edge.` | 一个细节放大成事件 | `extreme_close` |
| 插入特写 | `Insert shot: a thumb pressing the phone's lock button, nothing else in frame.` | 证据、道具、关键动作 | 落 `extreme_close` |

**规则**

- 切点避开关节：腋下、胸下、腰下、臀下、膝下可以，脚踝、膝盖、手腕不行；全景必须带脚。
- 相邻两镜的景别跨一档以上（中景接特写），只差半档像跳帧；同景别相接要换角度至少 30°。
- 景别越近，表演越要小：特写里只写一个微动作（眼神移开、下颌收紧）。
- **生成**：远景、中景、特写都**稳**；大特写和插入特写在参考图生里常被拉宽，**定帧**更稳。无首帧时要近景，写「脸占画面上三分之一」这类比例。
- **竖屏**：主力是中近景和特写；远景两侧窄，空间靠纵深交代。

---

## 2. 垂直角度

角度改变的是**观众和人物的权力关系**（《镜头的语法》2.2；《电影镜头设计》第十四章）。拍人物时，摄影机高度以人物眼睛为基准。

### 平视 Eye level
- **写法**：`Eye-level shot, the camera at her eye height.` B: `eye level`
- **作用**：中立，观众和人物平等。
- **用 / 不用**：对话、日常、信息交代的默认值；要表达权力变化时离开它。
- **生成**：稳。模型默认就是平视略高，写明更稳。
- **短剧**：`eye_level`

### 俯拍 High angle
- **写法**：`High angle from above head height, looking down at him; the floor fills the frame around his feet.` B: `high angle, looking down`
- **作用**：人物变小、被压住、被审视；也可以是「上帝在看」。
- **用 / 不用**：失势、被困、被审判、孤立；给胜利者、施压者用俯拍会把权力关系拍反。
- **生成**：稳。幅度小时模型常画成平视，写出「地面占画面大半」这类后果。
- **失败**：头大身小的广角变形——加 `natural proportions` 或换长焦。
- **短剧**：`high`

### 仰拍 Low angle
- **写法**：`Low angle from waist height, looking up at her; the ceiling presses in behind her head.` B: `low angle, looking up`
- **作用**：人物变高、有威胁或有力量；配广角时近乎压迫。
- **用 / 不用**：掌权、威胁、反转后的「站起来」；整场都用会失效，留给权力转折那一镜。
- **生成**：稳。
- **失败**：鼻孔、下巴变形——角度收小，或写 `slight low angle`。
- **短剧**：`low`

### 顶拍 Overhead / top-down
- **写法**：`Directly overhead, the camera looking straight down at the bed; she lies curled at the center of the frame.` B: `top-down shot, overhead`
- **作用**：把场景变成图案或地图；人物失去面孔，成为被摆放的东西。
- **用 / 不用**：俯视棋局般的局面、死亡或昏迷、桌面上的物件布局、开场的地理交代。情绪特写不用。
- **生成**：稳（图像）；视频里人物容易被画成侧躺透视，**定帧**更稳。
- **短剧**：`overhead`

### 虫视 Worm's-eye
- **写法**：`Worm's-eye view from the ground; the boots step over the lens toward the sky.` B: `worm's-eye view, ground level`
- **作用**：极端仰视，环境或人物压倒一切；有时是地上某物的主观视角。
- **用 / 不用**：怪物、建筑、倒地者看到的世界；只用一次。
- **生成**：定帧。文字常被画成普通仰拍，先出关键帧。
- **短剧**：落 `low`

---

## 3. 水平角度

《镜头的语法》2.2 把水平角度分成正面、3/4、侧面、背面。离正面越远，观众越像旁观者。

| 角度 | 写法 | 作用 | 生成 |
|---|---|---|---|
| 正面 | `Frontal, she faces the camera straight on.` | 对质、宣告、向观众坦白；对称感 | 稳 |
| 3/4 侧面 | `Three-quarter view, her face turned 45 degrees toward frame right.` | 最自然的人物角度，立体感 | 稳；参考图多为正面时脸可能偏正 |
| 侧面 | `Profile, she faces frame right; only one eye visible.` | 冷静、旁观；两人侧面相对是对峙 | 稳 |
| 背面 | `From behind, over the back of her head; we see what she faces.` | 让观众跟随她看；隐藏表情制造悬念 | 稳；参考图生时身份难辨，先给一镜正面锚定 |

对话戏的两个单人镜，水平角度要对称：A 是 3/4 朝右，B 就是 3/4 朝左，镜头高度、焦段一致（《镜头的语法》6.11）。

---

## 4. 倾斜：荷兰角 Dutch angle

- **写法**：`Dutch angle, the camera tilted about 20 degrees; the door frame runs diagonally across the shot.` B: `dutch angle, tilted horizon`
- **作用**：世界失衡——醉、疯、梦、被骗，或局面即将失控（《镜头的语法》3.1；《电影镜头入门》Step2）。
- **用 / 不用**：一场里只给失衡发生的那几镜，倾斜方向随局势变；作为「酷」的装饰最廉价。
- **生成**：稳。幅度靠写参照物（门框、地平线），只写 `tilted` 时常只歪几度。
- **失败**：无动机倾斜——不需要时写 `level horizon`。
- **短剧**：`dutch`

---

## 5. 关系视角

### 过肩 Over the shoulder
- **写法**：`Over B's shoulder: B's dark, out-of-focus shoulder fills frame left; A faces the camera in the right two-thirds.` B: `over-the-shoulder, foreground shoulder soft`
- **作用**：把两个人放进同一镜，同时让一方成为主角；对话正反打的标准单元（《镜头的语法》2.3）。
- **用 / 不用**：要观众感到「两人连在一起」时用；关系断裂后改成干净单人镜（不带对方肩膀），距离感立刻出来。
- **生成**：稳。参考图生时要写清前景是谁、哪一侧，否则两人身份会互串。
- **短剧**：`over_shoulder`；竖屏里把前景肩膀放在画面下角，比左右排开更省宽度。

### 主观镜头 POV
- **写法**：`Point-of-view shot from his eyes: the hallway ahead, his own hands not visible, the camera at standing eye height.` B: `first-person POV`
- **作用**：观众占据人物的眼睛（《电影镜头入门》Step5；《电影镜头设计》第十六章）。
- **用 / 不用**：前后要有「他在看」的镜头夹住（看 → 看到什么 → 反应），否则观众不知道是谁的眼睛。
- **生成**：稳（图像）；视频里模型常把「我」画进画面，**定帧**更稳。
- **短剧**：`pov`

### 带物主观 POV with hands
- **写法**：`First-person view: his own hands enter the bottom of the frame, unfolding the letter.` B: `POV, own hands in frame`
- **作用**：主观 + 身体感；观众替他动手。
- **用 / 不用**：拆信、开门、拿枪、看手机。
- **生成**：定帧。手的数量、左右手常出错，首帧先修好。
- **短剧**：落 `pov`

### 物体视点 Object POV
- **写法**：`From inside the open refrigerator, looking out: she leans in, lit by the fridge light.` B: `view from inside the fridge`
- **作用**：让物件「看」人——幽默、窥视感或宿命感（《电影镜头入门》Step5）。
- **用 / 不用**：一部片用一两次；要和道具的戏剧功能相关。
- **生成**：定帧。文生常画成普通视角，先出关键帧。

### 遮挡偷窥 Through-foreground
- **写法**：`Seen through the half-open blinds across the street; the slats cut dark bars across the shot, she is small in the gap.` B: `through foreground blinds, voyeuristic`
- **作用**：有人在看她——即使画面里没有偷窥者。
- **用 / 不用**：跟踪、监视、不被允许靠近；前景物要属于这个空间（百叶、门缝、车窗、植物）。
- **生成**：稳。

### 双人镜头 Two-shot
- **写法**：`Two-shot in profile: A frame left facing right, B frame right facing left, a table between them.` B: `two-shot, profiles facing each other`
- **作用**：把关系本身作为主语。《镜头的语法》2.3 分侧面双人、面向镜头双人、过肩双人三种：侧面是对峙，面向镜头是「我们一起面对」，过肩把重心交给一方。
- **生成**：稳；两人以上靠参考图分配身份并写清左右（`craft/staging/05-multi-character.md`）。
- **短剧**：竖屏不要左右排开，用前后纵深或上下错落（`references/drama/06-storyboard.md` 第 4 节）。

---

## 6. 焦段与透视

焦段决定**透视和人物被看的距离感**。写法按 `craft/visual/03-lens.md` 的顺序：焦段 → 透视后果 → 景深 → 焦点对象。

| 焦段 | 写法 | 后果与作用 | 不用于 | 生成 |
|---|---|---|---|---|
| 鱼眼 / 超广 | `Ultra-wide fisheye very close to his face; the room bends around him.` | 强烈变形：幻觉、醉、喜剧、运动视角 | 正常对话、需要好看的脸 | 稳 |
| 广角（约 18–28mm） | `Wide 24mm lens close to her; the corridor stretches deep behind.` | 纵深被拉长，前大后小；空间感、紧张、靠近时有侵入感 | 特写肖像（鼻子放大，《镜头的语法》6.28） | 稳 |
| 标准（约 35–50mm） | `A 40mm lens at conversational distance, natural perspective.` | 接近人眼，中立 | 要强烈情绪时 | 稳 |
| 长焦（约 85–135mm） | `An 85mm lens from across the room; her face sharp, the background soft.` | 脸型好看、背景分离；观察者距离 | 交代空间 | 稳 |
| 远摄压缩（200mm+） | `A long telephoto lens from far away: the crowd and the buildings behind are compressed into one flat wall.` | 前后被压扁，人群拥挤、追赶的人永远到不了 | 需要读清前后距离时 | 稳 |

- 一个角色或空间锁一个主焦段，跨镜逐字复用；换焦段写理由。
- 写 mm 数模型能理解，但后果句更重要：只写 `24mm` 不写「走廊被拉长」，透视常不到位。

---

## 7. 景深与焦点

### 深焦 Deep focus
- **写法**：`Deep focus: the child in the foreground and the parents arguing at the back door are both sharp.` B: `deep focus, everything sharp`
- **作用**：前后景同时清楚，让观众自己选看哪里；前后景之间有戏剧关系（《镜头的语法》3.2；《导演的摄影课》第三章）。
- **用 / 不用**：前景人物不知道后景发生的事；群戏。单人情绪特写不用。
- **生成**：稳（图像）；模型偏爱浅景深，要写出前后都是谁、都清楚。

### 浅景深 Shallow focus
- **写法**：`Shallow focus: only her eyes are sharp; the party behind dissolves into soft blur.` B: `shallow depth of field, background soft`
- **作用**：把人物从环境里切出来——孤立、专注、亲密。
- **用 / 不用**：主观情绪、亲密；需要读环境信息时不用。全片都浅景深等于没有选择。
- **生成**：稳。

### 焦点转移 Rack focus
- **写法**：`The focus starts on the ring on the table, then shifts to her face behind it as she looks up; the ring goes soft.` B: `rack focus from ring to face`
- **作用**：在一个镜头里把注意力从 A 交给 B，不动机位就完成「发现」（《电影镜头入门》Step6「焦点前移」「调焦转场」；《镜头的语法》3.2）。
- **用 / 不用**：前景物件与后景人物有因果；一场一次。
- **生成**：定帧，部分模型不可靠。先出焦点在 A、焦点在 B 两张帧走首尾帧；不行就拆成两镜硬切。
- **失败**：两处一起糊、焦点来回呼吸——写 `one smooth focus shift, once`。

### 前景虚化 Foreground blur
- **写法**：`A blurred wine glass fills the left edge of the frame; he sits sharp in the middle distance.` B: `soft foreground element`
- **作用**：加纵深层次；暗示观察者或阻隔。
- **生成**：稳。

### 分屈光 Split diopter
- **写法**：`Split-diopter look: a face very close on the left and a figure far away on the right are both in sharp focus, a soft blur line between them.` B: `split diopter, two planes in focus`
- **作用**：两个距离同时清楚，比深焦更刻意，适合「两人命运并置」。（行业惯例）
- **生成**：定帧。只在图像阶段做得出，视频走首帧生视频且运动要小。

### 移轴微缩 Tilt-shift
- **写法**：`Tilt-shift miniature look: a high view of the street, a sharp band across the middle, top and bottom blurred; the cars look like toys.` B: `tilt-shift, miniature effect`
- **作用**：现实被变成玩具模型——荒诞、俯视人间、时间流逝段落。（行业惯例）
- **生成**：稳（图像）；视频配延时运动效果更好。

---

## 8. 竖屏取景速查

- 景别主力：中近景、特写；远景只用来交代一次空间。
- 角度：平视为主；权力转折用仰 / 俯；对话用过肩，前景肩放在画面下角。
- 纵深代替横向：两人前后站，焦点在谁身上谁是主角。
- 脸放在画面中上部，下方约 20% 留给字幕与平台界面。
- 细则见 `references/drama/06-storyboard.md` 第 4 节。

## 来源

见 `camera/sources.md`。
