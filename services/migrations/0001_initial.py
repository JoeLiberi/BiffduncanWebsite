# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-18 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smartfields.fields
import smartfields.models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='services', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=24, verbose_name='title')),
                ('image', models.ImageField(height_field=100, upload_to='services/%Y/%m/%d', width_field=100)),
                ('description', models.CharField(max_length=120, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'services',
                'get_latest_by': 'created',
                'verbose_name': 'service',
                'db_table': 'services_rendered',
            },
        ),
    ]
