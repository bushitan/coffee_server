# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0006_auto_20190425_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='valid_time',
            field=models.DateTimeField(verbose_name='有效期', default=django.utils.timezone.now),
        ),
    ]
