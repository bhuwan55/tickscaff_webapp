# Generated by Django 2.2.7 on 2020-09-01 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20200901_1011'),
        ('main', '0017_auto_20200710_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='amount_of_bays',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='o', max_length=50),
        ),
    ]
