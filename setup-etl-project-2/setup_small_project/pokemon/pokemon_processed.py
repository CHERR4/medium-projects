from typing import List

from pydantic import BaseModel

from setup_small_project.pokemon.egg_group import EggGroup
from setup_small_project.pokemon.ev_field_stat import EvFieldStat
from setup_small_project.pokemon.growth_rate import GrowthRate
from setup_small_project.pokemon.pokemon_ability import PokemonAbility
from setup_small_project.pokemon.pokemon_type import PokemonType


class PokemonProcessed(BaseModel):
    id: str
    pokemon: str
    main_type: PokemonType
    secondary_type: PokemonType | None
    species: str
    height: float | None
    weight: float | None
    main_ability: PokemonAbility | None
    secondary_ability: PokemonAbility | None
    hidden_ability: PokemonAbility | None
    ev_field_stats: List[EvFieldStat]
    catch_rate: float | None
    lowest_catch_rate: float | None
    base_friendship: int | None
    base_exp: int | None
    growth_rate: GrowthRate
    egg_groups: List[EggGroup]
    male_gender_rate: float | None
    female_gender_rate: float | None
    egg_cycles: int | None
    shortest_egg_cycle_steps: int | None
    longest_egg_cycle_steps: int | None
    hp_base: int
    hp_min: int
    hp_max: int
    attack_base: int
    attack_min: int
    attack_max: int
    defense_base: int
    defense_min: int
    defense_max: int
    special_attack_base: int
    special_attack_min: int
    special_attack_max: int
    special_defense_base: int
    special_defense_min: int
    special_defense_max: int
    speed_base: int
    speed_min: int
    speed_max: int
