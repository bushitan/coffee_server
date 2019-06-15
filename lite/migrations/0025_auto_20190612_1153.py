# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0024_wmticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='source',
            field=models.IntegerField(choices=[(1, '扫描来源'), (2, '外卖来源')], verbose_name='来源（默认扫码）', default=1),
        ),
        migrations.AddField(
            model_name='score',
            name='source',
            field=models.IntegerField(choices=[(1, '扫描来源'), (2, '外卖来源')], verbose_name='来源（默认扫码）', default=1),
        ),
        migrations.AddField(
            model_name='share',
            name='source',
            field=models.IntegerField(choices=[(1, '扫描来源'), (2, '外卖来源')], verbose_name='来源（默认扫码）', default=1),
        ),
    ]
