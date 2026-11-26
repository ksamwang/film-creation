# 锁与 negative：从错误版本倒推

长提示词里，正面描述告诉模型要什么；锁和 negative 告诉它**最可能在哪里错**。两者分工：

| | 写什么 | 放在哪 |
|---|---|---|
| **硬约束** | 模型最顽固的默认（音乐、文字、慢动作），同义说法列全 | 提示词开头 |
| **总锁** | 这场戏一错就作废的不变量（人数、谁坐谁站、谁说话、轴线、道具状态） | 提示词结尾 |
| **negative** | 这场戏的错误版本（演错的方式、多出的东西） | 负面参数框，或正文末尾 |

原则见 `video-prompt/anatomy.md` 末尾的四条写法原则：正面描述优先，顽固默认集中封住，negative 只写这场戏的错误版本。

---

## 1. 顽固默认与同义词

模型有一些「改不掉」的默认。只写一个词封不住，因为它会换一种形式出现。下表是常见的顽固默认和要一起写上的同义说法。

### 音乐 Music

**写法**：

```text
No music of any kind: no score, no soundtrack, no background music, no musical stings,
no ambient drone, no humming.
```

**防什么误读**：封了 music，模型加 ambient drone（低频铺底）或者让人物哼歌。

**用在**：全片硬约束。竖屏短剧的固定写法见 `references/drama/07-segment-prompt.md` §3。

**别这样写**：只写 no music。

### 画面文字 On-screen text

**写法**：

```text
No on-screen text: no subtitles, no captions, no titles, no credits, no watermark,
no logo, no UI overlay, no timestamp. Screens, signs and papers show no readable words.
```

**防什么误读**：封了 subtitles，模型在屏幕、招牌、纸上画出乱码字；监控画面自动加时间戳。

**用在**：全片硬约束。需要文字的地方后期合成。

**别这样写**：只写 no subtitles。

### 多余的人 Extra people

**写法**：

```text
ONLY TWO PEOPLE in the entire scene. No passers-by, no staff, no figures in the
background, no silhouettes behind glass, no reflections of other people.
```

**防什么误读**：封了 extra people，模型在玻璃后、倒影里、远处走廊加人影。

**用在**：人数锁和总锁。这是最值得标 CRITICAL 的一条。

**别这样写**：只写 empty room。

### 稳定器式漂移 Floating camera

**写法**：

```text
Locked-off: no drift, no slow push, no gimbal float, no reframing, no micro-movement.
```

**防什么误读**：封了 camera movement，模型保留了「缓慢推近」，因为它不认为那是运动。

**用在**：CAMERA 段和总锁。摄影机的写法见 `video-prompt/camera-behavior.md`。

**别这样写**：只写 static。

### 慢动作 Slow motion

**写法**：

```text
Real-time speed throughout: no slow motion, no speed ramps, no frozen moments,
no time-lapse.
```

**防什么误读**：动作戏、情绪高潮、雨和水的镜头，模型很爱自动放慢。

**用在**：全片硬约束；需要慢动作的后期做（`video-prompt/audio.md` 慢动作的声音）。

**别这样写**：只写 normal speed。

### AI 质感 AI look

**写法**：

```text
No waxy skin, no airbrushing, no plastic sheen, no glowing rim light on everyone,
no oversaturated colour, no HDR look.
```

**防什么误读**：封了 AI look 这种笼统说法，模型不知道具体是什么。

**用在**：ATMOSPHERE 段末尾或 negative；按画风选。详见 `video-prompt/physics.md`。

**别这样写**：no AI look、not fake。

---

## 2. 从错误版本倒推

negative 不是一份万能清单。每条提示词写之前，先回答一个问题：**这场戏最可能被生成成什么错的样子？**

### 倒推的五个方向

**写法**：对这场戏逐一想这五个方向，每个方向最多写一两条：

```text
1. Acting: how would a soap opera play this?        → crying, shouting, smirking
2. People: who might wander in?                      → colleagues, waiters, passers-by
3. Objects: what might appear, vanish or change?     → readable screen text, a third cup
4. Space: what might flip or jump?                   → the two swap sides, he sits down
5. Time and camera: what might the model add?        → slow motion, drift, daylight
```

**防什么误读**：凭感觉写 negative，漏掉这场戏真正的风险，写进一堆无关的通用词。

**用在**：每条提示词的第六步（`video-prompt/compile.md`）。

**别这样写**：从别的提示词复制 negative。

### 错误版本按类型

**写法**：按场景类型查下表，取这一类型的条目作为起点，再改成这场戏的具体人和物。

| 场景类型 | 最常见的错误版本 |
|---|---|
| 压抑的对白 | 哭、喊、拍桌子；坏人冷笑；两人同时说话；背景有人 |
| 亲密戏 | 两人肢体融合；过度煽情的慢动作；逆光光晕；配乐 |
| 追逐 | 人物忽大忽小；跑步不落地；方向乱跳；自动慢动作 |
| 打斗 | 拳脚穿模；无重量的击打；武器变形；多出的人 |
| 悬疑 / 恐怖 | 提前露出威胁；人物直视镜头；不合理的光；惊吓音效 |
| 喜剧 | 做鬼脸、夸张表情；人物对镜头使眼色；配乐提示笑点 |
| 广告 / 产品 | 产品变形、logo 乱码；手指穿过产品；画面文字 |
| 儿童 / 动物 | 孩子表情成人化；动物像人一样表演；动物数量变化 |

**防什么误读**：这些是各类型最常见的生成失败，写 negative 时作为起点。

**用在**：五个方向里一时想不全时。类型的写作约定见 `writing/genres/index.md`。

**别这样写**：整行照抄，不检查和这场戏是否有关。

### 和正文不矛盾 No contradictions

**写法**：

```text
Body: "Lin stays seated in every shot."
Negative: "Lin standing up."              ✓ consistent
Negative: "people standing"                ✗ Gu is standing — this fights the body
```

**防什么误读**：negative 写得太宽，误伤正文里要的东西；模型在两个指令之间摇摆。

**用在**：写完 negative 后逐条对照正文。

**别这样写**：用泛指（people、standing、light）写 negative。

---

## 3. 总锁

### 选什么进总锁 What goes into LOCKS

**写法**：

```text
LOCKS:
- Only two people, the whole time.
- She stays seated; he stays standing.
- She is always frame left, he always frame right.
- The letter stays sealed until shot 5.
- One speaker per shot.
- No music, no readable text.
```

**防什么误读**：长提示词中段的约束被稀释，模型在后半段忘了人数或轴线。

**用在**：标准档和重型档。只放「错了整条作废」的东西，5–8 条。选的标准：如果这条错了，你会不会直接重抽？会，就进总锁。

**别这样写**：把风格、光、色也塞进总锁——那些错了可以修，不必重复。

### 道具状态锁 Prop state

**写法**：

```text
The coffee cup on her desk stays untouched and full in every shot.
```

**防什么误读**：道具状态跨镜漂移：杯子空了又满、信封拆了又封上。

**用在**：剧情依赖道具状态时（连续性记录见 `storyboard/continuity.md`）。

**别这样写**：只在某一镜写，其他镜不提。

### 「关键」的配额 CRITICAL budget

**写法**：整条提示词里，CRITICAL 最多 2–3 处，通常给：

```text
CRITICAL — ONLY TWO PEOPLE.
CRITICAL — only the speaking character's lips move.
CRITICAL — no readable text anywhere, including screens.
```

**防什么误读**：处处 CRITICAL，模型分不出主次，等于没有。

**用在**：长提示词。挑一错就作废、模型又最容易错的。

**别这样写**：每段开头都加 IMPORTANT。

---

## 4. 解释权：稿子没写死，模型就补

成片穿帮大多不是模型随机出错，而是稿子把某件事留给了模型去猜。三条规律：

1. **状态不会自己消失。** 一个人建立了姿态（趴在桌上、拎着外套），后文不写它结束，它要么一直保留，要么转到画面里最近的另一个人身上。
2. **模型靠位移自洽，不靠方位词。** 只写「从东侧门进来」，门被放错边，模型就让人横穿整个房间来圆。
3. **连续路径只剩终态。** 「手从门框一路摸到窗沿」，模型只理解「手在窗沿」，中间直接跳过。

下面五条锁对着这三条写。复盘时也用同一个问法：穿帮的这一下，是稿子里哪一句没写死（`aigc/workflow.md` §7）。

### 姿态交接 Pose handoff

**写法**：

```text
Shot 3: Mia, who was leaning across the desk, now sits back upright with both hands on her
lap and stays that way. Only Mia leaned on the desk; nobody else leans on it in this shot.
```

**防什么误读**：上一镜的姿态没写结束，模型把它挂到同框的另一个人身上（换成别人趴桌、别人拎包）。

**用在**：每个有标志性姿态的人物，在姿态结束的那一镜。先问三件事：谁建立、在哪一镜结束、结束后换成什么。交出方和可能的接手方两头都写；只禁接手方，模型会换一个人挂。

**别这样写**：只在新进画的人身上写动作，对原来那个人一字不提；或只写「禁止 Leo 趴桌」，不写 Mia 已经坐直。

### 点到人头 One actor per action

**写法**：

```text
Only Tom raises a hand and cheers; the two boys beside him stay seated and still, out of focus.
```

**防什么误读**：「旁边几个人起哄」没限定人数，所有背景人物同时做同一个动作。

**用在**：画面里有两人以上、只该一个人动的时候。一镜里背景只给一个声音、一个动作，其余人静着，静才衬得出主角。人群整体怎么反应见 `video-prompt/one-take.md` §2。

**别这样写**：the friends cheer / 几个同学起哄。

### 状态写到可执行 State to the button

**写法**：

```text
Leo has taken off the jersey and holds it in his left hand; he wears a plain grey T-shirt
under the open black jacket, zipper down.
```

**防什么误读**：「外套还穿着」没说里面穿什么、拉链到哪，模型自己补，补出来的常常违和（里面什么都没穿、换了衣服）。

**用在**：服装、道具、伤妆偏离参考图的时候。写清在哪只手、拉到哪、里面是什么，每次关键状态出现都复述一次。道具状态的跨镜锁见上面第 3 节「道具状态锁」。

**别这样写**：仍、依然、照旧、同上、as before。这类词等于把解释权交给模型。

### 画左画右 Screen left, screen right

**写法**：

```text
The back door is on the right edge of frame. Leo enters through it, takes two steps toward
frame center and stops beside the last desk.
```

**防什么误读**：只写东南西北或「后门」，模型把门放错边，再让人走一大段路圆回来。

**用在**：所有入画、出画、位移。场景的绝对方位留在空间地图里（`video-prompt/compile.md` 第四步），镜头里一律落成画左、画右、前景、深处；位移写步数和终点。过肩镜：越过 A 的右肩，A 在画面左前景。

**别这样写**：he comes in from the east door / 他从后门进来，走到她身边。

### 路径拆点 Path as waypoints

**写法**：

```text
Shot 4 (3s): his fingertips rest on the door frame. Shot 5 (3s): his palm slides onto the
window sill. Her shoulders tighten as his hand moves; her eyes follow it.
```

**防什么误读**：一句「从 A 一路到 B」，模型只给终态，手在中途瞬移。

**用在**：长路径动作。短镜装不下完整路径，就按路径上的落点拆成几镜，每镜写当前接触点、主动方的手、被动方的反应；被动方的反应是模型的进度条。单镜够长（一镜到底）时可以一镜写完，但要写出经过的点，见 `video-prompt/one-take.md` §1。

**别这样写**：his hand traces all the way from the door frame to the window.

---

## 5. 常见问题

| 问题 | 原因 | 改法 |
|---|---|---|
| 封了还出现 | 同义词没列全 | 按第 1 节列全 |
| negative 没用 | 写的是通用词 | 按五个方向倒推这场戏的错误版本 |
| 正文要的东西被抑制 | negative 太宽 | 逐条对照正文，写具体的人和动作 |
| 后半段人数错 | 中段被稀释 | 总锁里再写一次 |
| 处处强调 | CRITICAL 太多 | 只留 2–3 处 |
| 姿态转到别人身上、背景人一起动、衣服被补错、门在错的一边、动作瞬移 | 稿子把解释权留给了模型 | 按第 4 节写死 |

## 来源

见 `video-prompt/sources.md`。
