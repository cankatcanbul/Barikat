# Generated by Django 3.1.3 on 2020-11-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weather', '0003_auto_20201122_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Fday',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Tday',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
