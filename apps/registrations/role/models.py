from django.db import models


class Role(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=140)
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="role",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'role'
        db_table = 'role'
