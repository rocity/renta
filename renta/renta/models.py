from uuid import uuid4
from django.db import models


class BaseRentaModel(models.Model):
    """
    Base of all models
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
