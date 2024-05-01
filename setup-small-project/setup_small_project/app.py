from typing import List

import pymongo
from fastapi import FastAPI, Query

from config.constants import MONGO_DB, MONGO_HOST, MONGO_PORT
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon_repository import (
    MongoPokemonRepository,
)
from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.usecases.get_pokemon_qry import GetPokemonQry
from setup_small_project.pokemon.usecases.get_pokemons_qry import GetPokemonsQry

app = FastAPI()


client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
database = client[MONGO_DB]
pokemon_repo = MongoPokemonRepository(database)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemons")
def pokemons() -> List[Pokemon]:
    return GetPokemonsQry(pokemon_repo).get()


@app.get("/pokemon")
def pokemon(id: str = Query(...)) -> Pokemon:
    return GetPokemonQry(pokemon_repo, id).get()
