# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_featurehistory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='override_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]