# Scene to Shots

## 场景

- 地点 / 时间 / 人物：
- 目标（谁想要什么）：
- 障碍（谁挡着）：
- 转折（结束时什么变了）：
- 与全片的关系：

## 镜头序列

| # | 画面 | 景别 | 机位 | 运动 | 时长 | 资产 | 声音 |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |

## 图像 prompt

```text
STYLE: ...
SUBJECT: {{character_token}} | {{action}}
ENVIRONMENT: {{scene_token}} | {{time}} | {{weather}}
SHOT: {{size}} | {{angle}} | {{lens}} | {{composition}}
LIGHT: ...
COLOR: ...
TEXTURE: ...
```

## 视频 motion

```text
MOTION: <subject action> | <camera movement> | <duration> | <speed>
```

## Negative

```text
extra face | duplicate head | morphing | extra limbs | flicker | jump cut | text | watermark
```

## 检查

- [ ] 每个镜头是否改变信息？
- [ ] 轴线 / 屏幕方向是否可读？
- [ ] 身份 / 场景是否用固定 token？
- [ ] 视频提示是否只写运动？
