# Generated by Django 2.2.7 on 2020-10-07 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_remove_invoice_quote'),
        ('quote', '0003_auto_20200831_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice'),
            preserve_default=False,
        ),
    ]
