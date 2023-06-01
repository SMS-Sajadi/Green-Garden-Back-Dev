# Generated by Django 4.2 on 2023-06-01 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0001_initial'),
        ('scores', '0005_alter_gardenscore_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardenscore',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 1, 20, 12, 39, 872350)),
        ),
        migrations.AlterField(
            model_name='gardenscore',
            name='garden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='garden.garden'),
        ),
    ]
