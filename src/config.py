from dotenv import load_dotenv
import os

load_dotenv()

GENERAL = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "DEBUG": os.getenv("DEBUG"),
}

DB_CONFIG = {
    "NAME": os.getenv("DB_NAME"),
    "USER": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASSWORD"),
    "HOST": os.getenv("DB_HOST"),
    "PORT": os.getenv("DB_PORT"),
}