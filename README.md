# Loan API

This API provides endpoints for ...

## Available Endpoints (WIP)

### 1. POST /../..

**Purpose:** ..

**Request Body:**
- **None:** ..

### 2. **POST /..**

**Purpose:** ..

**Description:**

* ...

**Request Body:**

```json
{
  "..": ".."  
}
```

### 3. GET /../../{..}

**Purpose:** ..

**Description:**

* ...

**Request Parameter:**

- `..` (path parameter): ...
  
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
   docker-compose up --build
   ```
### 5. Use Postman to Test Endpoints (WIP)

Open Postman and use the following endpoints:

* POST /.../...: ...
* POST /...: ...
* GET /.../...: ...

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

Ensure Migrations Are Applied: before creating the superuser, make sure the database migrations have been applied. If not, you can run the migrations with this command:

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
