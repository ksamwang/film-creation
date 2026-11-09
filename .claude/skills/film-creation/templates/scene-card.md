# Scene to Shots

## 场景

- 地点 / 时间 / 人物：
- 目标（谁想要什么）：
- 障碍（谁挡着）：
- 转折（结束时什么变了）：
- 与全片的关系：

## 镜头序列

| # | 画面（起点 → 动作 → 落点） | 景别 | 机位 | 运动 | 时长 | 资产 / 参考图 | 声音 |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |

## 镜头提示（模式 A）

```text
参考图 1 是 {C1}，参考图 2 是 {S1}。
{C1} 在画左，{起点}；{动作 1}，{动作 2}，停在 {落点}。
{景别}，{机位}，{运镜}。{光线变化}。
```

## 镜头提示（模式 B）

```text
STYLE: ...
SUBJECT: {character_token} | {action}
ENVIRONMENT: {scene_token} | {time} | {weather}
SHOT: {size} | {angle} | {lens} | {composition}
LIGHT: ...
COLOR: ...
MOTION（图生视频）: <subject action> | <camera movement> | <duration>
NEGATIVE: extra face | duplicate head | morphing | extra limbs | flicker | text | watermark
```

## 检查

- [ ] 每个镜头是否改变信息？
- [ ] 轴线 / 画面方向是否可读，前后深度按机位写了？
- [ ] 身份 / 场景靠参考图（或逐字复用的文本锁），正文没重复外貌？
- [ ] 一镜不超过 2–3 个动作？图生视频只写运动？
