# Resting-state Task (EC + EO)

![Maturity: piloted](https://img.shields.io/badge/Maturity-piloted-16a34a?style=flat-square&labelColor=111827)

| Field | Value |
|---|---|
| Name | Resting-state Task (EC + EO) |
| Version | v1.1.0 |
| URL / Repository | https://github.com/TaskBeacon/T000010-rest |
| Short Description | Eyes-closed / eyes-open resting-state paradigm for EEG baseline acquisition |
| Created By | Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated | 2026-02-17 |
| PsyFlow Version | 0.1.9 |
| PsychoPy Version | 2025.1.1 |
| Modality | Behavior/EEG |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |

## 1. Task Overview

This task runs one resting-state block with EC/EO conditions in sequence.
Participants read/listen to instructions and do not provide trial responses during rest windows.

## 2. Task Flow

### Block-Level Flow

- Load runtime settings, initialize triggers/window, and register stimuli.
- Run condition sequence (EC/EO) per block configuration.
- Save outputs and close runtime resources.

### Trial-Level Flow

- `block_instruction`: condition-specific instruction display.
- `rest_state`: passive rest window for the configured duration.

## Runtime Modes

- Human (default): `python main.py`
- QA: `python main.py qa --config config/config_qa.yaml`
- Scripted sim: `python main.py sim --config config/config_scripted_sim.yaml`
- Sampler sim: `python main.py sim --config config/config_sampler_sim.yaml`

## 3. Configuration Summary

- `config/config.yaml`: base human run profile
- `config/config_qa.yaml`: QA/dev profile (short smoke run)
- `config/config_scripted_sim.yaml`: scripted simulation profile
- `config/config_sampler_sim.yaml`: task-local sampler simulation profile

## Outputs

- Human: `outputs/human/`
- QA: `outputs/qa/`
- Scripted sim: `outputs/sim/`
- Sampler sim: `outputs/sim_sampler/`

## Task Notes

- Trigger schema uses structured `triggers.map/driver/policy/timing`.
- Trial context for responder plugins is set in `src/run_trial.py` via `set_trial_context(...)`.
- Sampler implementation for this task is in `responders/task_sampler.py`.

### Runtime Context Phases
| Phase Label | Meaning |
|---|---|
| `block_instruction` | block instruction stage in `src/run_trial.py` responder context. |
| `rest_state` | rest state stage in `src/run_trial.py` responder context. |

## 4. Methods (for academic publication)

This resting-state task presents alternating condition instructions (e.g., eyes-open/eyes-closed) followed by passive rest windows with no active response requirement. Trial context labels separate instruction and rest stages for consistent QA/simulation logging. Timing and trigger events are controlled to support auditable baseline acquisition workflows.

