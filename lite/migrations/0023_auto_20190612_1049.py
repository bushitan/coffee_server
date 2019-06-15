# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0022_auto_20190611_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='relstorecustomer',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='share',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='short_uuid',
            field=models.CharField(default='', verbose_name='短uuid', max_length=36, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='wm_check_num',
            field=models.IntegerField(default=1, verbose_name='发放普通核销点数量'),
        ),
        migrations.AddField(
            model_name='store',
            name='wm_mode',
            field=models.IntegerField(default=1, verbose_name='外卖模式', choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式')]),
        ),
        migrations.AddField(
            model_name='store',
            name='wm_share_num',
            field=models.IntegerField(default=1, verbose_name='发放分享券数量'),
        ),
    ]
