from typing import Set

from config.constants import POKEMONS_FILE
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.usecase.csv_extract import CsvExtract


def get_growth_rate(extractor: PokemonExtractor) -> Set[str]:
    pokemons = extractor.extract()
    return set(pokemon.growth_rate for pokemon in pokemons)


if __name__ == "__main__":
    extractor = CsvExtract(POKEMONS_FILE)
    types = get_growth_rate(extractor)
    print(types)
