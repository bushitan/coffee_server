# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0016_auto_20190604_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_auto',
            field=models.BooleanField(verbose_name='是否自助集点', default=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='icon_check_image_url',
            field=models.CharField(verbose_name='已集点印章图标', max_length=500, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='icon_full_image_url',
            field=models.CharField(verbose_name='集满点印章图标', max_length=500, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='icon_mode',
            field=models.IntegerField(verbose_name='图标模式', choices=[(1, '杯子图案'), (2, '印章图案')], default=1),
        ),
        migrations.AlterField(
            model_name='store',
            name='icon_un_check_image_url',
            field=models.CharField(verbose_name='未集点印章图标', max_length=500, blank=True, null=True, default=''),
        ),
    ]
