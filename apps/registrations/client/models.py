from django.db import models

C_GENDER = (
    (1, 'Female'),
    (2, 'Male'),
)


class ClientBase(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=140)
    date_birth = models.DateField()
    general_record = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.IntegerField(choices=C_GENDER, default=1)

    class Meta:
        abstract = True


class Client(ClientBase, models.Model):
    adresses = models.ForeignKey('address.Address', verbose_name='address', related_name="client",
                                 on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'client'
        db_table = 'client'


class ClientCompany(ClientBase, models.Model):
    adresses = models.ForeignKey('address.Address', verbose_name='address', related_name="client_company",
                                 on_delete=models.PROTECT)
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="client_company",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'client_company'
        db_table = 'client_company'
