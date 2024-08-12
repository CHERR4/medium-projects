#!/usr/bin/env python3
import unittest

from fastapi.testclient import TestClient

from setup_small_project.app import app
from setup_small_project.pokemon.pokemon import Pokemon
from setup_small_project.pokemon.pokemon_processed import PokemonProcessed


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_get_pokemons(self):
        response = self.client.get("/pokemons")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        assert isinstance(data, list)
        for item in data:
            self.assertIsNotNone(Pokemon(**item))

        pokemon = Pokemon(**data[0])
        response = self.client.get("/pokemon", params={"id": pokemon.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(Pokemon(**data), pokemon)

    def test_get_pokemons_processed(self):
        response = self.client.get("/pokemons-processed")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        assert isinstance(data, list)
        for item in data:
            self.assertIsNotNone(PokemonProcessed(**item))

        pokemon = PokemonProcessed(**data[0])
        response = self.client.get("/pokemon-processed", params={"id": pokemon.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(PokemonProcessed(**data), pokemon)


if __name__ == "__main__":
    unittest.main()
