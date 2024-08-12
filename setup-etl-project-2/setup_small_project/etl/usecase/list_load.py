import logging
from typing import List

from setup_small_project.etl.pokemon_loader import PokemonLoader
from setup_small_project.pokemon.persistence.pokemon_processed_repository import (
    PokemonProcessedRepository,
)
from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed
from setup_small_project.pokemon.processors.pokemon_processor import PokemonProcessor
from setup_small_project.pokemon.usecases.save_pokemons_processed_cmd import (
    SavePokemonsProcessedCmd,
)
from setup_small_project.pokemon.usecases.truncate_pokemons_processed_cmd import (
    TruncatePokemonsProcessedCmd,
)


class ListLoad(PokemonLoader):
    pokemon_processed_repository: PokemonProcessedRepository
    pokemon_processor: PokemonProcessor

    def __init__(
        self,
        pokemon_processed_repository: PokemonProcessedRepository,
        pokemon_processor: PokemonProcessor,
    ):
        self.pokemon_processed_repository = pokemon_processed_repository
        self.pokemon_processor = pokemon_processor

    def load(self, pokemons: List[Pokemon]) -> List[PokemonProcessed]:
        pokemons_processed = [
            self.pokemon_processor.process(pokemon) for pokemon in pokemons
        ]
        logging.info("Truncating processed records...")
        truncated_records = TruncatePokemonsProcessedCmd(
            self.pokemon_processed_repository
        ).execute()
        logging.info(f"Truncated {truncated_records} records")
        SavePokemonsProcessedCmd(
            self.pokemon_processed_repository, pokemons_processed
        ).save()
        return pokemons_processed
