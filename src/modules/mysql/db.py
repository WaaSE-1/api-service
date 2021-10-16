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
        find_user_by_email Finds a user account by their email address.

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
        self.cursor.callproc(
            "UpdateCustomerDetails",
            [
                email,
                user["firstname"],
                user["lastname"],
                user["email"],
                user["phone_number"],
                user["address"],
                user["password"],
            ],
        )
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
        self.cursor.callproc(
            "CreateNewCar",
            [car["manufacturer"], car["model"], car["year"], car["price"]],
        )
        self.conn.commit()

    def get_car_by_id(self, id):
        self.cursor.callproc("GetCarDetails", [id])
        return [i.fetchone() for i in self.cursor.stored_results()][0]

    def update_vehicle_inventory(self, inventory):
        self.cursor.callproc(
            "UpdateVehicleInventory",
            [inventory["vehicle"], inventory["dealership"], inventory["inventory"]],
        )
        self.conn.commit()

    def update_car_part_inventory(self, carpart):
        self.cursor.callproc(
            "UpdateCarPartInventory",
            [carpart["car_part_id"], carpart["dealership"], carpart["inventory"]],
        )
        self.conn.commit()

    def create_new_product(self, product):
        self.cursor.callproc(
            "CreateNewCarPart",
            [
                product["manufacturer"],
                product["weight"],
                product["dimensions"],
                product["material"],
                product["barcode"],
                product["serial_number"],
                product["price"],
            ],
        )
        self.conn.commit()
        return {"success": "Succesfully added a new product!"}

    def create_service_request(self, service):
        """
        Find all of the products available for sale

        Args:
            Service: Details of service request.

        """
        self.cursor.callproc(
            "CreateServiceRequest",
            [
                service["VIN"],
                service["service"],
                service["mechanic"],
                service["date"],
            ],
        )
        self.conn.commit()

    def get_all_products(self):
        """
        Find all of the products available for sale

        Returns:
            products: list of products available for sale.

        """
        self.cursor.callproc("ListAvailableParts", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def remove_car(self, car):
        """
        Remove a specific car from inventory

        Returns:
            car: car details.

        """
        self.cursor.callproc(
            "DeleteVehicleInventory", [car["vehicle"], car["dealership"]]
        )
        self.conn.commit()

    def delete_product(self, product):
        """
        Delete a product from the inventory
        """
        self.cursor.callproc(
            "DeleteCarPartInventory", [product["part"], product["dealership"]]
        )
        self.conn.commit()
        return {"success": "Product has been succesfully deleted!"}

    def get_all_services(self):
        self.cursor.callproc("ListAvailableServices", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def create_employee(self, employee):
        """
        create_employee Saves the created employee to the database

        Args:
            employee (Employee): Data for the employee account that was created before.

        Returns:
            tuple: Created employee account
        """
        self.cursor.callproc("CreateNewEmployee", employee.get_values())
        self.conn.commit()
        return {"success": "Created a new employee!"}

    def valid_dealership_id(self, dealership):
        """
        valid_dealership_id Updates a user account by their email address.

        Args:
            dealership (int): Dealership that user has provided

        Returns:
            bool: Dealership exists in the database
        """
        self.cursor.callproc("ValidDealership", [dealership])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def valid_department_id(self, department):
        """
        valid_department_id Updates a user account by their email address.

        Args:
            department (int): Department that user has provided

        Returns:
            bool: Department exists in the database
        """
        self.cursor.callproc("ValidDepartment", [department])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def valid_position_id(self, position):
        """
        valid_position_id Updates a user account by their email address.

        Args:
            position (int): Position that employee has provided

        Returns:
            bool: Position exists in the database
        """
        self.cursor.callproc("ValidPosition", [position])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def find_employee_by_email(self, email: str):
        """
        find_employee_by_email Finds a employee account by their email address.

        Args:
            email (str): Email address that will be used to look up the employee

        Returns:
            tuple: Located Employee account
        """
        self.cursor.callproc("FindEmployeeByEmail", [email])
        return [i.fetchone() for i in self.cursor.stored_results()][0]

    def delete_employee(self, email):
        """
        delete_employee Deletes a employee account by their email address.

        Args:
            email (str): Email address that will be used to locate the employee
        """
        self.cursor.callproc("DeleteEmployee", [email])
        self.conn.commit()

    def get_all_employees(self):
        self.cursor.callproc("ListEmployees", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def __del__(self):
        # Garbage collector goes brrr....
        self.cursor.close()
        self.conn.close()
