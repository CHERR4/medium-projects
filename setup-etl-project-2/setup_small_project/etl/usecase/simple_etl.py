import logging

from setup_small_project.etl.pokemon_etl import PokemonEtl
from setup_small_project.etl.pokemon_extractor import PokemonExtractor
from setup_small_project.etl.pokemon_loader import PokemonLoader
from setup_small_project.etl.pokemon_transformer import PokemonTransformer


class SimpleEtl(PokemonEtl):
    def __init__(
        self,
        extract: PokemonExtractor,
        transform: PokemonTransformer,
        load: PokemonLoader,
    ):
        self.extractor = extract
        self.transformer = transform
        self.loader = load

    def execute(self) -> int:
        logging.info(f"Running extract... {self.extractor.__class__}")
        pokemons_raw = self.extractor.extract()
        logging.info(f"Got {len(pokemons_raw)} pokemons")
        logging.info(f"Running transform... {self.transformer.__class__}")
        pokemons = self.transformer.transform(pokemons_raw)
        logging.info(f"Running load... {self.loader.__class__}")
        pokemons_processed = self.loader.load(pokemons)
        logging.info(f"{len(pokemons_processed)} records loaded. ETL Success")
        return len(pokemons_processed)
