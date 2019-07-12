# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0031_auto_20190709_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmticket',
            name='source',
            field=models.IntegerField(verbose_name='来源（默认扫码）', choices=[(1, '扫描来源'), (2, '地图来源')], default=1),
        ),
        migrations.AddField(
            model_name='wmticket',
            name='type',
            field=models.IntegerField(verbose_name='门票类型', choices=[(1, '积分码'), (2, '分享码'), (3, '积分与分享共码')], default=1),
        ),
    ]
