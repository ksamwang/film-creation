# IMDb Top 50 补充包（25 位）

目标：保留现有 100 位，新增 IMDb 榜上缺失的 25 位，总数 **125**。

## 统一要求

### 风格档案

路径：`references/directors/<slug>.md`

先读：
- `AGENT_BRIEF.md`
- `VISUAL_BRIEF.md`
- `references/directors/wong-kar-wai.md`（金标准）

硬指标：
- 15 节结构（八节核心 + 视觉配方 + 视觉参考等）。
- 正文 1200–1800 汉字。
- 视觉规则 ≥180 字，至少覆盖 4/6 维（景别、构图、空间、色彩、光线、材质），每项写“选 A 不选 B”。
- 镜头语法 ≥160 字，至少覆盖 3/7 维（机位、焦段、运动、静止、靠近、远离、权力）。
- 视觉配方七项齐全、具体。
- 反向约束 6–10 条，至少 4 条该导演专属。
- 同族差异：与现有 100 位中最近亲的一位对比，写成可执行判据，做互换测试。
- film-grab：用 WebFetch 验证导演页；404 改 `https://film-grab.com/?s=<name>`；不猜日期路径。

写作原则：
- 核心命题是“对人的基本看法”，不是题材总结。
- 不要用“他反复拍的是…他不相信…”的统一模板开头。
- 如果某位导演的视觉签名较弱（如 Hirani、Darabont、Mendes、Cameron），写他的类型工艺与场面调度，不要硬造作者神话。
- 同批内避免同质化：印度五位、史诗/奇观五位、身体/表演五位，各自要写出差异。

### AI 提示文件

路径：`references/prompts/<slug>.md`

先读：
- `references/prompting.md`
- `templates/ai-prompt.md`
- `references/prompts/wong-kar-wai.md`（金标准）

硬指标：
- 6 区块：风格锚点 / 图像提示 / 视频提示 / 负面提示 / 一致性锚点 / 平台备注。
- 英文风格锚点 40–80 词，具体到光/色/材质/构图/镜头。
- 图像 7 项、视频 3 项、负面提示从反向约束转写。
- 视频只给一种运镜。
- 一致性锚点锁色彩/镜头/光线/构图/材质 + 禁止漂移。
- 平台备注分 Midjourney、SDXL/ComfyUI、Runway/Kling/Sora/Veo。

## 批次

### A. 奇观 / 技术型（5）
christopher-nolan、denis-villeneuve、sam-mendes、james-cameron、peter-jackson

### B. 欧洲史诗 / 政治 / 狂欢（5）
david-lean、luchino-visconti、giuseppe-tornatore、gillo-pontecorvo、emir-kusturica

### C. 身体 / 表演 / 语调（5）
charlie-chaplin、frank-darabont、darren-aronofsky、alejandro-gonzalez-inarritu、taika-waititi

### D. 极简 / 道德 / 成长（5）
cristian-mungiu、jean-pierre-melville、milos-forman、masaki-kobayashi、majid-majidi

### E. 印度电影（5）
rajkumar-hirani、upendra、mrinal-sen、mani-ratnam、bimal-roy

## 交付

每份风格档案 + 对应 AI 提示文件。写完后：
- 跑 `python tools/check_structure.py`
- 跑 `python tools/check_visual.py`
- 跑 `python tools/check_prompts.py`
- 汇报完成文件、字数、检查结果、film-grab 未收录项。
