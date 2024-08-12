from dataclasses import dataclass
from typing import List

from setup_small_project.pokemon.persistence.pokemon_processed_repository import (
    PokemonProcessedRepository,
)
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


@dataclass
class SavePokemonsProcessedCmd:
    pokemon_processed_repository: PokemonProcessedRepository
    pokemons: List[PokemonProcessed]

    def save(self) -> int:
        for pokemon in self.pokemons:
            self.pokemon_processed_repository.save(pokemon)
        return len(self.pokemons)
