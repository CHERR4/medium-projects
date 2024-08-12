import re
from typing import Set

from config.constants import POKEMONS_FILE
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.usecase.csv_extract import CsvExtract


def clean_ability(ability: str) -> str:
    ability = ability.strip()
    if re.match(r"\d+\.", ability):
        cleaned_ability = ability.split(". ")[1]
    else:
        cleaned_ability = re.sub(r"\s*\(hidden ability\)", "", ability)
    return cleaned_ability


def get_pokemon_abilities(extractor: PokemonExtractor) -> Set[str]:
    pokemons = extractor.extract()
    abilities = set()
    for pokemon in pokemons:
        poke_ability = [
            clean_ability(ability) for ability in pokemon.abilities.split(",")
        ]
        abilities.update(poke_ability)
    return abilities


if __name__ == "__main__":
    extractor = CsvExtract(POKEMONS_FILE)
    abilities = get_pokemon_abilities(extractor)
    print(abilities)
