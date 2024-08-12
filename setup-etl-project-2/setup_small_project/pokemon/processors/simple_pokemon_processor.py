from typing import List

from setup_small_project.pokemon.egg_group import EggGroup
from setup_small_project.pokemon.ev_field_stat import EvFieldStat
from setup_small_project.pokemon.growth_rate import GrowthRate
from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_ability import PokemonAbility
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed
from setup_small_project.pokemon.pokemon_stat import PokemonStat
from setup_small_project.pokemon.pokemon_stat_raw import PokemonStatRaw
from setup_small_project.pokemon.pokemon_type import PokemonType
from setup_small_project.pokemon.processors.pokemon_processor import PokemonProcessor


class SimplePokemonProcessor(PokemonProcessor):

    def __get_height(self, pokemon: Pokemon) -> float | None:
        return float(pokemon.height.split(" ")[0])

    def __get_weight(self, pokemon: Pokemon) -> float | None:
        if pokemon.weight == "—":
            return None
        return float(pokemon.weight.split(" ")[0])

    def __get_types(self, pokemon: Pokemon) -> List[PokemonType]:
        return [PokemonType(type.strip()) for type in pokemon.type.split(",")]

    def __get_abilities(self, pokemon: Pokemon) -> List[PokemonAbility]:
        if pokemon.abilities == "—":
            return []
        return [
            PokemonAbility(ability.split(".")[1].strip())
            for ability in pokemon.abilities.split(",")
            if "(hidden ability)" not in ability
        ]

    def __get_hidden_ability(self, pokemon: Pokemon) -> PokemonAbility | None:
        if "(hidden ability)" not in pokemon.abilities:
            return None
        return PokemonAbility(pokemon.abilities.split(",")[-1].split("(")[0].strip())

    def __get_ev_field_stat(self, ev_field_stat: str) -> EvFieldStat:
        ev_field_stat = ev_field_stat.strip()

        return EvFieldStat(
            rate=int(ev_field_stat.split(" ")[0]),
            stat=PokemonStat[
                PokemonStatRaw(" ".join(ev_field_stat.split(" ")[1:])).name
            ],
        )

    def __get_ev_field_stats(self, pokemon: Pokemon) -> List[EvFieldStat]:
        return [
            self.__get_ev_field_stat(ev_field_stat)
            for ev_field_stat in pokemon.ev_field.split(",")
        ]

    def __get_catch_rate(self, pokemon: Pokemon) -> float | None:
        if pokemon.catch_rate == "—":
            return None
        return float(pokemon.catch_rate.split(" ")[0])

    def __get_lowest_catch_rate(self, pokemon: Pokemon) -> float | None:
        if pokemon.catch_rate == "—":
            return None
        return float(pokemon.catch_rate.split("(")[1].split("%")[0])

    def __get_base_friendship(self, pokemon: Pokemon) -> int | None:
        if pokemon.base_friendship == "—":
            return None
        return int(pokemon.base_friendship.split(" ")[0])

    def __get_base_exp(self, pokemon: Pokemon) -> int | None:
        if pokemon.base_exp == "—":
            return None
        return int(pokemon.base_exp)

    def __get_egg_groups(self, pokemon: Pokemon) -> List[EggGroup]:
        return [
            EggGroup(egg_group.strip()) for egg_group in pokemon.egg_groups.split(",")
        ]

    def __get_male_gender_rate(self, pokemon: Pokemon) -> float | None:
        if pokemon.gender == "Genderless" or pokemon.gender == "—":
            return None
        return float(pokemon.gender.split("%")[0])

    def __get_female_gender_rate(self, pokemon: Pokemon) -> float | None:
        if pokemon.gender == "Genderless" or pokemon.gender == "—":
            return None
        return float(pokemon.gender.split(",")[1].split("%")[0].strip())

    def __get_egg_cycles(self, pokemon: Pokemon) -> int | None:
        if pokemon.egg_cycles == "—":
            return None
        return int(pokemon.egg_cycles.split(" ")[0])

    def __get_shortest_egg_cycle_steps(self, pokemon: Pokemon) -> int | None:
        if pokemon.egg_cycles == "—":
            return None
        return int(pokemon.egg_cycles.split("(")[1].split("–")[0].replace(",", ""))

    def __get_longest_egg_cycle_steps(self, pokemon: Pokemon) -> int | None:
        if pokemon.egg_cycles == "—":
            return None
        return int(pokemon.egg_cycles.split("–")[1].split(" ")[0].replace(",", ""))

    def process(self, pokemon: Pokemon) -> PokemonProcessed:
        types = self.__get_types(pokemon)
        abilities = self.__get_abilities(pokemon)

        return PokemonProcessed(
            id=pokemon.id,
            pokemon=pokemon.pokemon,
            main_type=types[0],
            secondary_type=types[1] if len(types) > 1 else None,
            species=pokemon.species,
            height=self.__get_height(pokemon),
            weight=self.__get_weight(pokemon),
            main_ability=abilities[0] if len(abilities) > 0 else None,
            secondary_ability=abilities[1] if len(abilities) > 1 else None,
            hidden_ability=self.__get_hidden_ability(pokemon),
            ev_field_stats=self.__get_ev_field_stats(pokemon),
            catch_rate=self.__get_catch_rate(pokemon),
            lowest_catch_rate=self.__get_lowest_catch_rate(pokemon),
            base_friendship=self.__get_base_friendship(pokemon),
            base_exp=self.__get_base_exp(pokemon),
            growth_rate=GrowthRate(pokemon.growth_rate),
            egg_groups=self.__get_egg_groups(pokemon),
            male_gender_rate=self.__get_male_gender_rate(pokemon),
            female_gender_rate=self.__get_female_gender_rate(pokemon),
            egg_cycles=self.__get_egg_cycles(pokemon),
            shortest_egg_cycle_steps=self.__get_shortest_egg_cycle_steps(pokemon),
            longest_egg_cycle_steps=self.__get_longest_egg_cycle_steps(pokemon),
            hp_base=int(pokemon.hp_base),
            hp_min=int(pokemon.hp_min),
            hp_max=int(pokemon.hp_max),
            attack_base=int(pokemon.attack_base),
            attack_min=int(pokemon.attack_min),
            attack_max=int(pokemon.attack_max),
            defense_base=int(pokemon.defense_base),
            defense_min=int(pokemon.defense_min),
            defense_max=int(pokemon.defense_max),
            special_attack_base=int(pokemon.special_attack_base),
            special_attack_min=int(pokemon.special_attack_min),
            special_attack_max=int(pokemon.special_attack_max),
            special_defense_base=int(pokemon.special_defense_base),
            special_defense_min=int(pokemon.special_defense_min),
            special_defense_max=int(pokemon.special_defense_max),
            speed_base=int(pokemon.speed_base),
            speed_min=int(pokemon.speed_min),
            speed_max=int(pokemon.speed_max),
        )
