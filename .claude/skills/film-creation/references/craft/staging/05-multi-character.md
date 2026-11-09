# 多人：表演区域、三角群与特征污染

## 核心判断

三人以上，模型会平均人脸：同一张脸、互换衣服、多手多腿。多人调度先定"这一刻谁和谁一组"，把其余人降成环境；再控制生成：一条提示里人物越少，身份越稳。

## 书里的原则

**表演区域**（《场面调度：影像的运动》7.1）：把多人场景划成几区，每组占一区，镜头只处理当前区，其余用景深、背身或暗部降级。AIGC 用法：区域表进分镜不进提示；每镜只写当前区人物，其余写 `background group | defocused`。

**三角群**（《电影镜头入门》Step2 三人、四人构图）：用身体朝向与视线组织三角形，多人场景拆成三角群，换组用一次走位或视线。AIGC 用法：先写主三角群 `C1 front-center | C2 back-left | C3 back-right`，其他人物不进此镜。

**形态 A 和 L**（《电影镜头设计》10.1）：A 形一人在前、两人在后，前方者被共同注视；L 形一人侧翼、两人成一线。AIGC 用法：形态写成位置行，不写"孤立""结盟"；形态就是权力平面图。

**面向观众原则**（9.2）：关键台词与反应时，说话者与听者各有一侧脸可读；背对者承担被排除。AIGC 用法：写 `3/4 face camera`、`profile`、`back to camera`，不写"所有人看向对方"。

**四人以上**（第 11 章）：可单一正面排开，或有纵深地分前中后三层；长焦压缩拥挤，广角拉开孤立。AIGC 用法：先选平面或纵深，不混用；超过三人就拆层。

**层次**（《电影镜头入门》Step2）：前中后景各放一组信息，同一时刻只让一层"响"。AIGC 用法：每层给一个明确角色或物体，其余层降对比、背身或虚化。

## AIGC 执行

硬约束：一条提示最多两个有名角色。三人以上用三种方式之一：

1. 双人镜头拍关系，第三人另起一镜。
2. 单人反应镜头，背景写 `S1 | empty background`。
3. 分层合成：前景人物一张、后景群像一张，同一 S1 与光色，靠门框、柱子、遮挡接缝。

位置图用文本三角：

```text
MAIN TRIANGLE: C1 front-center | faces camera 3/4 | C2 back-left | profile right | C3 back-right | back to camera
ENV LAYER: background group | defocused | low contrast | no faces
```

A 形写 `C1 front-center | C2 back-left | C3 back-right`；L 形写 `C1 screen-left | C2 center | C3 screen-right back`。形态定了再调站位，不边写边改。

换组只允许一次走位或视线转移。跨镜头时，所有人物左右位置逐字复用方向锁；否则观众以为换位。

四人以上先选方式。平面：`front row C1 C2 C3 | all facing camera | wide`，适合仪式、审讯、排队。纵深：`foreground C1 back to camera | midground C2 C3 | background crowd | deep focus`，适合空间与孤立。长焦压缩时有名角色放最前，背景只写 `crowd | silhouettes | no faces`，避免给背景人生成脸。

特征污染控制：每角色一条固定 C token；给可区分的轮廓或服装色；同画面只让一张脸清晰；用手部遮挡、背身、门框切断易崩部位；背景不写五官。negative 写 `merged faces | identical people | duplicate characters | extra limbs | swapped costumes | everyone facing camera | detailed background faces`。

## 检查清单

- [ ] 多人场景是否划成可命名表演区？
- [ ] 主三角群是否明确，其他人是否降为环境？
- [ ] 形态是否对应权力关系？
- [ ] 说话者与听者是否各有一侧脸可读？
- [ ] 一条提示是否不超过两个有名角色？
- [ ] 换组是否有走位或视线过渡？
- [ ] 人群用平面还是纵深，是否只选一种？
- [ ] 是否只有一层承担主要信息？

## 常见错误

- 一条提示写五个名字 → 脸糊、衣服互换。改：拆双人/单人镜头，或分层合成。
- 所有人正对镜头 → 画面平、关系消失。改：写 3/4、侧脸、背身。
- 相邻镜头左右互换 → 观众以为换人。改：方向锁逐字复用。
- 背景群众写得太具体 → 抢焦点、多出脸。改：`silhouettes | defocused | no faces`。
- 服装同色 → 模型分不清谁是谁。改：每个 C token 给一个差异色。
- 四人以上平面前后混写 → 站位混乱。改：先选平面或纵深。

## 与风格层接口

群戏导演档案只取一条组织原则：三角群、平面或纵深；摄影档案取长焦压缩或广角拉开。主三角群、前景层、背景层写进 SHOT，不写"群像感"。两镜组关系变了却无过渡，补视线或走位，不靠台词解释。

## 来源

见 `_sources.md`；合并后见 `craft/sources.md#staging`。
