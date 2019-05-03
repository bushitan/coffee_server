# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelStoreCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, default='', null=True, verbose_name='名字', max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('uuid', models.CharField(blank=True, default='', null=True, verbose_name='uuid', max_length=32)),
                ('nick_name', models.CharField(blank=True, default='', null=True, verbose_name='昵称', max_length=100)),
                ('avatar_url', models.CharField(blank=True, default='', null=True, verbose_name='头像', max_length=100)),
                ('gender', models.CharField(blank=True, default='', null=True, verbose_name='性别', max_length=100)),
                ('city', models.CharField(blank=True, default='', null=True, verbose_name='城市', max_length=100)),
                ('province', models.CharField(blank=True, default='', null=True, verbose_name='省份', max_length=100)),
                ('country', models.CharField(blank=True, default='', null=True, verbose_name='国家', max_length=100)),
                ('wx_openid', models.CharField(blank=True, default='', null=True, verbose_name='微信OpenID', max_length=50)),
                ('wx_session', models.CharField(blank=True, default='', null=True, verbose_name='微信SessionKey', max_length=128)),
                ('wx_unionid', models.CharField(blank=True, default='', null=True, verbose_name='微信UnionID', max_length=50)),
                ('customer', models.ForeignKey(blank=True, null=True, verbose_name='所属店铺', to='lite.Customer')),
                ('store', models.ForeignKey(blank=True, null=True, verbose_name='所属店铺', to='lite.Store')),
            ],
            options={
                'verbose_name_plural': '客户访问的店铺表',
                'verbose_name': '客户访问的店铺表',
            },
        ),
    ]
