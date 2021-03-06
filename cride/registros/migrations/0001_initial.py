# Generated by Django 2.0.9 on 2019-07-28 03:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time for created instance', verbose_name='created_a')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time for modified instance', verbose_name='modified_at')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('importe', models.PositiveIntegerField(default=0)),
                ('mes', models.CharField(blank=True, max_length=30, null=True)),
                ('año', models.PositiveIntegerField(default=2019)),
                ('cliente', models.CharField(blank=True, max_length=30, null=True)),
                ('concepto', models.CharField(blank=True, max_length=30, null=True)),
                ('genero', models.CharField(blank=True, max_length=30, null=True)),
                ('cantidad', models.FloatField(blank=True, default=None, null=True)),
                ('usuario', models.CharField(blank=True, max_length=30, null=True)),
                ('lugar', models.CharField(blank=True, max_length=30, null=True)),
                ('cuenta_origen', models.PositiveIntegerField(default=0, null=True)),
                ('metodo_pago', models.CharField(blank=True, max_length=30, null=True)),
                ('forma_pago', models.CharField(blank=True, max_length=30, null=True)),
                ('cfdi', models.CharField(blank=True, max_length=30, null=True)),
                ('folio', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time for created instance', verbose_name='created_a')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time for modified instance', verbose_name='modified_at')),
                ('cliente', models.CharField(blank=True, max_length=30, null=True)),
                ('mes', models.CharField(blank=True, max_length=30, null=True)),
                ('año', models.PositiveIntegerField(default=2019)),
                ('importe', models.PositiveIntegerField(default=0)),
                ('adeudo_mes', models.PositiveIntegerField(default=0)),
                ('importante', models.BooleanField(default=False)),
                ('adeudo_acumulado', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': ['created'],
                'abstract': False,
            },
        ),
    ]
