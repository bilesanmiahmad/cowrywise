import uuid
from django.db import models

# Create your models here.

class DataModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.uuid)