#!/usr/bin/env python3
"""Bayesian combination of cognitive-test attempts in ../results.json.

Model:  y_i = theta + b + e_i
  theta ~ N(PRIOR_MEAN, PRIOR_SD^2)      true (proctored-WAIS-equivalent) FSIQ
  b     ~ N(BIAS_MEAN, BIAS_SD^2)        bias shared by all self-administered online tests
  e_i   ~ N(0, se_i^2)                   per-test measurement error (se_i from TEST_SE)
Shared bias does NOT average out with more attempts; only e_i does.
Run:  python3 notes/model.py            (from the repo root)
"""
import json, math, pathlib

PRIOR_MEAN, PRIOR_SD = 100.0, 15.0   # population prior; set PRIOR_SD=1e6 for a flat prior
BIAS_MEAN, BIAS_SD = 0.0, 4.0        # online-vs-proctored shared bias (unknown sign, ~±4)
TEST_SE = {                          # 1-SD measurement error per test
    "CAIT": 3.5,        # site gives ±7 as a 95% band -> SD ≈ 3.5
    "Online IQ": 7.0,   # short unnormed online test; generous
    "RAIT": 4.0,        # placeholder until the RAIT manual's SEM is checked
}
SCORE_KEY = {"CAIT": "FSIQ", "Online IQ": "IQ", "RAIT": "FSIQ"}

def main():
    data = json.loads((pathlib.Path(__file__).parent.parent / "results.json").read_text())
    atts = [a for a in data["attempts"] if a["test"] in SCORE_KEY]
    # 1) combine attempts into an estimate of (theta + b) — precision-weighted mean
    w = [(a, 1 / TEST_SE[a["test"]] ** 2) for a in atts]
    prec = sum(p for _, p in w)
    mean = sum(a["scores"][SCORE_KEY[a["test"]]] * p for a, p in w) / prec
    var_tb = 1 / prec
    # 2) remove the shared bias: theta = (theta+b) - b
    like_mean, like_var = mean - BIAS_MEAN, var_tb + BIAS_SD ** 2
    # 3) prior
    post_prec = 1 / like_var + 1 / PRIOR_SD ** 2
    post_mean = (like_mean / like_var + PRIOR_MEAN / PRIOR_SD ** 2) / post_prec
    post_sd = math.sqrt(1 / post_prec)
    for a, p in w:
        print(f"{a['date']}  {a['test']:<10} {a['scores'][SCORE_KEY[a['test']]]:>4}  se={TEST_SE[a['test']]}  medicated={a.get('medicated')}")
    print(f"\nattempts combined (theta+b): {mean:.1f} ± {math.sqrt(var_tb):.1f}")
    print(f"likelihood for theta (bias removed): {like_mean:.1f} ± {math.sqrt(like_var):.1f}")
    print(f"posterior theta (prior N({PRIOR_MEAN:.0f},{PRIOR_SD:.0f})): {post_mean:.1f} ± {post_sd:.1f}")

if __name__ == "__main__":
    main()
