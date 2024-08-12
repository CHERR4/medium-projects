from dataclasses import dataclass

from setup_small_project.pokemon.persistence.pokemon_processed_repository import (
    PokemonProcessedRepository,
)


@dataclass
class TruncatePokemonsProcessedCmd:
    pokemon_processed_repository: PokemonProcessedRepository

    def execute(self) -> int:
        return self.pokemon_processed_repository.truncate()
