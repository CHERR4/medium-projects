from dataclasses import dataclass

from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository
from setup_small_project.pokemon.pokemon import Pokemon


@dataclass
class GetPokemonQry:
    repository: PokemonRepository
    id: str

    def get(self) -> Pokemon:
        return self.repository.get_by_id(self.id)
