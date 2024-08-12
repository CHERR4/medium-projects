import psycopg2
import pymongo

from config.constants import (
    CONFIG_DIR,
    LOCALHOST,
    LOGS_CONFIG_FILE,
    LOGS_DIR,
    MONGO_DB,
    MONGO_PORT,
    POKEMONS_FILE,
    POSTGRES_DB,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)
from setup_small_project.common.logging_utils import setup_logging
from setup_small_project.etl.usecase.csv_extract import CsvExtract
from setup_small_project.etl.usecase.list_load import ListLoad
from setup_small_project.etl.usecase.list_transform import ListTransform
from setup_small_project.etl.usecase.simple_etl import SimpleEtl
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon_repository import (
    MongoPokemonRepository,
)
from setup_small_project.pokemon.persistence.postgres.pg_pokemon_processed_repo import (
    PgPokemonProcessedRepo,
)
from setup_small_project.pokemon.processors.simple_pokemon_processor import (
    SimplePokemonProcessor,
)

if __name__ == "__main__":
    setup_logging(CONFIG_DIR, LOGS_CONFIG_FILE, LOGS_DIR)
    client = pymongo.MongoClient(LOCALHOST, MONGO_PORT)
    database = client[MONGO_DB]
    pokemon_repository = MongoPokemonRepository(database)
    pg_connection = psycopg2.connect(
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=LOCALHOST,
        port=POSTGRES_PORT,
    )
    pokemon_processed_repository = PgPokemonProcessedRepo(pg_connection)
    pokemon_processor = SimplePokemonProcessor()

    extractor = CsvExtract(POKEMONS_FILE)
    transformer = ListTransform(pokemon_repository)
    loader = ListLoad(pokemon_processed_repository, pokemon_processor)
    etl = SimpleEtl(extractor, transformer, loader)
    etl.execute()
