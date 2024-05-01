import abc
from typing import List

from setup_small_project.pokemon.pokemon import Pokemon


class PokemonRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, pokemon: Pokemon) -> str:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Pokemon]:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: str) -> Pokemon:
        pass
