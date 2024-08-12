import uuid
from typing import List, Tuple

import psycopg2

from setup_small_project.common.typing_utils import defined, single
from setup_small_project.pokemon.ev_field_stat import EvFieldStat
from setup_small_project.pokemon.persistence.pokemon_processed_repository import (
    PokemonProcessedRepository,
)
from setup_small_project.pokemon.persistence.postgres.pg_ev_field_stat import (
    PgEvFieldStat,
)
from setup_small_project.pokemon.persistence.postgres.pg_pokemon_processed import (
    PgPokemonProcessed,
)
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


class PgPokemonProcessedRepo(PokemonProcessedRepository):
    connection: psycopg2.extensions.connection
    __columns = [
        "id",
        "pokemon",
        "main_type",
        "secondary_type",
        "species",
        "height",
        "weight",
        "main_ability",
        "secondary_ability",
        "hidden_ability",
        "ev_field_stats",
        "catch_rate",
        "lowest_catch_rate",
        "base_friendship",
        "base_exp",
        "growth_rate",
        "egg_groups",
        "male_gender_rate",
        "female_gender_rate",
        "egg_cycles",
        "shortest_egg_cycle_steps",
        "longest_egg_cycle_steps",
        "hp_base",
        "hp_min",
        "hp_max",
        "attack_base",
        "attack_min",
        "attack_max",
        "defense_base",
        "defense_min",
        "defense_max",
        "special_attack_base",
        "special_attack_min",
        "special_attack_max",
        "special_defense_base",
        "special_defense_min",
        "special_defense_max",
        "speed_base",
        "speed_min",
        "speed_max",
    ]

    def __init__(
        self,
        connection: psycopg2.extensions.connection,
    ):
        self.connection = connection

    def __save_field_stat(self, field_stat: EvFieldStat) -> str:
        id = str(uuid.uuid4())
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO ev_field (id, rate, stat)
            VALUES (%s, %s, %s)
            """,
            (id, field_stat.rate, field_stat.stat.value),
        )
        return id

    def __get_field_stat_by_id(self, id: str) -> EvFieldStat:
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT id, rate, stat
            FROM ev_field
            WHERE id = %s
            """,
            (id,),
        )
        rows = cursor.fetchall()
        return PgEvFieldStat.from_tuple(single(rows)).to_ev_field_stat()

    def __save_pg_pokemon_processed(self, pokemon: PgPokemonProcessed) -> str:
        columns_str = ",".join(self.__columns)
        values_params = ",".join(["%s"] * len(self.__columns))
        insert_statement = (
            f"INSERT INTO pokemon_processed ({columns_str}) VALUES ({values_params})"
        )
        cursor = self.connection.cursor()
        cursor.execute(
            insert_statement,
            (
                pokemon.id,
                pokemon.pokemon,
                pokemon.main_type,
                pokemon.secondary_type,
                pokemon.species,
                pokemon.height,
                pokemon.weight,
                pokemon.main_ability,
                pokemon.secondary_ability,
                pokemon.hidden_ability,
                pokemon.ev_field_stats,
                pokemon.catch_rate,
                pokemon.lowest_catch_rate,
                pokemon.base_friendship,
                pokemon.base_exp,
                pokemon.growth_rate,
                pokemon.egg_groups,
                pokemon.male_gender_rate,
                pokemon.female_gender_rate,
                pokemon.egg_cycles,
                pokemon.shortest_egg_cycle_steps,
                pokemon.longest_egg_cycle_steps,
                pokemon.hp_base,
                pokemon.hp_min,
                pokemon.hp_max,
                pokemon.attack_base,
                pokemon.attack_min,
                pokemon.attack_max,
                pokemon.defense_base,
                pokemon.defense_min,
                pokemon.defense_max,
                pokemon.special_attack_base,
                pokemon.special_attack_min,
                pokemon.special_attack_max,
                pokemon.special_defense_base,
                pokemon.special_defense_min,
                pokemon.special_defense_max,
                pokemon.speed_base,
                pokemon.speed_min,
                pokemon.speed_max,
            ),
        )
        self.connection.commit()
        cursor.close()
        return pokemon.id

    def truncate(self) -> int:
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM pokemon_processed")
        affected_pokemons = defined(cursor.fetchone())[0]
        cursor.execute("TRUNCATE TABLE pokemon_processed CASCADE")
        cursor.execute("TRUNCATE TABLE ev_field CASCADE")
        self.connection.commit()
        cursor.close()
        return affected_pokemons

    def save(self, pokemon_processed: PokemonProcessed) -> str:
        field_stats_ids = [
            self.__save_field_stat(field_stat)
            for field_stat in pokemon_processed.ev_field_stats
        ]
        pg_pokemon_processed = PgPokemonProcessed.from_pokemon_processed(
            pokemon_processed, field_stats_ids
        )
        return self.__save_pg_pokemon_processed(pg_pokemon_processed)

    def __row_to_pokemon_processed(self, row: Tuple) -> PokemonProcessed:
        poke_pg = PgPokemonProcessed.from_tuple(row)
        ev_stats = [self.__get_field_stat_by_id(id) for id in poke_pg.ev_field_stats]
        return poke_pg.to_pokemon_processed(ev_stats)

    def get_by_id(self, id: str) -> PokemonProcessed:
        columns_str = ",".join(self.__columns)
        select_statement = f"""
            SELECT {columns_str}
            FROM pokemon_processed
            WHERE id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(select_statement, (id,))
        result = cursor.fetchall()
        return self.__row_to_pokemon_processed(single(result))

    def get_all(self) -> List[PokemonProcessed]:
        columns_str = ",".join(self.__columns)
        select_statement = f"""
            SELECT {columns_str}
            FROM pokemon_processed
            """
        cursor = self.connection.cursor()
        cursor.execute(select_statement, (id,))
        result = cursor.fetchall()
        return [self.__row_to_pokemon_processed(row) for row in result]
