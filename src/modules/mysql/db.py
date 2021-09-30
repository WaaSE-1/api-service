from mysql.connector import connect
from src.settings.envvariables import Settings


class DBConnection:
    def __init__(self):
        self.conn = connect(**Settings().db_details())
        self.cursor = self.conn.cursor(dictionary=True)

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

    def delete_user(self, email):
        """
        delete_user Deletes a user account by their email address.

        Args:
            email (str): Email address that will be used to locate the user
        """
        self.cursor.callproc("DeleteUser", [email])
        self.conn.commit()

    def __del__(self):
        # Garbage collector goes brrr....
        self.cursor.close()
        self.conn.close()
