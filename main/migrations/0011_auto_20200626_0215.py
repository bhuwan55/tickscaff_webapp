# Generated by Django 2.2.7 on 2020-06-26 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200624_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergear',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Gear'),
        ),
        migrations.AlterField(
            model_name='returnedgear',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Gear'),
        ),
    ]
