# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-22 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='facebook',
            field=models.CharField(blank=True, default='https://www.facebook.com', max_length=24, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='linkedin',
            field=models.CharField(blank=True, default='https://www.linkedin.com', max_length=24, verbose_name='linkedin'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='twitter',
            field=models.CharField(blank=True, default='https://www.twitter.com', max_length=24, verbose_name='twitter'),
        ),
    ]
