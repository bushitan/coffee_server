# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lite.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0023_auto_20190612_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='WmTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(default='', verbose_name='名字', max_length=32, null=True, blank=True)),
                ('uuid', models.CharField(default='', verbose_name='uuid', max_length=36, null=True, blank=True)),
                ('short_uuid', models.CharField(default='', verbose_name='短uuid', max_length=36, null=True, blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('is_used', models.BooleanField(default=False, verbose_name='是否已使用')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='外卖活动开始时间')),
                ('end_time', models.DateTimeField(default=lite.models.day_365_hence, verbose_name='外卖活动结束时间')),
                ('customer', models.ForeignKey(verbose_name='领取客户', null=True, to='lite.Customer', blank=True)),
                ('score', models.ForeignKey(verbose_name='生成的集点', null=True, to='lite.Score', blank=True)),
                ('share', models.ForeignKey(verbose_name='生成的分享券', null=True, to='lite.Share', blank=True)),
                ('store', models.ForeignKey(verbose_name='所属店铺', null=True, to='lite.Store', blank=True)),
            ],
            options={
                'verbose_name_plural': '外卖二维码',
                'verbose_name': '外卖二维码',
                'ordering': ['-create_time'],
            },
        ),
    ]
