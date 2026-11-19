# 器材与格式

AIGC 里，器材名是提示词锚点：模型通过器材名推断一组画面特征。这一篇把器材翻译成画面特征，回答三件事：某种器材 / 格式给画面带来什么、提示词怎么写、模型认不认。

**不涉及实拍选型。** 这里不讲采购、租赁、配置清单、参数设置。用户问「该买什么镜头 / 用什么机器」时，先说明 AIGC 不需要买器材，再问他想要的是哪种画面，把它翻译成本篇的特征写法；用户坚持要实拍建议，按 SKILL.md 的实拍规则处理。

## 0. 先读这几条

1. **先写特征，型号只做锚点。** `16mm film` 之外写「粗颗粒、暗部发闷、高光柔和地溢开」。模型对型号的理解不稳定，同一个型号在不同模型里给出的画面差得很远，画面特征是可以检查的（`video-prompt/anatomy.md` 风格段）。
2. **一片一套介质。** 格式和介质写进全局的质感句，所有镜头逐字复用（`craft/visual/06-texture.md`）。混用要有理由：闪回用 Super 8、监控画面用 CCTV，而且全片每次都用同一套。
3. **器材词不能和画面别的部分打架。** 写了 `IMAX 65mm` 又写 `shaky phone footage`；写了 `macro` 又写 `wide establishing shot`。冲突时，模型会随机取一个。
4. **画幅不写进提示词。** 2.39:1、16:9、9:16 是交付参数，在生成设置里选（`craft/visual/06-texture.md`）。变形镜头写它的光学后果，不写画幅比。
5. **运动器材见运镜词典。** 手持、斯坦尼康、摇臂、航拍、FPV、身体固定都在 `camera/lexicon-move.md`；这里只补那里没有的几种，其余列速查（§1）。

条目字段同 `camera/index.md`：写法、作用、用 / 不用、生成、失败、短剧。生成可靠性分级同那一篇（稳 / 定帧 / 后期）。

---

## 1. 支撑与运动器材

已在运镜词典里的，只列去哪查：

| 器材 | 画面上的标志 | 词条 |
|---|---|---|
| 三脚架 / 锁死机位 | 画框一动不动 | `camera/lexicon-move.md` 固定机位 |
| 手持 | 呼吸式的轻晃，跟人走 | `camera/lexicon-move.md` 手持；`video-prompt/camera-behavior.md` §2 |
| 斯坦尼康 / 稳定器 | 平滑漂浮，能穿门过廊 | `camera/lexicon-move.md` 稳定跟随 |
| 摇臂 / 升降 | 垂直升降，越过人群或墙头 | `camera/lexicon-move.md` 升、降 |
| 身体固定 | 人物不动、背景在晃 | `camera/lexicon-move.md` 身体固定 |
| 航拍 / FPV | 大范围升起；高速穿行 | `camera/lexicon-move.md` §4 |
| 监控 / 车载记录仪 | 高角、广角、低画质、固定 | `video-prompt/camera-behavior.md` 监控视角 |

### 滑轨微移 Slider
- **写法**：`A slow, short slider move from left to right past the coffee cup, revealing her at the window behind it; the move is barely a foot long.` B: `slow slider move, short lateral glide, subtle parallax`
- **作用**：小幅、匀速的横移或推近，前景和背景之间产生一点视差。画面活了，又不打扰戏。适合产品、静物、安静的情绪镜头（行业惯例）。
- **用 / 不用**：插入镜、物件镜、呼吸镜；想要「有一点动」但不想要运镜存在感时用。人物快速移动时不用，跟不上。
- **生成**：稳。写清「短」和「慢」，否则会变成大幅横移。
- **失败**：移得太远、太快，或者变成环绕。写幅度（`barely a foot`、`a few inches`）和终点。
- **短剧**：`tracking`（小幅横移），或 `push_in`。

### 车载 Car mount / camera car
- **写法**：`Camera mounted on the hood, facing back through the windshield at him driving at night; streetlights slide across his face in a steady rhythm.` B: `hood-mounted camera, through windshield, streetlights passing over face`
- **作用**：机位和车一起动：人物在画框里稳定，窗外的光和景在流动。观众坐在车里（行业惯例）。
- **用 / 不用**：车内对话、夜路独白、逃亡。并排跟车的外景改写成横移或航拍。
- **生成**：稳（车内）；车外跟拍 定帧，车身和道路容易变形。
- **失败**：车停在原地、背景不动，或者窗外的光不规律地乱闪。写「光以稳定的节奏扫过」和「窗外的景向后流动」。
- **短剧**：`static`（机位相对人物不动），在 `text` 里写车在行驶。

### 索道摄像机 Cable cam
- **写法**：`A high overhead camera glides in a straight line above the stadium crowd, smoothly tracking the runner below.` B: `cable cam, high overhead straight glide, smooth`
- **作用**：高位、直线、匀速的长距离滑行，比航拍更稳、更低。适合俯瞰人群、球场、街道（行业惯例）。
- **用 / 不用**：体育、集会、仪式；要「从上方一路跟着」时用。要升降或转弯，改用航拍。
- **生成**：定帧。模型常把它变成航拍或升降；用首尾帧锁住起点和终点。
- **失败**：变成拉升、或者转起弯来。写「直线、高度不变」。
- **短剧**：`tracking` 加 `angle` 俯；竖屏基本不用。

---

## 2. 镜头

焦段、鱼眼、移轴、分屈光、焦点转移已经在 `camera/lexicon-shot.md` §6–§7。这里补焦外、光学瑕疵和特殊镜头。

### 变形宽银幕镜头 Anamorphic
- **写法**：`Anamorphic lens look: oval bokeh in the background lights, a thin horizontal blue flare streaking across the frame from the headlights, slight barrel distortion at the edges.` B: `anamorphic, oval bokeh, horizontal lens flare, edge distortion`
- **作用**：镜头横向压缩再展开，带来三个可见特征：椭圆焦外、横向拉长的炫光、边缘轻微桶形畸变。观众读到的是「大银幕故事片」（《导演的摄影课》第三章；`craft/visual/03-lens.md`）。
- **用 / 不用**：夜景、霓虹、车灯、灯笼、烛火这些有点光源的戏，特征最明显。白天平光的戏，特征看不出来，只剩空词。炫光的颜色跟着光源走：车灯偏蓝白，灯笼和烛火写 `a warm amber horizontal flare`；写清炫光从哪个光源出来，长度和位置模型控制不准，要准就定帧。
- **生成**：稳（写出三个特征时）；只写 `anamorphic` 或 `cinematic lens`，效果随机。
- **失败**：炫光满屏、每个镜头都有；或者模型直接把画面做成黑边宽银幕。只在有点光源的镜头写炫光；画幅在生成设置里选，不写进提示词。
- **短剧**：竖屏里横向炫光会被截断，少用；写进全局 `style`。

### 老镜头 Vintage lens
- **写法**：`Shot through an old lens: soft edges, lower contrast, gentle glow around the highlights, and a slightly swirling background blur.` B: `vintage lens, soft edges, low contrast, highlight glow, swirly bokeh`
- **作用**：边缘软、反差低、高光发晕、焦外打旋。画面带着年代感和柔光，人物像被回忆包着（行业惯例）。
- **用 / 不用**：回忆、年代戏、温情；要「不那么锐」的数字画面时用。悬疑、科幻、广告产品镜头不用：锐度是那些片子的信息。
- **生成**：稳（软、低反差、发晕）；旋转焦外 定帧，模型常常不做。
- **失败**：变成整片糊，或者只加一个复古滤镜。写清「中心清楚，边缘软」。
- **短剧**：写进全局 `style`。

### 微距 Macro
- **写法**：`Extreme macro: a single drop of ink spreading into the wet paper fibres, the fibres sharp, everything else melting into blur.` B: `macro lens, extreme close-up, razor-thin focus`
- **作用**：把很小的东西拍成一整个世界：纸的纤维、眼睫上的水珠、昆虫的复眼。景深极浅，只有一条线是清楚的（行业惯例）。
- **用 / 不用**：物件细节、母题物件、转场里的质感镜头；能给一个普通物件分量。需要交代空间的镜头不用。
- **生成**：稳。静物和慢动作最好；手部和人脸的微距容易出皮肤伪影。
- **失败**：景深写深了，看不出是微距；或者主体变形。写「只有某一处清楚」。
- **短剧**：`size` 取 `extreme_close`。

### 探针镜头 Probe lens
- **写法**：`A probe lens creeps along the tabletop at ant height, past the toppled salt shaker and between the plates, toward his hand.` B: `probe lens, ground-level macro travel, wide close perspective`
- **作用**：镜头钻进很小的空间里移动：贴着桌面、穿过缝隙、钻进物件之间，近处的东西被夸张放大，又带着广角的纵深（行业惯例）。
- **用 / 不用**：微观视角的开场、物件之间的揭示、把普通场景变陌生。只是要一个特写时，用微距就够。
- **生成**：定帧。路径和终点要用首尾帧锁；文生常常变成普通微距或普通推近。
- **失败**：镜头穿过了固体，或者物件尺寸前后不一。写清路径经过哪几样东西。
- **短剧**：`push_in` 加 `size` `extreme_close`，在 `text` 里写路径。

### 柔光滤镜 Diffusion filter
- **写法**：`A soft diffusion filter look: highlights bloom gently, skin softened, a faint halo around the window light; blacks slightly lifted.` B: `diffusion filter, highlight bloom, soft halation, lifted blacks`
- **作用**：高光柔和地溢开、皮肤变柔、暗部微微抬起。画面变温柔、变梦，或变得像旧照片（行业惯例；`craft/visual/06-texture.md` 柔化）。
- **用 / 不用**：爱情、回忆、梦境、人像；也用来压住 AI 画面过分锐利的质感。追逐、动作戏不用，会显得软。
- **生成**：稳。
- **失败**：溢光过量，整片发灰。写「轻微」「只在高光处」。
- **短剧**：写进全局 `style`；漫剧不用。

---

## 3. 快门与帧率

快门决定运动模糊的长短，帧率决定动作的流畅程度。升格慢动作、快动作、变速、延时在 `camera/lexicon-move.md` §5。

### 窄快门 Narrow shutter / staccato
- **写法**：`Crisp, staccato motion with almost no motion blur: each spray of dirt and each swing of the arm looks frozen and jittery, like a narrow shutter.` B: `narrow shutter, no motion blur, staccato, crisp motion`
- **作用**：运动模糊几乎消失，动作一顿一顿、碎而脆。观众感到紧张、生硬、不舒服，常用在战争和打斗里（行业惯例：45° 或 90° 快门）。
- **用 / 不用**：战场、混乱、爆发的打斗、雨和沙这类颗粒飞溅的画面。抒情和慢节奏的戏不用。
- **生成**：后期。模型对运动模糊的控制很弱，文字偶尔有效；稳妥的做法是剪辑或后期处理（抽帧、去模糊）。
- **失败**：模型照样加上了自然的模糊，或者把它理解成卡顿掉帧。先生成正常素材，在后期做。
- **短剧**：基本不用。

### 拖影 Smear / step-printing
- **写法**：`Smeared motion: the crowd streaks into long trails of colored light while she stands still and sharp in the middle.` B: `motion smear, long trails, step-printed look, subject sharp`
- **作用**：运动拖成长长的色带，人物在中间清楚，周围的世界在流。观众读到的是失神、狂喜、时间被抽走（行业惯例：慢快门加抽帧印片）。
- **用 / 不用**：都市夜景里的孤独、醉、心动的一瞬、记忆闪回。叙事信息密集的镜头不用，观众看不清。
- **生成**：后期。拖影可以用文字近似，但「人物清楚、背景拖影」的分离要靠后期合成，或者用慢门效果的首帧。
- **失败**：整个画面都糊，人物也拖了。主体和背景分开生成或合成。
- **短剧**：基本不用。

---

## 4. 格式与介质

介质的画面特征只写一次，放进全局的质感句，全片复用（`craft/visual/06-texture.md` 五项：介质、颗粒、反差、柔化、空气）。

### Super 8 / 8mm 胶片 Super 8 film
- **写法**：`Super 8 home-movie look: heavy grain, warm faded colors, soft focus, slight gate weave and flicker, light leaks burning in at the edge.` B: `Super 8 film, heavy grain, faded warm color, gate weave, flicker, light leaks`
- **作用**：粗颗粒、褪色的暖调、画框轻微晃动、闪烁、漏光。观众读到的是家庭录像、童年、回不去的过去（行业惯例；《导演的摄影课》论画幅与格式：小画幅颗粒粗、反差高）。
- **用 / 不用**：闪回、回忆、家庭影像、片中片。全片都用会累，适合当作和「现在」区分的那一层。
- **生成**：稳。漏光和闪烁的强度不好控，写「轻微」。
- **失败**：变成泛黄的照片滤镜，没有运动特征。写晃动和闪烁。
- **短剧**：闪回段落可用，写进那一段的 `text`。

### 16mm 胶片 16mm film
- **写法**：`16mm film: visible coarse grain, muted colors, soft highlights rolling off gently, slightly murky shadows.` B: `16mm film, coarse grain, muted color, soft highlight rolloff`
- **作用**：可见的颗粒、偏闷的色彩、柔和的高光过渡。观众读到的是独立电影、纪实、粗粝的真实（行业惯例）。
- **用 / 不用**：现实题材、成长、纪录风格的剧情片。要光鲜、锐利的商业感时不用。
- **生成**：稳。
- **失败**：颗粒每镜不同。质感句逐字复用。
- **短剧**：写进全局 `style`。

### 35mm 胶片 35mm film
- **写法**：`35mm film: fine natural grain, rich but not oversaturated color, smooth highlight rolloff, gentle halation around bright lights.` B: `35mm film, fine grain, smooth highlight rolloff, halation`
- **作用**：细颗粒、饱满而不过分的色彩、平滑的高光过渡、亮处轻微的光晕。这是「故事片」的默认质感（行业惯例）。
- **用 / 不用**：大多数剧情片都可以作为默认。只写 `35mm` 不写特征，模型会给一个通用复古滤镜。
- **生成**：稳。
- **失败**：变成泛黄滤镜。写颗粒、高光过渡和光晕，不写「复古」。
- **短剧**：写进全局 `style`。

### 大画幅 65mm / IMAX Large format
- **写法**：`Large-format 65mm look: extremely fine detail, almost no grain, deep tonal range, the landscape stretching sharp all the way to the horizon.` B: `large format 65mm, ultra fine detail, no grain, wide tonal range`
- **作用**：几乎没有颗粒、细节极多、层次很宽。画面显得辽阔、庄重（《导演的摄影课》论格式：大画幅负片颗粒细、层次多）。
- **用 / 不用**：风景、史诗、太空、大场面。私密的小戏用它反而显得空。
- **生成**：稳，但效果轻：和普通高清画面差别不大，主要靠「辽阔」的构图撑。
- **失败**：被理解成过度锐化的 AI 质感。写「细节多但不锐利，层次宽」。
- **短剧**：不用。

### 黑白胶片 Black-and-white film
- **写法**：`Black-and-white film: deep blacks, bright clean whites, a full range of silver grays in between, fine grain.` B: `black and white film, deep blacks, rich gray scale, fine grain`
- **作用**：去掉颜色，画面只剩光和形状。观众读到的是年代、记忆、冷峻，或者把注意力全放在脸和光上（行业惯例）。
- **用 / 不用**：年代戏、回忆、冷峻的悬疑；某一段落和全片区分。只为「高级感」而用，会显得空。
- **生成**：稳。
- **失败**：灰蒙蒙一片，没有真正的黑和白。写「深黑、亮白、中间灰阶丰富」。
- **短剧**：闪回段落可用。

### 录像带 VHS
- **写法**：`VHS tape look: soft low resolution, color bleeding at the edges of red objects, horizontal tracking lines rolling through, slight wobble in the image.` B: `VHS, low resolution, chroma bleed, tracking lines, tape wobble`
- **作用**：分辨率低、颜色往外渗、横向滚动的干扰线、画面轻微抖。观众读到的是 80–90 年代、家庭录像、发现的录像（行业惯例）。
- **用 / 不用**：伪纪录片、恐怖片的「找到的录像」、年代回忆。不能当作每个镜头的质感，观众看不清信息。
- **生成**：稳。屏幕角落的日期时间码是字：后期加。
- **失败**：模型画出了乱码的时间码。提示词里不写时间码，后期叠。
- **短剧**：片中片、监控回放可用。

### DV 摄像机 Consumer camcorder
- **写法**：`Early-2000s consumer camcorder footage: sharp but flat video look, harsh clipped highlights, oversaturated colors, auto-focus hunting, slight handheld zoom.` B: `2000s camcorder, video look, clipped highlights, oversaturated, autofocus hunting`
- **作用**：锐而平的视频感、高光一过曝就死白、色彩偏艳、自动对焦来回找。观众读到的是 2000 年代的家庭影像和业余记录（行业惯例）。
- **用 / 不用**：成长回忆、伪纪录、青春片的片中片。
- **生成**：稳。
- **失败**：被做成高清画面。写「平」「高光死白」「对焦来回找」。
- **短剧**：片中片可用。

### 手机竖拍 Phone footage
- **写法**：`Vertical phone footage: wide lens, everything in focus, auto-exposure jumping when she turns toward the window, slight handheld wobble.` B: `phone footage, vertical, wide lens, deep focus, auto exposure shift, handheld`
- **作用**：广角、几乎全清晰、曝光会跳、手持晃动。观众读到的是「有人正在用手机拍」：现场、私人、社交媒体（行业惯例）。
- **用 / 不用**：片中的录像、直播、视频通话、社交媒体画面；竖屏短剧的伪直播段落。要电影感时不用。
- **生成**：稳。屏幕界面和文字后期加。
- **失败**：被拍成浅景深的电影画面。写「全清晰、广角」。
- **短剧**：直播、视频通话段落可用。

### 运动相机 Action camera
- **写法**：`Action camera strapped to his chest: ultra-wide view with curved edges, his hands at the bottom of the frame, the bike path rushing toward the lens.` B: `action camera, ultra wide, curved edges, chest mount POV`
- **作用**：超广角、边缘弯曲、贴身固定。观众被绑在人物身上，速度感和身体感放大（行业惯例）。
- **用 / 不用**：极限运动、追逐、跌落、第一人称的冲刺。
- **生成**：稳（构图和畸变）；高速运动中的细节容易糊。
- **失败**：变成普通主观镜头，没有畸变。写「边缘弯曲」和固定的位置。
- **短剧**：`handheld` 加主观镜头，在 `text` 里写固定在哪。

### 数字电影机 Digital cinema camera
- **写法**：`Clean digital cinema image: low noise, wide latitude holding detail in both the bright window and the dark corner, natural skin tones, highlights rolling off softly.` B: `digital cinema camera, clean, low noise, wide dynamic range, soft highlight rolloff`
- **作用**：干净、噪点少、宽容度大（亮处和暗处都有细节）、肤色自然、高光过渡柔和。这是当代剧集和广告的默认质感（行业惯例）。
- **用 / 不用**：大多数当代题材都可作默认。品牌和型号（如 ARRI Alexa）可以加在后面作锚点，但特征写在前面（`video-prompt/anatomy.md` 风格段）。
- **生成**：稳。
- **失败**：变成过度锐化、过度饱和的 AI 质感。写「干净但不锐利」「高光柔和」。
- **短剧**：写实画风的默认，写进全局 `style`（`drama/10-look.md`）。

---

## 5. 调色风格

调色风格的名字只是入口，模型对 `bleach bypass`、`cross-processed` 这类词的理解差别很大。每种风格都要写成三项：**色相**（高光、中间调、阴影各偏什么色）、**饱和度**、**反差**（黑有多深、高光多硬）。全片一套，写进全局的色彩句并逐字复用（`craft/visual/05-color.md`）；换风格只用来区分时间层或世界。生成时写特征就能大致做到，要全片完全统一靠后期。

| 风格 | 写成什么：色相 · 饱和 · 反差 | 用在 | 生成 |
|---|---|---|---|
| 漂白旁路 Bleach bypass | 颜色被洗掉一半，带银灰；饱和低；反差高，黑很深，高光发硬，颗粒重 | 战争、冷硬犯罪、精神崩坏 | 稳（写特征）；精确效果后期 |
| 低饱和 Desaturated | 色相还在但褪向灰；饱和低；反差中 | 压抑、冬天、灰色的现实 | 稳 |
| 高饱和 Saturated | 原色鲜亮，肤色仍自然；饱和高；反差中高 | 童话、喜剧、广告、梦 | 稳；肤色容易发橙，写「肤色自然」 |
| 冷蓝 Cool blue | 阴影和中间调偏蓝青，肤色微冷；饱和中低 | 孤独、夜、医院、科技 | 稳 |
| 暖琥珀 Warm amber | 中间调偏琥珀金，阴影是暖棕；饱和中 | 回忆、怀旧、乡村午后、烛光 | 稳 |
| 褪色胶片 Faded film | 黑位抬起成灰，高光偏奶黄，整体轻微偏色；饱和低；反差低 | 回忆、家庭影像、旧照片感 | 稳 |
| 交叉冲印 Cross-processing | 色相错位：高光偏黄绿，阴影偏青蓝，肤色发怪；饱和高；反差高 | 迷幻、MV、90 年代时尚 | 稳（色相）；程度难控，后期收 |
| 日拍夜 Day for night | 白天的光压暗成蓝调，硬阴影还在，天空压成深蓝黑；饱和低 | 古典的月夜质感 | 后期更可控；只要夜景就直接写夜景，要古典味才写这些特征 |
| 分离色调 Split toning | 高光一种色、阴影另一种色（如高光暖金、阴影墨绿）；饱和中低 | 风格化的类型片，给全片一个色彩签名 | 稳（写清两色） |
| 褐色 Sepia | 单一棕色调，没有别的颜色；反差中低 | 旧照片、年代开场 | 稳 |
| 过曝 Blown-out high key | 高光大片溢白，暗部只到浅灰；饱和低 | 梦、天堂、闪回、濒死 | 稳 |
| 黑白 | 见 §4 黑白胶片 | | |
| 青橙 Teal and orange | 肤色和暖光推向橙，阴影和背景推向青；饱和中高；反差高 | 动作大片，有意要这种商业感时 | 稳。模型的默认色就往这里漂：有意要时写清两色分工和强度，不是有意的就在约束句里排除（`craft/visual/05-color.md`） |

写法示例：`Bleach-bypass look: colours half washed out to a silvery grey, deep crushed blacks, hard highlights, heavy grain.` B: `bleach bypass, desaturated silver, crushed blacks, hard highlights, heavy grain`

---

## 6. 光学与画面效果

模拟镜头、胶片或合成带来的画面效果。多数在生成里能画出来，但程度不稳，要精确就后期做。

### 双重曝光 Double exposure
- **写法**：`Double exposure: the silhouette of her profile filled with a pine forest, the trees fading out where her hair ends, the rest of the frame plain white.` B: `double exposure, profile silhouette, forest inside silhouette, white background`
- **作用**：把两个画面叠成一个：人和他心里的地方、现在和过去。比叠化更像一张图，常用于片头、回忆和海报感的段落。
- **用 / 不用**：片头、回忆、人物与地点的关系。叙事段落里少用，观众要停下来读图。
- **生成**：定帧。先出静帧，再让里面的东西轻微动；两层都要动就后期合成。
- **失败**：两张图糊成一团，看不清轮廓。写清哪一层是外形（剪影）、哪一层填在里面、其余留白。
- **短剧**：片头或回忆标题卡可用，后期做。

### 暗角 Vignette
- **写法**：`A soft dark vignette closing in from the corners, the centre of the frame where she sits staying bright.` B: `soft vignette, dark corners, bright centre`
- **作用**：四角压暗，视线被推向中间；也带出老镜头、旧照片、窥视的感觉。
- **用 / 不用**：回忆、老照片、窥视、孤立一个人。全片都加会显得廉价。
- **生成**：稳。程度要精确就后期加。
- **失败**：暗角太重像加了滤镜。写 `soft`、`subtle`。
- **短剧**：回忆段落可用，后期统一加。

### 漏光 Light leak
- **写法**：`A warm orange light leak washing in from the right edge, flaring across the frame and fading out.` B: `light leak, warm orange, edge flare`
- **作用**：胶片相机漏进的光，暖色从画边涌进来又退掉。带来手工、私人、旧胶片的感觉，也能当转场。
- **用 / 不用**：回忆、家庭影像、MV、青春片的段落转换。写实正片里不用。
- **生成**：稳（静态的一片漏光）；涌进再退掉的时间变化不稳，后期叠素材更可控。
- **失败**：变成普通的镜头炫光。写颜色、从哪边进、形状不规则。
- **短剧**：段落转换可用，后期叠。

### 强制透视 Forced perspective
- **写法**：`Forced perspective: the woman in the foreground holds out her open palm, and the tiny-looking temple far behind her appears to sit right on it.` B: `forced perspective, foreground hand, distant temple appears on palm`
- **作用**：利用远近让大小错位：人托住远处的塔、巨人和小人同框。读起来是童趣、幽默、魔法。
- **用 / 不用**：喜剧、童话、广告的视觉玩笑；巨人与常人同框。
- **生成**：定帧。先出对齐好的静帧；一动，错位就容易穿帮，镜头尽量不动。
- **失败**：模型把远处的东西真的画小了放在手上。写清楚它在远处、只是「看起来」在手上。
- **短剧**：不常用。

### 故障效果 Glitch
- **写法**：生成干净的画面，剪辑时加像素错位、色彩通道分离、画面撕裂。提示词里可以写 `digital glitch, RGB channel split, pixel tearing` 作静帧质感。B: `glitch, RGB split, datamosh, pixel tearing`
- **作用**：数字信号坏掉：监控被入侵、人物神经错乱、虚拟世界出错、赛博朋克。
- **用 / 不用**：科技惊悚、赛博朋克、恐怖、片中片的信号中断。只当炫技用会遮住信息。
- **生成**：后期。生成出来的故障是固定的纹理，不会按节奏闪；故障要卡在剧情点上，剪辑时加。
- **失败**：画面通篇花掉，看不清人。故障只在几帧里出现。
- **短剧**：反转、系统出错的段落可用，后期加。

### 画幅切换 Aspect ratio change
- **写法**：提示词不写画幅。分段生成，剪辑时加黑边或撤掉黑边，从窄画面打开成宽画面（或反过来）。
- **作用**：画面突然变宽，世界被打开；变窄，人物被关起来。也用来区分时间层或片中片。
- **用 / 不用**：人物走进一个新世界、从回忆回到现在、高潮打开。一部片里用一两次。
- **生成**：后期。画幅在生成设置里选（§0），切换在剪辑里做。
- **失败**：几个镜头画幅随机不同。全片画幅只在设计好的点上变。
- **短剧**：竖屏不换画幅。

### 其他视觉噱头

| 效果 | 画面是什么 | 生成 |
|---|---|---|
| 狭缝扫描 Slit-scan | 画面拉成流动的光线和色带，像穿过时空隧道 | 后期 |
| 万花筒 Kaleidoscope | 画面被镜像成对称的花样，旋转 | 后期（静帧可定帧） |
| X 光 X-ray | 半透明的骨骼和轮廓，黑底蓝白 | 稳（静帧） |
| 热成像 Thermal | 人体红黄发亮，环境蓝紫，没有细节 | 稳 |
| 夜视 Night vision | 单色绿，颗粒重，眼睛反光 | 稳 |
| 红外 Infrared | 树叶变白或粉红，天空发黑 | 稳 |
| 抖动立体 Wigglegram | 两三个视角来回切，制造立体感 | 后期 |
| 西洋镜 Peephole / zoetrope | 圆孔或缝里看到的画面，四周全黑 | 稳（遮罩可后期加） |
| 分身 Clone | 同一个人在同一画面里出现两次或更多 | 定帧（参考图锁脸）；动起来容易串脸，可分层合成 |
| 悬浮 Levitation | 人或物体浮在空中，有阴影落在地面 | 稳（静帧）；浮起的过程定帧 |
| 混合媒介 Mixed media | 实拍和手绘、拼贴、动画元素同框 | 定帧；手绘层要统一就后期合成 |

---

## 7. 混用与一致性

| 情况 | 做法 |
|---|---|
| 全片一种介质 | 质感句写一次，全片逐字复用；模式 B 用同一个 TEXTURE 块 |
| 闪回 / 回忆换介质 | 换的那一层全片固定（每次闪回都是 Super 8），并至少改两项（颗粒、色彩、焦外、声音），观众才分得开（`writing/devices.md` 闪回） |
| 片中片（录像、监控、直播） | 用 VHS、DV、手机、监控，界面和文字后期加；切回正片时介质要明显变回来 |
| 器材词和运镜冲突 | 删一个：大画幅不配手机晃动，微距不配全景，车载不配环绕 |
| 有参考图 | 首帧已经决定了介质，运动提示词里不重复颗粒和质感（`craft/visual/06-texture.md`） |
| 介质层和镜头特征叠在一起 | 介质层优先：回忆段用 Super 8，就不再叠变形镜头的炫光（家庭录像不会有宽银幕镜头），除非有意做反差；正片层的镜头特征不带进回忆层 |
| 想知道某个模型做不做得到 | 这里的分级是通用经验，不点名模型；排进流程前跑一条小样（`references/aigc/models.md`） |

## 8. 常见错误

| 错误 | 改法 |
|---|---|
| 只写型号（`ARRI Alexa`、`Kodak`） | 先写它带来的特征，型号放后面或删掉 |
| `cinematic lens`、`film look` | 写具体特征：椭圆焦外、横向炫光；颗粒、高光过渡 |
| 每场换一种介质 | 全片一套；换介质只用来区分时间层或片中片 |
| 把画幅比写进提示词 | 画幅在生成设置里选 |
| 让模型画时间码、录像界面 | 后期叠加 |
| 写了快门角度，期待模型照做 | 运动模糊在后期处理 |
| 只写调色风格名（`bleach bypass`、`cinematic grade`） | 写成色相、饱和、反差三项（§5） |

## 来源

见 `camera/sources.md`。
