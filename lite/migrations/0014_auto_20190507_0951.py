# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0013_auto_20190506_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='alive',
            field=models.IntegerField(verbose_name='有效点数', default=1),
        ),
        migrations.AddField(
            model_name='store',
            name='share_num',
            field=models.IntegerField(verbose_name='分享人数', default=1),
        ),
    ]
