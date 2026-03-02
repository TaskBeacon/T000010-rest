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
    instruction_unit = make_unit(unit_label="instruction").add_stim(stim_bank.get(f"{condition_id}_instruction"))
    if bool(getattr(settings, "voice_enabled", True)):
        try:
            instruction_unit.add_stim(stim_bank.get(f"{condition_id}_instruction_voice"))
        except KeyError:
            pass

    set_trial_context(
        instruction_unit,
        trial_id=trial_id,
        phase="block_instruction",
        deadline_s=None,
        valid_keys=list(getattr(settings, "key_list", []) or []),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "block_instruction", "block_idx": block_idx},
        stim_id=f"{condition_id}_instruction",
    )
    instruction_unit.show().to_dict(trial_data)

    # phase: rest window
    rest_duration = getattr(settings, f"{condition_id}_duration")
    rest_unit = make_unit(unit_label="rest").add_stim(stim_bank.get(f"{condition_id}_stim"))
    set_trial_context(
        rest_unit,
        trial_id=trial_id,
        phase="fixation",
        deadline_s=rest_duration,
        valid_keys=[],
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "rest_window", "block_idx": block_idx},
        stim_id=f"{condition_id}_stim",
    )
    rest_unit.capture_response(
        keys=[],
        duration=rest_duration,
        onset_trigger=settings.triggers.get(f"{condition_id}_onset"),
        timeout_trigger=settings.triggers.get(f"{condition_id}_offset"),
        terminate_on_response=False,
    )
    rest_unit.to_dict(trial_data)
    return trial_data
