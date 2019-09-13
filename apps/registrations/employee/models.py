from django.db import models


class Employee(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=140)
    admission_date = models.DateField()
    date_birth = models.DateField()
    general_record = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    adresses = models.ForeignKey('address.Address', verbose_name='address', related_name="employee",
                                 on_delete=models.PROTECT)
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="employee",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'employee'
        db_table = 'employee'
