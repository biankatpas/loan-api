# Loan Management API

This REST API was developed using [Django](https://www.djangoproject.com/) and [Django REST framework](https://www.django-rest-framework.org/) to enable users to manage loans and payments.

## Core Features

* Users can create loans and register their payments.
* Users can view their loans and associated payments.
* Data privacy is enforced—users can only access and manage loans and payments associated with their own customers.
* Token-based authentication is used to secure access to the API.
* Core features are tested to ensure functionality and reliability.

## Upcoming Features

- **Outstanding Balance Calculation**: Implement API functionality to calculate and display the outstanding balance of each loan.
    * The outstanding balance reflects the remaining amount owed to the bank, considering the loan's interest rate and total payments made.

## Feature Enhancements

- **Outstanding Balance Calculation**: If the API is used by a bank or financial institution processing a high volume of payments, simultaneous balance calculations become critical. Celery can handle these calculations in the background, preventing the main application from becoming overloaded.

## Tests Improvements

- **Additional Tests**:
    * View Tests: Develop more comprehensive tests to cover all views and ensure correct functionality across various use cases.
    * Edge Case Testing: Evaluate how the application handles invalid or unexpected data to ensure resilience and effective management of unforeseen situations.
    * Performance Testing: Assess the application’s performance under load, including stress and load testing, to ensure it handles high volumes of requests efficiently.
    * Security Testing: Verify the application’s protection against common vulnerabilities such as SQL injection to ensure robust security measures are in place.

## Authentication Endpoints

These endpoints are used to obtain and refresh authentication tokens, required for accessing the API.

- **POST** `/api/token/`:  
  Generate a new access and refresh token pair by providing valid user credentials.

  **Request Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
  
- **POST** `/api/token/refresh`:  
  Refresh the access token using a valid refresh token.

  **Request Body:**
  ```json
  {
    "refresh": "refresh_token"
  }
  ```
  
## Available Endpoints

These are the main endpoints available for managing loans and payments in the system. Ensure that you are authenticated with a valid token to access them.

### Bank Endpoints

- **POST** `/api/banks/`:  

  Create a new bank.

   **Request Body:**
   
   ```json
   {
     "name": "My Bank",
     "code": "123456"  
   }
   ```

- **GET**  `/api/banks/`:

  Retrieve a list of all banks.
  
- **GET** `/api/banks/{id}/`:

  Retrieve details of a specific bank.

- **PUT** `/api/banks/{id}/`:  

  Update details of an existing bank. 

- **DELETE** `/api/banks/{id}/`:  

  Delete an existing bank.

### Customer Endpoints

- **POST** `/api/customers/`:  

  Create a new customer associated with the authenticated user.

   **Request Body:**
   
   ```json
   {
     "name": "Customer Name",
   }
   ```

- **GET**  `/api/customers/`:

  Retrieve a list of all customers associated with the authenticated user.
  
- **GET** `/api/customers/{id}/`:

  Retrieve details of a specific customer associated with the authenticated user.

- **PUT** `/api/customers/{id}/`:

  Update details of an existing customer associated with the authenticated user.

- **DELETE** `/api/customers/{id}/`:

  Delete an existing customer associated with the authenticated user.

### Loan Endpoints

- **POST** `/api/loans/`:  

  Create a new loan for a customer associated with the authenticated user.

  **Request Body:**
  ```json
  {
    "customer": "uuid_of_customer",
    "amount": "10000.00",
    "interest_rate": "5.00",
    "bank": "Bank name",
    "request_date": "2024-09-08"
  }
  ```

- **GET** `/api/loans/`:  

  Retrieve a list of all loans associated with the authenticated user.
  
- **GET** `/api/loans/{id}/`:  

  Retrieve details of a specific loan associated with the authenticated user. 

- **PUT** `/api/loans/{id}/`:  

  Update details of an existing loan associated with the authenticated user. 

- **DELETE** `/api/loans/{id}/`:  

  Delete an existing loan associated with the authenticated user.

### Payment Endpoints

- **POST** `/api/payments/`:  

  Create a new payment for a loan associated with the authenticated user.

  **Request Body:**
  ```json
  {
      "loan": "uuid_of_loan",
     "payment_date": "2024-09-08",
     "amount": "150.00"
  }
  ```

- **GET** `/api/payments/`:  

  Retrieve a list of all payments associated with the authenticated user.
  
- **GET** `/api/payments/{id}/`:  

  Retrieve details of a payment associated with the authenticated user. 

- **PUT** `/api/payments/{id}/`:  

  Update details of an existing payment associated with the authenticated user. 

- **DELETE** `/api/payments/{id}/`:  

  Delete an existing payment associated with the authenticated user.   

## Running the Project

Follow these steps to run the Loan API using Docker:

### 1. Prerequisites

Before starting the project, ensure you have the following:

- **Docker**: Make sure Docker is installed on your machine. You can download it from [Docker's official website](https://www.docker.com/get-started).

### 2. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

Replace `<repository-url>` with the URL of your repository and `<repository-directory>` with the name of the directory created by the clone command.

### 3. Configure Environment Variables

The project uses a .env file as a base, which should be configured based on example.env.

To run the Loan API project using Docker, follow these steps:

### 4. Start the Docker Container

   Navigate to the root directory of the project and run the following command:

   ```bash
   docker-compose up
   ```
### 5. Use Postman to Test Endpoints

Open Postman and use the available endpoints.

Note: If the `.env` file is not correctly configured or the Docker container is not running, the endpoints will not be accessible.

## Create Django Superuser

To create a superuser in Django (administrator), follow these steps:

### 1. Navigate to the root directory of the project and run the following command:

```bash
docker-compose up
```

### 2. Once the containers are running, create a superuser by running the following command:
```bash
docker-compose run web python manage.py createsuperuser
```
### 3. Follow the Prompts:

The command will prompt you to enter some details:

* Username: The username for the admin.
* Email address: The email address for the user.
* Password: Set a strong password for the admin account.

### 4. Access the Admin Panel:

After creating the superuser, you can access the Django admin panel in your browser:

```bash
http://localhost:8000/admin
```

### 5. Additional Notes:

* Ensure Migrations Are Applied: before creating the superuser, make sure the database migrations have been applied. If not, you can run the migrations with this command:

```bash
docker-compose run web python manage.py migrate
```

## Populate DB with Faker Data

Navigate to the root directory of the project and run the following command:

```bash
docker-compose up
```
```bash
docker-compose exec web python populate_db.py
```

## Running Tests

Navigate to the root directory of the project and run the following command:

```bash
docker-compose up
```
```bash
docker-compose exec web pytest
```

## Running Coverage Verification

Navigate to the root directory of the project and run the following command:

```bash
docker-compose up
```
```bash
docker-compose exec web pytest --cov=loan
```

## Running Linter Verification

Navigate to the root directory of the project and run the following command:

```bash
docker-compose up
```
```bash
docker-compose exec web pylint loan
```

## Running Code Formatter

Navigate to the root directory of the project and run the following command:

```bash
docker-compose up
```
```bash
docker-compose exec web python formatter.py 
```

## Pending Tasks

- Restore `request_ip_address` to be required. Currently set to allow null due to test issues after making the field auto-populated in the view and hidden from the serializer output.
- Implement logic for calculating the outstanding loan balance.
- After updating the Loan serializer to exclude `request_ip_address` and setting it as read-only via `extra_kwargs`, ensure that the Loan fixture and all associated tests are adjusted accordingly.
- Implement tests to verify the correct handling of `request_ip_address` in the view, ensuring it's auto-populated and behaves as expected.
