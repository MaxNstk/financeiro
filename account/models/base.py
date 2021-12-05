from django.db import models

from account.models.user import User


class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, null=True)

    class Meta:
        abstract = True