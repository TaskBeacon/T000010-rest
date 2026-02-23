from functools import partial

from psyflow import StimUnit, set_trial_context, next_trial_id

# trial stages use task-specific phase labels via set_trial_context(...)


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one rest trial (condition-specific instruction + rest window)."""
    trial_id = next_trial_id()
    condition_id = str(condition)
    trial_data = {"condition": condition_id}

    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    # phase: block_instruction
    cue_unit = make_unit(unit_label="cue").add_stim(stim_bank.get(f"{condition_id}_instruction"))
    if bool(getattr(settings, "voice_enabled", True)):
        try:
            cue_unit.add_stim(stim_bank.get(f"{condition_id}_instruction_voice"))
        except KeyError:
            pass

    set_trial_context(
        cue_unit,
        trial_id=trial_id,
        phase="block_instruction",
        deadline_s=None,
        valid_keys=list(getattr(settings, "key_list", []) or []),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "block_instruction", "block_idx": block_idx},
        stim_id=f"{condition_id}_instruction",
    )
    cue_unit.show().to_dict(trial_data)

    # phase: rest_state
    target_duration = getattr(settings, f"{condition_id}_duration")
    target_unit = make_unit(unit_label="target").add_stim(stim_bank.get(f"{condition_id}_stim"))
    set_trial_context(
        target_unit,
        trial_id=trial_id,
        phase="rest_state",
        deadline_s=target_duration,
        valid_keys=[],
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "rest_state", "block_idx": block_idx},
        stim_id=f"{condition_id}_stim",
    )
    target_unit.capture_response(
        keys=[],
        duration=target_duration,
        onset_trigger=settings.triggers.get(f"{condition_id}_onset"),
        timeout_trigger=settings.triggers.get(f"{condition_id}_offset"),
        terminate_on_response=False,
    )
    target_unit.to_dict(trial_data)

    # outcome display (no behavioral outcome in rest; zero-duration closeout stage)
    make_unit(unit_label="feedback").show(duration=0.0).to_dict(trial_data)
    return trial_data
