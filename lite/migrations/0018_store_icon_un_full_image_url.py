# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0017_auto_20190604_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='icon_un_full_image_url',
            field=models.CharField(max_length=500, null=True, blank=True, verbose_name='未集满点印章图标', default=''),
        ),
    ]
