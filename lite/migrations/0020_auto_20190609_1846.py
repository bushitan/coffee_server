# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0019_auto_20190609_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='share',
            name='is_delete',
        ),
    ]
