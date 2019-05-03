# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0008_auto_20190503_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='receive_time',
            field=models.DateTimeField(verbose_name='接受时间', default=django.utils.timezone.now),
        ),
    ]
