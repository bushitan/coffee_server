# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0009_share_receive_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_business',
            field=models.BooleanField(default=True, verbose_name='是否营业'),
        ),
    ]
