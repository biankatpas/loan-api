import uuid

from django.db import models


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nominal_value = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    request_date = models.DateField()
    request_ip_address = models.GenericIPAddressField()
    bank = models.ForeignKey("Bank", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)

    def __str__(self):
        return f"Loan {self.id} - Value: {self.nominal_value}, Interest Rate: {self.interest_rate}"
