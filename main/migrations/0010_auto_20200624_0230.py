# Generated by Django 2.2.7 on 2020-06-24 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('main', '0009_auto_20200619_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_name',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
            preserve_default=False,
        ),
    ]
