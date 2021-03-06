# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=100)),
                ('event_description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on:')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Published on:')),
            ],
        ),
    ]
