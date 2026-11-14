# 完整示例：一部短片的视频提示词

接 `storyboard/example.md`：陆川回老家替住院的父亲喂鸽子，发现脚环上的日期是他每次离家的日子。4 场、31 镜、约 100 秒的分镜脚本和按批次重排的生成清单都在那篇。这里走完最后一步：把生成清单切成生成单位，给每个单位定档位，写出全片共用的全局段，再写出三条完整提示词。

方法见 `video-prompt/compile.md`；段落见 `video-prompt/anatomy.md`。

---

## 1. 三层复用

一部片子的提示词不是 31 条独立的文字，而是三层：

| 层 | 内容 | 复用范围 |
|---|---|---|
| **全片层** | 硬约束、风格、人物的识别特征锁、表演总则 | 全片每条提示词逐字复用 |
| **场景层** | 场景参考图、THIS SCENE 状态、空间地图、光、色、空气 | 同一场景、同一时段的所有单位逐字复用 |
| **单位层** | 剪辑合同、戏的意图、首帧、镜头锁、逐镜时间线、声音、总锁、negative | 每条单独写 |

先写全片层，再按场景写场景层，最后逐个单位写单位层。改动全片层要全片同步；这正是一致性的来源。

## 2. 生成单位

| 单位 | 镜号 | 时长 | 档位 | 生成方式 | 说明 |
|---|---|---|---|---|---|
| A1 | 1-01、1-03、1-05 | 9.5 s | 标准 | 参考图生 | 屏幕只有空白光；1-03 打的字后期 |
| B1 | 1-06 | 2.5 s（生成 5 s） | 轻量 | 参考图生 | 单镜过渡 |
| C1 | 2-01、2-02 | 7.5 s | 标准 | 参考图生 | 鸽群退后有风险，多抽几次 |
| C2 | 2-03 | 3 s | 轻量 | 首尾帧 | 高风险；不成立换备选结果镜 |
| C3 | 2-04、2-06 | 各 1 条 | 轻量 | 首帧 | 只生成空白脚环底板，字后期 |
| C4 | 2-05、2-07、2-08、2-09 | 10.5 s | 标准 | 参考图生 | 不连续的镜头可以放在一条里生成，剪辑时分开 |
| D1 | 3-01 – 3-04 | 14 s | 标准 | 参考图生 | **完整提示词见 §4** |
| D2 | 3-05 – 3-08 | 12 s | 标准 | 参考图生 | **只改单位层，见 §5**；3-08 复用 3-01 关键帧 |
| E1 | 4-01、4-03、4-04 | 10 s | 标准 | 参考图生 | 鸽舍黄昏版参考图 |
| E2 | 4-05 | 4 s | 轻量 | 首尾帧 | **完整提示词见 §6** |
| E3 | 4-06 | 4 s | 轻量 | 首帧 | 只生成写字的手和空白脚环，字后期 |
| E4 | 4-07、4-08 | 7 s | 标准 | 参考图生 | 4-08 结尾留黑场余量 |
| F | 1-02、1-04、4-02 及各镜的字 | — | — | 后期合成 | 屏幕和字全部后期 |

切分依据：同一场景、同一时段、同一组参考图；单次不超过 15 秒；单位内的镜头尽量连续，不连续也可以，只要光和空间一致（`video-prompt/compile.md` 第一步）。

## 3. 全片层（每条逐字复用）

```text
GLOBAL RULES:
- No music of any kind: no score, no soundtrack, no background music, no musical stings,
  no ambient drone.
- No on-screen text: no subtitles, no captions, no titles, no watermark, no logo.
  Phone screens show only a blank glow. Leg rings carry no readable writing.
- Real-time speed throughout: no slow motion, no speed ramps.

STYLE: Photoreal, quiet contemporary family drama in a small Chinese city. Soft filmic
contrast, gently lifted blacks, smooth highlight rolloff, fine organic grain, natural skin
with visible pores and tiredness. Restrained colour. No HDR look, no glossy commercial finish.

CHARACTERS:
<<<luchuan>>> — face, hair and build only. Not pose or expression.
  Identity lock: early thirties, short black hair slightly overgrown, light stubble,
  no glasses, no visible jewellery.
<<<father>>> — face, hair and build only. Not pose or expression.
  Identity lock: mid sixties, thin, close-cropped grey hair, deep lines at the mouth,
  no glasses, no beard.
<<<greypigeon>>> — the one grey pigeon of the film.
  Identity lock: slate-grey body, two dark bars across each wing, green-purple sheen on
  the neck, a plain aluminium ring on the right leg only.

ACTING (whole film): Restrained, naturalistic, nothing performed for the camera.
Blinks at a normal rate. Nobody looks into the lens. Only the speaking character's lips
move; listeners keep their mouths closed. Feelings show in small behaviour, never in tears
or raised voices.
```

**为什么这样写**：

- 全片层只放**全片都成立**的东西。服装不放在这里，因为跨场会变（场 1 在出租屋穿家居服，场 2–4 换了外套），放进场景层的 THIS SCENE。
- 灰鸽在全片层，因为它是全片的母题道具，跨场必须是同一只（`storyboard/continuity.md`）。
- 表演总则写一次，单位层只写这一段的具体表演。

---

## 4. 单位 D1：病房 3-01 – 3-04（标准档，完整）

**读戏卡**（`storyboard/example.md` 场 3）：他第一次主动问，被父亲挡了回去；父亲的关心从灰鸽里透出来。D1 覆盖 B1 冷场 → B2 交差 → B3 父亲问灰鸽 → B4 他追问。

**预判误读**：父亲转头看儿子（这场戏的力量就在他不回头）；两人同时说话；陆川问话时语气激动；病房里出现护士或另一张床上的病人；监护仪屏幕上出现可读的数字；音乐。

```text
EDIT: 4 shots, 14 seconds total, hard cuts, continuous real time.
Shot 1 0–4s · Shot 2 4–6.5s · Shot 3 6.5–10s · Shot 4 10–14s.

[GLOBAL RULES, STYLE, CHARACTERS, ACTING (whole film) — paste the film layer verbatim]

THE BEAT: A son visits his father in hospital. They have not really talked in years.
The son reports that he fed the pigeons; the father, without looking at him, asks only
about one missing grey pigeon. The son then asks his first real question. This is a scene
of distance, NOT of conflict: nobody is angry, nobody cries. The father keeps looking out
of the window the whole time. He is not cold; he is avoiding.

CRITICAL — ONLY TWO PEOPLE: the father and Lu Chuan. A single hospital room.
No nurse, no other patient, no visitors, nobody passing the door.

SCENE ASSETS:
<<<ward>>> — room layout, bed, window and materials only. Not the time of day.
  THIS SCENE: overcast afternoon.
<<<luchuan>>> THIS SCENE: charcoal zip jacket over a grey T-shirt, jacket open.
<<<father>>> THIS SCENE: blue-and-white striped hospital pyjamas, a thin hospital blanket
  over his legs. No visible drip line or tubes.

GEOMETRY: A small single hospital room. The window is beyond frame right. The father sits
half upright in bed on the right side of the room, back against the raised headrest, his
face turned toward the window. Lu Chuan sits on a low plastic stool on the left. Between
them stands a bedside cabinet with a steel thermos and one cup. The heart monitor is off
screen behind the bed; only its beep is heard.
Axis for every shot: Lu Chuan is frame left, the father frame right. Lu Chuan looks frame
right toward his father. The father looks further frame right, out of the window, away
from his son.

FIRST FRAME: Both are already still, mid-silence: the father gazing out of the window,
Lu Chuan sitting with his forearms on his knees, looking at the cabinet.

LENS: Focal length fixed within each shot, no zoom.
Shot 1 — 35mm, medium two-shot from the side, camera at the eye level of a seated person.
Shot 2 — 50mm, medium close-up on Lu Chuan.
Shot 3 — 50mm, medium close-up on the father, his face in three-quarter profile toward the window.
Shot 4 — 75mm, close shot on Lu Chuan, the background soft.

CAMERA: All four shots locked-off on a tripod. No drift, no slow push, no reframing.

LIGHT: Flat, soft overcast daylight from the window, frame right. It falls fully on the
father's face; Lu Chuan, further from the window, is a little darker. No direct sun,
no beams, no rim glow.

COLOUR: 60% pale green-grey of the hospital walls, 30% soft overcast white,
10% the dull red of the thermos. Low saturation; skin natural, slightly pale.

ATMOSPHERE: Still air. A real, used ward: a scuffed cabinet top, a folded towel on the
bed rail, a paper cup. No airbrushed skin, no waxy faces.

SHOT 1 — 0–4s — two-shot, 35mm.
0.0–4.0s: Nobody moves except for breathing. The father looks out of the window. Lu Chuan
  looks at the thermos on the cabinet. The monitor beeps twice.
Ends: the same stillness.

SHOT 2 — 4–6.5s — Lu Chuan, medium close-up, 50mm.
4.5s: Still looking at the cabinet, not at his father, he says in Mandarin, flat and short:
  "鸽子喂了。"
  Only Lu Chuan's lips move.
Ends: his eyes stay on the cabinet.

SHOT 3 — 6.5–10s — the father, medium close-up, 50mm, three-quarter profile.
7.0s: Without turning from the window, the father says in Mandarin, quietly:
  "那只灰的回来没有？"
  Only the father's lips move. His head does not turn.
Ends: the father still looking out of the window.

SHOT 4 — 10–14s — Lu Chuan, close shot, 75mm.
10.0s: Lu Chuan lifts his eyes and turns his head toward his father, frame right.
11.0s: He says in Mandarin, carefully, a real question for the first time:
  "脚环上那些日期，是什么？"
  Only Lu Chuan's lips move.
13.0s: He waits, looking at his father. No answer comes in this shot.
Ends: Lu Chuan looking frame right, lips closed.

PHYSICS: The stool creaks slightly when Lu Chuan shifts. The blanket rests with real weight.
Objects keep their shape and position; the thermos and cup never move.

AUDIO: Diegetic only. Room tone: the soft beep of the heart monitor about once a second,
faint corridor hum. Three lines only, all in Mandarin, one per shot (shots 2, 3, 4),
one speaker at a time. Silence between the lines.

LOCKS:
- Only two people, the whole time.
- The father never turns his head toward his son and never looks at the camera.
- Lu Chuan is always frame left, the father frame right.
- One line per shot; nobody else's lips move.
- No music; the monitor shows nothing readable.

NEGATIVE: the father turning to look at his son; tears; raised voices; Lu Chuan leaning in
or grabbing the bed; a nurse or another patient; a second bed occupied; readable numbers
on the monitor; drip lines and tubes; warm golden light; sunbeams; music; slow camera push.
```

**为什么这样写**：

- **父亲不回头写了三处**：THE BEAT、逐镜（3-03「His head does not turn」）、总锁，negative 里还有一条。这是这场戏一错就作废的东西，也是模型最想「修正」的：对话时转头看对方，是它的默认。
- **陆川的视线有变化**：3-02 看柜子、3-04 抬眼看父亲。视线从回避到直视，就是 B2 → B4 的变化，不用写任何情绪词。
- **没有给监护仪画面**：只留声音。屏幕上的数字是可读文字，放进画面就要后期处理。
- **光是阴天**：病房的冷和平，不要阳光和光束。模型对「医院」的默认常常是明亮干净的商业光，所以 negative 里写了暖光和光束。

---

## 5. 单位 D2：病房 3-05 – 3-08（只改单位层）

全片层和场景层（SCENE ASSETS、GEOMETRY、LIGHT、COLOUR、ATMOSPHERE、PHYSICS）**逐字复用 D1**。下面只列改动的段落：

```text
EDIT: 4 shots, 12 seconds total, hard cuts, continuous real time.
Shot 1 0–2s · Shot 2 2–5s · Shot 3 5–8.5s · Shot 4 8.5–12s.

THE BEAT: The son has just asked what the dates on the leg rings mean. The father does not
answer. His hand gives him away for a moment; then he changes the subject back to the grey
pigeon, warning his son not to grab it. It sounds like a complaint about the bird; it is
care for his son. The son gives up asking. NOT anger, NOT tears.

FIRST FRAME: The father's hand already resting on the blanket, fingers loose.

LENS:
Shot 1 — 85mm, close-up from above on the father's hand on the blanket.
Shot 2 — 50mm, close shot on the father, three-quarter profile toward the window.
Shot 3 — 75mm, close shot on Lu Chuan.
Shot 4 — 35mm, the same side two-shot as shot 1 of the previous unit, same position, same framing.

CAMERA: Shots 1, 2 and 4 locked-off. Shot 3 only: a very slow push-in over 3.5 seconds,
ending a little closer on Lu Chuan's face.

SHOT 1 — 0–2s — the father's hand.
0.5s: His fingers close slightly on the blanket, then stop. Nothing else moves.

SHOT 2 — 2–5s — the father.
2.5s: Still facing the window, he says in Mandarin, mildly: "那只灰的，爱啄人。"
  Only the father's lips move.

SHOT 3 — 5–8.5s — Lu Chuan, slow push-in.
5.5s: Lu Chuan opens his mouth as if to ask again, then closes it. No sound comes from him.
6.0s: The father, off-screen, says in Mandarin: "你别伸手抓它。"
  Lu Chuan's lips stay closed while the father's voice is heard.
Ends: Lu Chuan looking down.

SHOT 4 — 8.5–12s — side two-shot.
9.0s: The father pulls the blanket up a little over his chest. Lu Chuan does not move.
  The cabinet still stands between them.
Ends: stillness; the monitor beeps.

AUDIO: Diegetic only. Monitor beep, corridor hum. Two lines, both the father's, in Mandarin:
shot 2 on screen, shot 3 off screen. Lu Chuan says nothing in this unit.

LOCKS:
- Only two people, the whole time.
- The father never turns toward his son and never looks at the camera.
- Lu Chuan says nothing; his lips stay closed in every shot, including shot 3.
- Shot 4 matches the framing of the previous unit's shot 1 exactly.
- No music; nothing readable.

NEGATIVE: Lu Chuan speaking or mouthing words; the father turning his head; the father's
hand trembling dramatically; tears; a nurse; warm light; music.
```

**改了什么**：剪辑合同、THE BEAT、首帧、镜头锁、摄影机（3-07 是唯一的运动镜头）、逐镜、声音、总锁、negative。3-07「陆川张了张嘴，没再问」和画外台词同时发生，是口型最容易落错的地方，所以写在逐镜里，又写进总锁。3-08 镜像 3-01：生成时用 D1 的 3-01 关键帧做参考，总锁里写「framing matches exactly」。

---

## 6. 单位 E2：灰鸽落肩 4-05（轻量档，首尾帧）

分镜脚本标「定帧 · 首尾帧」：动物落肩是高风险镜头，先用图像模型做好首帧（灰鸽站在鸽舍顶上，陆川在旁边）和尾帧（灰鸽在他肩上，喙靠近他的耳朵），视频只负责中间的过程（`references/aigc/workflow.md`）。

首尾帧已经定了人、鸟、空间、光，所以全局段大幅缩减：保留硬约束、灰鸽的识别特征锁和必要的锁，其余交给两张图。

```text
Single shot, 4 seconds, from the supplied first frame to the supplied last frame.
Camera locked-off, no drift. Real-time speed, no slow motion. No music, no text.

The grey pigeon (slate-grey, two dark wing bars, aluminium ring on the right leg) is
standing on the roof of the loft beside Lu Chuan's right shoulder.
0.5s: It hops once onto his shoulder, one short flap of the wings for balance.
1.5s: Its claws grip the jacket; the fabric dents under them.
2.5s: It pecks once, lightly, at his ear.
Lu Chuan does not flinch and does not lift a hand. He blinks once at the peck, then
stays still, looking ahead. It reads as letting it happen, not as fear and not as
a smile for the camera.

Audio: the pigeon's wing flap, a soft coo, distant evening traffic. No music.

Locks: only one bird on his shoulder; the other pigeons stay inside the loft behind the
mesh. The grey pigeon keeps its exact look from first frame to last.
Negative: the bird changing colour or shape, a second bird landing, feathers multiplying,
Lu Chuan laughing, flinching or reaching for the bird, slow motion.
```

**为什么这样写**：

- **轻量档也写识别特征**：首尾帧之间模型会补帧，鸟最容易在中间几帧变色、变形，所以用一句话把灰鸽钉住。
- **陆川「不躲」写成三件套**：不躲、不抬手（行为），任它啄（理解），不是害怕、不是对镜头笑（不是）。这是场 3「你别伸手抓它」的回收，他这次没伸手。
- **物理写在接触点**：爪子抓住外套、布料凹下去。鸟的重量就体现在这里（`video-prompt/physics.md`）。
- **备选**：不成立就按 `storyboard/example.md` 的备选拆成两镜：灰鸽落在鸽舍顶（远）→ 他肩上的灰鸽（近，结果），后一镜从静止开始，风险小得多。

---

## 7. 写完之后

- **逐条过 `video-prompt/compile.md` 第七步的自检**，特别是全片层和场景层有没有被手改过。
- **生成顺序按生成清单的批次**（`storyboard/example.md`）：每批先出建立镜头的关键帧，通过后再跑视频。
- **失败先回分镜改**：一个单位反复失败，先看是不是一镜塞了太多动作、两个人同时说话，再改提示词（`references/drama/07-segment-prompt.md` §5 的原则同样适用）。
- **记录哪条提示词出了哪条成片**：返工时只改单位层，全片层不动。

## 来源

见 `video-prompt/sources.md`。
