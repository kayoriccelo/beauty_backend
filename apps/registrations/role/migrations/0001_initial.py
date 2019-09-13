# Generated by Django 2.2.5 on 2019-09-13 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=140)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='role', to='company.Company', verbose_name='company')),
            ],
            options={
                'verbose_name': 'role',
                'db_table': 'role',
            },
        ),
    ]