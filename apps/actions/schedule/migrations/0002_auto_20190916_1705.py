# Generated by Django 2.2.5 on 2019-09-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.IntegerField(choices=[(1, 'Waiting'), (2, 'Confirmed'), (3, 'In progress'), (4, 'Completed'), (5, 'Canceled')], default=1),
        ),
    ]