import abc

from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


class PokemonProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, pokemon: Pokemon) -> PokemonProcessed:
        pass
