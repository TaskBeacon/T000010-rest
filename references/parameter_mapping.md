# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `conditions` | `task.conditions` | `['EC', 'EO']` | `W2170702893` | Resting-state protocol variants are treated as distinct acquisition conditions (eyes-open vs eyes-closed style baselines). | `inferred` | Implemented as explicit condition tokens for auditable sequencing. |
| `trial_per_block` | `task.trial_per_block` | `4` (human), `2` (qa/sim) | `W2122451799` | Reliability work motivates repeated resting segments for stable feature estimates. | `inferred` | QA/sim uses reduced counts for smoke checks only. |
| `EC_duration` | `timing.EC_duration` | `180` (human), `1.0` (qa/sim) | `W2122451799` | Reliability emphasis supports multi-minute resting segments rather than very short windows. | `inferred` | `180 s` is an implementation decision for practical EEG baseline collection. |
| `EO_duration` | `timing.EO_duration` | `180` (human), `1.0` (qa/sim) | `W2030737932` | Eyes-open resting/fixation states are used to characterize ongoing network and alpha-related variation. | `inferred` | Same duration as EC for balanced acquisition. |
| `condition_order` | `BlockUnit.generate_conditions(order=...)` | `sequential` | `W2170702893` | Condition-specific dynamic resting states are compared across well-defined acquisition periods. | `inferred` | Sequence is fixed for reproducibility in this implementation. |
| `response_keys` | `task.key_list` | `['space']` | `W2170702893` | Resting-state windows are passive; response is only required to continue instruction/transition screens. | `implemented` | No response keys are valid during rest windows (`keys=[]`). |
| `EC_onset` | `triggers.map.EC_onset` | `10` | `W2170702893` | Distinct condition-wise onset markers are required for downstream EEG segmentation. | `implemented` | Marker emitted at rest-window onset for EC trials. |
| `EC_offset` | `triggers.map.EC_offset` | `11` | `W2170702893` | Distinct condition-wise offset markers are required for downstream EEG segmentation. | `implemented` | Marker emitted at rest-window offset for EC trials. |
| `EO_onset` | `triggers.map.EO_onset` | `20` | `W2170702893` | Distinct condition-wise onset markers are required for downstream EEG segmentation. | `implemented` | Marker emitted at rest-window onset for EO trials. |
| `EO_offset` | `triggers.map.EO_offset` | `21` | `W2170702893` | Distinct condition-wise offset markers are required for downstream EEG segmentation. | `implemented` | Marker emitted at rest-window offset for EO trials. |