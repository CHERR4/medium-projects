import abc

from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.pokemon_loader import PokemonLoader
from setup_small_project.etl.pokemon_transformer import PokemonTransformer


class PokemonEtl(abc.ABC):
    extractor: PokemonExtractor
    transformer: PokemonTransformer
    loader: PokemonLoader

    @abc.abstractmethod
    def execute(self) -> int:
        pass
