# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20190701_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapvisitor',
            name='nick_name_base64',
            field=models.TextField(default='', null=True, blank=True, verbose_name='昵称base64'),
        ),
    ]
