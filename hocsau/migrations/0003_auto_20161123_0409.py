# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hocsau', '0002_category_haschild'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('menu_index',), 'verbose_name_plural': 'Categories'},
        ),
    ]
