from mysql.connector import connect
from src.settings.envvariables import Settings
from typing import List, Dict


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

    def valid_zip_code(self, zip) -> List[dict]:
        """
        valid_zip_code Updates a user account by their email address.

        Args:
            zip (int): Post code that user has provided

        Returns:
            bool: Post code exists in the database
        """
        self.cursor.callproc("ValidZIP", [zip])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def get_all_cars(self) -> List[dict]:
        """
        get_all_cars Returns a list of cars available for purchase

        Returns:
            list [dict]: List of car objects
        """
        self.cursor.callproc("ListAvailableCars", [])
        return [i.fetchall() for i in self.cursor.stored_results()]

    def create_new_car(self, car) -> Dict:
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
        return {
            "success": "Car has been created successfully",
            "id": [i.fetchall() for i in self.cursor.stored_results()][0][0]["id"],
        }

    def get_car_by_id(self, id) -> List[dict]:
        self.cursor.callproc("GetCarDetails", [id])
        return [i.fetchone() for i in self.cursor.stored_results()][0]

    def update_vehicle_inventory(self, inventory) -> Dict:
        self.cursor.callproc(
            "UpdateVehicleInventory",
            [inventory["vehicle"], inventory["dealership"], inventory["inventory"]],
        )
        self.conn.commit()
        return {"success": "Vehicle has been added to the dealership!"}

    def update_car_part_inventory(self, carpart) -> Dict:
        self.cursor.callproc(
            "UpdateCarPartInventory",
            [carpart["car_part_id"], carpart["dealership"], carpart["inventory"]],
        )
        self.conn.commit()
        return {"success": "Succesfully updated a car part!"}

    def create_new_product(self, product) -> Dict:
        self.cursor.callproc(
            "CreateNewCarPart",
            [
                product["name"],
                product["description"],
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

    def create_service_request(self, service) -> Dict:
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
        return {"success": "Service request has been created succesfully!"}

    def get_all_products(self) -> List[dict]:
        """
        Find all of the products available for sale

        Returns:
            products: list of products available for sale.

        """
        self.cursor.callproc("ListAvailableParts", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def remove_car(self, car) -> Dict:
        """
        Remove a specific car from inventory

        Returns:
            car: car details.

        """
        self.cursor.callproc(
            "DeleteVehicleInventory", [car["vehicle"], car["dealership"]]
        )
        self.conn.commit()
        return {"success": "Car has been succesfully deleted!"}

    def delete_product(self, product) -> Dict:
        """
        Delete a product from the inventory
        """
        self.cursor.callproc("DeleteCarPartInventory", [product["id"]])
        self.conn.commit()
        return {"success": "Product has been succesfully deleted!"}

    def get_all_services(self) -> List[dict]:
        """
        get_all_services List of services offered by the car dealership

        Returns:
            List: List of services.
        """
        self.cursor.callproc("ListAvailableServices", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def get_service_history(self, customer_id) -> List[dict]:
        """
        get_service_history Service history for a given user.

        Args:
            customer_id (int): Customer ID.

        Returns:
            List: List of services done to user's cars.
        """
        self.cursor.callproc("FindServiceRequestsByCustomer", [customer_id])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def create_employee(self, employee) -> Dict:
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

    def valid_dealership_id(self, dealership) -> bool:
        """
        valid_dealership_id Updates a user account by their email address.

        Args:
            dealership (int): Dealership that user has provided

        Returns:
            bool: Dealership exists in the database
        """
        self.cursor.callproc("ValidDealership", [dealership])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def valid_department_id(self, department) -> bool:
        """
        valid_department_id Updates a user account by their email address.

        Args:
            department (int): Department that user has provided

        Returns:
            bool: Department exists in the database
        """
        self.cursor.callproc("ValidDepartment", [department])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def valid_position_id(self, position) -> bool:
        """
        valid_position_id Updates a user account by their email address.

        Args:
            position (int): Position that employee has provided

        Returns:
            bool: Position exists in the database
        """
        self.cursor.callproc("ValidPosition", [position])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def find_employee_by_email(self, email: str) -> List[dict]:
        """
        find_employee_by_email Finds a employee account by their email address.

        Args:
            email (str): Email address that will be used to look up the employee

        Returns:
            tuple: Located Employee account
        """
        self.cursor.callproc("FindEmployeeByEmail", [email])
        return [i.fetchone() for i in self.cursor.stored_results()][0]

    def delete_employee(self, email) -> None:
        """
        delete_employee Deletes a employee account by their email address.

        Args:
            email (str): Email address that will be used to locate the employee
        """
        self.cursor.callproc("DeleteEmployee", [email])
        self.conn.commit()

    def get_all_employees(self) -> List[dict]:
        """
        get_all_employees Calls a procedure to return a list of active employees.

        Returns:
            list: List of dictionaries representing employees
        """
        self.cursor.callproc("ListEmployees", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def get_user_cars(self, id: int) -> List[dict]:
        """
        get_user_cars Calls a procedure to return a list of user's cars.

        Args:
            id (int): customer ID.

        Returns:
            cars (list): List of cars that are in users garage.
        """
        self.cursor.callproc("GetCustomerVehicle", [id])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def add_car_for_customer(self, vehicle) -> Dict:
        """
        add_car_for_customer Adds a car to user's garage.

        Args:
            vehicle (dict): Details of a vehicle to be added to users garage.

        Returns:
            dict: success message.
        """
        self.cursor.callproc(
            "AssignCustomerVehicle",
            [
                vehicle["VIN"],
                vehicle["customer_id"],
                vehicle["vehicle_id"],
                vehicle["license_plate"],
            ],
        )
        self.conn.commit()
        return {"success": "Car has been added successfully!"}

    def valid_vehicle(self, id) -> bool:
        """
        valid_vehicle Check that vehicle with given ID exists in the vehicle table.

        Args:
            id (int): Vehicle ID.

        Returns:
            bool: Vehicle was found in the database
        """
        self.cursor.callproc("ValidVehicle", [id])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def valid_vin(self, vin) -> bool:
        """
        valid_vine Check that vehicle with given VIN doesn't exist in the vehicle table.

        Args:
            vin (str): Vehicle vin.

        Returns:
            bool: VIN was not found in the database
        """
        self.cursor.callproc("ValidVIN", [vin])
        return [i.fetchone() for i in self.cursor.stored_results()][0] == None

    def valid_license_plate(self, license) -> bool:
        """
        valid_license_plate Check that vehicle with given license plate doesn't exist in the vehicle table.

        Args:
            license (str): Vehicle license plate.

        Returns:
            bool: License plate was not found in the database
        """
        self.cursor.callproc("ValidLicensePlate", [license])
        return [i.fetchone() for i in self.cursor.stored_results()][0] == None

    def valid_manufacturer(self, brand) -> bool:
        """
        valid_manufacturer Check that manufacturer exists in the manufacturer table.

        Args:
            brand (str): Manufacturer.

        Returns:
            bool: Manufacturer was found in the database
        """
        self.cursor.callproc("ValidManufacturer", [brand])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def valid_service(self, id) -> bool:
        """
        valid_service Check that service id exists in the service_catalog table.

        Args:
            id (int): Service ID.

        Returns:
            bool: Service with provided ID was found in the database
        """
        self.cursor.callproc("ValidService", [id])
        return [i.fetchone() for i in self.cursor.stored_results()][0] != None

    def get_all_dealerships(self):
        self.cursor.callproc("ListDealerships", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def get_all_departments(self):
        self.cursor.callproc("ListDepartments", [])
        return [i.fetchall() for i in self.cursor.stored_results()][0]

    def __del__(self):
        """
        Close the database connection when all of the references to the object
        have been removed.
        akka... Garbage collector goes brrr....
        """
        self.cursor.close()
        self.conn.close()
