# Generated by Django 2.2.7 on 2020-07-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='hours',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='work',
            name='total_hours',
            field=models.DurationField(),
        ),
    ]
