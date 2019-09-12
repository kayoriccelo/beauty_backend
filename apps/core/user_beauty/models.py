from django.contrib.auth.models import AbstractUser
from django.db import models


class UserBeauty(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    is_admin = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['cpf']

    class Meta:
        verbose_name = 'user_beauty'
        db_table = 'user_beauty'
