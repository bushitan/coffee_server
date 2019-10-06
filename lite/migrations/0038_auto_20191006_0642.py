# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0037_auto_20191006_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, '基础统计，无类别'), (2, '广告点击'), (3, '外卖扫码'), (4, '台卡扫码')], verbose_name='门票类型'),
        ),
    ]
