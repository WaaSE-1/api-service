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
        """
        create_user Saves the created user to the database

        Args:
            user (User): Data for the user account that was created before.

        Returns:
            tuple: Created user account
        """
        self.cursor.callproc("CreateNewCustomer", user.get_values())
        self.conn.commit()

        return self.find_user_by_email(user.email)

    def find_user_by_email(self, email: str):
        """
        find_user Finds a user account by their email address.

        Args:
            email (str): Email address that will be used to look up the user

        Returns:
            tuple: Located User account
        """
        self.cursor.callproc("FindCustomerByEmail", [email])
        return [i.fetchone() for i in self.cursor.stored_results()][0]
