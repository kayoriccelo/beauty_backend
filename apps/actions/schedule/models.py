from django.db import models


class Schedule(models.Model):
    date = models.TimeField()
    time = models.DateField()
    client_company = models.ForeignKey('client.ClientCompany', verbose_name='client_company', related_name="schedule",
                                       on_delete=models.PROTECT)
    employee = models.ForeignKey('employee.Employee', verbose_name='employee', related_name="schedule",
                                 on_delete=models.PROTECT)
    service = models.ForeignKey('service.Service', verbose_name='service', related_name="schedule",
                                 on_delete=models.PROTECT)
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="schedule",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'schedule'
        db_table = 'schedule'
