# Generated by Django 2.2.5 on 2019-09-16 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('product', '0004_product_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='company.Company', verbose_name='company')),
                ('product', models.ManyToManyField(related_name='stock', to='product.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'stock',
                'db_table': 'stock',
            },
        ),
    ]
