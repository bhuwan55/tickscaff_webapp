# Generated by Django 2.2.7 on 2020-10-09 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('to', models.CharField(blank=True, max_length=50, null=True)),
                ('abn', models.CharField(blank=True, max_length=50, null=True)),
                ('site', models.CharField(blank=True, max_length=50, null=True)),
                ('description1', models.TextField(blank=True, null=True)),
                ('description2', models.TextField(blank=True, null=True)),
                ('description3', models.TextField(blank=True, null=True)),
                ('subtotal1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('subtotal3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gst2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_of_dismantle', models.DateField()),
                ('quantity1', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity2', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity3', models.CharField(blank=True, max_length=50, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quote', models.ManyToManyField(to='quote.Quote')),
            ],
        ),
    ]
