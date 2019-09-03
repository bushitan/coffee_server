# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0033_auto_20190712_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(blank=True, verbose_name='名字', max_length=32, null=True, default='')),
                ('uuid', models.CharField(blank=True, verbose_name='uuid', max_length=36, null=True, default='')),
                ('short_uuid', models.CharField(blank=True, verbose_name='短uuid', max_length=36, null=True, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('type', models.IntegerField(choices=[(1, '图片'), (2, '浏览网页')], verbose_name='广告', default=1)),
                ('cover', models.CharField(blank=True, verbose_name='封面图', max_length=500, null=True, default='')),
                ('web_url', models.CharField(blank=True, verbose_name='内容地址', max_length=500, null=True, default='')),
                ('sort', models.IntegerField(verbose_name='排序', default=0)),
            ],
            options={
                'verbose_name': '广告位',
                'verbose_name_plural': '广告位',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(blank=True, verbose_name='名字', max_length=32, null=True, default='')),
                ('uuid', models.CharField(blank=True, verbose_name='uuid', max_length=36, null=True, default='')),
                ('short_uuid', models.CharField(blank=True, verbose_name='短uuid', max_length=36, null=True, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('type', models.IntegerField(choices=[(1, '基础统计，无类别'), (2, '广告点击'), (3, '外卖扫码')], verbose_name='门票类型', default=1)),
                ('latitude', models.FloatField(blank=True, verbose_name='纬度', null=True, default=0)),
                ('longitude', models.FloatField(blank=True, verbose_name='经度', null=True, default=0)),
                ('ad', models.ForeignKey(verbose_name='广告', null=True, to='lite.Ad', blank=True)),
                ('customer', models.ForeignKey(verbose_name='客户', null=True, to='lite.Customer', blank=True)),
            ],
            options={
                'verbose_name': '数据统计',
                'verbose_name_plural': '数据统计',
            },
        ),
        migrations.AddField(
            model_name='store',
            name='is_ad',
            field=models.BooleanField(verbose_name='是否展示广告', default=True),
        ),
        migrations.AddField(
            model_name='collect',
            name='store',
            field=models.ForeignKey(verbose_name='店铺', null=True, to='lite.Store', blank=True),
        ),
        migrations.AddField(
            model_name='collect',
            name='wm_ticket',
            field=models.ForeignKey(verbose_name='外卖券', null=True, to='lite.WmTicket', blank=True),
        ),
    ]
