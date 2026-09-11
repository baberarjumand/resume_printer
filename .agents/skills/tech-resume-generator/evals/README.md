# Evals (core)

Eval-driven quality checks for `tech-resume-generator`, following [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills).

This is a **core** part of the skill — not an optional add-on. Agents maintaining or shipping this skill must keep `evals/evals.json` green when changing `SKILL.md` or scripts. There are **5** core evals (experienced general, JD-tailored frontend, student, thin-data junior, JD-tailored overflow).

## Files

| Path | Role |
| --- | --- |
| `evals.json` | Test prompts, expected outputs, assertions, fixture paths |
| `trigger_queries.json` | Description trigger true/false queries (train/validation) |
| `files/` | Synthetic career fixtures (no real PII) |

## Running an iteration

Workspace layout (repo root):

```
evals-workspace/iteration-1/
  eval-general-experienced/
    with_skill/outputs/     # agent writes resume artifacts here (or copy from output/)
    with_skill/grading.json # from eval_grade.py
    without_skill/...       # optional baseline
  benchmark.json            # from eval_aggregate.py
```

### Agent / human loop

1. For each eval in `evals.json`, start a **clean** session.
2. With skill activated, run the `prompt` using fixtures in `files/` (copy into a temp `tech-resume-generator_files/user_professional_data/` or point the agent at `evals/files/...`).
3. Save artifacts into `evals-workspace/iteration-N/eval-<slug>/with_skill/outputs/` mirroring workspace `output/` (`professional_data.md`, `general/*.json`, etc.).
4. Grade:

```bash
python3 scripts/eval_grade.py \
  --evals evals/evals.json \
  --eval-id 1 \
  --outputs ../../evals-workspace/iteration-1/eval-general-experienced/with_skill/outputs \
  --workspace ../../evals-workspace/iteration-1/eval-general-experienced/with_skill
```

5. Aggregate:

```bash
python3 scripts/eval_aggregate.py --iteration ../../evals-workspace/iteration-1
```

6. Fix `SKILL.md` / scripts from failed assertions; open `iteration-2/` and repeat.

### Programmatic grade only

If you already produced resumes under a folder:

```bash
npm run eval:grade -- --eval-id 1 --outputs ./path/to/outputs --workspace ./path/to/with_skill
npm run eval:aggregate -- --iteration ./evals-workspace/iteration-1
```

## Assertions

Assertions are objective checks (schema, forbidden inventions, section order). Style polish still needs human review (`feedback.json` per the agentskills guide).
