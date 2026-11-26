# 动作词典：武学、兵器、法术与受击

字段与可靠性分级见 `camera/index.md`。一场打戏怎么排镜头、镜内四拍、防守三态见 `camera/recipes/fight.md`；本篇只管「这种功夫 / 兵器 / 法术长什么样、怎么写、能不能出」。

**先读：只取神，不取形**

招式名对模型没有意义。写「白鹤亮翅」「铁山靠」，模型不知道身体该怎么动，只会给一个大概的武术姿势。选一门功夫，取的是它的**节奏、身形和距离**，再落成看得见的身体动作：哪只脚蹬地、重心往哪走、手从哪到哪、打在哪、对方怎么反应。

**发力写成链**

一记有分量的打击，力从脚下来：蹬地 → 转胯 → 送肩 → 出手 → 命中 → 对方受力。写不全时，至少写四件：脚下怎么动、腰胯怎么转、打在哪、对方哪里先动。只写手，动作就是飘的。

```text
He plants his rear foot and twists his hips; the turn travels up through his shoulder and his right fist drives into the man's ribs; the man's torso folds around the blow before his feet slide back.
```

---

## 1. 现代搏击

都市、警匪、写实打斗的首选。动作经济，没有花架子，观众信。

### 拳击 Boxing
- **写法**：`He slips left, his head dropping under the jab, and answers with a short right hook to the jaw; his feet stay planted shoulder-width apart.`
- **作用**：头部移动、组合拳、步法；节奏是「躲—打—躲」的短循环，近距离、高频率。
- **用 / 不用**：街头单挑、拳台、体力相当的对峙。不适合长距离和多人。
- **生成**：稳。组合拳一镜写两三下就够，多了后面的拳会被吞掉。

### 泰拳 Muay Thai
- **写法**：`She grabs his neck with both hands in a clinch and drives her right knee up into his stomach twice.`
- **作用**：肘、膝、扫踢，近身缠抱；每一下都重、短、硬，带骨头相撞的感觉。
- **用 / 不用**：要狠、要疼的贴身战。轻快的戏不用。
- **生成**：稳。缠抱两人贴得近，正脸只给一个人，防换脸。

### 散打与踢拳 Sanda / kickboxing
- **写法**：`He snaps a side kick into the man's chest from two steps away, then closes in and sweeps his front leg.`
- **作用**：远踢、近打、贴身摔，三种距离来回切；画面有纵深变化。
- **用 / 不用**：需要距离变化的写实打斗；动作片里最通用的底子。
- **生成**：稳。

### 柔术与摔投 Grappling and throws
- **写法**：`She hooks his ankle with her heel, pulls his collar down toward her hip, and he goes over her back onto the concrete.`
- **作用**：破坏重心、投摔、地面压制、锁关节；以小制大，女性、瘦小角色制服大块头最可信。
- **用 / 不用**：要写实、要「技术赢」的场面；儿童向的安全写法用擒拿锁腕，不写击打。
- **生成**：稳到定帧。地面缠斗肢体交叠容易穿模，压制镜头放宽到全景，或拆成「摔出—落地—压住」三镜。

### 近身格斗与擒拿 CQC
- **写法**：`He traps the wrist holding the knife, turns it outward against the joint, and the blade clatters onto the floor.`
- **作用**：夺械、锁腕、控制，快而无声，职业感强。
- **用 / 不用**：特工、保镖、警察；动作要短，一两下解决。
- **生成**：稳。

---

## 2. 传统国术

民国、武侠、功夫片。每一门的签名在节奏和身形，不在招式名。

### 咏春 Wing Chun
- **写法**：`Standing square to him, she blocks along the centerline and fires three straight punches in a rapid chain, each from barely a hand's length away.`
- **作用**：守中线、短桥、连环直拳、寸劲；近、密、快，手臂像在对方手臂上黏着走。
- **用 / 不用**：狭窄空间、贴身快打。不适合大开大合。
- **生成**：稳。连环拳写成「一串」而不是逐拳数，模型给出的频率更自然。

### 八极 Bajiquan
- **写法**：`He stamps forward and slams his shoulder and back into the man's chest; the man is thrown off his feet into the stall behind.`
- **作用**：贴身崩撞、跺脚震地、以肩背靠打；刚猛、短促、一击定局。
- **用 / 不用**：要爆发力和一招制敌；短剧「一招打飞」很合适。
- **生成**：稳。被撞飞的距离写具体（「撞进身后的摊子」），不写「飞出很远」。

### 太极 Taiji
- **写法**：`She yields as he pushes, her waist turning, and guides his force past her hip; his own momentum carries him stumbling forward.`
- **作用**：化劲、借力、走圆；攻方越用力越吃亏，节奏是「慢—慢—突然」。
- **用 / 不用**：高手对莽夫、以柔克刚、宗师气度。
- **生成**：稳。慢动作要写成本身就慢的动作，不是加慢放。

### 八卦掌 Baguazhang
- **写法**：`He circles her with gliding steps, always at her side, and strikes her flank with an open palm the moment she turns.`
- **作用**：走圈、避正打斜、绕到侧后；画面上是环绕运动，摄影机可以跟着反向绕。
- **用 / 不用**：要灵动、要「打不着他」的感觉；对多个对手时尤其好看。
- **生成**：稳。环绕跟拍见 `camera/lexicon-move.md`。

### 形意 Xingyiquan
- **写法**：`He advances in a straight line, each step landing with a strike, driving the man back across the courtyard.`
- **作用**：直线推进、步到拳到、整劲穿透；像推土机，一路压过去。
- **用 / 不用**：压制、一方被逼到墙角。
- **生成**：稳。

### 地趟与低位腿法 Ground and low kicks
- **写法**：`She drops into a roll under his swing and sweeps his ankles from the ground; he crashes onto his back.`
- **作用**：贴地滚翻、低扫、倒地起腿；画面重心压到最低，和对手形成高低差。
- **用 / 不用**：被击倒后的反击、对付持兵器的对手。
- **生成**：定帧。翻滚易崩，拆成「倒地—扫腿—对方倒」三镜，各从关键帧起。

---

## 3. 兵器

兵器先定分量：轻兵器靠手腕和速度，重兵器靠全身和惯性。分量写错，挥起来就是塑料道具。

### 剑 Sword
- **写法**：`Her wrist flicks and the tip of the sword darts at his throat, stopping a finger's width away; her body barely moves.`
- **作用**：轻、灵，点、刺、挑、抹；动作集中在手腕和步法，身体保持轻。诗意武侠、高手对决。
- **用 / 不用**：要飘逸、要精准。砍杀场面用刀。
- **生成**：稳。剑身反光和细长形状容易变形，关键镜头挂兵器参考图。

### 刀 Saber / blade
- **写法**：`He swings the heavy blade two-handed from over his right shoulder; his whole body follows the arc and the edge bites into the wooden post.`
- **作用**：重、狠，劈、砍、拖；全身跟着刀走，收刀也要时间。
- **用 / 不用**：要力量、要血性（写成砍进木柱、劈开器物，不写人体伤口）。
- **生成**：稳。

### 长兵 Spear / staff
- **写法**：`She sweeps the staff low in a wide circle, keeping three men at the length of the pole.`
- **作用**：距离控制、横扫、突刺；一人对多人时画面最清楚。
- **用 / 不用**：一对多、开阔场地。窄巷不用。
- **生成**：稳。长杆两端都要在画面里，景别别太紧。

### 软兵 Chain / whip / rope dart
- **写法**：`The chain whips out, wraps twice around his wrist and snaps taut.`
- **作用**：缠、甩、收，轨迹出人意料；诡异、灵巧的角色。
- **用 / 不用**：要奇；重场面少用。
- **生成**：定帧到后期。链条和鞭子的轨迹模型最难做对，常常断成几截或穿过身体。拆成「甩出」和「已缠住」两镜，各给关键帧；轨迹的弧线可以后期加动态模糊。

### 拔刀 Quick draw
- **写法**：`He stands motionless, hand on the hilt. Cut to: he is already past the man, blade back in the sheath. A beat later the lantern behind them splits in two.`
- **作用**：静—瞬—收：长时间的静止，一闪，结果延后出现；整场的张力在等待里。
- **用 / 不用**：宗师、一击定胜负；黑泽明式对峙见 `directors/akira-kurosawa.md`。
- **生成**：稳。出刀那一瞬不生成，用剪辑跳过，只拍前后。

---

## 4. 法术与特效

玄幻、仙侠、二次元。特效不是贴上去的光，它有形状、有来源、有分量，还会改变环境。

### 先定形再上光 Shape before glow
- **写法**：`A blade of dense blue water forms along his palm, its edge rippling; only then does a faint light run along it.`
- **作用**：先决定能量是什么形态：流体（水、火、雾）、固体（冰晶、岩刺、金属）、气浪（冲击波、风刃）、粒子（光点、灰烬），再给光。只写「发光的能量」，画面就是一团泛白的光，看不清，也不像这个世界的东西。
- **用 / 不用**：所有法术镜头的第一句。
- **生成**：稳。

### 三层构造 Core, edge, world
- **写法**：`At the center, a white-hot core; around it, crackling red arcs; where it touches the ground, stone cracks and dust rises in a ring.`
- **作用**：核心（最亮最实）→ 外缘（颜色、纹理、动态）→ 环境反馈（地裂、风压、碎物、衣发被吹动）。少了第三层，特效就浮在画面上，和世界没有关系。
- **用 / 不用**：每次命中、每次释放。
- **生成**：稳。

### 特效随动作生 Effect follows the move
- **写法**：`As her sword cuts left to right, a trail of flame follows the blade's path and lingers for a moment before breaking into embers.`
- **作用**：特效从兵器、手掌、脚下长出来，跟着动作轨迹走，动作停了特效才散。凭空出现的特效像后期贴图。
- **用 / 不用**：挥砍、出掌、踏地。
- **生成**：稳。

### 尺度证明 Prove the scale
- **写法**：`The sword formation fills the upper two-thirds of the sky; beneath it, the city walls look like a toy, and she is a small figure on the tower.`
- **作用**：大场面要给参照物：特效占画框多少、旁边有什么已知大小的东西、人物在画面里多大。只写「巨大的」「铺天盖地」，模型给的往往是人物身边的一团光。
- **用 / 不用**：法阵、法相、巨兽、天象。
- **生成**：稳。人物缩到画面下方的远景，脸会糊，脸部镜头另出。

### 法阵 Formation
- **写法**：`A ring of glowing runes spreads flat across the ground beneath him, then lifts into three stacked layers, the inner ring turning clockwise and the outer ring counter-clockwise.`
- **作用**：平面符纹 → 立体分层 → 层与层反向旋转；成型过程本身就是蓄力。
- **用 / 不用**：大招前的蓄势；同一场只用一套阵，复用时外观逐字一致。
- **生成**：稳到定帧。符文细节会乱码，阵的形状用参考图锁，符文只要「像文字」不要可读。

### 法相与巨像 Avatar
- **写法**：`Behind her, a translucent golden giant rises to ten times her height, mirroring her stance; when she raises her hand, it raises its hand.`
- **作用**：角色身后的巨大投影，动作与角色同步；和召唤巨兽不同，法相跟着人动。
- **用 / 不用**：终极招式、觉醒。
- **生成**：稳。写清和本体同步，不写的话巨像会自己乱动。

### 色彩对冲 Color clash
- **写法**：`Her cold blue frost meets his orange fire in the middle of the frame; where they collide, white steam bursts outward.`
- **作用**：双方各一个主色，冷对暖；碰撞处给第三种颜色或白。阵营多时一方一色，全场不串。
- **用 / 不用**：对决、群战。
- **生成**：稳。

### 手绘化 Match the style
- **写法**：`The fire is drawn in flat orange shapes with dark ink outlines and hand-drawn smoke curls, matching the 2D look of the characters.`
- **作用**：2D、水墨、国漫风里，特效要跟人物同一种画法：平涂、描边、笔触、有限帧；不然人物是手绘的，特效是写实粒子，像两部片子叠在一起。
- **用 / 不用**：非写实画风的所有特效。写实片反过来，特效要有真实的物理质感。
- **生成**：稳。

---

## 5. 受击与反馈

### 命中定格 Hit-stop
- **写法**：`On impact, everything freezes for a split second: his fist buried in the man's side, the sweat spray suspended in the air. Then motion resumes.`
- **作用**：命中瞬间停住两三帧，是「打到了」的证据。轻击短停，重击长停，终结一击停得最久；所有命中停一样长等于都没停。
- **用 / 不用**：每个回合的决定性一击。
- **生成**：后期。写进提示词能提示模型放慢，准确的停顿在剪辑里补帧。

### 环境反馈 World reacts
- **写法**：`The kick misses and smashes the wooden table behind him; splinters spray toward the camera and the hanging lamp swings.`
- **作用**：打空的也要有结果，打中的更要有：碎物、扬尘、震动、灯摇。环境是力量的放大器。
- **用 / 不用**：每场至少一两处；全程都炸会麻木。
- **生成**：稳。

### 方向性震屏 Directional shake
- **写法**：`On the impact the camera jolts once to the right, in the direction of the blow, then settles.`
- **作用**：摄影机顺着受力方向震一下，再稳住；比全程手持乱晃更有冲击。
- **用 / 不用**：重击、爆炸、落地。
- **生成**：稳到后期。模型可能晃过头，晃动也可以后期加。

### 合规转译 Safe for platform
- **写法**：`The blade passes through him and he freezes, then collapses as a shockwave of dust spreads from where he stood.`
- **作用**：断肢、喷血、伤口特写在多数平台过不了审，也容易让模型生成失败。改成气浪、火花、碎裂的器物、定格后倒下、画外声音。观众读到的力量不减。
- **用 / 不用**：所有要上平台的作品；用户明确要求写实暴力且平台允许时另说。
- **生成**：稳。

## 来源

见 `camera/sources.md`。
