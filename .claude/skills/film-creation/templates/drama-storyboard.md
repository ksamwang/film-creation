# 短剧分镜（storyboard）

> 写法见 `references/drama/06-storyboard.md`；字段与编译见 `references/drama/standard.md` P6、P7。

## 片段表

**片段 1** · 场景：`场景 · 区域_时段` · 合计 __ 秒（上限 __） · 引用造型 __ 个（上限 __）

| # | 秒 | 景别 size | 角度 angle | 运镜 move | 画面（站位 · 起点 → 动作 → 落点；造型写 `@[名字]`） | 台词（谁 · 语气 · 原文） |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |

结束状态（下一段的起点）：谁在哪 / 朝哪 / 拿着什么

## 枚举

- size：`extreme_wide` `wide` `full` `medium` `medium_close` `close` `extreme_close`
- angle：`eye_level` `high` `low` `overhead` `dutch` `over_shoulder` `pov`
- move：`static` `push_in` `pull_out` `pan` `tilt` `tracking` `orbit` `crane` `handheld` `zoom`

## JSON

```json
{"segments": [
  {"scene": "", "shots": [
    {"duration_s": 3, "size": "medium", "angle": "eye_level", "move": "static", "text": "", "dialogue": [{"who": "", "emotion": "", "text": ""}]}
  ]}
]}
```

## 时长速算

- 台词：中文字数 ÷ 4（快念 ÷ 5.5）+ 1–2 秒；英文词数 ÷ 2.5–3 + 1–2 秒
- 动作：3–5 秒 2–3 个
- 反应：1.5–3 秒

## 检查

- [ ] 每段一个子场景，时长贴近上限，相邻同场景段已合并？
- [ ] 引用造型（含场景）≤ 参考图上限，每段 ≤8 镜？
- [ ] 一镜一个说话人，其他人不抢正脸？
- [ ] 左右按画面、前后按机位，锚点在场景图里？
- [ ] `text` 里没有景别术语、外貌重复、否定堆叠？
- [ ] 段与段的结束 / 开始状态接得上？
