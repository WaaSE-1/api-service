import os
from dotenv import load_dotenv
from pathlib import Path


class Settings:
    load_dotenv()

    # Get current directory
    CURRENT_DIR = str(Path(os.getcwd()))

    # OTHERS
    envvar = 0
    JWT_SECRET = os.getenv("JWT_SECRET")

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

