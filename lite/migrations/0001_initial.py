# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('uuid', models.CharField(null=True, blank=True, default='', verbose_name='uuid', max_length=32)),
                ('nick_name', models.CharField(null=True, blank=True, default='', verbose_name='昵称', max_length=100)),
                ('avatar_url', models.CharField(null=True, blank=True, default='', verbose_name='头像', max_length=100)),
                ('gender', models.CharField(null=True, blank=True, default='', verbose_name='性别', max_length=100)),
                ('city', models.CharField(null=True, blank=True, default='', verbose_name='城市', max_length=100)),
                ('province', models.CharField(null=True, blank=True, default='', verbose_name='省份', max_length=100)),
                ('country', models.CharField(null=True, blank=True, default='', verbose_name='国家', max_length=100)),
                ('wx_openid', models.CharField(null=True, blank=True, default='', verbose_name='微信OpenID', max_length=50)),
                ('wx_session', models.CharField(null=True, blank=True, default='', verbose_name='微信SessionKey', max_length=128)),
                ('wx_unionid', models.CharField(null=True, blank=True, default='', verbose_name='微信UnionID', max_length=50)),
            ],
            options={
                'verbose_name_plural': '客户',
                'verbose_name': '客户',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('customer', models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Customer')),
            ],
            options={
                'verbose_name_plural': '奖品',
                'verbose_name': '奖品',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('is_used', models.BooleanField(default=False, verbose_name='是否已使用')),
                ('exchange_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('customer', models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Customer')),
            ],
            options={
                'verbose_name_plural': '积分',
                'verbose_name': '积分',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('uuid', models.CharField(null=True, blank=True, default='', verbose_name='uuid', max_length=32)),
                ('nick_name', models.CharField(null=True, blank=True, default='', verbose_name='昵称', max_length=100)),
                ('avatar_url', models.CharField(null=True, blank=True, default='', verbose_name='头像', max_length=100)),
                ('gender', models.CharField(null=True, blank=True, default='', verbose_name='性别', max_length=100)),
                ('city', models.CharField(null=True, blank=True, default='', verbose_name='城市', max_length=100)),
                ('province', models.CharField(null=True, blank=True, default='', verbose_name='省份', max_length=100)),
                ('country', models.CharField(null=True, blank=True, default='', verbose_name='国家', max_length=100)),
                ('wx_openid', models.CharField(null=True, blank=True, default='', verbose_name='微信OpenID', max_length=50)),
                ('wx_session', models.CharField(null=True, blank=True, default='', verbose_name='微信SessionKey', max_length=128)),
                ('wx_unionid', models.CharField(null=True, blank=True, default='', verbose_name='微信UnionID', max_length=50)),
                ('is_host', models.BooleanField(default=False, verbose_name='是否店主')),
            ],
            options={
                'verbose_name_plural': '店家',
                'verbose_name': '店家',
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('customer', models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Customer')),
                ('receive_customer', models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Customer', related_name='receive_customer')),
                ('seller', models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Seller')),
            ],
            options={
                'verbose_name_plural': '分享券',
                'verbose_name': '分享券',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('title', models.CharField(null=True, blank=True, default='', verbose_name='标题', max_length=100)),
                ('summary', models.CharField(null=True, blank=True, default='', verbose_name='简介', max_length=200)),
                ('description', models.CharField(null=True, blank=True, default='', verbose_name='描述', max_length=500)),
                ('logo', models.CharField(null=True, blank=True, default='', verbose_name='标志', max_length=500)),
                ('icon', models.CharField(null=True, blank=True, default='', verbose_name='图标', max_length=500)),
                ('phone', models.CharField(null=True, blank=True, default='', verbose_name='电话', max_length=32)),
                ('address', models.CharField(null=True, blank=True, default='', verbose_name='地址', max_length=100)),
                ('latitude', models.FloatField(null=True, blank=True, default=0, verbose_name='纬度')),
                ('longitude', models.FloatField(null=True, blank=True, default=0, verbose_name='经度')),
                ('mode', models.IntegerField(default=1, verbose_name='集点模式', choices=[(1, '普通模式'), (2, '分享模式')])),
                ('exchange_value', models.IntegerField(default=10, verbose_name='兑换礼物点数')),
                ('check_value', models.IntegerField(default=1, verbose_name='普通核销点数')),
                ('share_check_value', models.IntegerField(default=1, verbose_name='分享券核销点数')),
                ('share_gift_value', models.IntegerField(default=1, verbose_name='分享券获赠点数')),
                ('share_limit_time', models.IntegerField(default=1, verbose_name='分享券领取时间间隔')),
                ('share_valid_time', models.IntegerField(default=1, verbose_name='分享券有效期')),
            ],
            options={
                'verbose_name_plural': '商铺',
                'verbose_name': '商铺',
            },
        ),
        migrations.AddField(
            model_name='share',
            name='store',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Store'),
        ),
        migrations.AddField(
            model_name='seller',
            name='store',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Store'),
        ),
        migrations.AddField(
            model_name='score',
            name='seller',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Seller'),
        ),
        migrations.AddField(
            model_name='score',
            name='share',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Share'),
        ),
        migrations.AddField(
            model_name='score',
            name='store',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Store'),
        ),
        migrations.AddField(
            model_name='prize',
            name='seller',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Seller'),
        ),
        migrations.AddField(
            model_name='prize',
            name='store',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属店铺', to='lite.Store'),
        ),
    ]
