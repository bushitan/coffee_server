# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0018_store_icon_un_full_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否被删除'),
        ),
        migrations.AddField(
            model_name='share',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否被删除'),
        ),
    ]
