import abc
from typing import List

from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_raw import PokemonRaw


class PokemonTransformer(abc.ABC):

    @abc.abstractmethod
    def transform(self, pokemons: List[PokemonRaw]) -> List[Pokemon]:
        raise NotImplementedError()
