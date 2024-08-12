from dataclasses import dataclass
from typing import List

from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository
from setup_small_project.pokemon.pokemon_raw import PokemonRaw


@dataclass
class SavePokemonsRawCmd:
    repository: PokemonRepository
    pokemons: List[PokemonRaw]

    def execute(self) -> int:
        for pokemon in self.pokemons:
            pokemon.save(self.repository)
        return len(self.pokemons)
