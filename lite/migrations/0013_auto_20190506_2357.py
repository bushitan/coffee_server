# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0012_store_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='share_logo',
            field=models.CharField(blank=True, verbose_name='分享LOGO', max_length=500, null=True, default=''),
        ),
        migrations.AddField(
            model_name='store',
            name='share_title',
            field=models.CharField(blank=True, verbose_name='分享标题', max_length=100, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.CharField(blank=True, verbose_name='LOGO', max_length=500, null=True, default=''),
        ),
    ]
