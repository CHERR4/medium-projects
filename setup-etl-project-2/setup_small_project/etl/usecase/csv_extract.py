import csv
from dataclasses import dataclass
from typing import List

from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.pokemon.pokemon_raw import PokemonRaw


@dataclass
class CsvExtract(PokemonExtractor):
    csv_path: str

    def extract(self) -> List[PokemonRaw]:
        with open(self.csv_path) as file:
            reader = csv.DictReader(file)
            return [PokemonRaw.from_dict(row) for row in reader]
