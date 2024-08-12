from typing import Set

from config.constants import POKEMONS_FILE
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.usecase.csv_extract import CsvExtract


def clean_field_stat(ev_field: str) -> str:
    return ev_field.strip()[2:]


def get_pokemon_ev_field_stats(extractor: PokemonExtractor) -> Set[str]:
    pokemons = extractor.extract()
    field_stats = set()
    for pokemon in pokemons:
        ev_field_stats = [
            clean_field_stat(ev_field) for ev_field in pokemon.ev_field.split(",")
        ]
        field_stats.update(ev_field_stats)
    return field_stats


if __name__ == "__main__":
    extractor = CsvExtract(POKEMONS_FILE)
    ev_field_stats = get_pokemon_ev_field_stats(extractor)
    print(ev_field_stats)
