from mysql.connector import connect

db_details = {
    "host": "cardealership-db.mysql.database.azure.com",
    "user": "cardealershipadmin",
    "password": "nJi0HePX1DVdX8bSnXIEjc0S",
    "database": "cardealership",
    "port": 3306,
}


class DBConnection:
    def __init__(self):
        self.conn = connect(**db_details)
        self.cursor = self.conn.cursor()

    def create_user(self, user):
        insert_query = f"""
            INSERT INTO customer (firstname, lastname, email, phone_number, location_id, address, password)
            VALUES ('{user.firstname}', '{user.lastname}', '{user.email}', '{user.phonenumber}', '{user.loc_id}', '{user.address}', {user.password});
        """
        self.cursor.execute(insert_query)
        self.conn.commit()
        self.cursor.close()
        return 200

    def find_user(self, email: str):
        insert_query = f"""
            SELECT * FROM customer WHERE email='{email}'
        """
        self.cursor.execute(insert_query)
        user = self.cursor.fetchone()
        self.cursor.close()
        return user
