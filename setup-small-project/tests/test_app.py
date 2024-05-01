#!/usr/bin/env python3
import unittest

from fastapi.testclient import TestClient

from setup_small_project.app import app
from setup_small_project.pokemon.pokemon import Pokemon


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
        self.assertEquals(Pokemon(**data), pokemon)


if __name__ == "__main__":
    unittest.main()
