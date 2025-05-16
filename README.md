# 🏏 Cricket Match Series Simulator

This is a Python-based T20 match simulator that generates a configurable number of matches between **India** and **New Zealand**. Player performances, match outcomes, and other match data are randomly simulated with reasonable constraints.

---


## 📁 Project Structure

<details> <summary><strong>📂 Project Structure</strong> (click to expand)</summary>

cricket_match_simulator/
│
├── config/ # 📁 External configurations (editable JSON files)
│ ├── teams.json # 👥 List of players for India and New Zealand
│ ├── venues.json # 🏟️ List of possible match venues
│ └── umpires.json # 🧑‍⚖️ List of available umpires
│
├── config_loader.py # 🔧 Module to load data from config JSON files
├── match_generator.py # 🎲 Core logic to simulate one T20 match
├── series_generator.py # 🔁 Logic to generate and save multiple matches
├── main.py # 🚀 Entry script to trigger the simulation
│
└── output/ # 📦 Auto-created directory to store the JSON results

</details>


---

## ⚙️ Configuration

All match details are driven by JSON files inside the `config/` directory. You can modify them without touching the code.

### 1. `config/teams.json`

Define teams and make sure each team has at least 11 players.

### 2. `config/venues.json`

Define match venues.

### 3. `config/umpires.json`

Define umpires list.


## How to Run

### Step 1: Install Python (3.7+)
Make sure you have Python installed:

`python --version`

### Step 2: Run the simulator
Navigate to the project directory and run:

`python main.py`

This will:

    * Simulate 4545 matches between India and New Zealand

    * Save the output to: output/india_vs_newzealand_t20_series_large.json

To simulate a different number of matches, edit main.py:

`series_data = generate_series(50)`  # Simulate 50 matches instead of 4545

### 🧪 Sample Output (Structure)

Each match entry includes:

```json
{
    "match_id": "T20_IND_New Zealand_20240501_1",
    "date": "2024-05-01",
    "venue": "Mumbai",
    "match_type": "T20",
    "umpires": ["Nitin Menon", "Aleem Dar"],
    "team1": "India",
    "team2": "New Zealand",
    "team1_score": {"total_runs": 173},
    "team2_score": {"total_runs": 159},
    "toss_winner": "India",
    "toss_decision": "bat",
    "winner": "India",
    "player_of_match": "Virat Kohli",
    "scorecard": [...]
}
```