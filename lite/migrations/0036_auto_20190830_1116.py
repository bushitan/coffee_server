# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0035_ad_is_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='cover',
            field=models.CharField(null=True, blank=True, max_length=2000, default='', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='web_url',
            field=models.CharField(null=True, blank=True, max_length=2000, default='', verbose_name='内容地址'),
        ),
    ]
