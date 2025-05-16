import json
import os

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")


def load_json(file_name):
    with open(os.path.join(CONFIG_DIR, file_name), "r") as f:
        return json.load(f)


def load_teams():
    return load_json("teams.json")


def load_venues():
    return load_json("venues.json")


def load_umpires():
    return load_json("umpires.json")

