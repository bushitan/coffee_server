# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0027_auto_20190618_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseimage',
            name='local_path',
            field=models.ImageField(verbose_name='图标', upload_to='img/', null=True, blank=True),
        ),
    ]
