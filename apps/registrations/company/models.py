from django.db import models


class Company(models.Model):
    cnpj = models.CharField(max_length=14)
    business_name = models.CharField(max_length=140)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    adresses = models.ManyToManyField('address.Address', verbose_name='address', related_name="company")

    class Meta:
        verbose_name = 'company'
        db_table = 'company'
