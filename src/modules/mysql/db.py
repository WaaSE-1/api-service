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

    def update_user(self, email, user):
        """
        update_user Updates a user account by their email address.

        Args:
            email (str): Email address that will be used to locate the user
        """
        self.cursor.callproc("UpdateCustomerDetails", [email, user["firstname"], user["lastname"], user["email"], user["phone_number"], user["address"], user["password"]])
        self.conn.commit()

    def valid_zip_code(self, zip):
        """
        valid_zip_code Updates a user account by their email address.

        Args:
            zip (int): Post code that user has provided

        Returns:
            bool: Post code exists in the database
        """
        self.cursor.callproc("ValidZIP", [zip])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def get_all_cars(self):
        """
        get_all_cars Returns a list of cars available for purchase

        Returns:
            list [dict]: List of car objects
        """
        self.cursor.callproc("ListAvailableCars", [])
        return [i.fetchall() for i in self.cursor.stored_results()]
        
    def create_new_car(self, car): 
        """
        Create a new car with a single object with car details 
        Details are manufacturer, model, year, brand, dealership, the quantity availble and price.

        Args: 
            car(dict): car object existing of manufacturer, model, year and price

        """
        self.cursor.callproc("CreateNewCar", [car["manufacturer"], car["model"], car["year"], car["price"]])
        self.conn.commit()

    def __del__(self):
        # Garbage collector goes brrr....
        self.cursor.close()
        self.conn.close()
