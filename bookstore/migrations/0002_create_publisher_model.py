# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_create_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('num_awards', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'bookstore_publishers',
            },
        ),
    ]