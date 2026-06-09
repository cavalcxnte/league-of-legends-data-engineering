# 🎮 League of Legends Data Pipeline (Riot API)

This project is a complete data pipeline using the **Riot Games API** for collecting, transforming, and analyzing League of Legends matches.

The goal is to build a data engineering solution from scratch, encompassing API input, data processing, relational database storage, and the generation of analytical insights.

## 📊 What the project does

- Collects player matches via Riot API
- Stores raw data in JSON
- Extracts match statistics
- Calculates metrics such as:
- Most played champion
- Win rate per champion
- Average KDA
- Damage dealt and received
- Healing and vision (support)
- Most played role (SUP / ADC / MID etc.)
- Stores structured data in PostgreSQL

---

## 🧰 Technologies used

- Python 3.14.4
- Riot Games API
- Pandas
- PostgreSQL
- SQLAlchemy
- dotenv
- WSL (Ubuntu)

## ⚙️ How to run the project

### 1. Clone the repository

git clone <repo-url>

### 2. Create the virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Intall dependecies

pip install -r requirements.txt

### 4. Configure environment variables

Remove the .env.example file or rename it to .env and update it with your information.

RIOT_API_KEY=SUA_CHAVE_AQUI
RIOT_PUUID=SEU_PUUID_AQUI
POSTGRES_HOST=localhost
POSTGRES_PORT=0000
POSTGRES_DB=seu_banco_de_dados_aqui
POSTGRES_USER=postgres
POSTGRES_PASSWORD=suasenhaaqui
