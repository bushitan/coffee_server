# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20190620_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapvisitor',
            name='nick_name_base64',
            field=models.TextField(default='', verbose_name='昵称', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maparticle',
            name='type',
            field=models.IntegerField(default=2, choices=[(1, '微信公众号'), (2, '小红书'), (3, '实景导航')], verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='mapvisitor',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, '博主'), (2, '路人')], verbose_name='类别'),
        ),
    ]
