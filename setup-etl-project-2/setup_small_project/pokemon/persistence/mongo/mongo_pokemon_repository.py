from typing import List

import pymongo
import pymongo.collection
import pymongo.database

from setup_small_project.common.typing_utils import single
from setup_small_project.pokemon.persistence.mongo.mongo_pokemon import MongoPokemon
from setup_small_project.pokemon.persistence.pokemon_repository import PokemonRepository
from setup_small_project.pokemon.pokemon import Pokemon


class MongoPokemonRepository(PokemonRepository):
    pokemon_collection: pymongo.collection.Collection

    def __init__(self, database: pymongo.database.Database):
        self.pokemon_collection = database["pokemon"]

    def truncate(self) -> int:
        return self.pokemon_collection.delete_many({}).deleted_count

    def save(self, pokemon: Pokemon) -> str:
        self.pokemon_collection.insert_one(pokemon.__dict__)
        return pokemon.id

    def get_all(self) -> List[Pokemon]:
        cursor = self.pokemon_collection.find({})
        return [MongoPokemon(**pokemon).to_pokemon() for pokemon in cursor]

    def get_by_id(self, id: str) -> Pokemon:
        pokemon_dict = single(list(self.pokemon_collection.find({"id": id})))
        return MongoPokemon(**pokemon_dict).to_pokemon()
