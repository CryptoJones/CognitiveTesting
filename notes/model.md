# Bayesian model of the attempts

Goal: a running estimate of true (proctored-WAIS-equivalent) FSIQ from self-administered
tests, kept honest about the two things a single online score hides — per-test noise and a
bias shared by *all* online tests. Rerun `python3 notes/model.py` after each new attempt.

## Setup

    y_i   = θ + b + e_i
    θ     ~ N(100, 15²)      population prior (flat prior also reported)
    b     ~ N(0, 4²)         shared online-vs-proctored bias; unknown sign, does NOT average out
    e_i   ~ N(0, se_i²)      per-test error

| Test | se (1 SD) | Source |
|---|---|---|
| CAIT | 3.5 | site's ±7 read as a 95% band |
| Online IQ (cognitivetesting.org) | 7.0 | short, unnormed; generous |
| RAIT | 4.0 | placeholder — replace with the manual's SEM when the result comes in |

The Online IQ score is used as 124 only; the site's "1.6σ / 84th percentile" is internally
inconsistent (1.6σ ≈ 94.5th), so its percentile is ignored.

## Current estimate (2 attempts, as of 2026-10-17)

| Stage | Estimate |
|---|---|
| Attempts combined, precision-weighted (θ + b) | 120.0 ± 3.1 |
| Shared bias removed (θ, flat prior) | **120 ± 5** |
| With population prior N(100, 15²) | 118 ± 5 |

The shared-bias term is the floor on the uncertainty: more online attempts tighten the 3.1 but
never the ±4 from `b`. Only a proctored test (or a test with known norming vs. WAIS) shrinks it.

## Medication variable

`results.json` carries `medicated: true|false` per attempt. CAIT 2024-12-28 was unmedicated;
Online IQ 2026-10-16 was medicated. Once there are attempts of the *same* test in both states,
compare them directly (same `b`, so the difference is `Δθ_meds + e_i − e_j`) rather than
through this pooled model, which currently assumes one θ.

## To do when the RAIT result arrives

1. Add the attempt to `results.json` (score, `medicated`, report path).
2. Set `TEST_SE["RAIT"]` from the manual's SEM.
3. Rerun `model.py`; update the table above and the date in the heading.
