import csv
import uuid
from dataclasses import dataclass
from typing import List, Self

from setup_small_project.common.datetime_utils import get_utc_datetime
from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository
from setup_small_project.pokemon.pokemon import Pokemon


@dataclass
class PokemonRaw:
    pokemon: str
    type: str
    species: str
    height: str
    weight: str
    abilities: str
    ev_field: str
    catch_rate: str
    base_friendship: str
    base_exp: str
    growth_rate: str
    egg_groups: str
    gender: str
    egg_cycles: str
    hp_base: str
    hp_min: str
    hp_max: str
    attack_base: str
    attack_min: str
    attack_max: str
    defense_base: str
    defense_min: str
    defense_max: str
    special_attack_base: str
    special_attack_min: str
    special_attack_max: str
    special_defense_base: str
    special_defense_min: str
    special_defense_max: str
    speed_base: str
    speed_min: str
    speed_max: str

    def save(self, repository: PokemonRepository) -> str:
        pokemon = Pokemon(
            **self.__dict__, id=str(uuid.uuid4()), inserted_date=get_utc_datetime()
        )
        return pokemon.save(repository)

    @classmethod
    def from_dict(cls, pokemon_dict: dict) -> Self:
        return cls(*pokemon_dict.values())

    @classmethod
    def from_csv(cls, csv_path: str) -> List[Self]:
        with open(csv_path) as file:
            reader = csv.DictReader(file)
            return [cls.from_dict(row) for row in reader]
