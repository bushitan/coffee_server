# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0034_auto_20190830_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='是否展示'),
        ),
    ]
