import os

from dotenv import main

main.load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")
