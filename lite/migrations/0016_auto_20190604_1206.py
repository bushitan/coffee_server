# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0015_auto_20190515_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prize',
            options={'verbose_name': '奖品', 'ordering': ['-create_time'], 'verbose_name_plural': '奖品'},
        ),
        migrations.AlterModelOptions(
            name='share',
            options={'verbose_name': '分享券', 'ordering': ['-create_time'], 'verbose_name_plural': '分享券'},
        ),
        migrations.AddField(
            model_name='store',
            name='icon_check_image_url',
            field=models.CharField(verbose_name='已集点图标', blank=True, null=True, max_length=500, default=''),
        ),
        migrations.AddField(
            model_name='store',
            name='icon_full_image_url',
            field=models.CharField(verbose_name='集满点图标', blank=True, null=True, max_length=500, default=''),
        ),
        migrations.AddField(
            model_name='store',
            name='icon_mode',
            field=models.IntegerField(verbose_name='集点模式', default=1, choices=[(1, '杯子图案'), (2, '印章图案')]),
        ),
        migrations.AddField(
            model_name='store',
            name='icon_un_check_image_url',
            field=models.CharField(verbose_name='未集点图标', blank=True, null=True, max_length=500, default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='mode',
            field=models.IntegerField(verbose_name='集点模式', default=1, choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式')]),
        ),
    ]
