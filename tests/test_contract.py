from src.delivery_cockpit.main import prioritize_use_case


def test_high_value_low_risk_scales():
    assert prioritize_use_case(90, 80, 20)["tier"] == "scale"


def test_low_feasibility_is_deferred():
    assert prioritize_use_case(30, 20, 80)["tier"] == "defer"