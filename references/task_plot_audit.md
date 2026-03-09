# Task Plot Audit

- generated_at: 2026-03-10T00:17:34
- mode: existing
- task_path: E:\Taskbeacon\T000010-rest

## 1. Inputs and provenance

- E:\Taskbeacon\T000010-rest\README.md
- E:\Taskbeacon\T000010-rest\config\config.yaml
- E:\Taskbeacon\T000010-rest\src\run_trial.py

## 2. Evidence extracted from README

- Trial-Level Flow table not found; run_trial.py used as primary source.

## 3. Evidence extracted from config/source

- EC: phase=block instruction, deadline_expr=None, response_expr=n/a, stim_expr=f'{condition_id}_instruction'
- EC: phase=fixation, deadline_expr=rest_duration, response_expr=rest_duration, stim_expr=f'{condition_id}_stim'
- EO: phase=block instruction, deadline_expr=None, response_expr=n/a, stim_expr=f'{condition_id}_instruction'
- EO: phase=fixation, deadline_expr=rest_duration, response_expr=rest_duration, stim_expr=f'{condition_id}_stim'

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 4
- screens_per_timeline: 6
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.044, right=0.044, blank=0.171
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0444, 'right_ratio': 0.0444, 'blank_ratio': 0.1712}
- validator_warnings:
  - timelines[0].phases[0] missing duration_ms; renderer will annotate as n/a.
  - timelines[0].phases[1] missing duration_ms; renderer will annotate as n/a.

## 7. Output files and checksums

- E:\Taskbeacon\T000010-rest\references\task_plot_spec.yaml: sha256=1e5881a8f6609a68eec0e94f08ac596d3b987e6badb52de4a03abbc9c00f0e8b
- E:\Taskbeacon\T000010-rest\references\task_plot_spec.json: sha256=9487e946aa6a9a3e728c952b92216a51e766f66c02f12e8470c03064a6cde216
- E:\Taskbeacon\T000010-rest\references\task_plot_source_excerpt.md: sha256=a4d250278c6845c7b4f24ec41d1668d2dd2bd2b3cc5095055ea409cf1277d49a
- E:\Taskbeacon\T000010-rest\task_flow.png: sha256=2ff5cf71e6a107c21ca6b8cbdbce4bb34e2e242518a3260863880424efe9380e

## 8. Inferred/uncertain items

- EC:block instruction:unresolved variable 'None'
- EC:fixation:unable to resolve duration from 'getattr(settings, f'{condition_id}_duration')'
- EO:block instruction:unresolved variable 'None'
- EO:fixation:unable to resolve duration from 'getattr(settings, f'{condition_id}_duration')'
- collapsed equivalent condition logic into representative timeline: EC, EO
- unparsed if-tests defaulted to condition-agnostic applicability: bool(getattr(settings, 'voice_enabled', True))
