# Generated by Django 2.0.9 on 2019-07-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20190716_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='comments',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='stop',
            name='contact',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stop',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stop',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]