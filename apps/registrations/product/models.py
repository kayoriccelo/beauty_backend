from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=140)
    provider = models.ManyToManyField('provider.Provider', verbose_name='provider', related_name='product')
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="product",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'product'
        db_table = 'product'
