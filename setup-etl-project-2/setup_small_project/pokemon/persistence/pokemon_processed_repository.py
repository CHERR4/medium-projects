import abc
from typing import List

from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


class PokemonProcessedRepository(abc.ABC):

    @abc.abstractmethod
    def truncate(self) -> int:
        pass

    @abc.abstractmethod
    def save(self, pokemon: PokemonProcessed) -> str:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[PokemonProcessed]:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: str) -> PokemonProcessed:
        pass
