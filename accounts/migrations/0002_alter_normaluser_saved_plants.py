# Generated by Django 4.2 on 2023-06-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='saved_plants',
            field=models.ManyToManyField(blank=True, to='plants.plant'),
        ),
    ]
