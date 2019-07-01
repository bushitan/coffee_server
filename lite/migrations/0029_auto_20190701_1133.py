# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lib.image_utils


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0028_auto_20190620_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nick_name_base64',
            field=models.TextField(default='', verbose_name='昵称', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='relstorecustomer',
            name='nick_name_base64',
            field=models.TextField(default='', verbose_name='昵称', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='nick_name_base64',
            field=models.TextField(default='', verbose_name='昵称', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baseimage',
            name='local_path',
            field=models.ImageField(verbose_name='图标', blank=True, upload_to=lib.image_utils.ImageUtils.rename, null=True),
        ),
        migrations.AlterField(
            model_name='baseimage',
            name='type',
            field=models.IntegerField(default=3, choices=[(1, '封面'), (2, '图标'), (3, '二维码')], verbose_name='类别'),
        ),
    ]
