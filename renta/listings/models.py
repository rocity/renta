from django.db import models
from django.conf import settings

from model_utils import Choices

from renta.models import BaseRentaModel


BILLING_FREQUENCY_CHOICES = Choices(
    ('daily', 'Daily'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
)


class Listing(BaseRentaModel):
    """
    Listing Model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_frequency = models.CharField(max_length=10, choices=BILLING_FREQUENCY_CHOICES,
                                         default=BILLING_FREQUENCY_CHOICES.monthly)

    location = models.CharField(max_length=255)
    location_coordinates = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} - {self.title}'
