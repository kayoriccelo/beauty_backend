from django.db import models


class Address(models.Model):
    postal_code = models.CharField(max_length=8)
    street = models.CharField(max_length=140, null=True, blank=True)
    neighborhood = models.CharField(max_length=140, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=80, null=True, blank=True)
    nation = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = 'address'
        db_table = 'address'
