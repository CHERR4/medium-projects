import os

from dotenv import main

from setup_small_project.common.typing_utils import defined

main.load_dotenv()

POKEMONS_FILE = "data/raw/pokemonDB_dataset.csv"
PROCESSED_FILE = "data/processed/pokemon_processed.csv"
MONGO_DB = defined(os.getenv("MONGO_DB"))
MONGO_HOST = defined(os.getenv("MONGO_HOST"))
MONGO_PORT = int(defined(os.getenv("MONGO_PORT")))
