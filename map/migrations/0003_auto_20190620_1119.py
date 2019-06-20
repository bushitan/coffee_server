# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20190618_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='maparticle',
            name='author',
            field=models.ForeignKey(to='map.MapVisitor', blank=True, null=True, verbose_name='博主'),
        ),
        migrations.AddField(
            model_name='mapvisitor',
            name='type',
            field=models.IntegerField(choices=[(1, '博主'), (2, '路人')], default=2, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='maparticle',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=True),
        ),
        migrations.AlterField(
            model_name='maparticle',
            name='type',
            field=models.IntegerField(choices=[(1, '微信公众号'), (2, '小红书'), (3, '实景导航')], default=1, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='mappoi',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=True),
        ),
        migrations.AlterField(
            model_name='maptag',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=True),
        ),
    ]
