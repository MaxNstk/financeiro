from colorfield.fields import ColorField
from django.db import models
from account.models.base import BaseModel


class Category(BaseModel):

    name = models.CharField(max_length=50)
    color = ColorField(default='#FFFFFF')
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name