from dataclasses import dataclass
from typing import List

from setup_small_project.pokemon.persistence.pokemon_processed_repository import (
    PokemonProcessedRepository,
)
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


@dataclass
class GetPokemonsProcessedQry:
    repository: PokemonProcessedRepository

    def get(self) -> List[PokemonProcessed]:
        return self.repository.get_all()
