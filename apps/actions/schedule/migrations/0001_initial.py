# Generated by Django 2.2.5 on 2019-09-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('company', '0001_initial'),
        ('employee', '0003_employee_company'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField()),
                ('time', models.DateField()),
                ('client_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule', to='client.ClientCompany', verbose_name='client_company')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule', to='company.Company', verbose_name='company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule', to='employee.Employee', verbose_name='employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule', to='service.Service', verbose_name='service')),
            ],
            options={
                'verbose_name': 'schedule',
                'db_table': 'schedule',
            },
        ),
    ]
