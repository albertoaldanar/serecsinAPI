# Generated by Django 2.0.9 on 2019-09-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_busroute_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='fail',
            field=models.BooleanField(default=False),
        ),
    ]