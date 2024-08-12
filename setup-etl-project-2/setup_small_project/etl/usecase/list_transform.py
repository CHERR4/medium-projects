import logging
from typing import List

from setup_small_project.etl.pokemon_transformer import PokemonTransformer
from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository
from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_raw import PokemonRaw
from setup_small_project.pokemon.usecases.get_pokemons_qry import GetPokemonsQry
from setup_small_project.pokemon.usecases.save_pokemons_raw_cmd import (
    SavePokemonsRawCmd,
)
from setup_small_project.pokemon.usecases.truncate_pokemons_raw_cmd import (
    TruncatePokemonsRawCmd,
)


class ListTransform(PokemonTransformer):
    pokemon_repository: PokemonRepository

    def __init__(self, pokemon_repository: PokemonRepository):
        self.pokemon_repository = pokemon_repository

    def transform(self, pokemons: List[PokemonRaw]) -> List[Pokemon]:
        logging.info("Truncating raw records...")
        truncated_records = TruncatePokemonsRawCmd(self.pokemon_repository).execute()
        logging.info(f"Truncated {truncated_records} records")
        SavePokemonsRawCmd(self.pokemon_repository, pokemons).execute()
        return GetPokemonsQry(self.pokemon_repository).get()
