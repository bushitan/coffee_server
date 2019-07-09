# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20190705_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmticket',
            name='sn',
            field=models.IntegerField(default=0, verbose_name='序列号'),
        ),
        migrations.AlterField(
            model_name='store',
            name='icon_mode',
            field=models.IntegerField(choices=[(1, '杯子图案'), (2, '印章图案'), (3, '天梯图案')], default=1, verbose_name='图标模式'),
        ),
    ]
