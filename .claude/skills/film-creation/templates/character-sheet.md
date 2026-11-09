# 人物角色表提示词规范

> 每个角色一张 3:2 三面板表：左无头正面、中背面、右 3/4 特写。全表只有一张脸。
> skill 只定义格式与提示词，不规定生成步骤；怎么执行由 LLM 决定。

## Trait card（先填）

```text
age | build | face | hair | outfit | palette (hex) | props | headwear
```

## 固定格式

- **画幅**：3:2 横向，三个等宽、等高面板。
- **背景**：统一纯色 `#D9D9D9`；均匀、无阴影的棚拍光。
- **左面板**：正面全身，无头。
  - 颈根以上（脸、耳、头发、头饰）全部是 `#D9D9D9`，与背景无缝；无轮廓、无阴影、无纹理、无渐变、无遮罩边。
  - 颈根到鞋底完整可见；自然站立，肩放松，手臂下垂，手空。
  - 保持全身构图；头顶留空；不裁切脖子、不放大身体、不上移。
  - 头饰或衣领若延伸到颈根以下，保留颈根及以下部分。
  - 干净的图形切面；不得出现颈断面、伤口、损伤。
- **中面板**：背面全身，头可见，无脸。
  - 与左面板同身体比例、姿态、机位高度、距离、透视；同一地面基线。
  - 不得独立缩放或重新居中。
- **右面板**：3/4 头肩特写，从胸口以上。
  - 身体和脸转向观众左侧（角色右侧），目光直视镜头。
  - 与左/中同身份、同服装、同头饰。
  - 全表只有这一张脸。
- **对齐**：
  - 颈根、肩线、肘、腰、胯、膝、踝、鞋底在相同垂直坐标。
  - 躯干长度、四肢长度、肩宽、站距、整体比例一致；同一地面基线；各自在面板垂直中轴。
  - 左肩以上空白 = 中面板头部所占区域；不得拉伸、压缩、位移、缩放。

## 提示词

正面写目标效果（多数图像模型没有 negative 参数，正文里的「no ...」反而会招来那样东西）。

```text
CHARACTER SHEET, 3:2 horizontal, three equal side-by-side panels on one seamless solid #D9D9D9 background, even shadowless studio lighting.

IDENTITY (all panels): {{age}}, {{build}}, wearing {{outfit}} ({{palette hex}}), carrying {{props}}.
HEAD (middle and right panels): {{face}}, {{hair}}, {{headwear}}.

LEFT PANEL: front full-body view from the neck base down to the shoe soles. The area above the neck base is plain #D9D9D9, continuous with the background, so the figure reads as a clean headless garment-and-body reference cut flat at the neck base. Natural standing pose, shoulders relaxed, arms hanging, hands empty. Same framing and scale as the middle panel. Headwear or collars that reach below the neck base keep that lower part.

MIDDLE PANEL: full-body back view, head visible from behind. Same outfit, proportions, camera height, distance and body scale; shared ground baseline.

RIGHT PANEL: three-quarter head-and-shoulders portrait from the chest up, body and face turned toward the viewer's left, eyes looking into the lens. Same person and outfit. This is the single face shown on the sheet.

ALIGNMENT: neck base, shoulder line, elbows, waist, hips, knees, ankles and shoe soles sit at the same heights in the left and middle panels; same torso length, limb length, shoulder width and stance width; each figure centred in its panel.
```

以参考图做变体时，开头加一句：`Same person as the reference image: keep face, skin tone, body shape and hair identical; change only the outfit and condition described below.`

## Negative（模型有 negative 参数时）

```text
extra face | duplicate head | neck cross-section | wound | outline | shadow | gradient | mask edge | cropped body | inconsistent outfit | different body scale | misaligned panels | text | watermark
```
