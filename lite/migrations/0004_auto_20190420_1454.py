# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0003_auto_20190420_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='delete_seller',
            field=models.ForeignKey(blank=True, to='lite.Seller', verbose_name='删除的店员', related_name='delete_seller', null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否被删除'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='customer',
            field=models.ForeignKey(blank=True, to='lite.Customer', verbose_name='所属客户', null=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='seller',
            field=models.ForeignKey(blank=True, to='lite.Seller', verbose_name='核销店员', null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='customer',
            field=models.ForeignKey(blank=True, to='lite.Customer', verbose_name='所属客户', null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='seller',
            field=models.ForeignKey(blank=True, to='lite.Seller', verbose_name='核销店员', null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='share',
            field=models.ForeignKey(blank=True, to='lite.Share', verbose_name='分享券', null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='customer',
            field=models.ForeignKey(blank=True, to='lite.Customer', verbose_name='所属客户', null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='seller',
            field=models.ForeignKey(blank=True, to='lite.Seller', verbose_name='核销店员', null=True),
        ),
    ]
