import csv
from dataclasses import dataclass
from typing import List

from setup_small_project.pokemon.pokemon import Pokemon


@dataclass
class SavePokemonsCsvCmd:
    pokemons: List[Pokemon]
    csv_path: str

    def execute(self) -> int:
        with open(self.csv_path, "w", newline="") as csvfile:
            fieldnames = Pokemon.__annotations__.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in self.pokemons:
                writer.writerow(obj.__dict__)

        return len(self.pokemons)
