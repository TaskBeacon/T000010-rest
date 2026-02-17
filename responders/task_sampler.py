from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from psyflow.sim.contracts import Action, Observation, SessionInfo


@dataclass
class TaskSamplerResponder:
    """Minimal rest-task sampler.

    - Continue screens (`wait_and_continue`) receive a key press.
    - Rest windows default to no response.
    - Optional low-probability false presses can be enabled for stress tests.
    """

    continue_key: str = "space"
    rt_continue_s: float = 0.25
    p_false_press: float = 0.0
    rt_false_press_s: float = 0.35

    def __post_init__(self) -> None:
        self._rng: Any = None
        self.rt_continue_s = max(0.01, float(self.rt_continue_s))
        self.p_false_press = max(0.0, min(1.0, float(self.p_false_press)))
        self.rt_false_press_s = max(0.01, float(self.rt_false_press_s))

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def on_feedback(self, fb: Any) -> None:
        return None

    def end_session(self) -> None:
        return None

    def act(self, obs: Observation) -> Action:
        valid_keys = list(obs.valid_keys or [])
        if not valid_keys:
            return Action(key=None, rt_s=None, meta={"source": "rest_sampler", "reason": "no_valid_keys"})

        phase = str(obs.phase or "").strip().lower()
        # wait_and_continue phases in this task.
        if phase in {"instruction", "block"}:
            key = self.continue_key if self.continue_key in valid_keys else valid_keys[0]
            return Action(key=key, rt_s=self.rt_continue_s, meta={"source": "rest_sampler", "outcome": "continue"})

        if self._rng is not None and float(self._rng.random()) < self.p_false_press:
            return Action(
                key=valid_keys[0],
                rt_s=self.rt_false_press_s,
                meta={"source": "rest_sampler", "outcome": "false_press"},
            )

        return Action(key=None, rt_s=None, meta={"source": "rest_sampler", "outcome": "no_response"})
