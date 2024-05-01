#!/usr/bin/env python
import pymongo

from config.constants import MONGO_DB, MONGO_HOST, MONGO_PORT, POKEMONS_FILE
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon_repository import (
    MongoPokemonRepository,
)
from setup_small_project.pokemon.pokemon_raw import PokemonRaw
from setup_small_project.pokemon.usecases.save_pokemons_raw_cmd import (
    SavePokemonsRawCmd,
)


def load_pokemons_scripts(host: str, port: int, db_name: str, file: str):
    client = pymongo.MongoClient(host, port)
    database = client[db_name]
    pokemon_repo = MongoPokemonRepository(database)
    pokemons = PokemonRaw.from_csv(file)
    print(f"Loading {len(pokemons)} pokemons...")
    n_inserted = SavePokemonsRawCmd(pokemon_repo, pokemons).execute()
    print(f"{n_inserted} pokemons loaded")


if __name__ == "__main__":
    load_pokemons_scripts(MONGO_HOST, MONGO_PORT, MONGO_DB, POKEMONS_FILE)
