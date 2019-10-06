# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0036_auto_20190830_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content_image',
            field=models.ForeignKey(related_name='content_image', blank=True, null=True, verbose_name='封面图片', to='lite.BaseImage'),
        ),
        migrations.AddField(
            model_name='ad',
            name='content_lite_app_id',
            field=models.CharField(default='', max_length=100, null=True, blank=True, verbose_name='打开小程序的app_id'),
        ),
        migrations.AddField(
            model_name='ad',
            name='content_lite_env_version',
            field=models.CharField(default='', max_length=100, null=True, blank=True, verbose_name='打开小程序的env_version'),
        ),
        migrations.AddField(
            model_name='ad',
            name='content_lite_extra_data',
            field=models.CharField(default='', max_length=100, null=True, blank=True, verbose_name='打开小程序的extra_data'),
        ),
        migrations.AddField(
            model_name='ad',
            name='content_lite_path',
            field=models.CharField(default='', max_length=100, null=True, blank=True, verbose_name='打开小程序的path'),
        ),
        migrations.AddField(
            model_name='ad',
            name='content_url',
            field=models.CharField(default='', max_length=2000, null=True, blank=True, verbose_name='内容地址'),
        ),
        migrations.AddField(
            model_name='ad',
            name='cover_image',
            field=models.ForeignKey(related_name='cover_image', blank=True, null=True, verbose_name='封面图片', to='lite.BaseImage'),
        ),
        migrations.AddField(
            model_name='ad',
            name='store',
            field=models.ManyToManyField(null=True, blank=True, to='lite.Store', verbose_name='限制浏览店铺（不填则全部可浏览）'),
        ),
        migrations.AddField(
            model_name='prize',
            name='latitude',
            field=models.FloatField(default=0, null=True, blank=True, verbose_name='纬度'),
        ),
        migrations.AddField(
            model_name='prize',
            name='longitude',
            field=models.FloatField(default=0, null=True, blank=True, verbose_name='经度'),
        ),
        migrations.AddField(
            model_name='score',
            name='latitude',
            field=models.FloatField(default=0, null=True, blank=True, verbose_name='纬度'),
        ),
        migrations.AddField(
            model_name='score',
            name='longitude',
            field=models.FloatField(default=0, null=True, blank=True, verbose_name='经度'),
        ),
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(default='', max_length=32, null=True, blank=True, verbose_name='数据统计密码'),
        ),
        migrations.AddField(
            model_name='seller',
            name='username',
            field=models.CharField(default='', max_length=32, null=True, blank=True, verbose_name='数据统计登陆账号'),
        ),
        migrations.AddField(
            model_name='share',
            name='latitude',
            field=models.FloatField(default=0, null=True, blank=True, verbose_name='纬度'),
        ),
        migrations.AddField(
            model_name='share',
            name='longitude',
            field=models.FloatField(default=0, null=True, blank=True, verbose_name='经度'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, '图片'), (2, '浏览网页'), (3, '打开小程序')], verbose_name='广告'),
        ),
    ]
