# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0005_auto_20190421_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar_url',
            field=models.CharField(null=True, max_length=500, blank=True, default='', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='relstorecustomer',
            name='avatar_url',
            field=models.CharField(null=True, max_length=500, blank=True, default='', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='avatar_url',
            field=models.CharField(null=True, max_length=500, blank=True, default='', verbose_name='头像'),
        ),
    ]
