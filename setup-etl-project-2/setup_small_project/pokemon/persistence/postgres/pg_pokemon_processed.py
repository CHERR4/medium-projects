from typing import List, Tuple

from pydantic import BaseModel

from setup_small_project.pokemon.ev_field_stat import EvFieldStat
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


class PgPokemonProcessed(BaseModel):
    id: str
    pokemon: str
    main_type: str | None
    secondary_type: str | None
    species: str
    height: float | None
    weight: float | None
    main_ability: str | None
    secondary_ability: str | None
    hidden_ability: str | None
    ev_field_stats: List[str]
    catch_rate: float | None
    lowest_catch_rate: float | None
    base_friendship: int | None
    base_exp: int | None
    growth_rate: str
    egg_groups: List[str]
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

    @classmethod
    def from_pokemon_processed(
        cls, pokemon_processed: PokemonProcessed, ev_field_stats: List[str]
    ) -> "PgPokemonProcessed":
        poke_dict = pokemon_processed.__dict__
        poke_dict["ev_field_stats"] = ev_field_stats
        return cls(**poke_dict)

    @classmethod
    def from_tuple(cls, tuple: Tuple) -> "PgPokemonProcessed":
        return cls(**dict(zip(cls.model_fields, tuple)))

    def to_pokemon_processed(
        self, ev_field_stats: List[EvFieldStat]
    ) -> PokemonProcessed:
        poke_dict = self.__dict__
        poke_dict["ev_field_stats"] = ev_field_stats
        return PokemonProcessed(**poke_dict)
