# api-service
Back-end API service for the car delaership platform developed for a educational project on KEA.

### Authors
- Toms Audrins
- Niels Bleijerveld
- Benjamin Skovhøj
- Patrick Klausgaard
- Jacob Sibbern
- Sebastian Arnvig
- Silke Castrone
- Țurcan Corina

#### Coding Standards
We've created our own coding-standard.md

## Requirements
- Docker installed
- MySQL server

## Installation 
### Docker
1. Set the environment variables
```
DB_HOSTNAME = MySQL Host
DB_USERNAME = MySQL Username
DB_PASSWORD = MySQL Password
DB_DATABASE = MySQL Database
JWT_SECRET = Token to authenticate users
```

2. Pull and run the image from the docker repository
```
docker run -h 0.0.0.0 -p 8000:80 waasegroup/api-service:latest
``` 

3. Go to the FastAPI docs: http://localhost:8000/docs

### Python
1. Clone the repository
```
git clone https://github.com/WaaSE-1/api-service.git
```

2. Go into the directory of the repository you just cloned
```
cd ./api-service
```

3. Install packages from requirmements.txt
```
pip install -r requirements.txt
```
4. Run the app depending on your python interpreter
```
python3 ./main.py
```
## Useful links

#### Production
- [Front-end](https://cardealership.unqhosting.com/)
- [Back-end](https://api-service.azurewebsites.net/docs)
- Database on Azure
#### Development
- [Front-end](http://localhost:3000)
- [Back-end](http://localhost:8000/docs)

## Folder structure
- src
    - modules
        - auth
        - mysql
    - routes
    - schema
    - settings

## Data model

Add description of the schema and database inserts


## Stored Procedures
- CreateNewCustomer
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `CreateNewCustomer`(
Firstname VARCHAR(20),
Lastname VARCHAR(45),
Email VARCHAR(45),
`Phone Number` VARCHAR(15),
Zipcode int,
Address VARCHAR(45),
`Password` VARCHAR(100)
)
BEGIN
	SET @location_id = (SELECT id FROM location WHERE postcode=Zipcode LIMIT 1);
	INSERT INTO customer (firstname, lastname, email, phone_number, location_id, address, password)
	VALUES (Firstname, Lastname, Email, `Phone Number`, @location_id, address, `Password`);
END
```
- CreateNewService
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `CreateNewService`(service VARCHAR(55))
BEGIN
 INSERT INTO service_catalog(service_type) VALUES(service);
END
```
- CreateServiceRequest
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `CreateServiceRequest`(VIN VARCHAR(17), Service int, Mechanic int, `Service Date[YYYY-MM-DD]` date)
BEGIN
 INSERT INTO service_request (vehicle_ident_number, service_catalog_id, mechanic, service_date)
 VALUES(VIN, Service, Mechanic, `Service Date[YYYY-MM-DD]`);
END
```
- DeleteUser
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `DeleteUser`(customer_email VARCHAR(55))
BEGIN
SET @customer_id = (SELECT id from customer where email=customer_email);
DELETE FROM customer_vehicle 
WHERE
    customer_id = @customer_id;
DELETE FROM customer 
WHERE
    id = @customer_id;
END
```
- FindCustomerByEmail
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `FindCustomerByEmail`(customeremail VARCHAR(50))
BEGIN
 SELECT * FROM customer
 WHERE email=customeremail;
END
```
- FindServiceRequestsByCustomer
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `FindServiceRequestsByCustomer`(`Customer ID` int)
BEGIN
SELECT CONCAT(c.firstname, ' ', c.lastname) as `Customer`,
       sr.vehicle_ident_number as VIN, sr.service_date,
       sc.service_type,
       CONCAT(e.firstname, ' ', e.lastname) as Mechanic, sr.invoice_id
FROM service_request sr
JOIN customer_vehicle cv on cv.vehicle_ident_number = sr.vehicle_ident_number
JOIN customer c on c.id = cv.customer_id
JOIN service_catalog sc on sr.service_catalog_id = sc.id
JOIN employee e on sr.mechanic = e.id
WHERE customer_id = `Customer ID`;
END
```
- UpdateCustomerDetails
```
CREATE DEFINER=`cardealershipadmin`@`%` PROCEDURE `UpdateCustomerDetails`(
customer_email VARCHAR(55),
new_firstname VARCHAR(20),
new_lastname VARCHAR(45),
new_email VARCHAR(55),
new_phone_number VARCHAR(15),
new_address VARCHAR(45),
new_password VARCHAR(100)
)
BEGIN
SET @customer_id = (SELECT id FROM customer WHERE email = customer_email);
UPDATE customer 
SET 
    firstname = new_firstname,
    lastname = new_lastname,
    email = new_email,
    phone_number = new_phone_number,
    address = new_address,
    password = new_password
WHERE
    id = @customer_id;
END
```
