# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-09 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0011_postimg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostImg',
            new_name='Img',
        ),
    ]
