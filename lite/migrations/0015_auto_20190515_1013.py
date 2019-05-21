# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lite.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0014_auto_20190507_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-create_time'], 'verbose_name': '积分', 'verbose_name_plural': '积分'},
        ),
        migrations.AddField(
            model_name='store',
            name='end_time',
            field=models.DateTimeField(verbose_name='集点结束时间', default=lite.models.day_365_hence),
        ),
        migrations.AddField(
            model_name='store',
            name='start_time',
            field=models.DateTimeField(verbose_name='集点开始时间', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='share',
            name='alive',
            field=models.IntegerField(verbose_name='有效份数', default=1),
        ),
    ]
