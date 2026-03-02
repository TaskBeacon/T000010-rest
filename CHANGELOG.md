# CHANGELOG

All notable development changes for T000010-rest are documented here.

## [Unreleased]

### Changed
- Refactored `src/run_trial.py` to use `psyflow`'s native `next_trial_id()` and removed legacy internal `_next_trial_id` and `_deadline_s` boilerplate.

## [1.2.0] - 2026-03-02

### Added
- Added required reference artifacts:
  - `references/references.yaml`
  - `references/references.md`
  - `references/parameter_mapping.md`
  - `references/stimulus_mapping.md`
  - `references/task_logic_audit.md`

### Changed
- Refactored `src/run_trial.py` to remove leftover template labels (`cue/target/feedback`) and use task-native trial units (`instruction`, `rest`).
- Removed zero-duration terminal feedback stage from trial runtime flow.
- Updated responder context stage naming for rest window to `fixation`.
- Updated `README.md` to include required configuration subsections and controller logic section.
- Updated all `config/*.yaml` files with encoding-clean participant-facing Chinese text.
- Updated `taskbeacon.yaml` metadata (`release_tag`, evidence paths, maintainer block).

## [1.1.1] - 2026-02-18
- Refactored responder context phase names in `src/run_trial.py` to task-specific labels (removed generic MID-style phase naming).
- Updated stage comments in `src/run_trial.py` to phase-aligned labels for cleaner auditability.
- Updated `README.md` to keep runtime phase documentation aligned with the implemented trial context phases.

### Fixed
- Removed legacy stage comment patterns (`cue/anticipation/target/feedback`) from trial runtime code.

## [1.1.0] - 2026-02-17

### Added
- Added mode-aware `main.py` flow for human/qa/sim execution.
- Added split runtime configs:
  - `config/config.yaml`
  - `config/config_qa.yaml`
  - `config/config_scripted_sim.yaml`
  - `config/config_sampler_sim.yaml`
- Added task-local responder scaffold:
  - `responders/__init__.py`
  - `responders/README.md`
  - `responders/task_sampler.py`
- Added `outputs/.gitkeep` and standardized output folder handling.

### Changed
- Refactored `src/run_trial.py` to include responder trial-context plumbing via `set_trial_context(...)`.
- Added no-response capture window in rest stage using `capture_response(...)` for simulation compatibility.
- Upgraded trigger config to structured schema (`triggers.map/driver/policy/timing`).
- Updated `taskbeacon.yaml` to declare contract adoption (`contracts.psyflow_taps: v0.1.0`).
- Updated `.gitignore` for standardized outputs and QA/sim artifact handling.
- Updated `README.md` metadata and mode/config usage documentation.

### Fixed
- No task-logic bug fixes in this alignment release.

### Verified
- `psyflow-validate <task>` passes contract checks.
- `psyflow-qa <task> --config config/config_qa.yaml --no-maturity-update` passes.
- `python main.py sim --config config/config_scripted_sim.yaml` runs and writes sim artifacts.
