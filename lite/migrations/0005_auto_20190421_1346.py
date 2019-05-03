# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0004_auto_20190420_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='relstorecustomer',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='score',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='share',
            name='receive_customer',
            field=models.ForeignKey(related_name='receive_customer', null=True, blank=True, to='lite.Customer', verbose_name='接受客户'),
        ),
        migrations.AlterField(
            model_name='share',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='store',
            name='uuid',
            field=models.CharField(blank=True, null=True, max_length=36, default='', verbose_name='uuid'),
        ),
    ]
