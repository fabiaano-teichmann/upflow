# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0009_auto_20160902_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Preenchido automaticamente, não editar.', max_length=150, unique=True, verbose_name='Slug / URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]
