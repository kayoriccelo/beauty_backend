from django.db import models


class Stock(models.Model):
    product = models.ManyToManyField('product.Product', verbose_name='product', related_name='stock')
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=0)
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="stock",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'stock'
        db_table = 'stock'
