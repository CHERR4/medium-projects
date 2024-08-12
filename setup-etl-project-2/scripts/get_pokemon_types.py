from typing import Set

from config.constants import POKEMONS_FILE
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.usecase.csv_extract import CsvExtract


def get_pokemon_types(extractor: PokemonExtractor) -> Set[str]:
    pokemons = extractor.extract()
    types = set()
    for pokemon in pokemons:
        poke_types = [type.strip() for type in pokemon.type.split(",")]
        types.update(poke_types)
    return types


if __name__ == "__main__":
    extractor = CsvExtract(POKEMONS_FILE)
    types = get_pokemon_types(extractor)
    print(types)
