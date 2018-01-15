# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-15 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('date', models.DateTimeField()),
                ('article_content', models.CharField(max_length=300)),
                ('score', models.DecimalField(decimal_places=1, max_digits=1)),
                ('magnitude', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
        ),
    ]