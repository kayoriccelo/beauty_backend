# Generated by Django 2.2.5 on 2019-09-16 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('schedule', '0002_auto_20190916_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job', to='company.Company', verbose_name='company')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job', to='schedule.Schedule', verbose_name='schedule')),
            ],
            options={
                'verbose_name': 'job',
                'db_table': 'job',
            },
        ),
    ]
