# Task Plot Review

## Evidence Match

- Pass: title and construct match the resting-state EC/EO task.
- Pass: EC and EO rows match configured conditions and sequential condition logic.
- Pass: phase order matches `src/run_trial.py`: Instruction -> Rest window.
- Pass: timing labels match config: 4 s instruction and 180 s rest.
- Pass: SPACE is shown only as a continue key before rest.
- Pass: rest windows show no response keys and correct EC/EO visible content.

## Visual Quality

- Pass: text is readable and row order is clear.
- Pass: generated content stays below the header area.
- Pass: fixed title and Construct subtitle are centered.
- Pass: top-right TaskBeacon logo lockup is borderless and non-overlapping.
- Pass: no extra generated title, logo, watermark, people, devices, or decorative scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
