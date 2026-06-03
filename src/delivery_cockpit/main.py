from __future__ import annotations

import csv
from pathlib import Path


def prioritize_use_case(value: int, feasibility: int, risk: int) -> dict:
    score = (0.45 * value) + (0.35 * feasibility) - (0.20 * risk)
    tier = "scale" if score >= 60 else "pilot" if score >= 35 else "defer"
    return {"score": round(score, 2), "tier": tier}


def load_use_cases(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["business_value"] = int(row["business_value"])
        row["feasibility"] = int(row["feasibility"])
        row["risk"] = int(row["risk"])
    return rows


def rank_portfolio(rows: list[dict]) -> list[dict]:
    ranked = []
    for row in rows:
        decision = prioritize_use_case(row["business_value"], row["feasibility"], row["risk"])
        control = "human approval required" if row["risk"] >= 50 else "standard monitoring"
        ranked.append({**row, **decision, "control": control})
    return sorted(ranked, key=lambda item: item["score"], reverse=True)