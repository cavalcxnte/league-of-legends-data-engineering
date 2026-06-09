import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RIOT_API_KEY')

game_name = "twentyfive"
tag_line = "011"

url = (
    f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}")

headers = {
    "X-Riot-Token": API_KEY
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
