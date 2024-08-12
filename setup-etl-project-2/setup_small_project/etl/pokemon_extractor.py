import abc
from typing import List

from setup_small_project.pokemon.pokemon_raw import PokemonRaw


class PokemonExtractor(abc.ABC):

    @abc.abstractmethod
    def extract(self) -> List[PokemonRaw]:
        raise NotImplementedError()
