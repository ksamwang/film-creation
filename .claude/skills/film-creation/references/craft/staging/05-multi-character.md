# 多人：表演区域、三角群与特征污染

## 核心判断

三人以上，模型会平均人脸：同一张脸、互换衣服、多手多腿。多人调度先定"这一刻谁和谁一组"，把其余人降成环境；再控制生成：一条提示里人物越少，身份越稳。

## 书里的原则

**表演区域**（《场面调度：影像的运动》7.1）：把多人场景划成几区，每组占一区，镜头只处理当前区，其余用景深、背身或暗部降级。AIGC 用法：区域表进分镜不进提示；每镜只写当前区人物，其余写 `a few people further back, out of focus`。

**三角群**（《电影镜头入门》Step2 三人、四人构图）：用身体朝向与视线组织三角形，多人场景拆成三角群，换组用一次走位或视线。AIGC 用法：先写主三角群（谁在前、谁在后左右），其他人物不进此镜。

**形态 A 和 L**（《电影镜头设计》10.1）：A 形一人在前、两人在后，前方者被共同注视；L 形一人侧翼、两人成一线。AIGC 用法：形态写成位置行，不写"孤立""结盟"；形态就是权力平面图。

**面向观众原则**（9.2）：关键台词与反应时，说话者与听者各有一侧脸可读；背对者承担被排除。AIGC 用法：写 `3/4 face camera`、`profile`、`back to camera`，不写"所有人看向对方"。

**四人以上**（第 11 章）：可单一正面排开，或有纵深地分前中后三层；长焦压缩拥挤，广角拉开孤立。AIGC 用法：先选平面或纵深，不混用；超过三人就拆层。

**层次**（《电影镜头入门》Step2）：前中后景各放一组信息，同一时刻只让一层"响"。AIGC 用法：每层给一个明确角色或物体，其余层降对比、背身或虚化。

## AIGC 执行

一条提示最好只有一两个承担动作的有名角色；多参考图模型能放下更多人，但同时动起来的人越多越乱。三人以上用三种方式之一：

1. 双人镜头拍关系，第三人另起一镜。
2. 单人反应镜头，背景只留 S1 的空间。
3. 分层合成：前景人物一张、后景群像一张，同一 S1 与光色，靠门框、柱子、遮挡接缝。

位置图用文本三角，挂齐三人参考图：

```text
Lin stands front and centre, turned three-quarters to the camera. Behind her, Gu stands back left in profile facing right, and Mei stands back right with her back to us.
A few guests further back are soft and low in contrast, their faces turned away.
```

模式 B 一条提示只放一个主语，三人分开生成再合成。A 形写 `one in front at centre, two behind at left and right`；L 形写 `one on the left flank, two in a line receding to the right`。形态定了再调站位，不边写边改。

换组只允许一次走位或视线转移。跨镜头复用方向锁。

四人以上先选方式。平面：`Wide shot, the three of them in one row facing the camera.` 适合仪式、审讯、排队。纵深：`Lin in the foreground with her back to us, Gu and Mei in the middle ground, a crowd behind, all in deep focus.` 适合空间与孤立。长焦压缩时有名角色放最前，背景只写 `a crowd in silhouette`，避免给背景人生成脸。

特征污染控制：每角色挂自己的参考图（纯文本时一条固定描述）；给可区分的轮廓或服装色；同画面只让一张脸清晰；用手部遮挡、背身、门框切断易崩部位；背景不写五官。失败模式（模式 B 进 NEGATIVE）：`merged faces | identical people | duplicate characters | extra limbs | swapped costumes | everyone facing camera | detailed background faces`。

## 检查清单

- [ ] 多人场景是否划成可命名表演区？
- [ ] 主三角群是否明确，其他人是否降为环境？
- [ ] 形态是否对应权力关系？
- [ ] 说话者与听者是否各有一侧脸可读？
- [ ] 同时承担动作的有名角色是否不超过两个？
- [ ] 换组是否有走位或视线过渡？
- [ ] 人群用平面还是纵深，是否只选一种？
- [ ] 是否只有一层承担主要信息？

## 常见错误

- 一条提示写五个名字 → 脸糊、衣服互换。改：挂齐参考图，只让一两人动；或拆双人/单人镜头、分层合成。
- 所有人正对镜头 → 画面平、关系消失。改：写 3/4、侧脸、背身。
- 相邻镜头左右互换 → 观众以为换人。改：方向锁逐字复用。
- 背景群众写得太具体 → 抢焦点、多出脸。改：`out-of-focus silhouettes`。
- 服装同色 → 模型分不清谁是谁。改：每个人物资产给一个差异色。
- 四人以上平面前后混写 → 站位混乱。改：先选平面或纵深。

## 与风格层接口

群戏导演档案只取一条组织原则：三角群、平面或纵深；摄影档案取长焦压缩或广角拉开。主三角群、前景层、背景层写进 SHOT，不写"群像感"。两镜组关系变了却无过渡，补视线或走位，不靠台词解释。

## 来源

见 `craft/sources.md#staging`。
