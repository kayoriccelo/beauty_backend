from django.db import models


class Job(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule = models.ForeignKey('schedule.Schedule', verbose_name='schedule', related_name="job",
                                 on_delete=models.PROTECT)
    company = models.ForeignKey('company.Company', verbose_name='company', related_name="job",
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'job'
        db_table = 'job'
