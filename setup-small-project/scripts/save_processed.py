#!/usr/bin/env python
import pymongo

from config.constants import MONGO_DB, MONGO_HOST, MONGO_PORT, PROCESSED_FILE
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon_repository import (
    MongoPokemonRepository,
)
from setup_small_project.pokemon.usecases.get_pokemons_qry import GetPokemonsQry
from setup_small_project.pokemon.usecases.save_pokemons_csv_cmd import (
    SavePokemonsCsvCmd,
)


def save_pokemon_script(host: str, port: int, db_name: str, file: str):
    client = pymongo.MongoClient(host, port)
    database = client[db_name]
    pokemon_repo = MongoPokemonRepository(database)
    pokemons = GetPokemonsQry(pokemon_repo).get()
    print(f"Saving {len(pokemons)} pokemons...")
    n_inserted = SavePokemonsCsvCmd(pokemons, file).execute()
    print(f"{n_inserted} pokemons loaded")


if __name__ == "__main__":
    save_pokemon_script(MONGO_HOST, MONGO_PORT, MONGO_DB, PROCESSED_FILE)
