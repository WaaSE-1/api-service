import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.security.api_key import APIKeyHeader
from pathlib import Path

class Settings:
    load_dotenv()

    # Get current directory
    CURRENT_DIR = str(Path(os.getcwd()))

    # DB SETTINGS
    SETTINGS_DB_Host = os.getenv('DB_HOSTNAME')
    SETTINGS_DB_User = os.getenv('DB_USERNAME')
    SETTINGS_DB_Password = os.getenv('DB_PASSWORD')
    SETTINGS_DB_Database = os.getenv('DB_DATABASE')
    SETTINGS_DB_CA_CERT = os.path.join(os.path.realpath(CURRENT_DIR), Path('src/settings/cardealership-dbCA.crt.pem'))

    # OTHERS
    envvar = 0
    