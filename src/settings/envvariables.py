import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.security.api_key import APIKeyHeader


class Settings:
    load_dotenv()

    # DB SETTINGS
    SETTINGS_DB_Host = "cardealership-db.mysql.database.azure.com"
    SETTINGS_DB_User = "cardealershipadmin"
    SETTINGS_DB_Password = "nJi0HePX1DVdX8bSnXIEjc0S"
    SETTINGS_DB_Database = "cardealership"

    # OTHERS
    envvar = 0