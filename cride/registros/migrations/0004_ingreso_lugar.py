# Generated by Django 2.0.9 on 2019-09-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20190902_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='lugar',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
