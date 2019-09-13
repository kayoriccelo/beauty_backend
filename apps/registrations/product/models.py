from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=140)

    class Meta:
        verbose_name = 'product'
        db_table = 'product'
