# T000010-rest 源摘录

## 1. README 关键点

- 该任务是一个静息态区块，按顺序运行 EC 和 EO 两个条件。
- `Trial-Level Flow` 明确列出两个阶段：`block_instruction` 和 `fixation`。
- 条件顺序由 `BlockUnit.generate_conditions(order="sequential")` 决定。

## 2. 配置关键点

- `task.conditions` 只有 `EC` 和 `EO`。
- `stimuli.EC_instruction` 和 `stimuli.EO_instruction` 是参与者可见的区块说明。
- `stimuli.EC_stim` 的屏显文本是 `请闭眼`。
- `stimuli.EO_stim` 的屏显文本是 `+`。
- `timing.EC_duration` 和 `timing.EO_duration` 都是 `180`。
- `task.voice_enabled` 默认开启，因此说明阶段可能伴随语音。

## 3. run_trial.py 关键点

```python
# block_instruction
set_trial_context(
    instruction_unit,
    phase="block_instruction",
    deadline_s=None,
    valid_keys=list(getattr(settings, "key_list", []) or []),
    stim_id=f"{condition_id}_instruction",
)
instruction_unit.show()
```

```python
# fixation
rest_duration = getattr(settings, f"{condition_id}_duration")
set_trial_context(
    rest_unit,
    phase="fixation",
    deadline_s=rest_duration,
    valid_keys=[],
    stim_id=f"{condition_id}_stim",
)
rest_unit.capture_response(
    keys=[],
    duration=rest_duration,
)
```

- `block_instruction` 是等待继续的说明阶段，没有固定时长。
- `fixation` 是被动静息窗口，持续时间来自条件对应的 `*_duration`。
- 两个条件在流程结构上相同，差异只在说明文本和静息提示文本。

## 4. 绘图映射

- `EC` 和 `EO` 各保留为一条时间线。
- 每条时间线都包含两个阶段：`block_instruction` 和 `fixation`。
- 静息窗口在图中按 `180 s` 显示。
- 由于当前环境的字体栈无法稳定直接渲染中文，说明阶段和 `请闭眼` 提示改为 `image_ref` 资源，以保留原始中文内容。

