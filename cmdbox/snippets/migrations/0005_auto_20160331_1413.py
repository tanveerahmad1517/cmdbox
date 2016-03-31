# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20160331_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=models.CharField(blank=True, help_text='Give a brief description of what this snippet is about. Not required.', max_length=100, null=True, verbose_name='description'),
        ),
    ]
