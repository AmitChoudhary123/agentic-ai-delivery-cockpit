def prioritize_use_case(value: int, feasibility: int, risk: int) -> dict:
    """Score an agentic AI use case for enterprise delivery sequencing."""
    score = (0.45 * value) + (0.35 * feasibility) - (0.20 * risk)
    tier = "scale" if score >= 65 else "pilot" if score >= 40 else "defer"
    return {"score": round(score, 2), "tier": tier}