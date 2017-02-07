# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 05:22
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
            name='TimeControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Старт')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Стоп')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комменарии')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_controls', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
        ),
    ]
