# 三档示例：轻量、标准、重型

同样是「把分镜脚本编译成提示词」，不同的镜头需要的长度差别很大。这份文件用 `storyboard/scene-types.md` 里的两场戏，演示三档各写成什么样：

| 档位 | 示例 | 为什么是这一档 |
|---|---|---|
| 轻量 | 场 9 · 9-05 停顿镜（6 秒，单人，无台词，固定） | 一个人坐着、画外一个声音；全局段已在同场的标准档里定好 |
| 标准 | 场 9 · 9-03 – 9-04（10 秒，2 镜，情绪转折） | 道具资产 + 一段要演准的表演 |
| 重型 | 场 7 · 7-01 – 7-06（11 秒，6 镜，追逐） | 动作、方向、距离、物理、多人，任何一处错都整条作废 |

档位的定义见 `video-prompt/index.md`。最后一节讲长镜头对白（`storyboard/three-ways.md` 的 5-L2）这种特殊情况怎么写。

---

## 1. 标准档：场 9 · 9-03 – 9-04

**这场戏**：林晚回到去世母亲的老房子，发现一条织到一半的围巾，比了比，长度刚好——是给她织的（`storyboard/scene-types.md` C）。无台词。

**单位划分**：9-01 – 9-02（11 s）、**9-03 – 9-04（10 s）**、9-05（6 s，轻量）、9-06 – 9-07（11 s）。

**预判误读**：她哭；她把围巾抱在胸前抽泣；回忆闪回画面；围巾的颜色、长度在两镜之间变化；针掉了；温暖的配乐；镜头缓慢推近她的脸。

```text
EDIT: 2 shots, 10 seconds total, hard cut, continuous real time.
Shot 1 0–4s · Shot 2 4–10s.

GLOBAL RULES:
- No music of any kind: no score, no soundtrack, no background music, no musical stings.
- No on-screen text: no subtitles, no captions, no titles, no watermark, no logo.
- Real-time speed: no slow motion. No flashbacks, no dream images, no dissolves.

STYLE: Photoreal quiet drama. Soft filmic contrast, gently lifted blacks, smooth highlight
rolloff, fine organic grain, natural skin with visible pores. No HDR, no glossy finish.

THE BEAT: Lin has come to clear out her late mother's flat. On the coffee table she finds
a half-knitted scarf, needles still in it. She holds it up against her own neck: it is
exactly her length. She understands it was being made for her. This is the moment the
feeling arrives, NOT the moment it spills: she does not cry, does not clutch the scarf,
does not break down. Everything happens in her hands and her breath.

CRITICAL — ONLY ONE PERSON: Lin. Nobody else, no reflections of anyone else.

ASSETS:
<<<lin>>> — face, hair and wardrobe only. Not pose or expression.
  Identity lock: straight black hair tied in a low ponytail, thin black-framed glasses,
  no earrings, no visible jewellery.
  THIS SCENE: a plain dark-green coat, unbuttoned, over a black jumper.
<<<oldflat>>> — layout, furniture and materials only. Furniture covered in white dust sheets.
  THIS SCENE: daytime, the dust sheet already pulled off the sofa where Lin sits.
<<<scarf>>> — the half-knitted scarf: oatmeal-coloured wool, ribbed pattern, about 1.2 metres
  long so far, two bamboo needles still in the last row, the ball of yarn attached.

GEOMETRY: Lin sits on the sofa, centre of the room, facing the camera side. A low wooden
coffee table in front of her. A window behind her on frame right. Other furniture around
the room remains under white sheets.

FIRST FRAME: The scarf and the ball of yarn are already lying on the table, still.

LENS: Fixed within each shot.
Shot 1 — 85mm, close-up from above on the coffee table.
Shot 2 — 50mm, medium close-up on Lin, eye level of a seated person.

CAMERA: Both shots locked-off on a tripod. No drift, no push-in.

LIGHT: Soft daylight from the window behind her, frame right, catching the edge of her
face and hair. Dust drifting slowly in the light. The front of her face in soft shadow,
still readable.

COLOUR: 60% pale off-white of sheets and walls, 30% warm daylight, 10% the dark green of
her coat. The oatmeal scarf sits between them. Low saturation.

ATMOSPHERE: Dust motes visible only inside the window light. A faint layer of dust on the
table. A room no one has lived in for months.

SHOT 1 — 0–4s — coffee table, from above, 85mm.
0.0–2.5s: The scarf lies on the table: half-finished, the needles crossed in the last row,
  the ball of yarn beside it. Nothing moves.
2.5s: Lin's hand enters frame from the top and rests on the scarf. Her fingers flatten
  the wool gently.
Ends: her hand resting on the scarf.

SHOT 2 — 4–10s — Lin, medium close-up, 50mm.
4.0s: She lifts the scarf with both hands, the needles still in it, the yarn trailing.
5.5s: She holds it up against her own neck, measuring. It reaches exactly where it should.
7.0s: Her hands stop. Her breathing slows; her shoulders lower a little. She keeps holding
  the scarf in place and does not move.
8.5s: She blinks once, slowly. Her eyes are bright, but no tears fall.
Ends: Lin holding the scarf against her neck, still, looking at nothing in particular.

PHYSICS: The wool is soft and heavy; it drapes over her hands. The needles stay in the
stitches and do not fall. The ball of yarn rolls a little across the table when the scarf
is lifted.

ACTING: Restrained. Blinks normally until the slow blink at 8.5s. She does not look into
the lens. Her lips stay closed throughout. It reads as understanding, not as grief
breaking out.

AUDIO: Diegetic only. A very quiet room: faint distant traffic through the window,
the soft sound of wool. No music, no voice.

LOCKS:
- Only Lin, the whole time.
- The scarf keeps the same colour, length and two needles in both shots.
- No tears fall; she does not cry or sob.
- No flashback images; we stay in this room, in real time.
- No music.

NEGATIVE: crying, tears streaming, sobbing, hugging the scarf to her chest, her mother
appearing, flashback, soft-focus memory glow, the scarf changing colour, needles falling,
camera pushing in, music, golden-hour glow.
```

**为什么是标准档**：两镜、一个人、一样关键道具。重要的是道具资产（围巾颜色、长度、两根针）和一段表演（9-04 的明白），两者都需要单独写段落。物理和空气只写和这两镜有关的几句，不写成重型档的全套。

---

## 2. 轻量档：场 9 · 9-05

同场的标准档已经定好了人物、空间、光；9-05 用 9-04 的结束帧（或同场的关键帧）做首帧，视频只需要写这 6 秒里发生的事。

```text
Single shot, 6 seconds, starting on the supplied first frame. Locked-off wide shot,
no drift, no push-in. Real-time speed. No music, no on-screen text.

Lin sits small on the sofa in the window light, the half-knitted scarf lying across her
lap, her hands resting on it. She does not move except for breathing; once, at about 3s,
she lifts her head slightly toward the window, as if listening.

Audio: from outside the window, off-screen, a primary-school bell rings for the end of
the day, then distant children's voices. Inside, silence. No music.

Only Lin in the room. No tears. The scarf keeps its colour and needles.
```

**为什么能这么短**：首帧带来了人物、服装、围巾、空间和光，全局段的工作已经由图完成。剩下要说清的只有三件事：她几乎不动（模型默认会让人物「做点什么」）、画外的铃声和她的反应、三条最容易错的锁。约 110 词。

---

## 3. 重型档：场 7 · 7-01 – 7-06

**这场戏**：送外卖的陆川的电动车被偷，他扔下外卖追进小巷（`storyboard/scene-types.md` B）。7-01 – 7-06 是追逐的前半段：偷车、开追、追者、距离、障碍、钻过障碍。

**为什么是重型**：六个镜头、两个移动的人、一辆车、一个障碍；方向错一镜，观众以为两人迎面相撞；1.5–2 秒的镜头要从生成里裁，每镜的动作必须干净。

**预判误读**：方向在某一镜反了（最常见）；电动车造型漂移；贼和陆川长得像、或换了衣服；跑步不落地、漂浮；自动慢动作；手持晃到看不清；小巷里冒出路人；晾衣竿和衣服穿过人体；音乐。

```text
EDIT: 6 shots, 11 seconds total, hard cuts, continuous real time.
Shot 1 0–2s · Shot 2 2–4s · Shot 3 4–6s · Shot 4 6–8s · Shot 5 8–9.5s · Shot 6 9.5–11s.

GLOBAL RULES:
- No music of any kind: no score, no soundtrack, no action music, no stings, no drums.
- No on-screen text: no subtitles, no titles, no watermark, no logo, no readable shop signs.
- Real-time speed throughout: no slow motion, no speed ramps, no freeze frames.

STYLE: Photoreal, grounded urban drama in an old Chinese residential district. Natural
daylight, soft filmic contrast, fine grain, real textures. Not an action-movie look:
no teal-and-orange grade, no lens flares, no HDR.

THE BEAT: A delivery rider's e-bike is stolen in front of him. He drops everything and
chases on foot. He is desperate, not heroic: he is losing his livelihood. The thief is
just a thief in a hurry, not a movie villain. The chase is clumsy and real.

CRITICAL — SCREEN DIRECTION: in every shot where they move sideways, both the thief and
Lu Chuan move from frame LEFT to frame RIGHT. Never right to left.

CRITICAL — ONLY TWO PEOPLE: Lu Chuan and the thief. The alley is empty: no residents,
no passers-by, no faces at windows.

ASSETS:
<<<luchuan>>> — face, hair and build only.
  Identity lock: early thirties, short black hair, light stubble, no glasses.
  THIS SCENE: a yellow delivery jacket with no readable logo, dark trousers, a yellow helmet
  in shot 2 only, which he drops with the bag.
<<<thief>>> — face and build only.
  Identity lock: lean man in his twenties, black baseball cap pulled low, grey hoodie,
  face mostly hidden. Clearly a different person from Lu Chuan.
<<<ebike>>> — Lu Chuan's e-bike: small white electric scooter-bike, a black delivery box
  on the back, no readable text. Same bike in every shot.
<<<alley>>> — the narrow alley: layout, walls and materials only.

GEOMETRY: The alley runs from frame left to frame right in side views. It starts at an
open street mouth on the left and narrows toward the right. Halfway along, a bamboo pole
with laundry hangs across the alley at head height. The thief is always ahead, further
right; Lu Chuan is always behind, further left.

FIRST FRAME: The thief is already riding the e-bike out of the alley mouth at speed,
mid-motion, frame left.

LENS: Fixed within each shot, no zoom.
Shot 1 — 28mm, wide, camera at waist height, the alley mouth and the street.
Shot 2 — 35mm, medium shot of Lu Chuan.
Shot 3 — 50mm, medium close-up of Lu Chuan in profile.
Shot 4 — 135mm, long lens looking back down the alley: compressed, the thief large in the
  foreground, Lu Chuan small far behind, the alley flattened between them.
Shot 5 — 35mm, medium shot of the bamboo pole and the laundry across the alley.
Shot 6 — 35mm, medium shot of the thief at the pole.

CAMERA: Shots 1, 2, 4, 5 and 6 locked-off on a tripod: no drift, no shake.
Shot 3 only: the camera tracks alongside Lu Chuan at his speed, at a constant two-metre
distance, his size in frame never changing. A slight natural bounce from the movement,
not a violent shake.

LIGHT: Overcast midday. Soft, even daylight from above, the alley floor slightly darker
than the open street. No sun beams, no rim light.

COLOUR: 50% grey concrete and brick, 30% muted daylight, 20% the yellow of Lu Chuan's
jacket. The jacket is the brightest thing in every frame he is in.

ATMOSPHERE: Real old-alley texture: cracked concrete, a drain cover, potted plants against
a wall, electric cables overhead, damp patches. No airbrushed skin.

SHOT 1 — 0–2s — the alley mouth, wide, 28mm.
0.0s: The thief is already riding the e-bike out of the alley, crossing from frame left
  to frame right at speed, leaning into the turn.
1.5s: He exits frame right.
Ends: the empty alley mouth, a little dust settling.

SHOT 2 — 2–4s — Lu Chuan, medium, 35mm.
2.0s: Lu Chuan, a takeaway bag in his hand, sees it. He drops the bag; it hits the ground
  and tips over.
2.8s: He bursts into a run from frame left toward frame right.
Ends: he is leaving frame right.

SHOT 3 — 4–6s — Lu Chuan running, profile, 50mm, tracking.
4.0–6.0s: He runs hard toward frame right, arms pumping, mouth open, breathing hard.
  Each footfall lands with weight. The alley wall slides past behind him.
Ends: still running, same size in frame.

SHOT 4 — 6–8s — looking back down the alley, 135mm.
6.0–8.0s: The thief rides toward the camera in the foreground, glancing back once over his
  shoulder. Far behind him, small, Lu Chuan runs after him. The distance between them
  is large.
Ends: the thief close to the camera, Lu Chuan far behind.

SHOT 5 — 8–9.5s — the pole across the alley, 35mm.
8.0–9.5s: A bamboo pole with laundry hangs across the alley at head height: shirts and
  a white sheet, swaying slightly. The alley beyond it is empty. Nobody in frame yet.
Ends: the laundry still swaying.

SHOT 6 — 9.5–11s — the thief at the pole, 35mm.
9.5s: The thief rides in from frame left toward frame right and ducks low over the
  handlebars.
10.2s: He passes under the pole; a shirt brushes his cap and swings back.
Ends: he exits frame right; the shirt still swinging.

PHYSICS: The e-bike has weight: it leans into turns and the rear box sways. Footsteps land
heel to toe with real impact. The dropped bag falls with weight and tips over. Laundry
moves with real cloth weight and swings back after contact. No one passes through any
object.

ACTING: Lu Chuan is desperate and out of breath, not heroic. The thief looks back once,
anxious, not menacing. Nobody looks into the lens. No dialogue.

AUDIO: Diegetic only. The whine of the e-bike motor, tyres on concrete, the bag dropping,
Lu Chuan's footsteps and hard breathing, the rustle of laundry. No voices, no music.

LOCKS:
- Sideways movement is always left to right, for both of them, in every shot.
- The thief is always ahead, Lu Chuan always behind.
- Only two people; the alley is otherwise empty.
- The same white e-bike with the black box in every shot.
- Lu Chuan wears the yellow jacket; the thief wears the cap and grey hoodie, in every shot.
- Real-time speed; no music.

NEGATIVE: anyone moving right to left; the two of them running toward each other;
passers-by; residents watching; a different bike; the thief's face clearly visible;
the thief and Lu Chuan looking alike; floating runners; slow motion; shaky-cam blur;
action-movie music; lens flare; laundry passing through bodies.
```

**为什么是重型**：

- **两条 CRITICAL 给了方向和人数**：这两样任何一镜错了，整条都不能用。方向还在 GEOMETRY、逐镜、总锁、negative 里各出现一次——这是本层允许的有意冗余（`video-prompt/anatomy.md` 关于冗余）。
- **贼和陆川必须一眼分开**：衣服颜色对比（黄 / 灰）、贼的脸藏在帽檐下、「clearly a different person」。追逐戏里两人长得像，观众会分不清谁追谁。
- **7-04 不写左右**：长焦朝后看，贼朝镜头骑来，屏幕方向是中性的；写左右反而会让模型困惑。所以 CRITICAL 里写的是「横向移动时」。
- **物理段比标准档长**：车的重量、脚落地、袋子落地、衣服的回弹，每一样都出现在画面里，每一样不写都会发飘。
- **剩下的 7-07 – 7-12 是下一个单位**：全局段逐字复用；7-07 床单扑面按分镜脚本的建议用首尾帧单独生成。

---

## 4. 特殊情况：长镜头对白

`storyboard/three-ways.md` 的 5-L2：一个 15 秒的固定中景，两人同框完成全部对话。这违反「一镜一个说话人」，口型风险最高。两种写法：

**做法一：生成表演，后期配音。** 提示词照写台词和时间点（让模型知道谁在什么时候说话、口型要动），但在硬约束里写「dialogue audio will be replaced in post」，验收只看表演和口型时机，不看音质。

```text
AUDIO: Lip movement must follow the lines below exactly, one speaker at a time.
Dialogue audio will be replaced in post; room tone only is needed.
6.0s Gu (frame right) speaks: "还没走？明天汇报别太紧张。" — Lin's lips stay closed.
10.5s Lin (frame left) speaks: "第七页，是你改的？" — Gu's lips stay closed.
```

**做法二：让说话的人背对或侧对镜头。** 改分镜：顾言说话时背对镜头或在画面边缘侧脸，林晚说话时正脸。口型问题从源头消失，提示词照常写（`references/drama/07-segment-prompt.md` §5「口型落在不说话的人脸上」的修法）。

长镜头超过模型单次上限时，按 `video-prompt/one-take.md` 第五步分段生成，首尾帧续接。

## 来源

见 `video-prompt/sources.md`。
