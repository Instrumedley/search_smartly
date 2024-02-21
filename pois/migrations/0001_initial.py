# Generated by Django 5.0.2 on 2024-02-21 09:41

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=255, unique=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('ratings', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
            ],
            options={
                'db_table': 'points_of_interest',
            },
        ),
    ]
