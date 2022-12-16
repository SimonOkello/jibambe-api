from tabnanny import verbose
from django.db import models

# Create your models here.

PAYMENT_CHOICES = (
    ('M-PESA', 'M-PESA'),
    ('CASH', 'CASH'),
)


class Payment(models.Model):
    name = models.CharField(max_length=100)
    payment_method = models.CharField(
        max_length=100, choices=PAYMENT_CHOICES, default='CASH')
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0.0)

    class Meta:
        db_table='payment'

    def __str__(self):
        return f'{self.name}-{self.amount}'
