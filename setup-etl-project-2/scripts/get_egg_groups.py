from typing import Set

from config.constants import POKEMONS_FILE
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.usecase.csv_extract import CsvExtract


def get_egg_groups(extractor: PokemonExtractor) -> Set[str]:
    pokemons = extractor.extract()
    egg_groups = set()
    for pokemon in pokemons:
        poke_types = [egg_group.strip() for egg_group in pokemon.egg_groups.split(",")]
        egg_groups.update(poke_types)
    return egg_groups


if __name__ == "__main__":
    extractor = CsvExtract(POKEMONS_FILE)
    types = get_egg_groups(extractor)
    print(types)
