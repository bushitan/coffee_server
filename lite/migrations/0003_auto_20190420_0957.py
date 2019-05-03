# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0002_relstorecustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='uuid',
            field=models.CharField(null=True, blank=True, default='', max_length=32, verbose_name='uuid'),
        ),
        migrations.AddField(
            model_name='score',
            name='uuid',
            field=models.CharField(null=True, blank=True, default='', max_length=32, verbose_name='uuid'),
        ),
        migrations.AddField(
            model_name='share',
            name='uuid',
            field=models.CharField(null=True, blank=True, default='', max_length=32, verbose_name='uuid'),
        ),
        migrations.AddField(
            model_name='store',
            name='uuid',
            field=models.CharField(null=True, blank=True, default='', max_length=32, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='score',
            name='exchange_time',
            field=models.DateTimeField(verbose_name='礼物兑换时间', default=django.utils.timezone.now),
        ),
    ]
