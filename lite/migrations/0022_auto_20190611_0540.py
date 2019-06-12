# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0021_auto_20190611_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='delete_seller',
            field=models.ForeignKey(related_name='prize_delete_seller', to='lite.Seller', blank=True, null=True, verbose_name='删除的店员'),
        ),
        migrations.AddField(
            model_name='share',
            name='delete_seller',
            field=models.ForeignKey(related_name='share_delete_seller', to='lite.Seller', blank=True, null=True, verbose_name='删除的店员'),
        ),
        migrations.AlterField(
            model_name='score',
            name='delete_seller',
            field=models.ForeignKey(related_name='score_delete_seller', to='lite.Seller', blank=True, null=True, verbose_name='删除的店员'),
        ),
    ]
