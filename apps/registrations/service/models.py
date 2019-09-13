from django.db import models


class Service(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=140)
    products = models.ManyToManyField('product.Product', verbose_name='products', related_name='service')
    employees = models.ManyToManyField('employee.Employee', verbose_name='employees', related_name="service")
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="service",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'service'
        db_table = 'service'
