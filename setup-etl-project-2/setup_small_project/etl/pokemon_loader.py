import abc
from typing import List

from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


class PokemonLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, pokemons: List[Pokemon]) -> List[PokemonProcessed]:
        raise NotImplementedError()
