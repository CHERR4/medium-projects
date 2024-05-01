from dataclasses import dataclass
from typing import List

from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository
from setup_small_project.pokemon.pokemon import Pokemon


@dataclass
class GetPokemonsQry:
    repository: PokemonRepository

    def get(self) -> List[Pokemon]:
        return self.repository.get_all()
