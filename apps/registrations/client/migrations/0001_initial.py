# Generated by Django 2.2.5 on 2019-09-16 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=140)),
                ('date_birth', models.DateField()),
                ('general_record', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male')], default=1)),
                ('adresses', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_company', to='address.Address', verbose_name='address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_company', to='company.Company', verbose_name='company')),
            ],
            options={
                'verbose_name': 'client_company',
                'db_table': 'client_company',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=140)),
                ('date_birth', models.DateField()),
                ('general_record', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male')], default=1)),
                ('adresses', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client', to='address.Address', verbose_name='address')),
            ],
            options={
                'verbose_name': 'client',
                'db_table': 'client',
            },
        ),
    ]
