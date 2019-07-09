# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0029_auto_20190701_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='prize',
            field=models.ForeignKey(to='lite.Prize', null=True, blank=True, verbose_name='绑定的奖品'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nick_name_base64',
            field=models.TextField(default='', null=True, blank=True, verbose_name='昵称base64'),
        ),
        migrations.AlterField(
            model_name='relstorecustomer',
            name='nick_name_base64',
            field=models.TextField(default='', null=True, blank=True, verbose_name='昵称base64'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='nick_name_base64',
            field=models.TextField(default='', null=True, blank=True, verbose_name='昵称base64'),
        ),
    ]
