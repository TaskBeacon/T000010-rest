# Task Logic Audit

## 1. Paradigm Intent

- Task: Resting-state EEG baseline with alternating eyes-closed (EC) and eyes-open (EO) segments.
- Primary construct: Ongoing intrinsic neural activity during passive rest states.
- Manipulated factors: Resting condition (`EC` vs `EO`).
- Dependent measures: EEG signal quality/features segmented by condition; no trial-level behavioral accuracy metric.
- Key citations:
  - W2170702893
  - W2030737932
  - W2122451799

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: 1.
- Trials per block: 4 in human mode; 2 in QA/sim smoke profiles.
- Randomization/counterbalancing: Sequential condition generation from `task.conditions`.
- Condition weight policy:
  - `task.condition_weights` is not defined.
  - Runtime weight resolution is not used.
  - Generation is even/default via built-in condition generation and configured trial count.
- Condition generation method:
  - Built-in `BlockUnit.generate_conditions(order="sequential")`.
  - No custom condition generator is required because condition labels are simple (`EC`, `EO`).
  - Generated condition data passed into `run_trial.py` is a single token per trial (`"EC"` or `"EO"`).
- Runtime-generated trial values (if any):
  - No stochastic trial values are generated in `run_trial.py`.
  - Durations and triggers are read directly from config.

### Trial State Machine

1. State name: `block_instruction`
   - Onset trigger: none (instruction screens are not mapped to condition trigger codes).
   - Stimuli shown: `EC_instruction` or `EO_instruction` (plus optional voice prompt).
   - Valid keys: `task.key_list` (`space`) for continue.
   - Timeout behavior: waits until continue key press.
   - Next state: `fixation`.
2. State name: `fixation`
   - Onset trigger: `EC_onset` or `EO_onset`.
   - Stimuli shown: `EC_stim` ("请闭眼") or `EO_stim` (`+`).
   - Valid keys: none (`keys=[]`).
   - Timeout behavior: runs full configured duration, emits `EC_offset`/`EO_offset` on timeout end.
   - Next state: trial end.

## 3. Condition Semantics

- Condition ID: `EC`
- Participant-facing meaning: Eyes-closed resting segment.
- Concrete stimulus realization (visual/audio): Instruction textbox (`EC_instruction`), optional voice (`EC_instruction_voice`), then passive display text (`EC_stim: 请闭眼`).
- Outcome rules: No behavioral score; EEG segment is marked by onset/offset triggers.

- Condition ID: `EO`
- Participant-facing meaning: Eyes-open resting segment with central fixation.
- Concrete stimulus realization (visual/audio): Instruction textbox (`EO_instruction`), optional voice (`EO_instruction_voice`), then fixation cross (`EO_stim: +`).
- Outcome rules: No behavioral score; EEG segment is marked by onset/offset triggers.

Also document where participant-facing condition text/stimuli are defined:

- Participant-facing text source (config stimuli / code formatting / generated assets): `config/*.yaml -> stimuli` entries.
- Why this source is appropriate for auditability: All participant wording is declarative and versioned in config; no wording is hardcoded in `run_trial.py`.
- Localization strategy (how language variants are swapped via config without code edits): Replace localized text in `stimuli` blocks (and optional voice files) while preserving stimulus IDs.

## 4. Response and Scoring Rules

- Response mapping: Continue key (`space`) is used for instruction/goodbye waits; no response mapping during rest windows.
- Response key source (config field vs code constant): Config field `task.key_list`.
- If code-defined, why config-driven mapping is not sufficient: Not applicable.
- Missing-response policy: Not applicable during rest windows (responses disabled).
- Correctness logic: None (passive paradigm).
- Reward/penalty updates: None.
- Running metrics: Condition-wise timing and trigger markers only.

## 5. Stimulus Layout Plan

For every screen with multiple simultaneous options/stimuli:

- Screen name: Not applicable.
- Stimulus IDs shown together: Single stimulus per frame in trial flow (`*_instruction` then `*_stim`).
- Layout anchors (`pos`): Instruction text centered; EO fixation cross centered.
- Size/spacing (`height`, width, wrap): Textbox uses `letterHeight: 0.78`, `size: [20, 5]`; fixation cross uses default text style.
- Readability/overlap checks: Single-element screens avoid overlap risk.
- Rationale: Resting protocols prioritize minimal visual complexity and clear state instructions.

## 6. Trigger Plan

Map each phase/state to trigger code and semantics.

- `exp_onset` (98): experiment start.
- `block_onset` (100): block start.
- `block_instruction`: no condition-specific trigger.
- `fixation` with `EC`: onset 10, offset 11.
- `fixation` with `EO`: onset 20, offset 21.
- `block_end` (101): block end.
- `exp_end` (99): experiment end.

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style (simple single flow / helper-heavy / why): Simple single mode-aware flow (`human|qa|sim`) for auditability.
- `utils.py` used? (yes/no): No.
- If yes, exact purpose (adaptive controller / sequence generation / asset pool / other): Not applicable.
- Custom controller used? (yes/no): No.
- If yes, why PsyFlow-native path is insufficient: Not applicable.
- Legacy/backward-compatibility fallback logic required? (yes/no): No.
- If yes, scope and removal plan: Not applicable.

## 8. Inference Log

List any inferred decisions not directly specified by references:

- Decision: Use `180 s` per EC/EO segment in human mode.
- Why inference was required: Selected references motivate resting-state condition contrasts but do not enforce a single universal segment duration for this implementation.
- Citation-supported rationale: Reliability-focused resting EEG literature supports multi-minute segments for stable features.

- Decision: Use sequential EC/EO ordering in this baseline task.
- Why inference was required: References emphasize condition comparison but do not prescribe one fixed order for all studies.
- Citation-supported rationale: Deterministic ordering simplifies reproducibility and trigger audit in baseline acquisition.

## Contract Note

- Participant-facing labels/instructions/options are config-defined.
- `src/run_trial.py` does not hardcode participant-facing localization text.