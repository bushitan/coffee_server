# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0010_store_is_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='share_limit_time',
            field=models.IntegerField(default=1, verbose_name='分享券领取时间间隔(天）'),
        ),
        migrations.AlterField(
            model_name='store',
            name='share_valid_time',
            field=models.IntegerField(default=1, verbose_name='分享券有效期(天）'),
        ),
    ]
