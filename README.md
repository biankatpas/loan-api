# Loan API

This API provides endpoints for managing loans, including loan creation, viewing loan details, making payments, and retrieving payment information.

## Available Endpoints (WIP)

### 1. POST /api/banks/

**Purpose:** Create a new bank entry.

**Request Body:**

```json
{
  "name": "My Bank",
  "code": "123456"  
}
```

### 2. GET /api/banks/{uuid}/

**Purpose:** Retrieve details of a specific bank.

**Description:**

* Retrieves details of a bank identified by its UUID.
* Returns a 404 error if the UUID is missing, invalid, or does not exist.

**Request Parameter:**

- `uuid` (path parameter): A unique identifier for the bank.

### 3. GET /api/banks/

**Purpose:** List all banks.

**Description:**

* Retrieves a list of all banks in the database.

### 4. POST /api/customers/

**Purpose:** Create a new customer entry.

**Request Body:**

```json
{
  "name": "Customer Name",
}
```

### 5. GET /api/customers/{uuid}/

**Purpose:** Retrieve details of a specific customer.

**Description:**

* Retrieves details of a customer identified by its UUID.
* Returns a 404 error if the UUID is missing, invalid, or does not exist.

**Request Parameter:**

- `uuid` (path parameter): A unique identifier for the customer.

### 6. GET /api/customers/

**Purpose:** List all customers.

**Description:**

* Retrieves a list of all customers in the database.  

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
