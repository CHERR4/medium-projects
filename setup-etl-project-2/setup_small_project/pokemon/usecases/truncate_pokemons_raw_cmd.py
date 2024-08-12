from dataclasses import dataclass

from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository


@dataclass
class TruncatePokemonsRawCmd:
    repository: PokemonRepository

    def execute(self) -> int:
        return self.repository.truncate()
