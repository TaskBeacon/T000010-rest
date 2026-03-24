# Task Plot 审计

- generated_at: 2026-03-23T23:36:29.7436277+08:00
- mode: existing
- task_path: E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest

## 1. 输入与来源

- `README.md`
- `config/config.yaml`
- `src/run_trial.py`

## 2. README 提取证据

- 任务是静息态区块，按顺序运行 `EC` 和 `EO` 两个条件。
- `Trial-Level Flow` 明确列出两个阶段：`block_instruction` 和 `fixation`。
- 说明阶段不提供试次反应，静息窗口阶段为被动保持状态。

## 3. config 与源码提取证据

- `task.conditions` 只有 `EC` 和 `EO`。
- `stimuli.EC_instruction` / `stimuli.EO_instruction` 是条件对应的区块说明文本。
- `stimuli.EC_stim` 是 `请闭眼`，`stimuli.EO_stim` 是 `+`。
- `timing.EC_duration` 和 `timing.EO_duration` 都是 `180`。
- `block_instruction` 使用 `set_trial_context(... phase="block_instruction", deadline_s=None, valid_keys=[...])`，随后调用 `show()`。
- `fixation` 使用 `set_trial_context(... phase="fixation", deadline_s=rest_duration, valid_keys=[])`，随后调用 `capture_response(keys=[], duration=rest_duration)`。
- 说明阶段是等待继续的开放式阶段；静息窗口阶段是 180 秒的被动保持阶段。

## 4. 映射到 task_plot_spec

- `root_key` 为 `task_plot_spec`。
- `spec_version` 为 `0.2`。
- 保留两条时间线：`EC` 和 `EO`。
- 每条时间线保留两个阶段：`block_instruction` 和 `fixation`。
- `fixation` 的时长在图中显式写为 `180 s`，并在 spec 中按 `180000 ms` 记录。
- 由于当前环境下直接文本渲染中文不稳定，`EC_instruction`、`EO_instruction` 和 `EC_stim` 改为 `image_ref` 资源，以保留可读中文内容。
- `EO_stim` 仍使用直接文本 `+`，因为该内容在图中可以稳定显示。

## 5. 样式决策与理由

- 继续使用 timeline collection，因为这是 task-plot 的固定图型。
- `EC` 和 `EO` 之所以分成两条时间线，是因为说明文本与静息提示文本不同。
- `block_instruction` 不强行伪造固定时长，保持为空值并由文本语义表达“按空格继续”。

## 6. 渲染参数与 QA

- `output_file`: `task_flow.png`
- `dpi`: `300`
- `max_conditions`: `2`
- `screens_per_timeline`: `4`
- `screen_overlap_ratio`: `0.1`
- `screen_slope`: `0.08`
- `screen_slope_deg`: `25.0`
- `screen_aspect_ratio`: `1.4545454545454546`
- `qa_mode`: `local`
- `auto_layout_feedback`:
  - `layout pass 1: crop-only; left=0.046, right=0.046, blank=0.151`
- `auto_layout_feedback_records`:
  - `pass: 1`
    `metrics`: `{'left_ratio': 0.0459, 'right_ratio': 0.0459, 'blank_ratio': 0.1507}`
- `validator_warnings`:
  - `timelines[0].phases[0] missing duration_ms; renderer will annotate as n/a.`
  - `timelines[1].phases[0] missing duration_ms; renderer will annotate as n/a.`

## 7. 输出文件

- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\references\task_plot_spec.yaml`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\references\task_plot_spec.json`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\references\task_plot_source_excerpt.md`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\references\ec_instruction_text.png`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\references\eo_instruction_text.png`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\references\ec_rest_text.png`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000010-rest\task_flow.png`

## 8. 说明

- 第一版自动推断时，静息窗口时长没有被正确展开。
- 已改为显式 `180 s`，并重新渲染最终流程图。
- 当前最终图已能正常显示中文说明内容和静息提示。

