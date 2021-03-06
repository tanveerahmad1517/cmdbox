# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 18:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScaffoldTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='updated at')),
                ('last_used', models.DateTimeField(blank=True, null=True, verbose_name='last used')),
                ('visibility', models.PositiveSmallIntegerField(choices=[(1, 'Public'), (2, 'Unlisted'), (3, 'Private')], default=1, verbose_name='visibility')),
                ('version', models.PositiveIntegerField(default=1, verbose_name='version')),
                ('stars', models.PositiveIntegerField(default=0, verbose_name='stars')),
                ('used', models.PositiveIntegerField(default=0, verbose_name='used')),
                ('language', models.CharField(blank=True, max_length=50, null=True, verbose_name='language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scaffoldtemplate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'scaffold template',
                'verbose_name_plural': 'scaffold template',
            },
        ),
    ]
