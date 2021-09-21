from mysql.connector import connect

db_details = {
    "host": "cardealership-db.mysql.database.azure.com",
    "user": "cardealershipadmin",
    "password": "nJi0HePX1DVdX8bSnXIEjc0S",
    "database": "cardealership",
    "port": 3306
}

class DBConnection:
    def __init__(self):
        self.conn = connect(**db_details)
        self.cursor = self.conn.cursor()

    def create_user():
        pass

    def find_user(email: str):
        return {
            "id": 1,
            "name":"Rick Astley",
            "email": "toms@gmail.com",
            "password":"argon2"
        }


