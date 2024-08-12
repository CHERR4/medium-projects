#!/usr/bin/env python
import logging

import pymongo

from config.constants import MONGO_DB, MONGO_HOST, MONGO_PORT, POKEMONS_FILE
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.usecase.csv_extract import CsvExtract
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon_repository import (
    MongoPokemonRepository,
)
from setup_small_project.pokemon.usecases.save_pokemons_raw_cmd import (
    SavePokemonsRawCmd,
)

logger = logging.getLogger(__name__)


def load_pokemons_scripts(
    host: str, port: int, db_name: str, file: str, extractor: PokemonExtractor
):
    client = pymongo.MongoClient(host, port)
    database = client[db_name]
    pokemon_repo = MongoPokemonRepository(database)
    pokemons = extractor.extract()
    logger.info(f"Loading {len(pokemons)} pokemons...")
    n_inserted = SavePokemonsRawCmd(pokemon_repo, pokemons).execute()
    logger.info(f"{n_inserted} pokemons loaded")


if __name__ == "__main__":
    extractor = CsvExtract(POKEMONS_FILE)
    load_pokemons_scripts(MONGO_HOST, MONGO_PORT, MONGO_DB, POKEMONS_FILE, extractor)
