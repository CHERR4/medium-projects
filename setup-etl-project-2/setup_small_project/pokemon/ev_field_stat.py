from pydantic import BaseModel

from setup_small_project.pokemon.pokemon_stat import PokemonStat


class EvFieldStat(BaseModel):
    rate: int
    stat: PokemonStat
