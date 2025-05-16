import random


def generate_player_stats(player, team):
    while True:
        fours = random.randint(0, 4)
        sixes = random.randint(0, 1)
        boundary_runs = fours * 4 + sixes * 6
        if boundary_runs <= 20:
            break

    max_additional = 20 - boundary_runs
    additional_runs = random.randint(0, max_additional)
    runs = boundary_runs + additional_runs
    balls = random.randint(10, 50)
    wickets = random.randint(0, 3)
    strike_rate = round((runs / balls) * 100, 2) if balls > 0 else 0
    economy_rate = round(random.uniform(5.0, 10.0), 2)

    return {
        "player": player,
        "team": team,
        "runs": runs,
        "balls": balls,
        "fours": fours,
        "sixes": sixes,
        "wickets": wickets,
        "strike_rate": strike_rate,
        "economy_rate": economy_rate
    }


def generate_match(match_number, match_date, india_players, opponent, opponent_players, venues, umpires_list):
    match_id = f"T20_IND_{opponent}_{match_date.strftime('%Y%m%d')}_{match_number}"
    team1 = "India"
    team2 = opponent
    venue = random.choice(venues)
    umpires = random.sample(umpires_list, 2)

    team1_players = random.sample(india_players, 11)
    team2_players = random.sample(opponent_players, 11)

    scorecard = []
    team1_runs = 0
    team2_runs = 0

    for player in team1_players:
        stats = generate_player_stats(player, team1)
        team1_runs += stats["runs"]
        scorecard.append(stats)

    for player in team2_players:
        stats = generate_player_stats(player, team2)
        team2_runs += stats["runs"]
        scorecard.append(stats)

    toss_winner = random.choice([team1, team2])
    toss_decision = random.choice(["bat", "bowl"])
    winner = team1 if team1_runs > team2_runs else team2 if team2_runs > team1_runs else "Tie"
    player_of_match = random.choice(scorecard)["player"]

    return {
        "match_id": match_id,
        "date": match_date.strftime("%Y-%m-%d"),
        "venue": venue,
        "match_type": "T20",
        "umpires": umpires,
        "team1": team1,
        "team2": team2,
        "team1_score": {"total_runs": team1_runs},
        "team2_score": {"total_runs": team2_runs},
        "toss_winner": toss_winner,
        "toss_decision": toss_decision,
        "winner": winner,
        "player_of_match": player_of_match,
        "scorecard": scorecard
    }

