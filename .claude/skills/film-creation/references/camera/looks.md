# 类型影调卡：一种类型的画面长什么样

导演和摄影档案管的是「某个人的风格」；这一篇管的是「一类片子的画面」：黑色电影、武侠、赛博朋克……用户说「要那种武侠的感觉」「做成黑色电影」时，先读这里，再按需要加读对应档案。

字段与可靠性分级见 `camera/index.md`。每张卡：**视觉基元**（6–8 条，可以直接拆进光、色、运镜、构图、质感各段）、**写法**（模式 A 的风格句）、**作用**、**档案**（可借的导演 / 摄影档案，没有就写近邻）、**生成**、**失败**。

## 0. 怎么用

1. **类型名只做锚点，先写特征。** 只写 `film noir style`，模型给的是一张平均的「黑白 + 礼帽」海报；写「单一硬光、百叶窗影子、湿街反光」才可控。和器材名同理（`camera/lexicon-gear.md` §0）。
2. **取 3–5 条，不全用。** 视觉基元按这场戏挑：光和色进全局风格句（逐字复用），运镜和构图进逐镜；全部堆上去会变成拼贴。
3. **影调卡管画面，不管故事。** 类型的叙事约定见 `references/writing/genres/index.md`。一部片子可以是爱情类型、武侠影调。
4. **混搭以一张卡为主。** 主卡定光和色，副卡只借 1–2 条（例如「武侠 + 魔幻现实」：武侠的山雾与衣袂，魔幻现实的「奇事当平常事拍」）。规则同 `references/mixing.md`。
5. **画面里不要可读文字。** 赛博朋克、伪纪实最容易生成招牌和时间码的乱码，写成光和色块，或进总锁（`video-prompt/locks.md`）。

---

## 1. 经典与类型工艺

### 黑色电影 Film noir
- **视觉基元**：单一硬光、深黑阴影占画面大半；百叶窗或窗格投下的条纹影；夜里的湿街和反光；烟雾在光束里；低机位、广角让人物压在天花板下；黑白或接近黑白。
- **写法**：`Black-and-white night interior, a single hard light from frame left, venetian-blind shadows striping the wall and his face, cigarette smoke hanging in the beam, deep black shadows filling most of the frame.` B: `film noir | low key | hard single source | venetian blind shadows | black and white`
- **作用**：宿命、欺骗、被困；光只照到一部分人，另一部分永远在暗里。
- **档案**：`directors/orson-welles.md`、`directors/billy-wilder.md`；摄影 `cinematographers/gregg-toland.md`。
- **生成**：稳；模型爱把黑白做成灰平，要写「深黑、高反差」。
- **失败**：所有人都戴礼帽、穿风衣，像化装舞会。写光和影，服装按剧情。

### 新黑色 Neo-noir
- **视觉基元**：彩色，夜里的钠灯橙与霓虹冷色混光；阴影仍深；湿路面反射招牌颜色（不写字）；城市夜景、车内戏多；画面干净、冷。
- **写法**：`Night city in colour, sodium-orange streetlight mixed with cold cyan neon spill, deep shadows, wet asphalt reflecting coloured light, a clean and cold image.` B: `neo-noir | sodium vapor | neon spill | wet streets | deep shadows`
- **作用**：黑色电影的道德灰度，换到当代都市。
- **档案**：`directors/david-fincher.md`、`directors/jean-pierre-melville.md`；近邻 `directors/wong-kar-wai.md` 的霓虹。
- **生成**：稳。
- **失败**：变成赛博朋克。新黑色没有全息、没有未来建筑，城市是现在的。

### 德国表现主义 German Expressionism
- **视觉基元**：歪斜的、像画出来的布景（门窗不成直角）；墙上巨大的人影；极端俯仰；硬光明暗对照；黑白，或单色调染色；人物动作僵硬、造型化。
- **写法**：`A crooked, painted-looking street with leaning walls and slanted doorways, a giant hard shadow of the man thrown across the wall, extreme low angle, stark black-and-white chiaroscuro.` B: `german expressionism | distorted painted set | giant cast shadow | chiaroscuro`
- **作用**：内心的恐惧和疯狂外化成空间。
- **档案**：无直接档案；近邻 `directors/orson-welles.md` 的角度与阴影。
- **生成**：定帧；歪斜布景先出关键帧，视频只写运动，否则模型会把墙「扶正」。
- **失败**：只是黑白恐怖片。要写「布景本身是歪的」。

### 铅黄 Giallo
- **视觉基元**：大块饱和的红、蓝、绿彩色光，彼此不混；凶手的主观镜头和戴手套的手；眼睛大特写；突然的急推；华丽的室内、玻璃、镜子。
- **写法**：`A lavish apartment washed in saturated red light from one side and deep blue from the other, the colours not mixing, an extreme close-up of a frightened eye, a gloved hand at the edge of frame.` B: `giallo | saturated red and blue gels | extreme close-up eye | gloved hand`
- **作用**：恐惧被做得华丽，色彩本身就是威胁。
- **档案**：无直接档案；近邻 `cinematographers/dan-laustsen.md` 的饱和色光、`directors/pedro-almodovar.md` 的原色。
- **生成**：稳；模型会把红蓝混成紫，写「两种颜色不混，各占一侧」。
- **失败**：血腥过量。铅黄的重点是色彩和视点，不是伤口。

### 意式西部 Spaghetti western
- **视觉基元**：大远景与眼睛大特写直接相接；烈日、干土、热浪；长焦压缩；人物长时间不动、不说话；脸上的汗和尘；对峙时机位不动。
- **写法**：`Harsh midday sun over a dusty town, heat shimmer in the distance; cut to an extreme close-up of his squinting eyes, sweat and dust in the creases, he does not blink.` B: `spaghetti western | extreme wide to extreme close-up eyes | harsh sun | dust | telephoto`
- **作用**：等待和对峙被拉长，暴力之前的沉默。
- **档案**：`directors/sergio-leone.md`、摄影 `cinematographers/tonino-delli-colli.md`。
- **生成**：稳；大远景接大特写在剪辑里完成（`storyboard/continuity.md` 景别衔接里的「极端跳」）。
- **失败**：画幅写进提示词。宽银幕在生成设置里选。

---

## 2. 纪实与现代主义

### 伪纪实 Found footage
- **视觉基元**：人物自己拿着的消费级摄像机；自动对焦来回找焦；曝光跳变；镜头跟着人的呼吸晃，跑起来画面乱甩；夜视绿、闪光灯；画面里的人会看镜头、对镜头说话。
- **写法**：`Shot on a cheap handheld camcorder held by one of the characters, autofocus hunting, exposure jumping when he turns toward the window, the image shaking with his breathing.` B: `found footage | consumer camcorder | autofocus hunting | handheld shake`
- **作用**：「这是真的发生过的」；观众只能看到持机人看到的。
- **档案**：无；器材写法见 `camera/lexicon-gear.md` 的 DV、手机、运动相机。
- **生成**：稳；时间码、录制标识会生成成乱码，后期加，提示词里写 `no on-screen text or timestamp`。
- **失败**：画面太好看、构图太准。要允许切掉头、对焦失败。

### 真实电影 Cinéma vérité
- **视觉基元**：肩扛跟随，像在旁边观察；只有现场的自然光；变焦推近去找表情；构图不完美，人会挡住镜头；没有配乐。
- **写法**：`Observational handheld camera at shoulder height, available light only, the lens zooms in slowly to find her face; someone walks through the foreground and blocks the frame for a second.` B: `cinema verite | observational handheld | available light | zoom to find face`
- **作用**：像在场，不像在看戏。
- **档案**：`directors/john-cassavetes.md`、`directors/wang-bing.md`、`directors/ken-loach.md`。
- **生成**：稳。
- **失败**：晃得太厉害，变成伪纪实。真实电影的摄影机是冷静的旁观者，不是剧中人。

### 法国新浪潮 French New Wave
- **视觉基元**：街头实景、自然光；黑白为主；轻便手持在街上跟着人走；跳切；人物偶尔直视镜头；随性、年轻、不讲究「完美」。
- **写法**：`Black-and-white street in daylight, natural light, a light handheld camera walks backwards in front of the couple as they talk; passers-by glance at the lens.` B: `french new wave | black and white | street | natural light | handheld walking`
- **作用**：自由、即兴、打破规则。
- **档案**：`directors/jean-luc-godard.md`、`directors/agnes-varda.md`、`directors/eric-rohmer.md`。
- **生成**：稳；跳切在剪辑里做（`camera/lexicon-transition.md`）。
- **失败**：只剩黑白滤镜。要有街头、自然光和走动。

### 纪录片质感 Documentary look
- **视觉基元**：观察式机位、自然光、真实地点的杂乱；采访式构图（人物偏一侧、视线看画外的提问者）；稍长的镜头；声音粗糙。
- **写法**：`Interview framing: she sits slightly left of centre, looking just off camera to the right at an unseen interviewer, natural window light, the real clutter of her kitchen behind her.` B: `documentary look | interview framing | natural light | real location clutter`
- **作用**：可信，像真人真事。
- **档案**：`directors/wang-bing.md`、`directors/agnes-varda.md`、`directors/abbas-kiarostami.md`。
- **生成**：稳。
- **失败**：背景被「美化」得太干净。写出真实的杂物。

### 艺术片质感 Arthouse
- **视觉基元**：固定长镜头；大面积负空间，人物很小；自然光、低饱和；镜头在人物离开后还停留；节奏慢，动作少。
- **写法**：`A long static wide shot, the figure small in the lower corner of a vast grey field, flat natural light, muted colour; after she walks out of frame the camera keeps watching the empty field.` B: `arthouse | long static take | negative space | muted palette | natural light`
- **作用**：让观众自己看、自己想；时间本身成为内容。
- **档案**：`directors/andrei-tarkovsky.md`、`directors/tsai-ming-liang.md`、`directors/nuri-bilge-ceylan.md`。
- **生成**：稳；长镜头的时长受模型上限限制，见 `video-prompt/one-take.md`。
- **失败**：只是慢。每个长镜头里要有一件在变化的事（光、风、一个动作）。

---

## 3. 亚洲与神话

### 武侠 Wuxia
- **视觉基元**：山间雾气、竹林、松、瀑布、客栈；风吹衣袂和发带；人物腾空时的低机位仰拍；长焦隔着枝叶看打斗；兵器反光；客栈里灯笼和烛火的暖光对窗外冷月；色彩可以是水墨般的灰青，也可以是大块纯色（一场一色）。
- **写法**：`A misty bamboo forest at dawn, pale grey-green light filtering through the stalks, wind pulling at her robe and hair ribbon; low angle as she pushes off a bamboo stem, the stem bending under her weight and springing back.` B: `wuxia | misty bamboo forest | wind in robes | low angle leap | ink-wash grey-green`
- **作用**：侠与江湖：轻功、意境、人在山水之间。
- **档案**：`directors/king-hu.md`、`directors/ang-lee.md`、`directors/zhang-yimou.md`；近邻 `directors/john-woo.md` 的慢动作枪战。
- **生成**：稳；腾空落地要写重量（`video-prompt/physics.md`）：起跳时踩弯竹子、落地时膝盖吃力、衣摆晚半拍落下，不然像漂浮。
- **失败**：人物轻飘飘地飘来飘去；衣服一直在飘没有风源；把古装片拍成影楼写真。写风从哪来、力落在哪。

### 魔幻现实主义 Magical realism
- **视觉基元**：画面完全写实（自然光、真实质感、日常空间）；只有一处不可能的事，被当成平常事拍：没人惊讶，摄影机也不特别强调；暖而旧的颜色；乡村、小镇。
- **写法**：`An ordinary village kitchen in warm afternoon light, worn wooden table, a grandmother shelling peas; a small cloud drifts through the room under the ceiling and nobody looks up.` B: `magical realism | naturalistic light | one impossible element treated as ordinary`
- **作用**：奇迹是生活的一部分；比奇幻更亲切，比写实更诗意。
- **档案**：`directors/emir-kusturica.md`、`directors/apichatpong-weerasethakul.md`；族谱见 `references/taxonomy.md` §9。
- **生成**：稳；模型会让人物对奇事做反应，写 `nobody reacts`。
- **失败**：奇事被打光、配乐、推镜强调，变成奇幻片。

---

## 4. 未来与反乌托邦

### Tech noir
- **视觉基元**：黑色电影的阴影加上机器与金属；夜里的蓝钢色；工业空间、管道、蒸汽；硬光从下方或侧面打在金属上；城市在夜里是敌意的。
- **写法**：`A night-time industrial corridor in steel-blue light, steam venting from pipes, hard sidelight glinting off wet metal, deep shadows between the machines.` B: `tech noir | steel blue night | steam | hard sidelight on metal`
- **作用**：机器和技术成为威胁。
- **档案**：`directors/james-cameron.md`。
- **生成**：稳。
- **失败**：变成满屏霓虹的赛博朋克。Tech noir 偏冷、偏工业、颜色少。

### 赛博朋克 Cyberpunk
- **视觉基元**：雨夜、密集的竖向城市；霓虹色块（品红、青）倒映在积水里；雾霾里的体积光；人群和小摊；高科技与破旧并存；招牌只写颜色和形状，不写字。
- **写法**：`A narrow rain-soaked alley between towering buildings, magenta and cyan neon glow reflected in puddles, haze catching the light in shafts, a crowded noodle stall under a plastic awning; signs are abstract glowing shapes with no readable text.` B: `cyberpunk | rain night | magenta cyan neon reflections | haze | dense vertical city`
- **作用**：繁华与贫困、人与技术的错位。
- **档案**：`directors/denis-villeneuve.md`、摄影 `cinematographers/roger-deakins.md`。
- **生成**：稳；招牌乱码是最大问题，进总锁。
- **失败**：每个镜头都是同一张霓虹海报。至少有一场在白天或室内，色彩换一换。

### 反乌托邦 Dystopian
- **视觉基元**：野兽派混凝土、巨大的对称空间；冷而低饱和的灰绿；人群穿统一的衣服、排成队；监控的高机位；画面里很少有自然的东西。
- **写法**：`A vast symmetrical concrete hall in cold desaturated grey-green light, rows of people in identical grey uniforms queuing, seen from a high surveillance angle.` B: `dystopian | brutalist concrete | symmetry | desaturated | uniform crowd | high angle`
- **作用**：个人被体制吞没。
- **档案**：`directors/stanley-kubrick.md`、`directors/bong-joon-ho.md`、`directors/alfonso-cuaron.md`；摄影 `cinematographers/emmanuel-lubezki.md`。
- **生成**：稳；大量统一的人群容易出脸和肢体错误，人群调度见 `video-prompt/one-take.md`。
- **失败**：只剩灰色。要有一个和体制对立的颜色或物件（一朵花、一件红衣）。

### 宇宙恐怖 Cosmic horror
- **视觉基元**：极端的尺度差（人很小，那个东西大到装不进画框）；看不清全貌，只见局部；浓雾、低饱和的灰绿；不可能的几何形状；地平线不稳；声音低沉。
- **写法**：`A tiny figure on a grey shore, and behind the fog a shape too large for the frame, only one curved edge of it visible, the geometry wrong; desaturated grey-green, the horizon slightly tilted.` B: `cosmic horror | extreme scale | partially seen entity | fog | desaturated`
- **作用**：人类的渺小和不可知。
- **档案**：`directors/denis-villeneuve.md`（尺度）；近邻 `directors/david-lynch.md`。
- **生成**：定帧；尺度关系先出关键帧，模型常把怪物画小、画全。
- **失败**：怪物被看得清清楚楚。宇宙恐怖的力量在看不全。

---

## 5. 大片、网络美学与梦境

### 大片质感 Blockbuster look
- **视觉基元**：高反差；暖肤色对冷背景（青橙，见 `camera/lexicon-gear.md` 调色风格）；金色轮廓光；航拍和摇臂的大幅运动；英雄仰拍；关键动作升格慢放；尘埃和火星在逆光里。
- **写法**：`High-contrast golden-hour backlight rimming the hero's shoulders, warm skin against a cool blue-grey sky, dust and embers drifting in the backlight, low angle as he turns toward camera.` B: `blockbuster look | golden rim light | warm skin cool background | low angle hero | embers`
- **作用**：规模、英雄感、观影奇观。
- **档案**：`directors/christopher-nolan.md`、`directors/james-cameron.md`、`directors/steven-spielberg.md`；摄影 `cinematographers/wally-pfister.md`、`cinematographers/janusz-kaminski.md`。
- **生成**：稳；模型的默认审美本来就偏这边，反而要防它漂到所有场景。
- **失败**：每场都是金色逆光加慢动作。只留给峰值。

### 蒸汽波 Vaporwave
- **视觉基元**：粉色和青色的渐变；八九十年代的早期电脑图形、网格地面、夕阳圆盘；大理石雕像、棕榈树；录像带的扫描线和色彩溢出；怀旧又空洞。
- **写法**：`A pastel pink and teal sunset gradient over a glowing wireframe grid floor, a white marble bust on a pedestal, palm silhouettes, VHS scan lines and colour bleed.` B: `vaporwave | pastel pink teal gradient | wireframe grid | marble bust | VHS scan lines`
- **作用**：消费时代的怀旧与讽刺；音乐视频、广告。
- **档案**：无；质感写法见 `camera/lexicon-gear.md` 录像带。
- **生成**：稳。
- **失败**：元素堆满画面。挑三样。

### 梦核 Dreamcore / liminal
- **视觉基元**：空无一人的日常空间（走廊、泳池、商场、学校），荧光灯的平光；轻微过曝、柔焦；略广角；熟悉又不对劲；没有声音或只有嗡鸣。
- **写法**：`An empty school corridor under flat buzzing fluorescent light, slightly overexposed and soft, a little too wide, no one there, the far end fading into white.` B: `dreamcore | liminal space | empty corridor | flat fluorescent | overexposed soft`
- **作用**：不安的怀旧，像梦里去过的地方。
- **档案**：无；近邻 `directors/david-lynch.md`。
- **生成**：稳；模型会加人，写 `no people anywhere`。
- **失败**：变成恐怖片，有怪物出现。梦核的不安来自空，而不是威胁。

### 南方哥特 Southern Gothic
- **视觉基元**：衰败的老宅、沼泽、垂挂的苔藓；潮湿的热雾；被晒得发白的木头和褪色的布；宗教物件；人物满脸汗，衣服贴在身上；表面平静，底下腐烂。
- **写法**：`A decaying wooden house at the edge of a swamp, Spanish moss hanging from the oaks, humid haze in the late afternoon, sun-bleached boards, a wooden cross nailed above the door, sweat on her neck.` B: `southern gothic | decaying house | swamp | spanish moss | humid haze | sun-bleached`
- **作用**：家族秘密、罪与宗教，湿热里的腐烂。
- **档案**：无直接档案；可借 `directors/terrence-malick.md` 的自然光与草木。
- **生成**：稳。
- **失败**：变成普通的鬼屋。重点是湿热和衰败，不是鬼。

## 来源

见 `camera/sources.md`。
