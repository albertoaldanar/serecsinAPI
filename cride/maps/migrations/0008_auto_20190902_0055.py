# Generated by Django 2.0.9 on 2019-09-02 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_stop_fail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busroute',
            name='mes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
