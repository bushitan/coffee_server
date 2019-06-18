# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0027_auto_20190618_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapArticle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, verbose_name='名字', max_length=32, default='')),
                ('uuid', models.CharField(null=True, blank=True, verbose_name='uuid', max_length=36, default='')),
                ('short_uuid', models.CharField(null=True, blank=True, verbose_name='短uuid', max_length=36, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('type', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], verbose_name='类别', default=1)),
                ('title', models.CharField(null=True, blank=True, verbose_name='标题', max_length=100, default='')),
                ('summary', models.CharField(null=True, blank=True, verbose_name='简介', max_length=200, default='')),
                ('description', models.CharField(null=True, blank=True, verbose_name='描述', max_length=500, default='')),
                ('content', models.TextField(null=True, blank=True, verbose_name='内容')),
                ('url', models.CharField(null=True, blank=True, verbose_name='web地址', max_length=1000)),
                ('cover', models.ForeignKey(to='lite.BaseImage', null=True, related_name='cover', blank=True, verbose_name='封面图片')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='MapPOI',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, verbose_name='名字', max_length=32, default='')),
                ('uuid', models.CharField(null=True, blank=True, verbose_name='uuid', max_length=36, default='')),
                ('short_uuid', models.CharField(null=True, blank=True, verbose_name='短uuid', max_length=36, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('title', models.CharField(null=True, blank=True, verbose_name='标题', max_length=100, default='')),
                ('summary', models.CharField(null=True, blank=True, verbose_name='简介', max_length=200, default='')),
                ('description', models.CharField(null=True, blank=True, verbose_name='描述', max_length=500, default='')),
                ('address', models.CharField(null=True, blank=True, verbose_name='地址', max_length=100, default='')),
                ('latitude', models.FloatField(null=True, blank=True, verbose_name='纬度', default=0)),
                ('longitude', models.FloatField(null=True, blank=True, verbose_name='经度', default=0)),
                ('icon', models.ForeignKey(null=True, to='lite.BaseImage', blank=True, verbose_name='封面图片')),
                ('store', models.ForeignKey(null=True, to='lite.Store', blank=True, verbose_name='所属店铺')),
            ],
            options={
                'verbose_name': 'POI地址',
                'verbose_name_plural': 'POI地址',
            },
        ),
        migrations.CreateModel(
            name='MapTag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, verbose_name='名字', max_length=32, default='')),
                ('uuid', models.CharField(null=True, blank=True, verbose_name='uuid', max_length=36, default='')),
                ('short_uuid', models.CharField(null=True, blank=True, verbose_name='短uuid', max_length=36, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('name_admin', models.CharField(null=True, blank=True, verbose_name='后台显示名字', max_length=32, default='')),
                ('sort', models.IntegerField(verbose_name='排序', default=0)),
                ('is_top', models.BooleanField(verbose_name='是否置顶', default=False)),
                ('service', models.IntegerField(choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式')], verbose_name='服务状态', default=1)),
                ('father', models.ForeignKey(null=True, to='map.MapTag', blank=True, verbose_name='所属店铺')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='MapVisitor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, verbose_name='名字', max_length=32, default='')),
                ('uuid', models.CharField(null=True, blank=True, verbose_name='uuid', max_length=36, default='')),
                ('short_uuid', models.CharField(null=True, blank=True, verbose_name='短uuid', max_length=36, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('nick_name', models.CharField(null=True, blank=True, verbose_name='昵称', max_length=100, default='')),
                ('avatar_url', models.CharField(null=True, blank=True, verbose_name='头像', max_length=500, default='')),
                ('gender', models.CharField(null=True, blank=True, verbose_name='性别', max_length=100, default='')),
                ('city', models.CharField(null=True, blank=True, verbose_name='城市', max_length=100, default='')),
                ('province', models.CharField(null=True, blank=True, verbose_name='省份', max_length=100, default='')),
                ('country', models.CharField(null=True, blank=True, verbose_name='国家', max_length=100, default='')),
                ('wx_openid', models.CharField(null=True, blank=True, verbose_name='微信OpenID', max_length=50, default='')),
                ('wx_session', models.CharField(null=True, blank=True, verbose_name='微信SessionKey', max_length=128, default='')),
                ('wx_unionid', models.CharField(null=True, blank=True, verbose_name='微信UnionID', max_length=50, default='')),
            ],
            options={
                'verbose_name': '浏览者',
                'verbose_name_plural': '浏览者',
            },
        ),
        migrations.AddField(
            model_name='mappoi',
            name='tag',
            field=models.ManyToManyField(null=True, to='map.MapTag', blank=True, verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='maparticle',
            name='poi',
            field=models.ForeignKey(null=True, to='map.MapPOI', blank=True, verbose_name='所属POI点'),
        ),
        migrations.AddField(
            model_name='maparticle',
            name='qr',
            field=models.ForeignKey(to='lite.BaseImage', null=True, related_name='qr', blank=True, verbose_name='二维码'),
        ),
    ]
