# 摄影指导层（29 位）

在 125 位导演之外，新增 29 位摄影指导（Director of Photography）。这不是导演档案的复制：DP 不负责叙事与表演，负责**光、镜头、色彩、运动、格式**。最终用途仍然是 AI 图像/视频生成。

## 目录

- 档案：`references/cinematographers/<slug>.md`
- AI 提示：`references/prompts-cinematographers/<slug>.md`

## 档案结构（14 节）

```
## 一句话签名
## 核心命题（视觉观）
## 人物关系（与导演/演员/空间）
## 视觉规则
## 镜头语法
## 光线与色彩
## 时间与运动
## 制作条件
## 反向约束
## 误读警告
## 可复用做法（3 条）
## 混搭接口
## 同族差异
## 视觉配方
## 视觉参考
```

### 各节写法

- **核心命题（视觉观）**：他反复如何看世界？光、空间、身体的关系是什么？不是叙事主题。
- **人物关系**：常与哪些导演合作；他如何服从/改写导演的语法；演员与空间的关系。
- **视觉规则**：景别、构图、空间、色彩、光线、材质；至少 4/6 维，每项写“选 A 不选 B”。
- **镜头语法**：机位、焦段、运动、静止/靠近/远离、权力；至少 3/7 维。
- **光线与色彩**：光源、光比、色温、曝光、色彩策略；至少 150 字，必须具体到选择。
- **时间与运动**：长镜/剪辑、手持/稳定、帧率、快门、运动模糊。
- **制作条件**：胶片/数字、画幅、镜头品牌/焦段、灯具、洗印/调色；必须具体。
- **反向约束**：6–10 条可执行禁令，至少 4 条该 DP 专属。
- **同族差异**：与最近亲的另一位 DP 比，写可执行判据，做互换测试。
- **视觉配方**：参考画幅、镜头/焦段、机位与运动、色彩、光线、材质/美术、构图，七项具体。

## 硬指标

- 正文 1200–1800 汉字。
- 视觉规则 ≥180 字（至少 4/6 维）。
- 镜头语法 ≥160 字（至少 3/7 维）。
- 光线与色彩 ≥150 字。
- 反向约束 6–10 条。
- 视觉配方七项齐全。

## AI 提示文件

6 区块，与导演提示一致：

- 风格锚点：英文 40–80 词，具体到光/色/材质/构图/镜头。
- 图像提示：主体/场景、景别/构图、镜头/焦段、光线、色彩、材质。画幅由用户/平台设定，不写入提示。
- 视频提示：镜头运动只选一种；主体运动；时长/帧率/运动模糊。
- 负面提示：从反向约束逐条转写。
- 一致性锚点：色彩/镜头/光线/构图/材质 + 禁止漂移。
- 平台备注：Midjourney、SDXL/ComfyUI、Runway/Kling/Sora/Veo。

## film-grab

- 摄影指导页：`https://film-grab.com/category/dops/<slug>/`
- 404 时用：`https://film-grab.com/?s=<name>`
- 仍无结果时，可用 MUBI / Criterion Channel 等可核验页面补充。
- 不猜日期路径。

## 批次

### A. 自然光 / 长镜 / 浸入（6）
emmanuel-lubezki（样片，已写）、john-toll、andrew-lesnie、allen-daviau、rodrigo-prieto、rachel-morrison

### B. 硬光 / 高反差 / 深焦（6）
robert-richardson、roger-deakins、janusz-kaminski、gordon-willis、gregg-toland、john-alcott

### C. 色彩 / 格式 / 史诗（6）
vittorio-storaro、geoffrey-unsworth、freddie-young、leon-shamroy、robert-surtees、tonino-delli-colli

### D. 现代 / 数字 / 类型（6）
hoyte-van-hoytema、wally-pfister、mauro-fiore、dan-laustsen、matthew-libatique、dean-cundey

### E. 风格化 / 作者合作 / 古典（5）
michael-ballhaus、larry-fong、robert-elswit、conrad-l-hall、joseph-ruttenberg

## 交付

每份档案 + 对应提示文件。写完后跑：
- `python tools/check_dp.py`
- `python tools/check_prompts.py prompts-cinematographers 29`
- 汇报完成文件、字数、检查结果、film-grab 未收录项。
