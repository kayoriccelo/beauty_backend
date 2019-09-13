from django.db import models


class Provider(models.Model):
    cnpj = models.CharField(max_length=14)
    business_name = models.CharField(max_length=140)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    adresses = models.ManyToManyField('address.Address', verbose_name='address', related_name="provider")

    class Meta:
        verbose_name = 'provider'
        db_table = 'provider'
