import os

from dotenv import main

from setup_small_project.common.typing_utils import defined

main.load_dotenv()

POKEMONS_FILE = "data/raw/pokemonDB_dataset.csv"
PROCESSED_FILE = "data/processed/pokemon_processed.csv"
LOGS_DIR = "./logs"
LOGS_CONFIG_FILE = "logging.ini"
CONFIG_DIR = "./config"
MONGO_DB = defined(os.getenv("MONGO_DB"))
MONGO_HOST = defined(os.getenv("MONGO_HOST"))
MONGO_PORT = int(defined(os.getenv("MONGO_PORT")))
POSTGRES_USER = defined(os.getenv("POSTGRES_USER"))
POSTGRES_PASSWORD = defined(os.getenv("POSTGRES_PASSWORD"))
POSTGRES_DB = defined(os.getenv("POSTGRES_DB"))
POSTGRES_PORT = defined(os.getenv("POSTGRES_PORT"))
POSTGRES_HOST = defined(os.getenv("POSTGRES_HOST"))
POSTGRES_URL = defined(os.getenv("POSTGRES_URL"))
LOCALHOST = "0.0.0.0"
