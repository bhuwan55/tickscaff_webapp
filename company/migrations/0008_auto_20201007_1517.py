# Generated by Django 2.2.7 on 2020-10-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20200901_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='builder_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]