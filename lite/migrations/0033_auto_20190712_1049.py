# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0032_auto_20190712_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='wm_mode',
            field=models.IntegerField(default=1, choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式'), (4, '关闭'), (5, '据门票的类别自定义')], verbose_name='外卖模式'),
        ),
        migrations.AlterField(
            model_name='wmticket',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, '积分码'), (2, '分享码'), (3, '积分与分享共码'), (4, '关闭')], verbose_name='门票类型'),
        ),
    ]
