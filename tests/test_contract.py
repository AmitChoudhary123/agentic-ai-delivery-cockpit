from pathlib import Path
from src.delivery_cockpit.main import load_use_cases, prioritize_use_case, rank_portfolio


def test_delivery_cockpit_ranks_portfolio():
    rows = load_use_cases(Path("data/agentic_use_cases.csv"))
    ranked = rank_portfolio(rows)
    assert ranked[0]["tier"] in {"scale", "pilot"}
    assert any(item["control"] == "human approval required" for item in ranked)


def test_high_value_low_risk_scales():
    assert prioritize_use_case(90, 80, 20)["tier"] == "scale"