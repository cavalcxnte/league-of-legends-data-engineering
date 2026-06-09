import os
import json
import pandas as pd

from dotenv import load_dotenv
from pathlib import Path
from logger import get_logger

load_dotenv()
logger = get_logger("transform_matches")
logger.info("Starting transformation of match data...")

RIOT_PUUID = os.getenv("RIOT_PUUID")


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

data = []

for file in RAW_DIR.glob("*.json"):
    logger.info(f"Processing file: {file}")
    with open(file, "r", encoding="utf-8") as f:
        game = json.load(f)

    game_id = game["metadata"]["matchId"]
    players = game["info"]["participants"]
    my_player = None

    logger.info(f"Looking for player with PUUID: {RIOT_PUUID}")
    for player in players:
        if player["puuid"] == RIOT_PUUID:
            my_player = player
            break

    if my_player is None:
        logger.warning(f"Player with PUUID {RIOT_PUUID} not found in {file}")
        continue

    kills = my_player["kills"]
    deaths = my_player["deaths"]
    assists = my_player["assists"]

    kda = round((kills + assists) / max(1, deaths), 2)

    data.append(
        {
            "match_id": game_id,
            "champion": my_player["championName"],
            "role": my_player["teamPosition"],
            "win": my_player["win"],
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "kda": kda,
            "damage_dealt": my_player["totalDamageDealtToChampions"],
            "damage_taken": my_player["totalDamageTaken"],
            "healing": my_player["totalHeal"],
            "vision_score": my_player["visionScore"],
            "gold_earned": my_player["goldEarned"],
            "cs": my_player["totalMinionsKilled"]
        }
    )
df = pd.DataFrame(data)

PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

csv_file = PROCESSED_DIR / "matches.csv"

df.to_csv(csv_file, index=False)

print("\n=== Most played champions ===")
champions = (
    df["champion"]
    .value_counts()
)

print(champions.head(10))

print("\n=== WIN RATE FOR CHAMPIONS ===")

winrate = (
    df.groupby("champion")["win"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)

print(winrate)

print("\n=== KDA AVERAGE ===")

print(round(df["kda"].mean(), 2))

print("\n=== ROLES ===")

print(
    df["role"]
    .value_counts()
)

print("\n=== AVERAGE DAMAGE DEALT ===")

print(
    round(
        df["damage_dealt"].mean(),
        2
    )
)

print("\n=== AVERAGE DAMAGE TAKEN ===")

print(
    round(
        df["damage_taken"].mean(),
        2
    )
)

print("\n=== AVERAGE HEALING ===")

print(
    round(
        df["healing"].mean(),
        2
    )
)

print("\n=== VISION SCORE AVERAGE ===")

print(
    round(
        df["vision_score"].mean(),
        2
    )
)

print(f"File saved in: {csv_file}")

print(df.head())

print("\nTotal number of matches:")
print(len(df))
