from datetime import datetime, timedelta
import json
import os
from match_generator import generate_match
from config_loader import load_teams, load_venues, load_umpires


def generate_series(num_matches=10):
    teams = load_teams()
    venues = load_venues()
    umpires_list = load_umpires()

    india_players = teams["india"]
    opponent = "New Zealand"
    opponent_players = teams["new_zealand"]

    start_date = datetime.today() - timedelta(days=num_matches * 2)
    series = []

    for i in range(1, num_matches + 1):
        match_date = start_date + timedelta(days=i * 2)
        match = generate_match(i, match_date, india_players, opponent, opponent_players, venues, umpires_list)
        series.append(match)

    return series


def save_to_json(data, filename="india_vs_newzealand_t20_series_large.json"):
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to: {filepath}")

