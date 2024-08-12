from typing import List

import psycopg2
import pymongo
from fastapi import FastAPI, Query

from config.constants import (
    CONFIG_DIR,
    LOGS_CONFIG_FILE,
    LOGS_DIR,
    MONGO_DB,
    MONGO_HOST,
    MONGO_PORT,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)
from setup_small_project.common.logging_utils import log_requests, setup_logging
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon_repository import (
    MongoPokemonRepository,
)
from setup_small_project.pokemon.persistence.postgres.pg_pokemon_processed_repo import (
    PgPokemonProcessedRepo,
)
from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed
from setup_small_project.pokemon.usecases.get_pokemon_processed_qry import (
    GetPokemonProcessedQry,
)
from setup_small_project.pokemon.usecases.get_pokemon_qry import GetPokemonQry
from setup_small_project.pokemon.usecases.get_pokemons_processed_qry import (
    GetPokemonsProcessedQry,
)
from setup_small_project.pokemon.usecases.get_pokemons_qry import GetPokemonsQry

app = FastAPI()

app.middleware("http")(log_requests)

mongo_client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
mongo_database = mongo_client[MONGO_DB]
pokemon_repo = MongoPokemonRepository(mongo_database)

postgres_connection = psycopg2.connect(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    database=POSTGRES_DB,
    port=POSTGRES_PORT,
)

pokemon_processed_repo = PgPokemonProcessedRepo(postgres_connection)

setup_logging(CONFIG_DIR, LOGS_CONFIG_FILE, LOGS_DIR)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemons")
def pokemons() -> List[Pokemon]:
    return GetPokemonsQry(pokemon_repo).get()


@app.get("/pokemon")
def pokemon(id: str = Query(...)) -> Pokemon:
    return GetPokemonQry(pokemon_repo, id).get()


@app.get("/pokemons-processed")
def pokemons_processed() -> List[PokemonProcessed]:
    return GetPokemonsProcessedQry(pokemon_processed_repo).get()


@app.get("/pokemon-processed")
def pokemon_processed(id: str = Query(...)) -> PokemonProcessed:
    return GetPokemonProcessedQry(pokemon_processed_repo, id).get()
