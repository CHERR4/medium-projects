from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This is done to prevent circular imports
    from setup_small_project.pokemon.persistence.pokemon_repository import (
        PokemonRepository,
    )


@dataclass
class Pokemon:
    id: str
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
    inserted_date: datetime

    def save(self, repository: "PokemonRepository") -> str:
        return repository.save(self)
