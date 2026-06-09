
import os
import json
import requests

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")
PUUID = os.getenv("RIOT_PUUID")

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

headers = {
    "X-Riot-Token": API_KEY
}

# Buscar IDs das partidas
url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids"

response = requests.get(
    url,
    headers=headers,
    params={
        "start": 0, 
        "count": 20}
)

match_ids = response.json()

# Buscar detalhes de cada partida
for match_id in match_ids:

    match_url = (
        f"https://americas.api.riotgames.com"
        f"/lol/match/v5/matches/{match_id}"
    )

    match_response = requests.get(
        match_url,
        headers=headers
    )

    if match_response.status_code == 200:

        with open(
            RAW_DIR / f"{match_id}.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                match_response.json(),
                f,
                ensure_ascii=False,
                indent=4
            )

        print(f"Salvo: {match_id}")

    else:
        print(
            f"Erro ao buscar {match_id}: "
            f"{match_response.status_code}"
        )
