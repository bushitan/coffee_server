# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maparticle',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=False),
        ),
        migrations.AddField(
            model_name='mappoi',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=False),
        ),
        migrations.AddField(
            model_name='maptag',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=False),
        ),
        migrations.AlterField(
            model_name='maptag',
            name='father',
            field=models.ForeignKey(verbose_name='父类', to='map.MapTag', blank=True, null=True),
        ),
    ]
