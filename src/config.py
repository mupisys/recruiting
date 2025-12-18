from dotenv import load_dotenv
import os

load_dotenv()

GENERAL = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "DEBUG": os.getenv("DEBUG"), 
}