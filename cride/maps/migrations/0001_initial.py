# Generated by Django 2.0.9 on 2019-07-15 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busroute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time for created instance', verbose_name='created_a')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time for modified instance', verbose_name='modified_at')),
                ('bus', models.CharField(max_length=30)),
                ('helper', models.CharField(max_length=30)),
                ('helper_b', models.CharField(max_length=30, null=True)),
                ('gas', models.CharField(max_length=10)),
                ('km', models.PositiveIntegerField(default=0)),
                ('start', models.DateTimeField(help_text='Date and time of stop', verbose_name='event_date')),
                ('finish', models.DateTimeField(help_text='Date and time of stop', verbose_name='event_date')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time for created instance', verbose_name='created_a')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time for modified instance', verbose_name='modified_at')),
                ('lng', models.FloatField(blank=True)),
                ('lat', models.FloatField(blank=True)),
                ('client', models.CharField(max_length=30, null=True)),
                ('comments', models.CharField(max_length=10)),
                ('km', models.PositiveIntegerField(default=0)),
                ('arrived_at', models.DateTimeField(help_text='Date and time of stop', verbose_name='event_date')),
                ('finished_at', models.DateTimeField(help_text='Date and time of stop', verbose_name='event_date')),
                ('busroute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busroute', to='maps.Busroute')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': ['created'],
                'abstract': False,
            },
        ),
    ]
