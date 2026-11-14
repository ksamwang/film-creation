# 视频提示词层 · 来源

书目同 `craft/sources.md`。视频提示词的写法在书里没有专门讲：本层的段落结构、写法规则和长度分档，是对社区流传的、成片效果较好的多镜头视频提示词做的**模式归纳**（谁负责什么、每条约束防什么误读、哪些地方有意重复），加上本包已有的镜头、分镜、短剧标准，属本包整理。归纳所用的社区提示词原文不收入本包；所有示例为本包原创。

长度与效果的关系、各段落对具体模型的作用，都是经验判断，未经本包实测（仓库根目录 DESIGN.md §9）。

## index

| 概念 / 规则 | 来源 |
|---|---|
| 提示词是压缩的制作文件，各段落对应剪辑、导演、摄影、美术、调色、声音、场记的工作 | 属本包整理 |
| 核心是预判模型的误读并提前封住 | 社区提示词模式归纳，属本包整理 |
| 三档长度（轻量 / 标准 / 重型）及字数区间 | 社区提示词模式归纳；区间为经验值，未经实测 |
| CLIP 系模型的截断与短提示词写法 | `references/aigc/prompt-syntax.md` §0 |
| 先全局、再逐镜、最后再锁；全局段跨段逐字复用 | 社区提示词模式归纳，属本包整理 |
| 情绪三件套：行为 + 理解 + 不是什么 | 社区提示词模式归纳；表演写微动作的原则见 `craft/performance/index.md` |

## anatomy

| 概念 / 规则 | 来源 |
|---|---|
| 十九个段落及其顺序 | 社区提示词模式归纳，属本包整理 |
| 剪辑合同：镜头数、时间码、切换方式 | 社区提示词模式归纳；镜头数上限见 `references/drama/06-storyboard.md` |
| 硬约束列全同义说法（音乐、文字） | 社区提示词模式归纳；两条固定约束见 `references/drama/07-segment-prompt.md` |
| 风格写画面特征，机身型号只做可选锚点 | 属本包整理 |
| 人数锁、识别特征锁、参考图「只管什么」 | 社区提示词模式归纳；参考图用法见 `references/aigc/assets.md` |
| 空间地图与轴线 | `storyboard/continuity.md`、`camera/recipes/dialogue-two.md` |
| 首帧已在动作中 | 社区提示词模式归纳，属本包整理 |
| 焦段写成视野效果、焦段锁 | `camera/lexicon-shot.md` 焦段一节 |
| 摄影机写成操作员的行为；静止要写死 | 社区提示词模式归纳；运镜词汇见 `camera/lexicon-move.md` |
| 光只写画面里的光源 | `camera/lexicon-light.md`，属本包整理 |
| 色彩用比例写 | 社区提示词模式归纳 |
| 防 AI 质感、物理后果 | 社区提示词模式归纳，属本包整理 |
| 逐镜时间码、一镜一个动作、结束状态 | 社区提示词模式归纳；一镜一个动作见 `references/drama/06-storyboard.md` §2 |
| 只有说话人动嘴、不看镜头 | `references/drama/07-segment-prompt.md`；社区提示词模式归纳 |
| 台词保留原语言、只写画内声、静默写出来 | 社区提示词模式归纳；声音分工见 `craft/sound/index.md` |
| 总锁、「CRITICAL」限量、冗余只给关键不变量 | 社区提示词模式归纳，属本包整理 |
| negative 写这场戏的错误版本 | 社区提示词模式归纳；模式 B 的 NEGATIVE 原则见 `references/aigc/prompt-syntax.md` |
| 四条写法原则（识别特征锁、正面优先、三档长度、机身锚点） | 属本包整理；与 `references/aigc/prompt-syntax.md` 单镜规则的关系见该文件 |

## compile

| 概念 / 规则 | 来源 |
|---|---|
| 分镜脚本字段与提示词段落的对应 | 属本包整理；分镜脚本格式见 `storyboard/breakdown.md` |
| 生成单位的切分原则 | `references/drama/06-storyboard.md`、`references/aigc/workflow.md`，属本包整理 |
| 读戏卡进戏的意图 | `storyboard/breakdown.md` 第一步 |
| 生成余量、后期变速 | `storyboard/pacing.md` §6 |
| 预判误读的三种处理位置、自检清单 | 属本包整理 |
| 场 5 段 B 示例 | 本包原创，延续 `storyboard/breakdown.md` 的场 5 |
| 竖屏短剧以 drama/07 为准 | `references/drama/07-segment-prompt.md` |
