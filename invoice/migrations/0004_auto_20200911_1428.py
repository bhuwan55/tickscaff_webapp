# Generated by Django 2.2.7 on 2020-09-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20200910_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='quantity1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
