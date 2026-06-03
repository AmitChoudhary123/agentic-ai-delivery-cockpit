from pathlib import Path
from src.delivery_cockpit.main import load_use_cases, rank_portfolio

if __name__ == "__main__":
    rows = load_use_cases(Path("data/agentic_use_cases.csv"))
    for item in rank_portfolio(rows):
        print(f"{item['tier'].upper():5} | {item['score']:5.1f} | {item['use_case']} | {item['control']}")