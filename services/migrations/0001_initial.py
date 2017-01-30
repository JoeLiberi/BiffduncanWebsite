# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-30 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='services_services', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('image', models.ImageField(upload_to='services/%Y/%m/%d')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
                'verbose_name': 'service',
                'db_table': 'services_rendered',
                'verbose_name_plural': 'services',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
