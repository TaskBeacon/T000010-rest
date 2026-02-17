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

## Overview

This task runs one resting-state block with EC/EO conditions in sequence.
Participants read/listen to instructions and do not provide trial responses during rest windows.

## Runtime Modes

- Human (default): `python main.py`
- QA: `python main.py qa --config config/config_qa.yaml`
- Scripted sim: `python main.py sim --config config/config_scripted_sim.yaml`
- Sampler sim: `python main.py sim --config config/config_sampler_sim.yaml`

## Config Files

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
