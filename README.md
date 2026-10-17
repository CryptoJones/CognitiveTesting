# CognitiveTesting

Personal cognitive-testing results. Source reports live in `reports/`
(`YYYY-MM-DD_<test>.pdf`); the numbers are also in [`results.json`](results.json).

## Attempts

| Date | Provider | Test | Score | Report |
|---|---|---|---|---|
| 2026-10-16 | [Cognitive Testing](https://cognitivetesting.org) | Online IQ | IQ 124 (1.6σ, 84th %ile[^1], "Superior") | [pdf](reports/2026-10-16_cognitivetesting.pdf) |
| 2024-12-28 | [CognitiveMetrics](https://cognitivemetrics.com) | CAIT | FSIQ 119 ±7 (89.7th %ile), GAI 120 | [pdf](reports/2024-12-28_cait.pdf) |

## CAIT (Cognitive Assessment and Intelligence Test)

Attempts are columns, oldest → newest. The `YYYY-MM-DD` column is a placeholder for the next retake:
rename it to the test date, fill it in, and put the change vs. the previous column in Δ.
Add another placeholder column after it so the pattern stays visible.

### Index scores

| Index | 2024-12-28 | YYYY-MM-DD | Δ |
|---|---|---|---|
| FSIQ | 119 ±7 | — | — |
| GAI | 120 | — | — |
| VCI (Verbal Comprehension) | 119 | — | — |
| PRI (Perceptual Reasoning) | 119 | — | — |
| VSI (Visual Spatial) | 127 | — | — |
| CPI (Cognitive Proficiency) | 111 | — | — |

### Subtests (scaled score / percentile)

| Subtest | Index | 2024-12-28 | YYYY-MM-DD | Δ |
|---|---|---|---|---|
| Vocabulary | VCI | 15 / 95.2 | — | — |
| General Knowledge | VCI | 12 / 74.8 | — | — |
| Figure Weights | PRI | 13 / 84.1 | — | — |
| Visual Puzzles | PRI | 14 / 90.9 | — | — |
| Block Design | VSI | 16 / 97.7 | — | — |
| Digit Span | WMI | 13 / 84.1 | — | — |
| Symbol Search | PSI | 11 / 63.1 | — | — |

## Online IQ (Cognitive Testing)

| Metric | 2026-10-16 | YYYY-MM-DD | Δ |
|---|---|---|---|
| IQ | 124 | — | — |
| Standard deviations | 1.6σ | — | — |
| Percentile | 84[^1] | — | — |
| Classification | Superior | — | — |

## Model

`notes/model.md` holds the Bayesian combination of attempts (prior, per-test error, shared
online-test bias) and `notes/model.py` recomputes it from `results.json`. Rerun it after each attempt.

## Adding an attempt

1. Drop the report in `reports/` as `YYYY-MM-DD_<test>.pdf`.
2. Append a record to `results.json` (include `medicated: true|false`).
3. Add a row to **Attempts**; in the matching test's tables, fill the `YYYY-MM-DD` placeholder
   column (rename it to the date), fill Δ, and add a fresh `YYYY-MM-DD` / Δ placeholder pair.

[^1]: As reported by the site. It is wrong: +1.6σ on a normal curve is the ~94.5th percentile
    (84% is +1.0σ). The site's stated SD and percentile are inconsistent; the model uses the IQ score only.
