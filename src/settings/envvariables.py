import os
from dotenv import load_dotenv
from pathlib import Path


class Settings:
    # Load environment envirables
    load_dotenv()
    
    ENV = os.getenv('ENV')

    # Ensure that all of the environmental variables are set.
    def check_variables(self) -> None:
        missing = [key for key, value in self.db_details().items() if value == None]
        if not self.JWT_SECRET:
            missing.append("JWT_SECRET")
        if missing:
            raise EnvironmentVariableException(missing)

    # Get environment
    ENV = os.getenv('ENV')

    # Get current directory
    CURRENT_DIR = str(Path(os.getcwd()))

    # JWT Secret required for authentication
    JWT_SECRET = os.getenv("JWT_SECRET")

    # MySQL connection details
    def db_details(self):
        return {
            "host": os.getenv("DB_HOSTNAME"),
            "user": os.getenv("DB_USERNAME"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_DATABASE"),
            "ssl_ca": os.path.join(
                os.path.realpath(self.CURRENT_DIR),
                Path("src/settings/cardealership-dbCA.crt.pem"),
            ),
            "port": 3306,
        }

    # OTHERS
    envvar = 0


class EnvironmentVariableException(Exception):
    def __init__(self, missing):
        self.missing = missing

    def __str__(self):
        return "Missing environmental variables:" + ", ".join(self.missing)
