# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0026_auto_20190613_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, verbose_name='名字', max_length=32, default='')),
                ('uuid', models.CharField(null=True, blank=True, verbose_name='uuid', max_length=36, default='')),
                ('short_uuid', models.CharField(null=True, blank=True, verbose_name='短uuid', max_length=36, default='')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('url', models.CharField(null=True, blank=True, verbose_name='云地址', max_length=1000)),
                ('local_path', models.ImageField(upload_to='img/', verbose_name='图标')),
                ('type', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], verbose_name='类别', default=1)),
            ],
            options={
                'verbose_name': '图库',
                'verbose_name_plural': '图库',
            },
        ),
        migrations.AlterField(
            model_name='store',
            name='wm_mode',
            field=models.IntegerField(choices=[(1, '普通模式'), (2, '分享模式'), (3, '普通分享并行模式'), (4, '关闭')], verbose_name='外卖模式', default=1),
        ),
    ]
