# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0007_share_valid_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='valid_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='有效期'),
        ),
        migrations.AddField(
            model_name='score',
            name='valid_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='有效期'),
        ),
    ]
