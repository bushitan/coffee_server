# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0038_auto_20191006_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='content_image',
            field=models.ForeignKey(related_name='content_image', to='lite.BaseImage', null=True, verbose_name='内容图片', blank=True),
        ),
    ]
