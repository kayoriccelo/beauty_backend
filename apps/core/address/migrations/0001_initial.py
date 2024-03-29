# Generated by Django 2.2.5 on 2019-09-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=8)),
                ('street', models.CharField(blank=True, max_length=140, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=140, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, max_length=80, null=True)),
                ('nation', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'address',
                'db_table': 'address',
            },
        ),
    ]
