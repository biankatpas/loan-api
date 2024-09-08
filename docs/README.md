# Loan Management API

This REST API was developed using [Django](https://www.djangoproject.com/) and [Django REST framework](https://www.django-rest-framework.org/) to enable users to manage loans and payments.

## Core Features
* Users can create loans and register their payments.
* Users can view their loans and associated payments.
* The API calculates and displays the outstanding balance of each loan:
    * The outstanding balance represents the remaining amount owed to the bank.
    * It accounts for the loan's interest rate and deducts the total amount already paid.
* Data privacy is enforced—users can only access and manage their own loans and payments.
* Token-based authentication is used to secure access to the API.

## Loan Details
Each loan includes the following information:
* Unique identifier (generated automatically).
* Nominal value (the amount borrowed).
* Interest rate (monthly rate).
* Request date (when the loan was initiated).
* IP address (of the user who created the loan).
* Bank and customer information.

## Payment Details
Each payment includes:
* Loan identifier.
* Payment date.
* Amount paid.

## Testing
* Core features are tested to ensure functionality and reliability.
