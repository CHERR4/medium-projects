from dataclasses import dataclass

from setup_small_project.pokemon.pokemon import Pokemon


@dataclass
class MongoPokemon(Pokemon):
    _id: str

    def to_pokemon(self) -> Pokemon:
        pokemon_dict = self.__dict__
        del pokemon_dict["_id"]
        return Pokemon(**pokemon_dict)
