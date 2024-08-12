from dataclasses import dataclass

from setup_small_project.pokemon.persistence.pokemon_processed_repository import (
    PokemonProcessedRepository,
)
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


@dataclass
class GetPokemonProcessedQry:
    repository: PokemonProcessedRepository
    id: str

    def get(self) -> PokemonProcessed:
        return self.repository.get_by_id(self.id)
