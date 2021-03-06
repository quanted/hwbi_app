# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaselineScore',
            fields=[
                ('county_FIPS', models.TextField(max_length=5, primary_key=True, serialize=False)),
                ('stateID', models.TextField(max_length=2)),
                ('state', models.TextField(max_length=20)),
                ('county', models.TextField(max_length=30)),
                ('serviceID', models.TextField(max_length=3)),
                ('serviceName', models.TextField(max_length=10)),
                ('description', models.TextField(max_length=50)),
                ('serviceType', models.TextField(max_length=15)),
                ('name', models.TextField(max_length=15)),
            ],
            options={
                'ordering': ('state', 'county', 'serviceID'),
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('domainID', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('domainName', models.TextField(max_length=25)),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serviceID', models.TextField(max_length=3, primary_key=True, serialize=False)),
                ('serviceTypeID', models.TextField(max_length=10)),
                ('serviceName', models.TextField(max_length=50)),
                ('serviceTypeName', models.TextField(max_length=10)),
                ('description', models.TextField(max_length=50)),
                ('name', models.TextField(max_length=50)),
            ],
            options={
                'ordering': ('serviceID', 'serviceName'),
            },
        ),
    ]
