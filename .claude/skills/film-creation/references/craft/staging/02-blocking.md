# 走位：区域调度与逐个角色调度

## 核心判断

AIGC 里走位不能试错，必须一次写进画面：静止图写最终位置，视频写一条 3–5 秒路径。模型不会安排"谁挡谁、谁先转身"；不写屏幕坐标，它就把两人并排摆正、同时看镜头。走位交付的是可重复的位置与朝向，不是动作描述。

## 书里的原则

**区域调度**（《场面调度：影像的运动》3.2）：把场景切成门口、桌边、窗边等表演区，分配起始区与目标区，再安排区间移动。AIGC 用法：先写区域表 `Z1 door | Z2 counter | Z3 window`，每镜只写当前区；区域名不进提示，但决定构图。

**逐个角色调度**（3.2）：一次只排一个角色，沿其欲望走完整条路线，再合成。AIGC 用法：每个角色单写一行位置与朝向，再决定谁与谁同框；不要一句话写三条路线。

**调度人物和摄影机**（3.3）：调度只做四件事——强调主体、强调组中一个、把注意力从 A 转到 B、连接区域。AIGC 用法：每次位置变化必须对应其中一个功能，否则删掉；"随便走走"只会带来漂移。

**反向运动**（3.4）：两主体反向移动，距离与张力同时变化。AIGC 用法：写成 `Lin walks toward frame right as Gu walks toward frame left along the same line; they pass at the table.`；若模型把两人融合，就拆成单人镜头，在交叉点剪开。

## AIGC 执行

每人一句，字段固定：角色、起始区、终点、画面位置、朝向、视线。模式 A：

```text
Lin walks in from the door and stops at the counter, frame left of Gu, facing him and looking at his face.
Gu stays by the window at frame right, turned three-quarters toward the camera, eyes on something off-screen left.
```

模式 B 每人一行：`C1: Z1 to Z2 | stops screen-left of C2 | faces C2 | eyeline to C2 face`。

位置只用屏幕坐标：`screen-left / screen-right / frame third / foreground / background`。不要写"舞台左""靠近观众"。

静止图只写最终位置，不写过程。视频 prompt 只写一条路径：`Lin walks from the door to the counter and stops at frame left of Gu.`一条提示出现两次转身、一次绕桌、一次坐下，模型会中途变形；拆成两镜，用动作接动作。

强调三法：主体靠近镜头；被两人夹在中间；前景遮挡另一人。转移注意力优先用前景擦过：`A waiter crosses the foreground, hiding Gu for a beat, then Gu is revealed.`连接区域用道具传递或门口穿越，比横穿画面稳。

视线是走位的一半。说话者与听者各有一侧脸可读；背对者承担"被排除"。写 `C1 3/4 face camera`、`C2 profile`、`C3 back to camera`；写"大家看向彼此"只会得到三张正脸。

跨镜头走位要连续：上一镜右出，下一镜左入，中间补空镜或插入。方向锁定下后，所有镜头复用同一句：`Lin at frame left, Gu at frame right`。

## 检查清单

- [ ] 场景是否被切成可命名的表演区？
- [ ] 每个人物是否有独立的位置、朝向、视线？
- [ ] 位置是否用屏幕坐标而非文学描述？
- [ ] 每次移动是否完成强调、转移或连接之一？
- [ ] 视频是否只有一条移动路径？
- [ ] 关系变化是否用距离或遮挡表达？
- [ ] 反向运动是否用在真正的转折点？
- [ ] 跨镜头人物左右是否一致？

## 常见错误

- 写"两人激烈争吵"→ 两张正脸并排，没有关系。改：写谁在前景、谁背向、谁被挡。
- 一条提示让两人相向走 → 身体融合、腿部错乱。改：同框只给一条路径，或拆单人。
- 只写情绪不写位置 → 模型自由发挥，镜头接不上。改：位置、朝向、视线。
- 相邻镜头左右互换 → 观众以为换人。改：锁定方向字符串，逐镜复用。
- 走位绕远只为"好看"→ 路径变长、崩坏率上升。改：删掉不承担功能的移动。

## 与风格层接口

区域表与方向锁进 SHOT：摄影档案定机位高度与焦段，导演档案定"人被框住还是留出通道"。分镜每行一条位置行，不写表演形容词。剪辑按"出画—入画"对齐；两镜位置无法用同一平面图解释，就改走位，不加台词补救。

## 来源

见 `craft/sources.md#staging`。
