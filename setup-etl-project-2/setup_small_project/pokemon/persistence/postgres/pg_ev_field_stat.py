from dataclasses import dataclass
from typing import Tuple

from setup_small_project.pokemon.ev_field_stat import EvFieldStat
from setup_small_project.pokemon.pokemon_stat import PokemonStat


@dataclass
class PgEvFieldStat:
    id: str
    rate: int
    stat: PokemonStat

    @classmethod
    def from_tuple(cls, tuple: Tuple) -> "PgEvFieldStat":
        return cls(
            id=tuple[0],
            rate=tuple[1],
            stat=tuple[2],
        )

    def to_ev_field_stat(self) -> EvFieldStat:
        return EvFieldStat(rate=self.rate, stat=self.stat)
