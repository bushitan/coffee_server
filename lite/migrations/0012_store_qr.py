# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0011_auto_20190505_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='qr',
            field=models.TextField(default='', null=True, verbose_name='店铺二维码', blank=True),
        ),
    ]
