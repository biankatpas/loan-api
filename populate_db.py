import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django

try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    raise

from django.contrib.auth.models import User
from faker import Faker

from loan.models import Bank, Customer, Loan, Payment

fake = Faker()


print("Populate the database with fake data...")

# Create Users
for _ in range(10):
    user = User.objects.create_user(username=fake.user_name(), password=fake.password())

    # Create Customers
    customer = Customer.objects.create(name=fake.name())

    # Create Banks
    bank = Bank.objects.create(name=fake.company(), code=fake.bban())

    # Create Loans
    for _ in range(fake.random_int(min=0, max=3)):
        loan = Loan.objects.create(
            nominal_value=fake.random_number(digits=5),
            interest_rate=fake.random_number(digits=2),
            request_date=fake.date_this_decade(),
            request_ip_address=fake.ipv4(),
            bank=bank,
            customer=customer,
        )

        # Decide if the loan should have payments
        if fake.boolean(chance_of_getting_true=50):  # 50% chance of having payments
            # Create Payments for this loan
            for _ in range(fake.random_int(min=1, max=3)):
                Payment.objects.create(
                    loan=loan,
                    payment_date=fake.date_this_decade(),
                    amount=fake.random_number(digits=4),
                )

print("Successfully populated the database with fake data!")
