import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from pathlib import Path
from logger import get_logger

load_dotenv()
logger = get_logger("load_postgres")
logger.info("Starting to load data into PostgreSQL...")

HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DB = os.getenv("POSTGRES_DB")
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
)

BASE_DIR = Path(__file__).resolve().parent.parent

logger.info(f"Connecting to database at {HOST}:{PORT}...")
csv_path = BASE_DIR / "data" / "processed" / "matches.csv"

df = pd.read_csv(csv_path)

print("Rows to insert:", len(df))

df.to_sql(
    "matches",
    engine,
    if_exists="append",
    index=False
)

print("Load completed successfully!")
